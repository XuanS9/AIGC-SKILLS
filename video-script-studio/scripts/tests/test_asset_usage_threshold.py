"""Asset threshold regressions on explicit inventories, not inferred prose identity."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import project_data_lint as lint


def inventory(kind='C', ids=None, registered=False):
    ids = ['1-1', '1-2'] if ids is None else ids
    asset = {'type': kind, 'name': '对象', 'handle': '@对象', 'file': None, 'status': 'planned'}
    return {'schema_version': 1, 'assets': [asset] if registered else [],
            'video_delivery': {'clips': [{'id': f'1-{n}', 'duration_seconds': 8} for n in (1, 2, 3)],
                               'object_usage': [{'type': kind, 'name': '对象', 'clip_ids': ids,
                                                 'asset_handle': '@对象' if registered else None}]}}


class AssetUsageThresholdTests(unittest.TestCase):
    def test_zero_one_two_three_distinct_prompts_for_every_asset_type(self):
        for kind in ('C', 'B', 'P', 'S'):
            for count in range(4):
                with self.subTest(kind=kind, count=count):
                    data = inventory(kind, [f'1-{n}' for n in range(1, count + 1)])
                    errors, _, counts = lint.validate_data(data)
                    self.assertEqual(bool(errors), count >= 2)
                    self.assertEqual(counts['shared_objects'], int(count >= 2))
                    if count >= 2:
                        self.assertTrue(any('必须建立共享资产' in e for e in errors))

    def test_same_clip_repeated_is_not_two_prompts(self):
        data = inventory(ids=['1-1'] * 5)
        data['video_delivery']['object_usage'][0]['appearance_count'] = 999
        errors, warnings, counts = lint.validate_data(data)
        self.assertEqual(errors, [])
        self.assertEqual(counts['shared_objects'], 0)
        self.assertTrue(any('集合去重' in w for w in warnings))

    def test_planned_shared_asset_passes_without_claiming_generated_file(self):
        for kind in ('C', 'B', 'P', 'S'):
            with self.subTest(kind=kind):
                errors, _, counts = lint.validate_data(inventory(kind, registered=True))
                self.assertEqual(errors, [])
                self.assertEqual(counts['shared_objects'], 1)

    def test_distinct_objects_in_different_prompts_do_not_merge(self):
        data = inventory('P', ['1-1'])
        data['video_delivery']['object_usage'].append(
            {'type': 'P', 'name': '另一把刀', 'clip_ids': ['1-2'], 'asset_handle': None})
        self.assertEqual(lint.validate_data(data)[0], [])

    def test_existing_asset_used_once_is_not_deleted_or_rejected(self):
        data = inventory(ids=['1-1'], registered=True)
        before = json.dumps(data, sort_keys=True)
        self.assertEqual(lint.validate_data(data)[0], [])
        self.assertEqual(json.dumps(data, sort_keys=True), before)

    def test_cross_batch_use_and_scoped_documents_still_require_shared_asset(self):
        data = inventory(ids=['1-1', '2-1'])
        data['video_delivery']['clips'].append({'id': '2-1', 'duration_seconds': 8})
        self.assertTrue(any('必须建立共享资产' in e for e in lint.validate_data(data, scoped=True)[0]))

    def test_unknown_clip_fake_handle_and_identity_mismatch_fail(self):
        for field, value in [('clip_ids', ['1-1', '9-9']), ('asset_handle', '@未登记'),
                             ('name', '别名未归并'), ('type', 'P')]:
            data = inventory(registered=True)
            data['video_delivery']['object_usage'][0][field] = value
            with self.subTest(field=field):
                self.assertTrue(lint.validate_data(data)[0])

    def test_duplicate_rows_or_splitting_same_registered_asset_fail(self):
        data = inventory(registered=True)
        row = data['video_delivery']['object_usage'][0]
        data['video_delivery']['object_usage'].append(dict(row))
        self.assertTrue(any('重复对象' in e for e in lint.validate_data(data)[0]))
        data['video_delivery']['object_usage'][1]['name'] = '未归并别名'
        self.assertTrue(any('拆成多行' in e for e in lint.validate_data(data)[0]))

    def test_legacy_registry_warns_threshold_not_checked_without_migration(self):
        data = inventory(registered=True)
        data['video_delivery'].pop('object_usage')
        errors, warnings, counts = lint.validate_data(data)
        self.assertEqual(errors, [])
        self.assertEqual(counts['object_usage'], 'not_provided')
        self.assertTrue(any('门槛未核验' in w for w in warnings))
        data.pop('video_delivery')
        self.assertEqual(lint.validate_data(data)[0], [])

    def test_bad_optional_shapes_are_rejected_without_tracebacks(self):
        for usage in [None, {}, [None], [{'type': [], 'name': '对象', 'clip_ids': []}],
                      [{'type': 'C', 'name': '', 'clip_ids': []}],
                      [{'type': 'C', 'name': '对象', 'clip_ids': '1-1'}],
                      [{'type': 'C', 'name': '对象', 'clip_ids': [False]}],
                      [{'type': 'C', 'name': '对象', 'clip_ids': [], 'asset_handle': []}]]:
            data = inventory()
            data['video_delivery']['object_usage'] = usage
            with self.subTest(usage=usage):
                self.assertTrue(lint.validate_data(data)[0])

    def test_cli_missing_shared_asset_fails_then_registration_passes(self):
        with tempfile.TemporaryDirectory() as td:
            registry, report = Path(td) / 'registry.json', Path(td) / 'report.json'
            command = [sys.executable, lint.__file__, '--asset-registry', str(registry),
                       '--report', str(report), '--scoped']
            for registered, code in [(False, 1), (True, 0)]:
                registry.write_text(json.dumps(inventory(registered=registered)), encoding='utf-8')
                result = subprocess.run(command, capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                self.assertNotIn('Traceback', result.stderr)
                data = json.loads(report.read_text())
                self.assertEqual(bool(data['errors']), not registered)
                self.assertEqual(data['counts']['shared_objects'], 1)


if __name__ == '__main__':
    unittest.main()

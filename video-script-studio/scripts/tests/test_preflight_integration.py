"""End-to-end regressions for the audit's actual preflight inputs."""
from decimal import Decimal
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SCRIPTS))
import director_contract_lint as contract
import seedance_lint as lint
import proofread_manifest as proof


def prompt(duration=8, event='人物沿窗边走到门口，手指按住门框。'):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from studio_fixtures import prompt as build, segment
    spoken = '{' in event
    action = event.split('{')[0].rstrip('：:说，,') if spoken else event
    line = (f'0s-{duration}s｜旅人压低声音说：{{' + event.split('{', 1)[1].rstrip('。')) if spoken else None
    seg = segment('0', f'{duration}', '侧面中景', 47, '固定', picture='人物站在窗边，面向画面右侧的门口。',
                  camera='固定，平视。', action=action, expression='人物眉头微皱，目光盯住门口。',
                  end_state='人物站定。')
    audio = f'对白语言：英语。\n{line}\nNO BGM。' if spoken else '本段无对白（设计）。现场声为房间底噪。NO BGM。'
    return build([seg], goal='人物走到门口。', style='窗光照到地面，5600K。', cut=False, audio=audio,
                 consistency='画面中只有 1 人。无字幕、无水印。')


def clip(number, duration=8, event=None, settings=''):
    body = prompt(duration) if event is None else prompt(duration, event)
    return f'# Clip {number}｜步行｜时长：{duration}秒{settings}\n```text\n{body}```\n'


class PreflightIntegrationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.specs = lint.load_specs(SCRIPTS.parent / 'references/model-specs.json')

    def findings(self, text, model='seedance_2_5', defaults=None):
        a, b, count = lint.preflight_document(text, defaults, self.specs[model])
        return a + b, count

    def cli(self, text, *args):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'prompt.txt'
            path.write_text(text, encoding='utf-8')
            return subprocess.run([sys.executable, str(SCRIPTS / 'seedance_lint.py'),
                                   '--preflight', '--file', str(path), *args],
                                  capture_output=True, text=True)

    def test_at_first_asset_declarations_are_recognised(self):
        for declaration in ('@母亲 对应 母亲。', '@母亲对应母亲。'):
            body = prompt().replace('本段无参考资产。', declaration)
            findings, _ = self.findings(body)
            self.assertFalse(any(f.rule in ('handles-not-declared-in-prompt', 'undeclared-handle', 'handle-used-before-declared') for f in findings), findings)
            self.assertEqual(contract.check_document(body), ([], 1))

    def test_chinese_settings_and_bold_english_settings(self):
        zh = lint.parse_settings_header('画幅：16:9｜分辨率：1080p｜模式：omni_reference｜时长：8.5秒')
        self.assertEqual(zh, lint.Settings('16:9', '1080p', 'omni_reference', Decimal('8.5')))
        en = lint.parse_settings_header('**Aspect ratio**: 16:9 **Duration**: 8.5s **Resolution**: 720p')
        self.assertEqual(en.duration, Decimal('8.5'))
        self.assertEqual(en.resolution, '720p')
        self.assertEqual(lint.parse_settings_header('Resolution: 2K').resolution, '2k')
        with self.assertRaises(ValueError):
            lint.parse_settings_header('时长：8秒 Duration: 10s')

    def test_chinese_timeline_exceeding_model_limit_is_rejected(self):
        text = clip('1-1', 20)
        self.assertEqual(contract.check_document(text), ([], 1))
        result = self.cli(text, '--model', 'seedance_2_0')
        self.assertEqual(result.returncode, 1, result.stdout)
        self.assertIn('beats-exceed-envelope', result.stdout)
        # No declaration: model maximum still constrains the timeline.
        findings, _ = self.findings(prompt(20), 'seedance_2_0')
        self.assertTrue(any(f.rule == 'beats-exceed-envelope' for f in findings))

    def test_chinese_unsupported_resolution_and_mode_are_rejected(self):
        for settings, rule in [('｜分辨率：4k', 'resolution-not-supported'),
                               ('｜模式：nonexistent', 'mode-not-supported')]:
            with self.subTest(settings=settings):
                result = self.cli(clip('1-1', settings=settings), '--model', 'seedance_2_5')
                self.assertEqual(result.returncode, 1)
                self.assertIn(rule, result.stdout)

    def test_seedance_2_5_accepts_1080p_since_2026_09_26_snapshot(self):
        result = self.cli(clip('1-1', settings='｜分辨率：1080p'), '--model', 'seedance_2_5')
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertNotIn('resolution-not-supported', result.stdout)
        self.assertIn('1080p', self.specs['seedance_2_5']['resolutions'])
        self.assertNotIn('4k', self.specs['seedance_2_5']['resolutions'])
        self.assertIn('start_image', self.specs['seedance_2_5']['media_roles']['medias'])

    def test_unfenced_metadata_is_outside_body_for_both_checkers(self):
        text = '# Clip 1-1｜步行｜时长：20秒\n' + prompt(20)
        parsed = contract.parse_clips(text)[0]
        self.assertIn('时长', parsed.metadata)
        self.assertNotIn('# Clip', parsed.body)
        self.assertEqual(contract.check_document(text), ([], 1))
        self.assertTrue(any(f.severity == 'FAIL' for f in self.findings(text, 'seedance_2_0')[0]))

    def test_two_complete_clips_are_not_aggregate_short_form(self):
        event = 'A figure walks along the path and follows the sunlight through the trees. ' * 11
        text = clip('1-1', 8, event) + clip('1-2', 8, event)
        self.assertEqual(lint.detect_regime(text), 'block')
        self.assertNotIn('overlength', [f.rule for f in lint.lint(text)])
        findings, count = self.findings(text)
        self.assertEqual(count, 2)
        self.assertFalse(any(f.severity == 'FAIL' for f in findings))

    def test_each_clip_has_its_own_metadata_and_timeline(self):
        text = clip('1-1', 8) + clip('1-2', 20)
        findings, count = self.findings(text, 'seedance_2_0')
        failures = [f for f in findings if f.severity == 'FAIL']
        self.assertEqual(count, 2)
        self.assertTrue(failures)
        self.assertTrue(all('Clip 1-2' in f.hit for f in failures))
        # Both legal intervals start at zero: not a cross-Clip overlap.
        findings, _ = self.findings(clip('1-1') + clip('1-2'))
        self.assertNotIn('overlapping-beats', [f.rule for f in findings])

    def test_common_settings_are_inherited_but_clip_override_wins(self):
        text = '分辨率：720p\n' + clip('1-1') + clip('1-2', settings='｜分辨率：4k')
        failures = [f for f in self.findings(text)[0] if f.severity == 'FAIL']
        self.assertEqual(len(failures), 1)
        self.assertIn('Clip 1-2', failures[0].hit)

    def test_discrete_duration_minimum_and_fractional_timeline(self):
        for text, model in [(clip('1-1', 5), 'seedance1_5'), (prompt(3), 'seedance_2_5')]:
            self.assertIn('duration-out-of-range', [f.rule for f in self.findings(text, model)[0]])
        text = prompt('8.5')
        self.assertFalse(any(f.severity == 'FAIL' for f in self.findings(text)[0]))

    def test_legacy_brackets_still_use_model_envelope(self):
        findings = lint.structural_lint('[0-20s] walking', lint.Settings(), self.specs['seedance_2_0'])
        self.assertIn('beats-exceed-envelope', [f.rule for f in findings])

    def test_duration_flag_cannot_hide_file_conflict(self):
        result = self.cli(clip('1-1', 20), '--model', 'seedance_2_0', '--duration', '8')
        self.assertEqual(result.returncode, 1)
        self.assertIn('duration-declaration-conflict', result.stdout)
        self.assertEqual(self.cli(prompt(), '--duration', '0').returncode, 2)

    def test_bad_clip_number_or_unclosed_fence_is_input_error(self):
        for text in [clip('1-1').replace('Clip 1-1', 'Clip 0-1'), clip('1-1')[:-4]]:
            with self.subTest(text=text):
                self.assertEqual(self.cli(text).returncode, 2)

    def test_approved_dialogue_is_not_a_cross_model_filter_failure(self):
        body = prompt(event='旅人抬起头，压低声音说：{Put down the knife.}')
        self.assertEqual(contract.check_document(body, dialogue_source='旅人：「Put down the knife.」'), ([], 1), body)
        for model in ['seedance_2_0', 'seedance_2_5', 'seedance_2_0_mini']:
            with self.subTest(model=model):
                findings, _ = self.findings(body, model)
                self.assertFalse(any(f.severity == 'FAIL' for f in findings))
                if model == 'seedance_2_0':
                    hit = next(f for f in findings if f.rule == 'weapon-noun')
                    self.assertEqual(hit.severity, 'WARN')
                    self.assertIn('preserve the approved line', hit.fix)
                else:
                    self.assertNotIn('weapon-noun', [f.rule for f in findings])
        self.assertIn('{Put down the knife.}', body)

    def test_empirical_patterns_never_claim_provider_acceptance(self):
        for text in ['A child holds a sword.', 'Tom Cruise walks outside.', 'Two people fight in a room.']:
            findings = lint.lint(text, model='seedance_2_0')
            self.assertFalse(any(f.severity == 'FAIL' for f in findings))
        result = self.cli(prompt(), '--model', 'seedance_2_5')
        self.assertNotIn('Safe to generate', result.stdout)
        self.assertNotIn('Likely to pass', result.stdout)

    def test_empty_scoped_manifest_and_bad_shapes_fail_cleanly(self):
        text = clip('1-1')
        baseline = {'unit_kind': 'clip', 'coverage_mode': 'scoped', 'scope': '复查当前改动',
                    'expected_units': [], 'reviews': {}, 'file_sha256': proof.digest(text),
                    'scope_file_sha256': proof.digest(text)}
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'prompt.txt'; path.write_text(text)
            manifest = Path(td) / 'proof.json'
            for data in [baseline, [], {**baseline, 'expected_units': [[]]},
                         {**baseline, 'expected_units': [None]}]:
                manifest.write_text(json.dumps(data))
                result = subprocess.run([sys.executable, str(SCRIPTS / 'proofread_manifest.py'),
                                         '--prompt', str(path), '--manifest', str(manifest)],
                                        capture_output=True, text=True)
                self.assertIn(result.returncode, (1, 2))
                self.assertNotIn('Traceback', result.stderr)

    def test_manifest_scoped_success_reports_real_count(self):
        text = clip('1-1') + clip('1-2')
        units = proof.units_for(text, 'clip')
        data = {'unit_kind': 'clip', 'coverage_mode': 'scoped', 'scope': '只复查1-2',
                'expected_units': ['1-2'], 'file_sha256': proof.digest(text),
                'scope_file_sha256': proof.digest(text),
                'reviews': {'1-2': {'status': 'reviewed', 'summary': '已回读当前正文与接缝。',
                                    'findings': [], 'sha256': proof.digest(units['1-2'])}}}
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'prompt.txt'; path.write_text(text)
            manifest = Path(td) / 'proof.json'; manifest.write_text(json.dumps(data))
            result = subprocess.run([sys.executable, str(SCRIPTS / 'proofread_manifest.py'),
                                     '--prompt', str(path), '--manifest', str(manifest)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0)
            self.assertIn('非全稿', result.stdout)
            self.assertIn('覆盖1条', result.stdout)

    def test_snapshot_date_and_invalid_export_do_not_silently_pass(self):
        from datetime import date, timedelta
        self.assertEqual(lint.snapshot_age_finding({}).rule, 'unknown-specs-date')
        for stamp in ['invalid', [], 42]:
            self.assertEqual(lint.snapshot_age_finding({'_snapshot_date': stamp}).rule,
                             'invalid-specs-date' if stamp else 'unknown-specs-date')
        future = (date.today() + timedelta(days=2)).isoformat()
        self.assertEqual(lint.snapshot_age_finding({'_snapshot_date': future}).rule, 'future-specs-date')
        stale = (date.today() - timedelta(days=31)).isoformat()
        self.assertEqual(lint.snapshot_age_finding({'_snapshot_date': stale}).rule, 'stale-specs-snapshot')
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'specs.json'
            for data in [[], {'models': []}, {'models': [None]}, {'models': [{'id': []}]}]:
                path.write_text(json.dumps(data))
                self.assertEqual(lint.load_specs(path), {})

    def test_manifest_uses_fence_aware_clip_boundaries(self):
        text = clip('1-1').replace('人物走到门口。', '# Clip 9-9｜只是正文引用\n人物走到门口。')
        self.assertEqual(list(proof.units_for(text, 'clip')), ['1-1'])


if __name__ == '__main__':
    unittest.main()

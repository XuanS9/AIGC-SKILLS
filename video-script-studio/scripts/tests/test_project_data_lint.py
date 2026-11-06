"""Scene graph, mapping and real title/registry integration regressions."""
import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import project_data_lint as lint
from test_preflight_integration import clip


def fixture():
    return {'schema_version': 1, 'assets': [{'type': 'S', 'name': '长屋', 'handle': '@长屋',
        'file': None, 'status': 'planned', 'view_plan': [
            {'name': '室内', 'image_id': 'S01', 'source_image_id': None,
             'actual_file': None, 'generate_separate_image': True, 'generation_method': 'base_scene',
             'clip_scope': '1-1、1-2（4—8秒）'},
            {'name': '雪院', 'image_id': 'S01-01', 'source_image_id': 'S01',
             'actual_file': None, 'generate_separate_image': True, 'generation_method': 'image_to_image',
             'clip_scope': '1-2（0—4秒）'}]}],
        'video_delivery': {'edit_order': ['1-1', '1-2'], 'clips': [
            {'id': '1-1', 'duration_seconds': 8, 'scene_image_references': [
                {'image_id': 'S01', 'time_range_seconds': None, 'actual_file': None}]},
            {'id': '1-2', 'duration_seconds': 8, 'scene_image_references': [
                {'image_id': 'S01-01', 'time_range_seconds': [0, 4], 'actual_file': None},
                {'image_id': 'S01', 'time_range_seconds': [4, 8], 'actual_file': None}]}]}}


def documents():
    video = clip('1-1', settings='｜场景图：S01') + clip('1-2', settings='｜场景图：S01-01（0—4秒）、S01（4—8秒）')
    scenes = ('# 场景图 S01｜长屋／室内｜Clip 1-1、1-2（4—8秒）\n```text\n空置长屋。\n```\n'
              '# 场景图 S01-01｜长屋／雪院｜图生图｜源图：S01｜Clip 1-2（0—4秒）\n```text\n空置雪院。\n```\n')
    return video, scenes


class ProjectDataTests(unittest.TestCase):
    def check(self, data, video=None, scenes=None, scoped=False):
        return lint.validate_data(data, video, scenes, scoped)[0]

    def test_planned_null_assets_and_complete_documents_pass(self):
        video, scenes = documents()
        errors, warnings, counts = lint.validate_data(fixture(), video, scenes)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(counts['images'], 2)

    def test_duplicate_independent_id_and_missing_source_fail(self):
        for patch in [{'image_id': 'S01'}, {'source_image_id': 'S99'}, {'source_image_id': []}]:
            data = fixture(); data['assets'][0]['view_plan'][1].update(patch)
            self.assertTrue(self.check(data))

    def test_cycles_and_self_references_fail(self):
        for source in ['S01', 'S01-01']:
            data = fixture(); data['assets'][0]['view_plan'][0]['source_image_id'] = source
            self.assertTrue(any('成环' in e for e in self.check(data)))

    def test_image_to_image_requires_real_logical_source(self):
        data = fixture(); data['assets'][0]['view_plan'][1]['source_image_id'] = None
        self.assertTrue(any('缺少直接源图' in e for e in self.check(data)))

    def test_reuse_does_not_count_as_new_image(self):
        data = fixture(); data['assets'][0]['view_plan'].append(
            {'name': '近景复用', 'image_id': 'S01', 'generate_separate_image': False})
        errors, _, counts = lint.validate_data(data)
        self.assertEqual(errors, [])
        self.assertEqual(counts['images'], 2)
        data['assets'][0]['view_plan'][-1]['image_id'] = 'S99'
        self.assertTrue(any('复用图号' in e for e in self.check(data)))

    def test_unknown_clip_image_and_bad_intervals_fail(self):
        for interval in [[-1, 4], [4, 4], [0, 9], [0, 31], [False, 4], [0, float('nan')], '0-4']:
            data = fixture(); data['video_delivery']['clips'][1]['scene_image_references'][0]['time_range_seconds'] = interval
            with self.subTest(interval=interval): self.assertTrue(self.check(data))
        data = fixture(); data['assets'][0]['view_plan'][0]['clip_scope'] = '9-9'
        self.assertTrue(any('不存在的Clip' in e for e in self.check(data)))
        data = fixture(); data['video_delivery']['clips'][0]['scene_image_references'][0]['image_id'] = 'S99'
        self.assertTrue(any('弃用图' in e for e in self.check(data)))

    def test_nonoverlap_repeated_uses_of_same_image_are_preserved(self):
        data = fixture()
        data['video_delivery']['clips'][0]['scene_image_references'] = [
            {'image_id': 'S01', 'time_range_seconds': [0, 2]},
            {'image_id': 'S01', 'time_range_seconds': [4, 8]}]
        data['assets'][0]['view_plan'][0]['clip_scope'] = [
            {'clip_id': '1-1', 'time_range_seconds': [0, 2]},
            {'clip_id': '1-1', 'time_range_seconds': [4, 8]},
            {'clip_id': '1-2', 'time_range_seconds': [4, 8]}]
        self.assertEqual(self.check(data), [])
        video, scenes = documents()
        video = video.replace('场景图：S01\n', '场景图：S01（0—2秒）（4—8秒）\n')
        scenes = scenes.replace('Clip 1-1、1-2', 'Clip 1-1（0—2秒）、1-1（4—8秒）、1-2')
        self.assertEqual(self.check(data, video, scenes), [])
        data['assets'][0]['view_plan'][0]['clip_scope'][0]['time_range_seconds'] = [0, 8]
        self.assertTrue(any('双向映射' in e for e in self.check(data)))

    def test_reverse_scope_and_file_version_mismatch_fail(self):
        data = fixture(); data['assets'][0]['view_plan'][0]['clip_scope'] = '1-1'
        self.assertTrue(any('双向映射' in e for e in self.check(data)))
        data = fixture(); data['video_delivery']['clips'][0]['scene_image_references'][0]['actual_file'] = 'old.png'
        self.assertTrue(any('文件版本' in e for e in self.check(data)))

    def test_video_title_duration_image_and_body_alias_mismatch_fail(self):
        video, scenes = documents()
        for changed in [video.replace('时长：8秒', '时长：7秒', 1),
                        video.replace('场景图：S01\n', '场景图：S99\n', 1),
                        video.replace('[生成目标]', '[场景]\n长屋 references @S99. Use only the layout. Do not use the people in the image. The set contains only what the reference shows; no added furniture or rooms.\n\n[生成目标]', 1),
                        video.replace('S01（4—8秒）', 'S01（3—8秒）')]:
            self.assertTrue(self.check(fixture(), changed, scenes))

    def test_scene_title_source_scope_and_abandoned_image_fail(self):
        video, scenes = documents()
        for changed in [scenes.replace('源图：S01', '源图：S99'),
                        scenes.replace('Clip 1-1、1-2（4—8秒）', 'Clip 1-1'),
                        scenes + '# 场景图 S99｜已弃用\n', scenes + '# 场景图 S01｜重复\n']:
            self.assertTrue(self.check(fixture(), video, changed))

    def test_edit_order_must_match_real_document_order(self):
        video, scenes = documents()
        data = fixture(); data['video_delivery']['edit_order'] = ['1-2', '1-1']
        self.assertTrue(any('顺序' in e for e in self.check(data, video, scenes)))
        for order in [['1-1'], ['1-1', '1-1'], None, [None]]:
            data = fixture(); data['video_delivery']['edit_order'] = order
            if order is not None: self.assertTrue(self.check(data))

    def test_scoped_batch_does_not_require_other_document_titles(self):
        video, scenes = documents()
        one = video.split('# Clip 1-2')[0]
        one_scene = scenes.split('# 场景图 S01-01')[0]
        self.assertTrue(self.check(fixture(), one, one_scene))
        self.assertEqual(self.check(fixture(), one, one_scene, True), [])
        self.assertTrue(self.check(fixture(), '', '', True))

    def test_no_file_evidence_yields_explicit_unchecked_warnings(self):
        errors, warnings, _ = lint.validate_data(fixture())
        self.assertEqual(errors, [])
        self.assertTrue(any('未提供视频' in w for w in warnings))
        data = fixture(); data['assets'][0]['view_plan'][0].pop('clip_scope')
        self.assertTrue(any('双向映射待核验' in w for w in lint.validate_data(data)[1]))

    def test_bad_shapes_do_not_traceback(self):
        for patch in [{'video_delivery': []}, {'video_delivery': {'clips': {}}},
                      {'assets': [None]}, {'assets': [{'view_plan': [None]}]}]:
            data = fixture(); data.update(patch)
            self.assertTrue(self.check(data))
        data = fixture(); data['video_delivery']['clips'][0]['duration_seconds'] = True
        self.assertTrue(self.check(data))

    def test_short_legacy_ids_and_scope_parser_remain_supported(self):
        self.assertEqual(lint.parse_scope('Clip 1-1、1-2（4—8秒）'), [('1-1', None), ('1-2', [4., 8.])])
        data = fixture()
        serialized = json.dumps(data, ensure_ascii=False).replace('S01-01', 'S1-1').replace('S01', 'S1')
        self.assertEqual(self.check(json.loads(serialized)), [])

    def test_cli_real_files_and_machine_report(self):
        video, scenes = documents()
        with tempfile.TemporaryDirectory() as td:
            folder = Path(td)
            for name, text in [('registry.json', json.dumps(fixture())), ('video.txt', video), ('scenes.txt', scenes)]:
                (folder / name).write_text(text, encoding='utf-8')
            command = [sys.executable, str(Path(lint.__file__)), '--asset-registry', str(folder / 'registry.json'),
                       '--video', str(folder / 'video.txt'), '--scenes', str(folder / 'scenes.txt'),
                       '--report', str(folder / 'report.json')]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertEqual(json.loads((folder / 'report.json').read_text())['errors'], [])
            (folder / 'scenes.txt').write_text(scenes.replace('源图：S01', '源图：S99'))
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertNotIn('Traceback', result.stderr)


if __name__ == '__main__':
    unittest.main()

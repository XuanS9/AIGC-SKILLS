"""Video is Seedance-only: other video generators and post-processing video tools stay removed."""
from pathlib import Path
import json
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
KEEP = {'seedance_2_5', 'seedance_2_0', 'seedance_2_0_mini', 'seedance1_5'}

# Video generators and video post tools removed (2026-11-05).
# Image-only models (Kling Image, Kling O1 image, image upscalers) are out of scope.
REMOVED = re.compile(
    r'\bsora\b|\bveo ?3|\bveo\b|\bwan ?2\.[5-7]|\bwan2_|hailuo|minimax[- ]h3|minimax hailuo'
    r'|grok imagine video|grok video|happy.horse|gemini omni|flux 3 video'
    r'|cinema studio video|kling (2\.[156]|3\.0|o1 video|avatars)|kling motion control'
    r'|lipsync studio|sync lipsync|\brecast\b|video upscale|video deflicker'
    r'|video background remover|\bdop\b|director panel',
    re.I)
# Historical notes that name removed models only to record the removal.
ALLOWED_LINES = ('removed', '已删除', '不再使用', 'not used by this studio')


class SeedanceOnlyVideoTests(unittest.TestCase):
    def test_video_specs_keep_only_seedance(self):
        specs = json.loads((ROOT / 'references/model-specs.json').read_text(encoding='utf-8'))
        self.assertEqual({m['id'] for m in specs['models']}, KEEP)
        table = (ROOT / 'references/MODEL-SPECS.md').read_text(encoding='utf-8')
        rows = [l for l in table.splitlines() if l.startswith('| ') and not l.startswith('| Model')]
        self.assertEqual(len(rows), len(KEEP))
        self.assertTrue(all('Seedance' in row for row in rows))

    def test_docs_do_not_route_to_removed_video_models(self):
        files = [ROOT / 'SKILL.md', *sorted((ROOT / 'references').glob('*.md'))]
        for path in files:
            for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
                if REMOVED.search(line) and not any(m in line for m in ALLOWED_LINES):
                    with self.subTest(file=path.name, line=number):
                        self.fail(line[:160])

    def test_seedance_2_5_snapshot_surface(self):
        s25 = next(m for m in json.loads((ROOT / 'references/model-specs.json').read_text(encoding='utf-8'))['models']
                   if m['id'] == 'seedance_2_5')
        self.assertEqual(s25['resolutions'], ['480p', '720p', '1080p'])
        self.assertIn('start_image', s25['media_roles']['medias'])


if __name__ == '__main__':
    unittest.main()

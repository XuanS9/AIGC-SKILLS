"""Real validators on the story-to-assets teaching example.

These tests prove template/feature coverage, not design causality, usability,
or generated-image quality. Manual evidence is recorded in the example.
"""
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
REF = ROOT / 'references'
sys.path.insert(0, str(ROOT / 'scripts'))
import asset_basis_lint as basis_lint

EXAMPLE = REF / 'template-story-driven-assets.md'
FEATURES = {
    '顾禾': ('C', ['两侧袖口收束且完整']),
    '闻柯': ('C', ['闻柯，45岁男性']),
    '木折尺': ('P', ['两片等长窄木尺', '一枚铜轴']),
    '修护廊道': ('S', ['右侧外墙唯一门洞', '长约8cm的边缘缺口']),
}


def registry():
    assets = []
    for name, (kind, features) in FEATURES.items():
        basis = {key: {'text': f'测试索引：{name}，详见教学输入与设计说明',
                       'source': '教学小样 §1—2'}
                 for key in basis_lint.REQUIRED[kind]}
        basis['traces'] = {'text': '维护磨耗为候选，不包含后续新伤', 'source': '推导'}
        assets.append({'type': kind, 'name': name, 'handle': '@' + name,
                       'status': 'planned', 'file': None,
                       'prompt_file': EXAMPLE.name, 'design_basis': basis,
                       'script_features': [{'feature': f, 'scene': '教学输入与设计对应 §1—2',
                                            'where': 'base'} for f in features]})
    return {'schema_version': 1, 'assets': assets}


class StoryDrivenAssetExampleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = EXAMPLE.read_text(encoding='utf-8')
        template = (REF / 'template-character-asset-delivery.md').read_text(encoding='utf-8')
        code = re.search(r'```python\n(def validate_character_sheet\(text\):.*?)\n```',
                         template, re.S).group(1)
        namespace = {}
        exec(compile(code, str(REF / 'template-character-asset-delivery.md'), 'exec'), namespace)
        cls.validate_character = staticmethod(namespace['validate_character_sheet'])

    def test_example_has_four_complete_copyable_asset_prompts(self):
        bodies = re.findall(r'```text\n(.*?)\n```', self.document, re.S)
        self.assertEqual(len(bodies), 4)
        for asset in registry()['assets']:
            section = basis_lint.prompt_block(self.document, asset)
            self.assertIsNotNone(section, asset['name'])
            body = basis_lint.prompt_body(section)
            self.assertTrue(body.strip(), asset['name'])
            self.assertNotRegex(body, r'<[^>]+>')
            if asset['type'] == 'C':
                self.assertEqual(self.validate_character(body), [])

    def test_base_features_are_in_real_prompts(self):
        findings = basis_lint.check(registry(), REF)
        self.assertEqual([f for f in findings if f[0] == 'FAIL'], [])
        self.assertTrue(any(f[0] == 'WARN' and 'derived' in f[2] for f in findings))

    def test_moving_feature_to_design_note_fails_each_asset(self):
        for asset in registry()['assets']:
            phrase = asset['script_features'][0]['feature']
            with self.subTest(asset=asset['name']):
                section = basis_lint.prompt_block(self.document, asset)
                body = basis_lint.prompt_body(section)
                self.assertIn(phrase, body)
                changed = section.replace(body, body.replace(phrase, '未落实结构'), 1)
                changed = changed.replace('```text', f'设计说明：{phrase}\n```text', 1)
                doc = self.document.replace(section, changed, 1)
                with tempfile.TemporaryDirectory() as folder:
                    Path(folder, EXAMPLE.name).write_text(doc, encoding='utf-8')
                    fails = [f for f in basis_lint.check(registry(), Path(folder)) if f[0] == 'FAIL']
                self.assertTrue(any(f[1] == asset['handle'] and phrase in f[2] for f in fails))
                self.assertFalse(any(f[1] != asset['handle'] for f in fails))

    def test_body_and_signature_evidence_is_in_copy_blocks_not_only_summary(self):
        # These are literal design choices in this example, not a recognizability
        # metric or a requirement that every project must use these motifs.
        evidence = {'顾禾': ['肩胯接近等宽', '躯干紧凑', '自身左肩一整块深褐厚布护片'],
                    '闻柯': ['躯干偏长', '腰腹略厚', '领下一枚横向扁铜扣'],
                    '木折尺': ['轴端略扩宽成扁圆头', '深灰褐与浅木褐'],
                    '修护廊道': ['连续的三角木撑', '连续采光开口形成一条长亮带']}
        for asset in registry()['assets']:
            body = basis_lint.prompt_body(basis_lint.prompt_block(self.document, asset))
            for phrase in evidence[asset['name']]:
                with self.subTest(asset=asset['name'], phrase=phrase):
                    self.assertIn(phrase, body)

    def test_actor_layout_regressions_are_rejected(self):
        for asset in registry()['assets']:
            if asset['type'] != 'C':
                continue
            body = basis_lint.prompt_body(basis_lint.prompt_block(self.document, asset))
            for before, after in [('全图共 4 格', '全图共 5 格'),
                                  ('头部不入画', '头部完整入画'),
                                  ('声纹波形', '装饰花纹')]:
                with self.subTest(asset=asset['name'], before=before):
                    self.assertTrue(self.validate_character(body.replace(before, after)))


if __name__ == '__main__':
    unittest.main()

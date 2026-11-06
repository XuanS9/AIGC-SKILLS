"""Regression tests for asset_basis_lint.py and the design-basis contract."""
from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest

SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))
import asset_basis_lint as lint

PROMPTS = """# 艾莉娅（艾莉娅@艾莉娅）

```text
一张写实角色资产参考图，象牙白低跟系带短靴，家族戒指，
```

# 雨林河谷（雨林河谷@雨林河谷）

```text
干净的雨林环境资产参考图，低凹鞍部，
```
"""


def basis(**overrides):
    item = lambda text, source='剧本 1a': {'text': text, 'source': source}
    data = {'world': item('远古雨林'), 'identity': item('贵族旅行者'),
            'traces': item('无伤', '不适用：剧情起点未受伤'), 'origin': item('定制服装', '推导'),
            'personality': item('端正整洁')}
    data.update(overrides)
    return data


def registry(**asset_overrides):
    asset = {'name': '艾莉娅', 'handle': '@艾莉娅', 'file': None, 'status': 'planned',
             'type': 'C', 'prompt_file': 'prompts.txt', 'design_basis': basis(),
             'script_features': [{'feature': '系带短靴', 'scene': '剧本 5e', 'where': 'base'},
                                 {'feature': '右脚赤足', 'scene': '剧本 5f', 'where': 'state:赤足'}],
             'state_plan': [{'state': '赤足', 'first': '剧本 5f', 'change': '右靴遗失',
                             'until': '剧本 13e', 'own_image': True}]}
    asset.update(asset_overrides)
    return {'schema_version': 1, 'assets': [asset]}


class AssetBasisLintTests(unittest.TestCase):
    def run_check(self, reg, prompts=PROMPTS):
        with tempfile.TemporaryDirectory() as td:
            Path(td, 'prompts.txt').write_text(prompts, encoding='utf-8')
            return lint.check(reg, Path(td))

    def fails(self, findings):
        return [f for f in findings if f[0] == 'FAIL']

    def test_complete_record_passes_with_derived_warning(self):
        findings = self.run_check(registry())
        self.assertEqual(self.fails(findings), [])
        self.assertTrue(any('derived' in f[2] for f in findings))

    def test_missing_basis_key_source_or_reason_fails(self):
        cases = {
            'missing basis': registry(design_basis=None),
            'missing key': registry(design_basis={k: v for k, v in basis().items() if k != 'traces'}),
            'missing source': registry(design_basis=basis(world={'text': '雨林', 'source': ''})),
            'reason-less n/a': registry(design_basis=basis(traces={'text': '无', 'source': '不适用'})),
        }
        for name, reg in cases.items():
            with self.subTest(name=name):
                self.assertTrue(self.fails(self.run_check(reg)))

    def test_base_feature_must_appear_in_prompt_block(self):
        reg = registry(script_features=[{'feature': '家徽布片', 'scene': '剧本 3b', 'where': 'base'}])
        self.assertTrue(any('家徽布片' in f[2] for f in self.fails(self.run_check(reg))))
        # A feature present only in another asset's block does not count.
        reg = registry(script_features=[{'feature': '低凹鞍部', 'scene': '剧本 1a', 'where': 'base'}])
        self.assertTrue(self.fails(self.run_check(reg)))

    def test_state_feature_must_point_to_planned_state(self):
        reg = registry(state_plan=[])
        self.assertTrue(any('unplanned' in f[2] for f in self.fails(self.run_check(reg))))
        reg = registry(script_features=[{'feature': '泥污', 'scene': '剧本 4c', 'where': 'elsewhere'}])
        self.assertTrue(self.fails(self.run_check(reg)))

    def test_external_style_anchor_in_prompt_fails(self):
        prompts = PROMPTS.replace('一张写实角色资产参考图', '《权力的游戏》北境暗色历史奇幻的真人定妆摄影质感')
        self.assertTrue(any('style anchor' in f[2] for f in self.fails(self.run_check(registry(), prompts))))

    def test_untyped_assets_are_skipped_and_cli_exit_codes(self):
        self.assertEqual(lint.check({'assets': [{'name': 'x', 'handle': '@x'}]}, Path('.')), [])
        with tempfile.TemporaryDirectory() as td:
            Path(td, 'prompts.txt').write_text(PROMPTS, encoding='utf-8')
            reg = Path(td, 'asset-registry.json')
            reg.write_text(json.dumps(registry(), ensure_ascii=False), encoding='utf-8')
            run = lambda p: subprocess.run([sys.executable, str(SCRIPTS / 'asset_basis_lint.py'),
                                            '--asset-registry', str(p)], capture_output=True, text=True)
            self.assertEqual(run(reg).returncode, 0)
            reg.write_text(json.dumps(registry(design_basis=None)), encoding='utf-8')
            self.assertEqual(run(reg).returncode, 1)
            self.assertEqual(run(Path(td, 'missing.json')).returncode, 2)


if __name__ == '__main__':
    unittest.main()

"""Document wiring/guardrail regressions, NOT narrative-quality evaluation."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
TARGET = 'narrative-planning.md#多线叙事与交叉剪辑'


class NarrativePlanningContractTests(unittest.TestCase):
    def test_entry_and_consumers_route_to_shared_rule(self):
        for name in ['SKILL.md', 'references/directing-workflow.md',
                     'references/directorial-shot-design.md',
                     'references/director-compiler.md',
                     'references/template-general-director-2-5.md',
                     'references/production-checks.md']:
            with self.subTest(file=name):
                self.assertIn(TARGET, (ROOT / name).read_text())
        self.assertIn('## 多线叙事与交叉剪辑',
                      (ROOT / 'references/narrative-planning.md').read_text())

    def test_entry_separates_narrative_and_production(self):
        text = (ROOT / 'SKILL.md').read_text()
        for term in ['快切不等于交叉剪辑', '生成顺序不等于成片顺序',
                     '约30秒只是兼容素材的生成效率目标',
                     '多线叙事与揭示关卡', '现有结构lint不判定']:
            self.assertIn(term, text)

    def test_shared_rule_protects_reveals_and_offscreen_continuity(self):
        text = (ROOT / 'references/narrative-planning.md').read_text()
        for term in ['不规定所有重要角色必须在前30秒出现',
                     '用户锁定的事件顺序、揭晓节点、限知视角与一镜到底优先',
                     '观众知情与角色知情分开', '离画不是暂停',
                     '时间关系不明时不凭剪辑制造同时发生',
                     '先锁成片切点', '人工评审，不是生成实测']:
            self.assertIn(term, text)

    def test_workcard_carries_crosscut_decisions(self):
        text = (ROOT / 'references/directorial-shot-design.md').read_text()
        for term in ['有效行动线与故事时间关系：', '单线/交叉选择及理由：',
                     '各线首次露出、回切新增信息、汇合/揭晓点：',
                     '切离期间各线如何继续：']:
            self.assertIn(term, text)

    def test_scene_mapping_supports_disjoint_uses_without_new_images(self):
        text = (ROOT / 'references/asset-registry.md').read_text()
        self.assertIn('每个连续使用区间登记一条相同image_id的引用', text)
        self.assertIn('相同图号复用不新增图片', text)
        self.assertIn('不能用包含空档的大区间冒充连续取景', text)

    def test_edited_document_local_links_exist(self):
        files = ['SKILL.md'] + ['references/' + name + '.md' for name in [
            'narrative-planning', 'directorial-shot-design', 'directing-workflow',
            'director-compiler', 'template-general-director-2-5',
            'asset-registry', 'production-checks']]
        for file in files:
            path = ROOT / file
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' in target or target.startswith('#'):
                    continue
                with self.subTest(file=file, target=target):
                    self.assertTrue((path.parent / target.split('#')[0]).exists())


if __name__ == '__main__':
    unittest.main()

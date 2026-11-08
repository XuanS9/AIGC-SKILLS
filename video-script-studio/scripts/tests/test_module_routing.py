"""Document routing regressions; links do not prove actual runtime reading."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

class ModuleRoutingTests(unittest.TestCase):
    def test_reference_documents_reachable_from_entry(self):
        docs = {ROOT / 'SKILL.md', * (ROOT / 'references').glob('*.md')}
        seen, queue = set(), [ROOT / 'SKILL.md']
        while queue:
            path = queue.pop().resolve()
            if path in seen or path not in docs:
                continue
            seen.add(path)
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if not target.startswith(('http:', 'https:', '#')):
                    queue.append((path.parent / target.split('#')[0]).resolve())
        self.assertEqual(sorted(str(p.relative_to(ROOT)) for p in docs - seen), [])

    def test_auto_routes_and_acceptance_have_operational_modules(self):
        routes = (ROOT / 'references/load-map.md').read_text().split('**按内容自动接入**')[1].split('## 详规唯一归属')[0]
        checks = (ROOT / 'references/production-checks.md').read_text().split('## 统一调用与验收总表')[1]
        for name in ('higgsfield-camera.md', 'higgsfield-image-shots.md',
                     'higgsfield-prompt.md', 'higgsfield-troubleshoot.md'):
            with self.subTest(module=name):
                self.assertIn(f']({name})', routes)
                self.assertIn(f']({name})', checks)

    def test_camera_design_and_compilation_link_detail(self):
        for name in ('directorial-shot-design.md', 'director-compiler.md'):
            text = (ROOT / 'references' / name).read_text()
            self.assertIn('](higgsfield-camera.md)', text)
            self.assertIn('](load-map.md)', text)

    def test_film_reference_route_reaches_design_compilation_and_acceptance(self):
        target = 'directorial-shot-design.md#影片方法参考'
        for name in ('SKILL.md', 'references/load-map.md', 'references/production-checks.md',
                     'references/director-compiler.md', 'references/higgsfield-style.md'):
            with self.subTest(file=name):
                self.assertIn(target, (ROOT / name).read_text())
        template = (ROOT / 'references/template-general-director-2-5.md').read_text()
        self.assertIn('导演方案｜Clip <批-序>\n影片参考：', template)

    def test_film_reference_precedes_shot_decisions_and_keeps_evidence_limits(self):
        text = (ROOT / 'references/directorial-shot-design.md').read_text()
        section = text.split('## 影片方法参考')[1].split('## 导演决策流程')[0]
        for evidence in ('候选／待核验', '静帧只能支持构图光色', '不设数量配额',
                         '局部修订', '不新增强制文件或独立审批', '不采用的部分',
                         '生成正文只写可见的', '不得把自己的解读冒充导演原话'):
            self.assertIn(evidence, section)
        self.assertLess(text.index('## 影片方法参考'), text.index('## 导演决策流程'))

    def test_film_method_does_not_override_visual_reference(self):
        text = (ROOT / 'references/higgsfield-style.md').read_text()
        self.assertIn('两者可以参考不同影片', text)
        self.assertIn('互不自动覆盖', text)

    def test_cross_batch_reference_route_is_connected(self):
        target = 'directorial-shot-design.md#全片与跨批次继承'
        for name in ('SKILL.md', 'references/load-map.md', 'references/production-checks.md',
                     'references/project-workspace.md', 'references/director-compiler.md'):
            with self.subTest(file=name):
                self.assertIn(target, (ROOT / name).read_text())

    def test_reference_scope_inheritance_and_change_boundaries(self):
        text = (ROOT / 'references/directorial-shot-design.md').read_text()
        section = text.split('### 全片与跨批次继承')[1].split('### 证据与转化')[0]
        for rule in ('全片主参考', '场景辅助参考', 'Clip执行', 'Clip不独立选片',
                     '成片顺序中相邻Clip', '只更新映射，不触发重新选片',
                     '不连带换成辅助片的快剪', '受影响已交付内容标待复核',
                     '未受影响内容保留原确认与版本', '继承待核对', '不虚报跨批次一致性通过'):
            self.assertIn(rule, section)

    def test_project_and_delivery_record_method_versions(self):
        project = (ROOT / 'references/project-workspace.md').read_text()
        template = project.split('## project.md 模板')[1]
        for field in ('## 导演方法与影片参考', '全片方法入口与版本', '场景辅助',
                      '本批继承与映射', '方法变更与复核'):
            self.assertIn(field, template)
        delivery = (ROOT / 'references/template-general-director-2-5.md').read_text()
        self.assertIn('影片参考：<全片方法版本＋本场辅助版本/无', delivery)
        self.assertIn('本批继承：<适用Clip范围、成片相邻接缝', delivery)

    def test_visual_continuity_is_routed_through_production(self):
        target = 'higgsfield-style.md#跨clip画风与明暗连续性'
        for name in ('SKILL.md', 'references/load-map.md', 'references/director-compiler.md',
                     'references/production-checks.md', 'references/project-workspace.md',
                     'references/director-control-retake.md', 'references/template-general-director-2-5.md'):
            with self.subTest(file=name):
                self.assertIn(target, (ROOT / name).read_text())

    def test_visual_continuity_evidence_and_physical_light_boundaries(self):
        text = (ROOT / 'references/higgsfield-style.md').read_text()
        section = text.split('## 跨Clip画风与明暗连续性')[1].split('## 核心平台风格')[0]
        for rule in ('30秒是生成边界', '世界光源不随镜头翻转', '不强迫昼夜或室内外一样亮',
                     '静帧只能说明这些帧', '文字已核对／未生成，视觉未验收',
                     '不默认把前Clip尾帧当下一条首帧', '调完须复验', '前后两个接缝',
                     '不凭空强填曝光值', '不靠全局调色'):
            self.assertIn(rule, section)

    def test_visual_project_records_are_separate_from_director_method(self):
        text = (ROOT / 'references/project-workspace.md').read_text().split('## project.md 模板')[1]
        section = text.split('## 视觉基准与接缝检查')[1].split('## 导演方法与影片参考')[0]
        for field in ('全片视觉入口与版本', '实际视觉基准', '本场光照', 'Clip继承',
                      '接缝检查', '文字/静帧/动态各自状态', '修复与复验'):
            self.assertIn(field, section)

    def test_ensemble_continuity_routes_reach_design_and_retake(self):
        target = 'higgsfield-acting.md#多角色持续参与与防僵硬检查'
        for name in ('SKILL.md', 'references/load-map.md', 'references/directorial-shot-design.md',
                     'references/director-compiler.md', 'references/production-checks.md',
                     'references/template-general-director-2-5.md', 'references/director-control-retake.md',
                     'references/template-ensemble-reaction.md'):
            with self.subTest(file=name):
                self.assertIn(target, (ROOT / name).read_text())

    def test_ensemble_review_keeps_causality_stillness_and_evidence_limits(self):
        text = (ROOT / 'references/higgsfield-acting.md').read_text()
        section = text.split('#### 多角色持续参与与防僵硬检查')[1].split('#### 编译与取景')[0]
        for rule in ('说话权交接不重置身体', '逐人遮挡主角审阅', '静止可以有任务',
                     '不要求每人一直运动', '共同突响允许同步回头', '未察觉者继续既定活动',
                     '不得为防僵硬新增剧本没有的人', '静帧不能判断持续僵硬',
                     '不擅删重要角色', '不增必填提示词栏目'):
            self.assertIn(rule, section)

    def test_ensemble_example_audits_non_speakers_over_time(self):
        text = (ROOT / 'references/template-ensemble-reaction.md').read_text()
        section = text.split('## 逐角色持续参与复核')[1]
        for evidence in ('林岚', '周远', '陈禾', '从说话者变为听者',
                         '画外不写可见表情', '本页只是文字示范'):
            self.assertIn(evidence, section)

    def test_film_batch_planning_connected_to_entry_and_workflow(self):
        target = 'narrative-planning.md#全片规划与分批交付'
        for name in ('SKILL.md', 'references/load-map.md', 'references/sample-approval.md',
                     'references/project-workspace.md', 'references/production-checks.md',
                     'references/template-general-director-2-5.md'):
            with self.subTest(file=name):
                self.assertIn(target, (ROOT / name).read_text())

    def test_batch_rules_preserve_story_scope_and_no_fixed_quotas(self):
        text = (ROOT / 'references/narrative-planning.md').read_text()
        section = text.split('## 全片规划与分批交付')[1].split('### 导演决策到提示词')[0]
        for rule in ('全片节拍表', '场景/段落导演方案', '交付批次', '生成Clip',
                     '不按固定Clip数量或固定分钟数硬切', '交叉剪辑的关联行动线',
                     '先设计整场', '短片、Clip很少且设计稳定时可一次交付',
                     '不必只选开场', '当前阶段/授权范围', '未知后续标待补',
                     '最终全片通读', '只可核计划交接'):
            self.assertIn(rule, section)

    def test_project_batch_mapping_preserves_final_review(self):
        text = (ROOT / 'references/project-workspace.md').read_text().split('## project.md 模板')[1]
        section = text.split('## 全片节拍与交付批次映射')[1].split('## 批次与阶段进度')[0]
        for field in ('全片规划依据', '段落导演方案', '批次映射', '批次复核', '全片最终复核'):
            self.assertIn(field, section)

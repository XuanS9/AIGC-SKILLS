"""Routing/evidence-contract regressions, not semantic or generated-video tests."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


def doc(name):
    return (ROOT / name).read_text(encoding='utf-8')


class AcceptanceWorkflowTests(unittest.TestCase):
    def test_single_acceptance_owner_and_entry_route(self):
        self.assertEqual(doc('references/production-checks.md').count('## 统一调用与验收总表'), 1)
        for file in ['SKILL.md', 'references/directing-workflow.md',
                     'references/director-compiler.md', 'references/directorial-shot-design.md',
                     'references/template-general-director-2-5.md',
                     'references/project-workspace.md', 'references/sample-approval.md']:
            with self.subTest(file=file):
                self.assertIn('production-checks.md#统一调用与验收总表', doc(file))

    def test_complete_proofreading_requires_hash_bound_coverage(self):
        checks = doc('references/production-checks.md')
        skill = doc('SKILL.md')
        for value in ['scripts/proofread_manifest.py', '覆盖清单', 'SHA-256',
                      '哈希漂移都不得称校对通过', '语义仍按T1—T9人工审']:
            self.assertIn(value, checks)
        self.assertIn('proofread_manifest.py', skill)
        test_source = (ROOT / 'scripts' / 'tests' / 'test_proofread_manifest.py').read_text()
        for value in ['test_missing_clip_is_not_complete', 'test_unreviewed_clip_fails',
                      'test_modified_clip_invalidates_its_record']:
            self.assertIn(value, test_source)

    def test_default_performance_applies_outside_platform_branch(self):
        text = doc('SKILL.md')
        start = text.index('## 默认调用与验收执行')
        end = text.index('## 工作流程')
        self.assertLess(start, end)
        for value in ['有人物即默认调用已有表演与FACS适用部分', '无对白、静音和动作镜头', '不等用户提醒']:
            self.assertIn(value, text[start:end])

    def test_routing_records_execution_and_landing_not_just_loading(self):
        text = doc('references/production-checks.md')
        for value in ['适用任务/触发依据', '实际读取模块及小节', '正文落点或不适用理由',
                      '读取模块不等于落实要求', '适用模块漏读、所需描写未进入正文']:
            self.assertIn(value, text)

    def test_nonhuman_owner_and_callers(self):
        self.assertEqual(doc('references/higgsfield-acting.md').count('## 非人角色表演适配'), 1)
        for file in ['SKILL.md', 'references/narrative-planning.md',
                     'references/directing-workflow.md', 'references/production-checks.md',
                     'references/higgsfield-facs.md']:
            with self.subTest(file=file):
                self.assertIn('higgsfield-acting.md#非人角色表演适配', doc(file))

    def test_nonhuman_preserves_anatomy_and_approved_style(self):
        text = doc('references/higgsfield-acting.md').split('## 非人角色表演适配')[1].split('## 表演证据验收')[0]
        for value in ['人类FACS不自动迁移到非人面部', '某物种没有的器官不写',
                      '不凭空增加脸', '不以写实默认删除', '不是越强越好',
                      '结构未知且影响关键动作则标待核验']:
            self.assertIn(value, text)

    def test_performance_has_eight_evidence_dimensions(self):
        text = doc('references/higgsfield-acting.md').split('## 表演证据验收')[1].split('# Part IV')[0]
        rows = re.findall(r'^\| ([^|\n]+) \|', text, re.M)
        expected = ['动机与注意', '表情与情绪发展', '听者及群体', '景别与身体',
                    '时序与接缝', '声音与表情', '风格与幅度', '非人适配']
        self.assertEqual(rows[1:], expected)
        self.assertIn('对象/版本/镜头时段＋演出原句', text)
        self.assertIn('不能以自评4分替代正文证据', text)

    def test_four_states_and_non_compensable_failures(self):
        text = doc('references/production-checks.md')
        for value in ['**通过**', '**失败**', '**待核验**', '**不适用**',
                      '适用的关键项失败不能被其他项高分抵消',
                      '未生成的视觉效果记待核验，不记不适用',
                      '缺实图/绑定不自动阻塞文字层']:
            self.assertIn(value, text)

    def test_three_acceptance_layers_have_unique_complete_ids(self):
        text = doc('references/production-checks.md')
        ids = re.findall(r'^\| ([TBV]\d+) ', text, re.M)
        expected = [f'T{i}' for i in range(1, 10)] + [f'B{i}' for i in range(1, 4)] + [f'V{i}' for i in range(1, 4)]
        self.assertEqual(ids, expected)
        self.assertIn('单段通过不能宣称整集通过', text)
        self.assertIn('只看静帧不能宣称动作或口型通过', text)

    def test_generation_grouping_is_mandatory_before_short_exceptions(self):
        text = doc('references/narrative-planning.md')
        for value in ['默认尽量接近30秒，先合并兼容内容', '每条保留为短生成的片段',
                      '记录合并候选及不能合并的具体理由',
                      '“剧情本来只有18秒”“不注水”不是完成合并核对的证明']:
            self.assertIn(value, text)
        for file in ['SKILL.md', 'references/director-compiler.md',
                     'references/directing-workflow.md', 'references/production-checks.md']:
            self.assertIn('narrative-planning.md#生成分组与短段例外验收', doc(file))

    def test_grouping_preserves_edit_map_and_avoids_duplicate_jobs(self):
        text = doc('references/narrative-planning.md')
        for value in ['生成片内区间→成片入出点', '计划生成时长/净使用时长',
                      '不能把合并后的母稿和被覆盖的短稿同时列作独立待生成任务',
                      '同场景不是自动兼容', '连续同场12秒＋18秒',
                      '上限不足30秒或只有离散档位', '不截断关键对白、命中或表演']:
            self.assertIn(value, text)

    def test_no_new_approval_or_project_directory_gate(self):
        text = doc('references/production-checks.md')
        for value in ['不新增用户审批', '无工作区时仅在复制块外交接',
                      '不另建强制目录/台账', '不索要全套素材作为写文字稿的前置']:
            self.assertIn(value, text)
        self.assertIn('不改原schema_version或资产必填字段', doc('references/project-workspace.md'))

    def test_audio_and_scene_engine_use_four_sections(self):
        for file in ['references/higgsfield-audio.md', 'references/higgsfield-scene-engine.md']:
            self.assertNotIn('seven-section', doc(file))
            self.assertIn('four-section', doc(file))
        audio = doc('references/higgsfield-audio.md')
        self.assertIn('native Cinema Studio SCELA submission', audio)
        self.assertIn('audio-only tasks', audio)
        workflow = doc('references/directing-workflow.md')
        self.assertNotIn('用 `<音效>`/`{台词}` 标记', workflow)
        self.assertIn('说话动词「原句」', workflow)

    def test_acting_has_no_universal_count_age_or_score_rules(self):
        text = doc('references/higgsfield-acting.md')
        for forbidden in ['only ≤3 characters', 'No age words anywhere',
                          'age-blind characters', '**Aim every hero shot at 4+.**',
                          'Every profile carries at least one',
                          'holds only three or four voices']:
            self.assertNotIn(forbidden, text)
        for required in ['Delivery is\nscene-dependent', 'sleeping or unconscious figures',
                         'A pure emotion, sustained stillness or simple truthful response can pass']:
            self.assertIn(required, text)

    def test_facs_optional_not_an_output_or_anatomy_requirement(self):
        text = doc('references/higgsfield-facs.md')
        self.assertIn('Reading this module does not require using AU codes or generating a sheet', text)
        self.assertNotIn('Duchenne smile — forced warmth', text)
        self.assertNotIn('forced Duchenne warmth', text)
        self.assertIn('neither quoting dialogue nor writing AUs guarantees synchronized mouths', text)
        self.assertIn('stylized/cartoon expression is valid when established', text)

    def test_modified_docs_local_links_and_new_anchors_exist(self):
        files = ['SKILL.md'] + ['references/' + s + '.md' for s in [
            'production-checks', 'higgsfield-acting', 'higgsfield-facs', 'higgsfield-audio',
            'higgsfield-scene-engine', 'narrative-planning', 'directing-workflow',
            'director-compiler', 'directorial-shot-design', 'template-general-director-2-5',
            'project-workspace', 'sample-approval']]
        new_anchors = {'统一调用与验收总表', '非人角色表演适配', '表演证据验收', '生成分组与短段例外验收'}
        for file in files:
            path = ROOT / file
            for target in re.findall(r'\]\(([^)]+)\)', doc(file)):
                if '://' in target:
                    continue
                name, _, anchor = target.partition('#')
                destination = path.parent / name if name else path
                with self.subTest(file=file, target=target):
                    self.assertTrue(destination.is_file())
                    if anchor in new_anchors:
                        self.assertRegex(destination.read_text(), rf'(?m)^#{{1,6}} {re.escape(anchor)}$')


if __name__ == '__main__':
    unittest.main()

"""Post-edit contract regressions; no generated-video or semantic quality claim."""
from decimal import Decimal
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import director_contract_lint as lint


ACTIVE = [
    'SKILL.md', 'references/production-checks.md',
    'references/narrative-planning.md', 'references/directing-workflow.md',
    'references/director-compiler.md', 'references/sample-approval.md',
    'references/template-general-director-2-5.md',
    'references/template-character-asset-delivery.md',
]


def doc(name):
    return (ROOT / name).read_text(encoding='utf-8')


def samples():
    section = doc('references/template-general-director-2-5.md').split(
        '## 5. 三个泛化小样\n', 1)[1].split('## 6. 交付前检查', 1)[0]
    return re.findall(r'```text\n(.*?)\n```', section, re.S)


class PostEditReviewTests(unittest.TestCase):
    def test_entry_summary_and_all_execution_routes_require_review(self):
        entry = doc('SKILL.md')
        self.assertIn('## 当前提示词标准与修改纪律', entry)
        self.assertIn('每次修改后必复查', entry)
        for file in ACTIVE:
            with self.subTest(file=file):
                self.assertIn('production-checks.md#修改后标准复查闭环', doc(file))

    def test_single_owner_covers_final_readback_dependencies_and_repair_loop(self):
        text = doc('references/production-checks.md')
        self.assertEqual(text.count('## 修改后标准复查闭环'), 1)
        section = text.split('## 修改后标准复查闭环', 1)[1].split('## 统一调用与验收总表', 1)[0]
        for value in ['重新读取最终落盘稿', '批量修改逐条检查全部改动Clip/图片',
                      '修改Clip同时核前后接缝', '重排核全部新相邻接缝',
                      '不能将旧版通过记录挪作新版结论', '失败修复并重跑',
                      '同范围 `--dialogue-source`', '说话人与顺序另核',
                      '内部复查不新增用户审批', '测试通过只证明已覆盖项',
                      '入口→详规→模板/示例→检查器/测试',
                      '未生成，视觉未验收', '不改用户项目']:
            with self.subTest(value=value):
                self.assertIn(value, section)

    def test_active_copy_contract_has_no_legacy_reference_header(self):
        for file in ACTIVE + ['references/asset-registry.md']:
            with self.subTest(file=file):
                self.assertNotIn('【资产与参考锁定】', doc(file))
        self.assertIn('视频直接写 `@中文名`', doc('references/director-compiler.md'))

    def test_missing_references_does_not_automatically_drop_sections(self):
        text = doc('references/narrative-planning.md')
        self.assertNotIn('素材少时可省本段', text)
        self.assertNotIn('素材少就删【参考素材职责】', text)
        self.assertIn('没有参考也保留本栏', text)
        self.assertIn('仅明确精简请求或实际提交硬限制', text)
        self.assertNotIn('默认电影级写实质感', text)

    def test_character_to_video_handoff_has_no_old_audio_or_identity_rules(self):
        text = doc('references/template-character-asset-delivery.md')
        handoff = text.split('## 5. 视频提示词的衔接标准', 1)[1].split('## 6.', 1)[0]
        self.assertNotIn('有声音时单独编写音频', handoff)
        self.assertNotIn('首次出现附一个辨识标记', handoff)
        self.assertIn('声音/对白内联进对应发声动作，不单列音频栏', handoff)
        self.assertIn('内部绑定/素材整理示例，不是视频复制正文', text)
        self.assertNotIn('写实电影质感，高清细节', text)

    def test_all_current_director_samples_pass_real_contract_checker(self):
        examples = samples()
        self.assertEqual(len(examples), 3)
        for body, duration in zip(examples, [12, 15, 10]):
            with self.subTest(duration=duration):
                self.assertEqual(lint.check_document(body, Decimal(duration),
                                                    '本段无对白（设计）'), ([], 1))
                beats = list(lint.TIME.finditer(body))
                # These particular examples use one explicit shot per beat;
                # this is not an automatic shot-length test for arbitrary prose.
                self.assertTrue(all(Decimal(m.group(2)) - Decimal(m.group(1)) <= 3
                                    for m in beats))
                for beat in beats[1:]:
                    end = next((m.start() for m in beats if m.start() > beat.start()), len(body))
                    self.assertIn('切', body[beat.end():end])

    def test_sample_mutations_are_rejected(self):
        body = samples()[0]
        for old, new in [
            ('【参考素材职责】', '【资产与参考锁定】'),
            ('【全局补充】', '【声音与连续性】'),
            ('3s-6s：', '4s-6s：'),
            ('本段无对白（设计）。', ''),
            ('NO BGM', '(背景播放钢琴)'),
        ]:
            with self.subTest(old=old):
                self.assertTrue(lint.check_document(body.replace(old, new))[0])

    def test_current_samples_cli_duration_and_dialogue_truth(self):
        with tempfile.TemporaryDirectory() as folder:
            prompt = Path(folder) / 'sample.txt'
            truth = Path(folder) / 'truth.txt'
            truth.write_text('本段无对白（设计）', encoding='utf-8')
            for body, duration in zip(samples(), [12, 15, 10]):
                prompt.write_text(body, encoding='utf-8')
                result = subprocess.run([
                    sys.executable, str(ROOT / 'scripts/director_contract_lint.py'),
                    '--file', str(prompt), '--duration', str(duration),
                    '--dialogue-source', str(truth),
                ], capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_review_links_and_anchor_exist(self):
        destination = ROOT / 'references/production-checks.md'
        self.assertRegex(destination.read_text(encoding='utf-8'),
                         r'(?m)^## 修改后标准复查闭环$')
        for file in ACTIVE:
            for target in re.findall(r'\]\(([^)]+)\)', doc(file)):
                if '://' in target:
                    continue
                name, _, anchor = target.partition('#')
                path = (ROOT / file).parent / name if name else ROOT / file
                with self.subTest(file=file, target=target):
                    self.assertTrue(path.is_file())


if __name__ == '__main__':
    unittest.main()

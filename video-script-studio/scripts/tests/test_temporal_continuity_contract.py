"""Guardrail/document regressions; these do NOT verify physical timing or acting."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
TARGET = 'narrative-planning.md#动作同步接缝去重与整场节奏'


class TemporalContinuityContractTests(unittest.TestCase):
    def test_execution_routes_share_temporal_rule(self):
        files = ['SKILL.md', 'references/directing-workflow.md',
                 'references/director-compiler.md', 'references/production-checks.md',
                 'references/directorial-shot-design.md', 'references/fight-director.md',
                 'references/template-general-director-2-5.md',
                 'references/template-full-performance-example.md']
        for name in files:
            with self.subTest(name=name):
                self.assertIn(TARGET, (ROOT / name).read_text())

    def test_rigid_cut_quotas_do_not_override_real_time(self):
        for name in ['SKILL.md', 'references/narrative-planning.md',
                     'references/template-general-director-2-5.md',
                     'references/template-full-performance-example.md']:
            text = (ROOT / name).read_text()
            for forbidden in ['任何 > 3 秒的单镜必须', '整体镜头均长控制在',
                              '默认切约 10–15', '每个 5 秒招式段内部应再拆']:
                with self.subTest(name=name, forbidden=forbidden):
                    self.assertNotIn(forbidden, text)
        entry = (ROOT / 'SKILL.md').read_text()
        self.assertIn('不规定每个 Clip 的分镜数量', entry)
        self.assertIn('不设单镜3秒上限', entry)
        self.assertIn('每个 Clip≤30秒', entry)
        for name in ['SKILL.md', 'references/narrative-planning.md',
                     'references/directing-workflow.md', 'references/directorial-shot-design.md',
                     'references/template-general-director-2-5.md',
                     'references/template-full-performance-example.md', 'references/production-checks.md']:
            text = (ROOT / name).read_text()
            for old in ['单镜≤3秒', '默认2–3秒', '默认每镜2–3秒', '强制运行单镜≤3秒硬校验',
                        '超过3秒即失败', '单镜≤3秒硬校验', '通常约10–15镜']:
                with self.subTest(name=name, old=old):
                    self.assertNotIn(old, text)
        self.assertIn('不能为了插入反应或特写拖长', entry)
        self.assertIn('同镜继续', entry)

    def test_clip_limit_and_overflow_flow_are_shared(self):
        target = 'narrative-planning.md#单个clip的30秒硬上限与超量处理'
        for name in ['SKILL.md', 'references/directing-workflow.md',
                     'references/project-workspace.md', 'references/production-checks.md']:
            with self.subTest(name=name):
                self.assertIn(target, (ROOT / name).read_text())
        text = (ROOT / 'references/narrative-planning.md').read_text()
        for phrase in ['总时长不得超过30秒', '压缩或顺延', '下一条片内时间从0开始',
                       '不截断一句对白', '需要时增加后续 Clip', '不能用“最后会裁掉”放行']:
            self.assertIn(phrase, text)

    def test_events_and_sound_phase_checked_at_seams(self):
        text = (ROOT / 'references/narrative-planning.md').read_text()
        for term in ['必要先后', '能够并行', '命中必须发生在到达目标的窗口内',
                     '事件身份、完成状态、位置与动量、声源相位',
                     '声音桥先交代同一声源', '成片只计净保留时间']:
            self.assertIn(term, text)

    def test_scene_level_review_has_no_automatic_gap_threshold(self):
        text = (ROOT / 'references/narrative-planning.md').read_text()
        for term in ['问句结束→回答开始', '行动线最后露出→再次露出',
                     '成片间隔不是故事行程时间', '不机械每隔N秒插一次追兵',
                     '必要提醒优先放在情绪段落之间']:
            self.assertIn(term, text)

    def test_recut_preserves_identity_and_rechecks_new_neighbors(self):
        text = (ROOT / 'references/narrative-planning.md').read_text()
        for term in ['video_delivery.edit_order', '新相邻接缝',
                     '减掉的重复时间不再填回原30秒', '对白顺序变化时记录例外',
                     '不证明实时物理或戏剧合理性']:
            self.assertIn(term, text)

    def test_fight_module_does_not_force_extra_sections_or_frozen_ending(self):
        text = (ROOT / 'references/fight-director.md').read_text()
        for forbidden in ['增设「行为与交互铁律」栏', '补「完整负面提示词」栏',
                          '**尾帧禁止收势离场**']:
            self.assertNotIn(forbidden, text)
        self.assertIn('段落按剧情逃离、停下、死亡或余韵', text)
        self.assertIn('四段式', text)

    def test_large_spatial_transfers_use_a_cut_or_whip_pan(self):
        target = 'directorial-shot-design.md#大幅度空间转移必须拆镜或用甩镜头过桥'
        for name in ['SKILL.md', 'references/directing-workflow.md',
                     'references/narrative-planning.md',
                     'references/director-compiler.md',
                     'references/production-checks.md',
                     'references/spatial-layout.md']:
            text = (ROOT / name).read_text()
            with self.subTest(name=name):
                if name == 'SKILL.md':
                    self.assertIn('大幅度物理空间转移不得只写成“从A到B”的单画面运镜', text)
                    self.assertIn(target, text)
                else:
                    self.assertTrue(
                        '大幅度' in text and ('甩镜' in text or '甩出' in text),
                        'spatial transfer rule is not wired into ' + name)

        planning = (ROOT / 'references/narrative-planning.md').read_text()
        for term in ['起点镜、交接和终点镜', '不能只写“从A移动到B”',
                     '不是让A和B在同一清晰画面中渐变叠加']:
            self.assertIn(term, planning)

    def test_spatial_transfer_one_take_is_a_scoped_exception(self):
        for name in ['SKILL.md', 'references/narrative-planning.md',
                     'references/director-compiler.md',
                     'references/template-general-director-2-5.md',
                     'references/spatial-layout.md']:
            text = (ROOT / name).read_text()
            with self.subTest(name=name):
                self.assertIn('一镜到底', text)
                self.assertIn('中间地标', text)
                self.assertIn('经过时间', text)


if __name__ == '__main__':
    unittest.main()

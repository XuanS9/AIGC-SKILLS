"""Regression tests for the studio video prompt contract ([具体情节] segments, dialogue lines in [声音])."""
from decimal import Decimal
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import director_contract_lint as lint
from studio_fixtures import HM, KEY, KEY_SEGMENTS, audio, fenced, prompt, segment, with_dialogue

PROMPT = KEY
SPOKEN = with_dialogue()
LINE = '{Here you go.}'
CHAR = '林岚。本段状态：站在柜台前，右手捏着钥匙。'
REF = PROMPT.replace('[参考资产]\n本段无参考资产。', '[参考资产]\n@林岚 对应 林岚。').replace('[生成目标]', '[角色]\n只有 1 人，不出现其他人：林岚。\n' + CHAR + '\n\n[生成目标]').replace(
    '本段无对白（设计）。', '本段无对白（设计）。\n' + HM.replace('她', '林岚') + '\n')


def one(end='3', move='固定', camera='固定，平视，不推拉。', size='近景', fov=29):
    return prompt([segment('0', end, size, fov, move, picture='她站在柜台前，画面左侧是窗，背景是货架。', camera=camera,
                           action='她先把钥匙推到指尖，再前伸约 20 cm 后站定。', expression='她目光落在钥匙上，嘴唇抿紧。',
                           end_state='最后一秒她站定不动。')], cut=False)


class ContractTests(unittest.TestCase):
    def test_raw_and_fenced_prompt(self):
        self.assertEqual(lint.check_document(PROMPT, Decimal(5)), ([], 1))
        self.assertEqual(lint.check_document(REF), ([], 1))
        self.assertEqual(lint.check_document(SPOKEN, dialogue_source=LINE), ([], 1))

    def test_multiple_clips_and_dialogue_truth(self):
        text = fenced(SPOKEN) + fenced(SPOKEN, name='1-2')
        self.assertEqual(lint.check_document(text, dialogue_source='「Here you go.」\n' + LINE), ([], 2))
        errors, _ = lint.check_document(SPOKEN, dialogue_source=LINE + '\n' + LINE)
        self.assertTrue(any('缺失 1 次' in e for e in errors))
        errors, _ = lint.check_document(fenced(SPOKEN) + fenced(SPOKEN, name='2-1'), dialogue_source=LINE)
        self.assertTrue(any('新增/重复 1 次' in e for e in errors))

    def test_metadata_outside_fence_is_not_dialogue(self):
        text = fenced(SPOKEN) + '\n检查说明：{这句不是台词}\n'
        self.assertEqual(lint.check_document(text, dialogue_source=LINE), ([], 1))

    def test_mutations_fail(self):
        cases = {
            'old stage blocks': PROMPT.replace('[具体情节]', '[阶段1 | 0-1秒 | 全景 | 视场角84° | 固定]'),
            'english block labels': PROMPT.replace('[生成目标]', '[Generation Goal]'),
            'legacy four-section heading': PROMPT.replace('[生成目标]', '【一句话概述】'),
            'legacy quote': SPOKEN.replace(LINE, '「Here you go.」'),
            'chinese dialogue': SPOKEN.replace(LINE, '{给你。}'),
            'dialogue in action': SPOKEN.replace('她才松开手指', '她才松开手指，说' + LINE).replace('2.5s-5s｜她压低气音说：' + LINE + '\n', ''),
            'dialogue line inside a segment': SPOKEN.replace('→ 结束：她的右手收回', '对白：她说：' + LINE + '\n→ 结束：她的右手收回').replace('2.5s-5s｜她压低气音说：' + LINE + '\n', ''),
            'untimed dialogue in audio': SPOKEN.replace('2.5s-5s｜她压低气音说：', '她压低气音说：'),
            'dialogue past the timeline': SPOKEN.replace('2.5s-5s｜她压低', '2.5s-7s｜她压低'),
            'sfx outside sound line': PROMPT.replace('她右手捏住', '<轻响>她右手捏住'),
            'no dialogue language': SPOKEN.replace('对白语言：英语。', ''),
            'silence in music bracket': PROMPT.replace('NO BGM。', '(无音乐)'),
            'no NO BGM': PROMPT.replace('NO BGM。', ''),
            'missing block': PROMPT.replace('[视觉风格]\n侧窗柔光从画面左侧射入，色温 4000K，玻璃反光低对比。\n\n', ''),
            'unknown block': PROMPT.replace('[视觉风格]', '[备注]'),
            'duplicate block': PROMPT + '\n[镜头]\n固定。\n',
            'wrong order': PROMPT.replace('[视觉风格]', '[TMP]').replace('[镜头]', '[视觉风格]').replace('[TMP]', '[镜头]'),
            'empty block': PROMPT.replace('她在柜台旁递还钥匙，对方接住。', ''),
            'content before first block': '前言。\n' + PROMPT,
            'content before first segment': PROMPT.replace('[具体情节]\n', '[具体情节]\n开场说明。\n'),
            'gap': PROMPT.replace('2.5s-5s｜', '3s-5s｜'),
            'overlap': PROMPT.replace('2.5s-5s｜', '2s-5s｜'),
            'not from zero': PROMPT.replace('0s-2.5s｜', '1s-2.5s｜'),
            'reverse': PROMPT.replace('2.5s-5s｜', '2.5s-1s｜'),
            'bad segment head': PROMPT.replace('｜视场角47°', '｜47°'),
            'off-anchor fov': PROMPT.replace('视场角47°', '视场角50°'),
            'non-size word': PROMPT.replace('侧面中景', '侧面看过去'),
            'no photography line': PROMPT.replace('摄影：', '构图：', 1),
            'no performance line': PROMPT.replace('演出：', '表演：', 1),
            'empty photography': PROMPT.replace('摄影：固定，平视，不推拉。柜台横在画面中部，她站在画面左，对方站在画面右。', '摄影：'),
            'duplicate photography': PROMPT.replace('摄影：', '摄影：固定。\n摄影：', 1),
            'legacy segment head': PROMPT.replace('视场角47°', '视场角47°｜固定', 1),
            'legacy field': PROMPT.replace('摄影：', '画面：', 1),
            'no end line': PROMPT.replace('→ 结束：钥匙仍在她指间。', '钥匙仍在她指间。'),
            'stray line': PROMPT.replace('摄影：', '随便一行。\n摄影：', 1),
            'settings inside': PROMPT.replace('NO BGM。', 'NO BGM。\n时长：5秒'),
            'no subtitles line': PROMPT.replace('无字幕、无水印。', ''),
            'contradictory silence': SPOKEN.replace('对白语言：英语。', '对白语言：英语。本段无对白（设计）。'),
            'no dialogue marker': PROMPT.replace('本段无对白（设计）。', ''),
            'empty dialogue': SPOKEN.replace(LINE, '{}'),
            'broken brace': SPOKEN.replace(LINE, '{Here you go.'),
            'nested brace': SPOKEN.replace(LINE, '{Here {you} go.}'),
        }
        for name, text in cases.items():
            with self.subTest(name=name):
                self.assertTrue(lint.check_document(text)[0])

    def test_higgsfield_readability_rules(self):
        cases = {
            'handle in plot': (REF.replace('她右手捏住', '@林岚 右手捏住'), '素材调用名'),
            'handle in goal': (REF.replace('她在柜台旁', '@林岚 在柜台旁'), '素材调用名'),
            'shot number': (PROMPT.replace('她右手捏住', '镜头1，她右手捏住'), '元语言'),
            'framing jargon': (PROMPT.replace('→ 结束：钥匙仍在她指间', '→ 结束：落幅钥匙仍在她指间'), '元语言'),
            'elision': (PROMPT.replace('对方手掌托住', '省略走到柜台的过程，对方手掌托住'), '元语言'),
            'cross-prompt ref': (PROMPT.replace('钥匙始终只有 1 把。', '同上，钥匙始终只有 1 把。'), '元语言'),
            'no count line': (REF.replace('只有 1 人，不出现其他人：林岚。\n', ''), '人数'),
            'no cut lock': (PROMPT.replace('只在指定处切镜，镜头不会自行切换。', ''), '只在指定处切镜'),
            'repeats plot': (PROMPT.replace('玻璃反光低对比', '对方手掌托住钥匙，她才松开手指'), '复述'),
            'scene without lock': (PROMPT.replace('[生成目标]', '[场景]\n柜台。柜台在画面中部。\n\n[生成目标]'), '场景只含参考所示内容'),
        }
        for name, (text, needle) in cases.items():
            with self.subTest(name=name):
                errors, _ = lint.check_document(text)
                self.assertTrue(any(needle in e for e in errors), errors)

    def test_fixed_asset_header(self):
        self.assertEqual(lint.check_document(REF), ([], 1))
        absent = REF.replace('[参考资产]\n@林岚 对应 林岚。\n\n', '')
        self.assertTrue(any('参考资产' in e for e in lint.check_document(absent)[0]))
        late = absent.replace('[具体情节]', '[参考资产]\n@林岚 对应 林岚。\n\n[具体情节]')
        self.assertTrue(lint.check_document(late)[0])
        for block in ('角色', '道具', '场景', '动作与声音参考', '声音', '保持一致'):
            with self.subTest(block=block):
                text = REF.replace('[' + block + ']', '[' + block + ']\n标签 @林岚。') if '[' + block + ']' in REF else REF.replace('[生成目标]', '[' + block + ']\n标签 @林岚。\n\n[生成目标]')
                self.assertTrue(any('素材调用名' in e for e in lint.check_document(text)[0]))
        for row in ('@林岚 对应 林岚。\n@林岚 对应 林岚。',
                    '角色｜林岚 对应 @林岚、@周远。',
                    '本段无参考资产。\n@林岚 对应 林岚。'):
            self.assertTrue(lint.check_document(REF.replace('@林岚 对应 林岚。', row))[0])
        many = REF.replace('@林岚 对应 林岚。',
                           '@林岚 对应 林岚。\n@幼龙 对应 幼龙。\n@钥匙 对应 钥匙。\n@柜台 对应 柜台。\n@递交参考 对应 递交参考。\n@声线参考 对应 声线参考。\n@暖光参考 对应 暖光参考。')
        for invalid in ('角色｜林岚 对应 @林岚。', '林岚 对应 @林岚。',
                        '- @林岚 对应 林岚。', '1. @林岚 对应 林岚。',
                        '@林岚、@周远 对应 两人。'):
            self.assertTrue(lint.check_document(REF.replace('@林岚 对应 林岚。', invalid))[0])
        compact = REF.replace('@林岚 对应 林岚。', '@林岚对应林岚。')
        self.assertEqual(lint.check_document(compact), ([], 1))
        renamed = REF.replace('@林岚 对应 林岚。', '@母亲定妆 对应 林岚。')
        self.assertEqual(lint.check_document(renamed), ([], 1))
        mixed = many.replace('@柜台 对应 柜台。', '@柜台 对应 柜台。\n@柜台 对应 另一个名称。')
        self.assertTrue(any('只列一次' in e for e in lint.check_document(mixed)[0]))
        self.assertEqual(lint.check_document(many), ([], 1))
        self.assertEqual(lint.check_document(PROMPT), ([], 1))

    def test_asset_introductions_and_states_are_not_lost(self):
        text = REF.replace('@林岚 对应 林岚。',
                           '@林岚 对应 林岚。介绍：旅人。本段状态：站在柜台前，右手捏钥匙。身高 165 cm。参考用途：身份与衣装。音色：female, low airy voice.')
        self.assertEqual(lint.check_document(text), ([], 1))
        for block in lint.split_blocks(lint.parse_clips(text)[0].body):
            if block[0] == '参考资产':
                for token in ('介绍：旅人', '本段状态：', '右手捏钥匙', '身高 165 cm', '参考用途：', '音色：'):
                    self.assertIn(token, block[2])
        compact = text.replace('@林岚 对应 林岚。', '@林岚对应林岚。')
        self.assertEqual(lint.check_document(compact), ([], 1))
        two = text.replace('只有 1 人，不出现其他人：林岚。', '只有 2 人，不出现其他人：林岚、周远。').replace(
            '[角色]', '@周远 对应 周远。本段状态：柜台后，左手接钥匙。身高 178 cm。\n\n[角色]')
        self.assertFalse(any('身高' in e for e in lint.check_document(two)[0]))

    def test_positioning_hm_fixes_blocking(self):
        self.assertEqual(lint.check_document(REF), ([], 1))
        errors, _ = lint.check_document(REF.replace(HM.replace('她', '林岚') + '\n', ''))
        self.assertTrue(any('定位秒' in e and 'Hm.' in e for e in errors), errors)
        errors, _ = lint.check_document(REF.replace('0s-2.5s｜林岚轻声', '0s-1s｜林岚轻声'))
        self.assertTrue(any('须与第一段' in e for e in errors), errors)
        nobody = REF.replace('只有 1 人，不出现其他人：林岚。\n' + CHAR, '只有 0 人：画面中没有人物。')
        self.assertTrue(any('只有 0 人' in e for e in lint.check_document(nobody)[0]))
        self.assertEqual(lint.check_document(nobody.replace(HM.replace('她', '林岚') + '\n', '')), ([], 1))
        # The hm is not script dialogue: the truth document need not contain it.
        self.assertEqual(lint.check_document(with_dialogue(REF), dialogue_source=LINE), ([], 1))

    def test_heights_required_for_two_characters(self):
        second = '周远。本段状态：站在柜台后。'
        two = REF.replace('只有 1 人，不出现其他人：林岚。', '只有 2 人，不出现其他人：林岚、周远。').replace(
            CHAR, CHAR + '\n' + second)
        self.assertTrue(any('身高' in e for e in lint.check_document(two)[0]))
        ok = two.replace(CHAR, CHAR + '身高 165 cm。').replace(second, second + '身高 178 cm。')
        self.assertFalse(any('身高' in e for e in lint.check_document(ok)[0]))
        # Creatures mapped with @ are not counted as people and need no height.
        beast = ok.replace(second + '身高 178 cm。', second + '身高 178 cm。\n古鳄。本段状态：半沉在水里。')
        self.assertFalse(any('身高' in e for e in lint.check_document(beast)[0]))

    def test_no_length_cap_and_state_line_needs_no_exclusion(self):
        long = REF.replace('指尖仍勾着环', '指尖仍勾着环，' + '袖口的毛线随手腕轻轻晃动，' * 200)
        self.assertFalse(any('字' in e and '上限' in e for e in lint.check_document(long)[0]))
        self.assertEqual(lint.check_document(REF), ([], 1))

    def test_continuous_take_needs_no_cut_lock(self):
        segs = [KEY_SEGMENTS[0], segment('2.5', '5', '双手近景', 29, '缓慢推近', picture='台面占满画面。',
                                         camera='用 2.5 秒前推约 20 cm，最后停住。', action='对方手掌托住钥匙。',
                                         expression='她的指尖发抖，呼吸放浅。', end_state='钥匙在对方掌心，镜头停住。')]
        self.assertEqual(lint.check_document(prompt(segs, cut=False)), ([], 1))

    def test_voice_description_only_in_characters(self):
        allowed = REF.replace(CHAR, CHAR + '音色：Voice: female, low airy mezzo.')
        self.assertEqual(lint.check_document(allowed), ([], 1))
        errors, _ = lint.check_document(PROMPT.replace('侧窗柔光', '音色：低中音。侧窗柔光'))
        self.assertTrue(any('音色描述只写在 [参考资产]/[角色]' in e for e in errors))

    def test_clip_limit(self):
        for end, passed in [('3', True), ('9', True), ('30', True), ('30.001', False), ('31', False)]:
            with self.subTest(end=end):
                self.assertEqual(not lint.check_document(one(end))[0], passed)
        errors, _ = lint.check_document(fenced(duration='31'))
        self.assertTrue(any('硬上限30秒' in e for e in errors))

    def test_each_clip_capped_but_document_total_can_exceed_thirty(self):
        long = PROMPT.replace('2.5s-5s｜', '2.5s-30s｜')
        self.assertEqual(lint.check_document(fenced(long, duration='30') + fenced(long, name='1-2', duration='30')), ([], 2))

    def test_segment_count_is_not_prescribed(self):
        for count in (1, 2, 6, 15):
            length = Decimal(30) / count
            segs = [segment(f'{length * i}', f'{length * (i + 1)}', '切至中景' if i else '全景', 47, '固定',
                            picture='人物站在路口，画面左侧是墙。', camera='固定，平视。', action='人物沿路前行。',
                            expression='人物抬头看路牌。', end_state='人物站定。') for i in range(count)]
            self.assertEqual(lint.check_document(prompt(segs), Decimal(30)), ([], 1), count)

    def test_wrong_duration(self):
        self.assertTrue(lint.check_document(PROMPT, Decimal(6))[0])
        self.assertTrue(lint.check_document(fenced(duration='6'))[0])

    def test_input_errors(self):
        for text in (
            fenced() + fenced(),
            fenced().replace('1-1｜', '01-1｜'),
            fenced().replace('1-1｜', '1｜'),
            fenced().rstrip()[:-3],
            fenced().replace('```text', '```json'),
            fenced() + '\n```text\nother\n```',
            PROMPT + '\n' + fenced(),
            fenced().replace('时长：5秒', '时长：5秒\n时长：6秒'),
            fenced().replace('时长：5秒', '时长：0秒'),
        ):
            with self.subTest(text=text[:60]), self.assertRaises(ValueError):
                lint.check_document(text)
        with self.assertRaises(ValueError):
            lint.check_document(fenced() + fenced(name='1-2'), Decimal(5))

    def test_no_phantom_clip_from_body(self):
        text = fenced(PROMPT.replace('NO BGM。', 'NO BGM。\n# Clip 7-7｜文本'))
        self.assertEqual(len(lint.parse_clips(text)), 1)

    def test_source_errors(self):
        for source in ['没有台词标记', '{Here you go.', '{}']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                lint.check_document(SPOKEN, dialogue_source=source)

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'prompt.txt'
            path.write_text(fenced(), encoding='utf-8')
            command = [sys.executable, str(Path(lint.__file__)), '--file', str(path)]
            for extra, code in [([], 0), (['--duration', 'NaN'], 2), (['--duration', 'bad'], 2)]:
                result = subprocess.run(command + extra, capture_output=True, text=True)
                self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                self.assertNotIn('Traceback', result.stderr)
            path.write_text(PROMPT.replace('无水印', ''), encoding='utf-8')
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 1)
            path.unlink()
            self.assertEqual(subprocess.run(command, capture_output=True).returncode, 2)


class CraftWarningTests(unittest.TestCase):
    def warns(self, text, needle):
        return any(needle in w for w in lint.boundary_warnings(text))

    def test_moving_camera_needs_distance_or_time(self):
        self.assertTrue(self.warns(one('6', '缓慢推近', '缓慢推近到特写。'), '未写距离'))
        self.assertFalse(self.warns(one('6', '缓慢推近', '用 5 秒从中景推近到特写，最后 1 秒停住。'), '未写距离'))

    def test_big_move_needs_more_time(self):
        self.assertTrue(self.warns(one('3', '缓慢推近', '用 3 秒从中景推近到特写，最后停住。'), '建议至少 6 秒'))
        self.assertFalse(self.warns(one('7', '缓慢推近', '用 6 秒从中景推近到特写，最后 1 秒停住。'), '建议至少'))
        self.assertTrue(self.warns(one('2', '环绕', '用 2 秒环绕 90°，最后停住。'), '建议至少 4 秒'))

    def test_conflicting_moves_warn(self):
        self.assertTrue(self.warns(one('6', '推近', '用 5 秒推近同时横摇。'), '一镜一个主运动'))

    def test_close_up_needs_two_to_four_cues(self):
        few = one().replace('她目光落在钥匙上，嘴唇抿紧。', '她很难过。')
        self.assertTrue(self.warns(few, '可见线索'))
        many = one().replace('她目光落在钥匙上，嘴唇抿紧。', '她眉心微收，眼眶泛红，嘴唇抿紧，鼻翼张开，喉结滚动，呼吸停顿，手指发抖。')
        self.assertFalse(self.warns(many, '偏多'))  # combined performance density requires semantic review
        self.assertFalse(self.warns(one(), '可见线索'))

    def test_picture_needs_two_layout_anchors(self):
        thin = one().replace('她站在柜台前，画面左侧是窗，背景是货架。', '她站在柜台前。')
        self.assertTrue(self.warns(thin, '方位词'))
        self.assertFalse(self.warns(one(), '方位词'))

    def test_natural_action_does_not_require_measure(self):
        thin = one('4').replace('她先把钥匙推到指尖，再前伸约 20 cm 后站定。', '她将钥匙推到指尖，伸手递出。')
        self.assertFalse(self.warns(thin, '动作写得太简略'))
        self.assertEqual(lint.check_document(thin)[0], [])
        full = one('4')
        self.assertFalse(self.warns(full, '动作写得太简略'))

    def test_interaction_can_be_inline_or_separate(self):
        two = '只有 2 人，不出现其他人：林岚、周远。\n林岚：短发。身高 165 cm。\n周远：衬衫。身高 178 cm。'
        body = one(size='双人中景', fov=47).replace('[生成目标]', '[角色]\n' + two + '\n\n[生成目标]')
        self.assertFalse(self.warns(body, '听者'))
        body = body.replace('她目光落在钥匙上，嘴唇抿紧。', '她目光落在钥匙上，嘴唇抿紧；周远见她停手，伸手托住钥匙。')
        body = body.replace('→ 结束：', '互动：周远看着她。\n→ 结束：')
        self.assertFalse(self.warns(body, '听者'))



def flat(n=8, size='中景', fov=47, move='固定', people=1, picture='她站在柜台前，画面左侧是窗，背景是货架。', dialogue=None):
    lines = ['0s-3s｜人0轻声：{Hm.}'] + ([f'3s-6s｜{dialogue}'] if dialogue else [])
    segs = [segment(f'{i * 3}', f'{i * 3 + 3}', (size if i == 0 else '切至' + size), fov, move,
                    picture=picture, camera='用 3 秒前推约 20 cm，最后停住。' if move != '固定' else '固定，平视。',
                    action='她先抬手约 10 cm，再把钥匙放到台面中央。', expression='她眉心微收，呼吸放浅。',
                    listener='对方看着她。' if people > 1 else None,
                    end_state='她站定。') for i in range(n)]
    names = '、'.join(f'人{i}' for i in range(people))
    heights = '\n'.join(f'人{i}：身高 17{i} cm。' for i in range(people))
    return prompt(segs, characters=f'只有 {people} 人，不出现其他人：{names}。\n{heights}',
                  audio=audio(*lines) if dialogue else '本段无对白（设计）。\n' + lines[0] + '\nNO BGM。')


class VarietyAndRiskTests(unittest.TestCase):
    def warns(self, text, needle):
        return any(needle in w for w in lint.boundary_warnings(text))

    def test_repeated_cuts_request_review_not_variety_quotas(self):
        text = flat()
        self.assertEqual(lint.check_document(text)[0], [])
        warnings = lint.variety_warnings(text)
        self.assertEqual(len(warnings), 1)
        self.assertIn('单调风险待复核', warnings[0])
        self.assertIn('有意重复可保留', warnings[0])
        for quota in ('至少 3 种', '至少 3 档', '至少给一个', '换景别或换角度'):
            self.assertNotIn(quota, warnings[0])

    def test_continuous_fixed_take_has_no_variety_quota(self):
        for text in (one('25'), flat().replace('切至中景', '中景')):
            self.assertEqual(lint.check_document(text)[0], [])
            self.assertEqual(lint.variety_warnings(text), [])

    def test_review_depends_on_repeated_shots_not_twenty_seconds(self):
        self.assertEqual(lint.variety_warnings(flat(2)), [])
        self.assertTrue(lint.variety_warnings(flat(3)))
        changing = flat(3).replace('3s-6s｜切至中景', '3s-6s｜切至近景')
        self.assertEqual(lint.variety_warnings(changing), [])

    def test_crowd_warns_unless_frame_limit_written(self):
        text = flat(2, people=5)
        self.assertTrue(self.warns(text, '同框 5 人'))
        limited = text.replace('不出现其他人：', '不出现其他人，每次最多 3 人入画：')
        self.assertFalse(self.warns(limited, '同框 5 人'))

    def test_dialogue_too_long_for_segment(self):
        line = '她说：{' + ' '.join(['word'] * 12) + '}'
        self.assertTrue(self.warns(flat(2, dialogue=line), '台词 12 个词'))
        self.assertEqual(lint.check_document(flat(2, dialogue=line))[0], [])
        self.assertFalse(self.warns(flat(2, dialogue='她说：{Here you go.}'), '个词约需'))

    def test_picture_in_picture_warns(self):
        text = flat(2, picture='屏幕里是四张笑脸，画面左侧是窗，背景是客舱。')
        self.assertTrue(self.warns(text, '画中画'))


ROOT = Path(__file__).resolve().parents[2]


def clip(name, first=('双人全景', 84, '固定', '画面：她站在柜台前，面向对方，右手握着钥匙。'),
         last=('切至近景', 29, '固定', '画面：她站在柜台前。', '最后一秒她站定不动，看着对方。')):
    size, fov, move, picture = first
    lsize, lfov, lmove, lpicture, lend = last
    segs = [segment('0', '1', size, fov, move, picture=picture.removeprefix('画面：') + '前景是台面边缘，背景是货架。', camera=move + '。',
                    action='两人站着不动。', expression='她目光落在钥匙上，嘴唇抿紧。',
                    listener='对方看着她。', end_state='两人站定。'),
            segment('1', '5', lsize, lfov, lmove, picture=lpicture.removeprefix('画面：') + '台面在画面下方，背景是虚化的货架。',
                    camera=('用 3 秒前推约 20 cm，最后停住。' if lmove != '固定' else '固定，平视。'),
                    action='她先抬手约 10 cm，再把钥匙放到台面中央。', expression='她眉心微收，呼吸放浅。', end_state=lend)]
    body = prompt(segs, goal='她递还钥匙。', style='侧窗柔光，4000K。',
                  consistency='钥匙始终只有 1 把。无字幕、无水印。')
    return f'# Clip {name}｜交还｜时长：5秒\n```text\n{body}```\n'


class ClipBoundaryWarningTests(unittest.TestCase):
    def test_clean_boundary_has_no_warnings(self):
        text = clip('1-1') + clip('1-2', first=('全景', 84, '固定', '画面：他坐在门边，面向柜台，双手空着。'))
        self.assertEqual(lint.check_document(text)[0], [])
        self.assertEqual(lint.boundary_warnings(text), [])

    def test_moving_tail_warns(self):
        text = clip('1-1', last=('切至近景', 29, '缓慢推近', '画面：她站在柜台前。', '她转身走向门口。'))
        text = text.replace('用 3 秒前推约 20 cm，最后停住。', '用 3 秒前推约 20 cm，一直推近。')
        self.assertTrue(any('尾镜可能仍在运动' in w for w in lint.boundary_warnings(text)))

    def test_opening_without_state_or_close_or_moving_warns(self):
        warnings = lint.boundary_warnings(clip('1-1', first=('全景', 84, '固定', '画面：光线变暗。')))
        self.assertTrue(any('人物位置' in w for w in warnings))
        warnings = lint.boundary_warnings(clip('1-1', first=('近景', 29, '固定', '画面：她的手握着钥匙。')))
        self.assertTrue(any('定位秒默认全景' in w for w in warnings))
        warnings = lint.boundary_warnings(clip('1-1', first=('全景', 84, '缓慢推近', '画面：她站在柜台前，右手握着钥匙。')))
        self.assertTrue(any('定位秒应为固定' in w for w in warnings))

    def test_medium_opening_is_allowed(self):
        text = clip('1-1', first=('双人中景', 47, '固定', '画面：她站在柜台前，面向对方，右手握着钥匙。'))
        self.assertFalse(any('定位秒默认' in w for w in lint.boundary_warnings(text)))

    def test_similar_sizes_across_boundary_warn(self):
        text = clip('1-1') + clip('1-2', first=('近景', 29, '固定', '画面：她站在柜台前，右手握着钥匙。'))
        self.assertTrue(any('1-1→1-2' in w for w in lint.boundary_warnings(text)))
        text = clip('1-1') + clip('1-2', first=('反打近景', 29, '固定', '画面：他站在柜台另一侧，双手空着。'))
        self.assertFalse(any('1-1→1-2' in w for w in lint.boundary_warnings(text)))

    def test_warnings_do_not_change_exit_code(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / 'p.txt'
            text = clip('1-1', last=('切至近景', 29, '缓慢推近', '画面：她站在柜台前。', '她转身走向门口。'))
            path.write_text(text.replace('最后停住', '一直推近'), encoding='utf-8')
            result = subprocess.run([sys.executable, str(ROOT / 'scripts/director_contract_lint.py'),
                                     '--file', str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout)
            self.assertIn('WARN:', result.stdout)


class CompactFormatTests(unittest.TestCase):
    def test_sync_performance_optional_interaction_and_natural_measure(self):
        scene = '''0s-3s｜中近景｜视场角47°
摄影：固定，侧面略俯；Runa在画面左下，工头腿部在右侧。
演出：Runa右掌向身下挪少许，借掌根撑起上身。右掌受力时动作短停，嘴唇轻颤、眼睑收窄；工头见她停下，空左手伸向她左上臂。
声音：<手掌擦过湿木板>
→ 结束：Runa上身稍起，工头左手已伸到她左上臂旁。'''
        body = prompt([scene], cut=False)
        self.assertEqual(lint.check_document(body)[0], [])
        seg = lint.split_segments(scene)[0]
        self.assertEqual(set(seg['fields']), {'摄影', '演出', '声音'})
        self.assertIn('受力时', seg['fields']['演出'][0])
        self.assertIn('固定', seg['move'])
        self.assertFalse(any('动作写得太简略' in w or '听者' in w
                             for w in lint.craft_warnings(body)))
        separate = body.replace('；工头见她停下', '。\n互动：工头见她停下')
        self.assertEqual(lint.check_document(separate)[0], [])

    def test_all_new_fields_nonempty_and_unique(self):
        for label in ('摄影', '演出'):
            with self.subTest(label=label):
                invalid = PROMPT.replace(label + '：', label + '：\n' + label + '：', 1)
                self.assertTrue(lint.check_document(invalid)[0])


if __name__ == '__main__':
    unittest.main()

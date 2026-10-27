"""Regression tests for the optional four-section text contract checker."""
from decimal import Decimal
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import director_contract_lint as lint


PROMPT = '''【参考素材职责】
本段采用纯文字描述，无参考素材。
【一句话概述】
她在柜台旁递还钥匙，侧面固定机位观察交接。
【具体情节】
0s-2.5s：侧面中景，她右手捏住钥匙环递到柜台中央，指尖仍勾着环；侧窗柔光映亮指背，玻璃反光低对比。钥匙轻触玻璃发出一声轻响，结束时仍在她指间。
2.5s-5s：切同轴线侧双手近景，对方手掌托住钥匙，她才松开手指，压低气音说「给你。」；固定机位保留钥匙落入对方掌心的结果，同一侧窗柔光沿手背滑过。结束时她的右手收回柜台外缘。
【全局补充】
位置、手别与持物连续。无字幕、无水印。NO BGM。
'''


def fenced(body=PROMPT, name='1-1', duration='5'):
    return f'# Clip {name}｜归还钥匙\n时长：{duration}秒\n```text\n{body}```\n'


class ContractTests(unittest.TestCase):
    def test_raw_prompt(self):
        self.assertEqual(lint.check_document(PROMPT, Decimal(5)), ([], 1))

    def test_multiple_clips(self):
        text = fenced() + fenced(name='1-2')
        self.assertEqual(lint.check_document(text, dialogue_source='「给你。」\n「给你。」'), ([], 2))

    def test_metadata_quotes_not_counted(self):
        text = fenced() + '\n检查说明：「这句不是台词」\n'
        self.assertEqual(lint.check_document(text, dialogue_source='「给你。」'), ([], 1))

    def test_repeated_dialogue_counts(self):
        errors, _ = lint.check_document(PROMPT, dialogue_source='「给你。」\n「给你。」')
        self.assertTrue(any('缺失 1 次' in error for error in errors))
        errors, _ = lint.check_document(fenced() + fenced(name='2-1'), dialogue_source='「给你。」')
        self.assertTrue(any('新增/重复 1 次' in error for error in errors))

    def test_no_dialogue_and_silent_design(self):
        silent = PROMPT.replace('，压低气音说「给你。」', '').replace('NO BGM。', '本段无对白（设计）。全程静音。')
        self.assertEqual(lint.check_document(silent, dialogue_source='本段无对白（设计）'), ([], 1))
        errors, _ = lint.check_document(silent.replace('本段无对白（设计）。', ''))
        self.assertTrue(any('显式标注' in error for error in errors))

    def test_mutations_fail(self):
        mutations = {
            'gap': ('2.5s-5s：', '3s-5s：'),
            'overlap': ('2.5s-5s：', '2s-5s：'),
            'not_zero': ('0s-2.5s：', '1s-2.5s：'),
            'zero_length': ('2.5s-5s：', '2.5s-2.5s：'),
            'reverse': ('2.5s-5s：', '2.5s-1s：'),
            'missing_section': ('【全局补充】', ''),
            'extra_section': ('NO BGM。', 'NO BGM。\n【结束状态】\n她停住。'),
            'duplicate_section': ('NO BGM。', 'NO BGM。\n【全局补充】\n无字幕、无水印。'),
            'legacy_dialogue': ('「给你。」', '{给你。}'),
            'legacy_effect': ('一声轻响', '<一声轻响>'),
            'legacy_music': ('NO BGM。', '(背景播放钢琴)'),
            'empty_dialogue': ('「给你。」', '「」'),
            'broken_quote': ('「给你。」', '「给你。'),
            'nested_quote': ('「给你。」', '「给「你」。」'),
            'settings_inside': ('NO BGM。', 'NO BGM。\n时长：5秒'),
            'fixed_voice_description': ('NO BGM。', 'NO BGM。\nRUNA固定声线：年轻低中音，宽胸腔共鸣。'),
            'english_voice_description': ('NO BGM。', 'NO BGM。\nVoice Description: warm female alto.'),
            'no_watermark': ('无水印', '清晰画面'),
            'malformed_time': ('2.5s-5s：', '2.5s-NaNs：'),
            'contradictory_silence': ('NO BGM。', 'NO BGM。本段无对白（设计）。'),
        }
        for name, (old, new) in mutations.items():
            with self.subTest(name=name):
                errors, _ = lint.check_document(PROMPT.replace(old, new))
                self.assertTrue(errors)

    def test_section_order_and_empty_content(self):
        for text in (
            PROMPT.replace('【一句话概述】', '【temp】').replace('【具体情节】', '【一句话概述】').replace('【temp】', '【具体情节】'),
            PROMPT.replace('本段采用纯文字描述，无参考素材。', ''),
            PROMPT.replace('【具体情节】\n', '【具体情节】\n未分配的动作。\n'),
            PROMPT.replace('【全局补充】', '声音：轻响\n【全局补充】'),
            PROMPT.replace('【一句话概述】\n', '【一句话概述】\n她说「额外台词」。\n'),
        ):
            self.assertTrue(lint.check_document(text)[0])

    def test_empty_beat(self):
        text = PROMPT.replace('0s-2.5s：', '0s-1s：\n1s-2.5s：')
        self.assertTrue(any('演出内容为空' in error for error in lint.check_document(text)[0]))

    def test_timestamp_variants(self):
        for first, second in [('0-2.5秒：', '2.5–5秒：'), ('0s — 2.5s:', '2.5s至5s：')]:
            text = PROMPT.replace('0s-2.5s：', first).replace('2.5s-5s：', second)
            self.assertEqual(lint.check_document(text, Decimal(5)), ([], 1))

    def test_long_shot_is_allowed_within_clip_limit(self):
        for end, passed in [('3', True), ('3.001', True), ('9', True),
                            ('30', True), ('30.001', False), ('31', False)]:
            body = PROMPT.split('【具体情节】')[0] + (
                f'【具体情节】\n0s-{end}s：固定近景，她递还钥匙，低声说「给你。」\n'
                '【全局补充】\n无字幕、无水印。NO BGM。\n')
            with self.subTest(end=end):
                self.assertEqual(not lint.check_document(body)[0], passed)

    def test_continuous_shot_can_span_multiple_rows(self):
        for continuation in ['同镜继续', '缓慢推近', '移焦到手部', '同一镜头继续，切近景']:
            body = PROMPT.replace('切同轴线侧双手近景', continuation)
            self.assertEqual(lint.check_document(body), ([], 1), continuation)

    def test_clip_limit_checks_declaration_even_if_timeline_is_short(self):
        for duration in ('30.001', '31', '60'):
            errors, _ = lint.check_document(fenced(duration=duration))
            self.assertTrue(any('声明时长' in e and '硬上限30秒' in e for e in errors))
        errors, _ = lint.check_document(PROMPT, Decimal('31'))
        self.assertTrue(any('硬上限30秒' in e for e in errors))

    def test_clip_limit_checks_every_beat_without_duration_metadata(self):
        body = PROMPT.replace('2.5s-5s：', '2.5s-31s：')
        errors, _ = lint.check_document(body)
        self.assertTrue(any('时间轴' in e and '硬上限30秒' in e for e in errors))
        # A late final row cannot hide an earlier overflowing interval.
        body = PROMPT.replace('2.5s-5s：', '2.5s-31s：切中景，交接。\n31s-5s：')
        self.assertTrue(any('硬上限30秒' in e for e in lint.check_document(body)[0]))

    def test_each_clip_is_capped_but_document_total_can_exceed_thirty(self):
        long = PROMPT.replace('2.5s-5s：', '2.5s-30s：')
        text = fenced(long, duration='30') + fenced(long, name='1-2', duration='30')
        self.assertEqual(lint.check_document(text), ([], 2))
        over = long.replace('2.5s-30s：', '2.5s-30.001s：')
        errors, _ = lint.check_document(fenced(long, duration='30') + fenced(over, name='1-2', duration='30.001'))
        self.assertTrue(any(e.startswith('1-2:') and '硬上限30秒' in e for e in errors))

    def test_shot_count_is_not_prescribed(self):
        for count in (1, 2, 6, 15, 30):
            length = Decimal(30) / count
            beats = '\n'.join(f'{length * i}s-{length * (i + 1)}s：切中景，人物继续沿路前行。'
                              for i in range(count))
            body = ('【参考素材职责】\n无参考。\n【一句话概述】\n人物沿路前行。\n'
                    '【具体情节】\n' + beats + '\n【全局补充】\n本段无对白（设计）。无字幕、无水印。')
            self.assertEqual(lint.check_document(body, Decimal(30)), ([], 1), count)

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
        with self.assertRaises(ValueError):
            lint.check_document(fenced(), Decimal(6))

    def test_no_phantom_clip_from_body(self):
        text = fenced(PROMPT.replace('NO BGM。', 'NO BGM。\n# Clip 7-7｜文本'))
        self.assertEqual(len(lint.parse_clips(text)), 1)

    def test_source_errors(self):
        for source in ['没有台词标记', '「给你。', '「」']:
            with self.subTest(source=source), self.assertRaises(ValueError):
                lint.check_document(PROMPT, dialogue_source=source)

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


if __name__ == '__main__':
    unittest.main()

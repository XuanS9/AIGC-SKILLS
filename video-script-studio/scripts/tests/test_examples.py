"""Every prompt example in the docs is checked by the real linters.

These are behaviour tests: they run director_contract_lint and seedance_lint on
the examples users are told to copy, so an example that drifts from the
contract fails here instead of being taught. They do not judge visual quality.
"""
from decimal import Decimal
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'scripts'))
import director_contract_lint as contract
import seedance_lint as preflight

REF = ROOT / 'references'
SPECS = preflight.load_specs(REF / 'model-specs.json')
FENCE = re.compile(r'```text\n(.*?)```', re.S)


def full_prompts(name):
    """Fenced studio prompts in a doc, excluding placeholder templates."""
    text = (REF / name).read_text(encoding='utf-8')
    return [b for b in FENCE.findall(text)
            if '[生成目标]' in b and '[具体情节]' in b and '<' not in b.split('[具体情节]', 1)[1][:40]]


def clip_document(name):
    """Example docs with '## Clip N-N｜…' sections become one multi-clip document."""
    text = (REF / name).read_text(encoding='utf-8')
    parts = re.findall(r'^## Clip (\d+-\d+)｜[^\n]*\n+```text\n(.*?)```', text, re.S | re.M)
    return ''.join(f'# Clip {n}｜例｜时长：30秒\n```text\n{body}```\n' for n, body in parts), len(parts)


# (doc, expected count of complete prompts, declared durations or None)
EXAMPLES = [
    ('template-general-director-2-5.md', 3, [16, 16, 14]),
    ('template-full-performance-example.md', 1, [30]),
    ('spatial-layout.md', 2, [6, 6]),
]
MULTI_CLIP = [('template-action-example-xianxia.md', 2)]


def preflight_failures(text, model='seedance_2_5'):
    filt, struct, _ = preflight.preflight_document(text, None, SPECS[model])
    return [f for f in filt + struct if f.severity in ('FAIL', 'WARN')]


class ExamplesPassBothLintersTests(unittest.TestCase):
    def test_single_clip_examples(self):
        for name, count, durations in EXAMPLES:
            prompts = full_prompts(name)
            self.assertEqual(len(prompts), count, name)
            for body, duration in zip(prompts, durations):
                with self.subTest(doc=name, start=body[:24]):
                    self.assertEqual(contract.check_document(body, Decimal(duration)), ([], 1))
                    self.assertEqual(contract.boundary_warnings(body), [])
                    self.assertEqual(preflight_failures(body), [])

    def test_multi_clip_examples(self):
        for name, count in MULTI_CLIP:
            with self.subTest(doc=name):
                text, found = clip_document(name)
                self.assertEqual(found, count)
                self.assertEqual(contract.check_document(text), ([], count))
                self.assertEqual(contract.boundary_warnings(text), [])
                self.assertEqual(preflight_failures(text), [])

    def test_examples_follow_the_entry_contract(self):
        """The three user rules, checked on every example rather than by phrase."""
        bodies = [b for n, c, _ in EXAMPLES for b in full_prompts(n)]
        bodies += re.findall(r'```text\n(.*?)```', clip_document(MULTI_CLIP[0][0])[0], re.S)
        for body in bodies:
            with self.subTest(start=body[:24]):
                blocks = {n: c for n, _, c in contract.split_blocks(body)}
                scene, audio = blocks['具体情节'], blocks['声音']
                # Dialogue follows Higgsfield: only in [声音], as timed lines.
                self.assertNotRegex(scene, r'(?m)^\s*对白\s*[:：]')
                self.assertEqual(contract.DIALOGUE.findall(body),
                                 [l['text'] for l in contract.audio_lines(audio)])
                # First second carries the positioning hm when people are present.
                people = int(re.search(r'恰好\s*(\d+)\s*人', blocks['角色']).group(1))
                first = contract.split_segments(scene)[0]
                self.assertLessEqual(first['end'] - first['start'], Decimal('1.5'))
                hm = [l for l in contract.audio_lines(audio) if contract.HM.match(l['text'])]
                self.assertEqual(bool(hm), people > 0)
        # No length cap: the longest example is far past the old 1,800 limit and still passes.
        self.assertGreater(max(len(b) for b in bodies), 1800)

    def test_cli_accepts_examples_with_dialogue_truth(self):
        body = full_prompts('template-general-director-2-5.md')[0]
        with tempfile.TemporaryDirectory() as folder:
            prompt, truth = Path(folder) / 'p.txt', Path(folder) / 't.txt'
            prompt.write_text(body, encoding='utf-8')
            truth.write_text('周远：「Keep it.」', encoding='utf-8')
            for script, extra in (('director_contract_lint.py', ['--dialogue-source', str(truth), '--duration', '16']),
                                  ('seedance_lint.py', ['--preflight', '--model', 'seedance_2_5'])):
                result = subprocess.run([sys.executable, str(ROOT / 'scripts' / script), '--file', str(prompt), *extra],
                                        capture_output=True, text=True)
                with self.subTest(script=script):
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_example_mutations_are_rejected(self):
        body = full_prompts('template-general-director-2-5.md')[0]
        for old, new in [
            ('[生成目标]', '[一句话概述]'),
            ('[保持一致]', '【全局补充】'),
            ('4s-7s｜', '5s-7s｜'),
            ('对白语言：英语。', ''),
            ('NO BGM。', '(无音乐)'),
            ('视场角47°', '视场角50°'),
            ('0s-1s｜周远轻声：{Hm.}\n', ''),
            ('8s-10s｜周远低声说：{Keep it.}\n', ''),
        ]:
            with self.subTest(old=old):
                self.assertTrue(contract.check_document(body.replace(old, new))[0])


if __name__ == '__main__':
    unittest.main()

"""No timbre/profile output in studio character/video drafts; audio cues remain."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]


class NoVoiceDescriptionTests(unittest.TestCase):
    def test_entry_removes_voice_descriptors_not_spoken_events(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        for value in ['**不输出音色描述。**', '对白原句、说话人', '痛喊/喘息/鼻息和现场音效保留',
                      '修改后复查（必做）', '不新增审批']:
            self.assertIn(value, text)
        for forbidden in ['另交英文音色完整版2–4句', '另交图外英文音色完整版', '≤8词英文音色速览标签']:
            self.assertNotIn(forbidden, text)

    def test_consumers_do_not_reintroduce_old_profile_or_asset_labels(self):
        for file in ['references/directing-workflow.md', 'references/sample-approval.md',
                     'references/higgsfield-character-design.md', 'references/higgsfield-soul.md',
                     'references/template-character-asset-delivery.md', 'references/higgsfield-seedance-2-5.md']:
            with self.subTest(file=file):
                text = (ROOT / file).read_text(encoding='utf-8')
                for forbidden in ['另交英文音色完整版2–4句', 'Voice Description 英文完整版（2–4句）',
                                  '图底非文字波形＋≤8词英文音色短标签']:
                    self.assertNotIn(forbidden, text)
        acting = (ROOT / 'references/higgsfield-acting.md').read_text(encoding='utf-8')
        self.assertNotIn('Vocal profile:', acting)
        self.assertNotIn('**Voice (pasted verbatim when VIKTOR speaks):**', acting)
        self.assertIn('Delivery is\nscene-dependent', acting)
        self.assertIn('Actual lip-sync and audio matching require results.', acting)
        audio = (ROOT / 'references/higgsfield-audio.md').read_text(encoding='utf-8')
        self.assertIn('not fixed timbre or voice-profile descriptions', audio)
        self.assertIn('speaker-attributed\ndialogue in 「」', audio)
        self.assertIn('native Cinema Studio SCELA submission', audio)


if __name__ == '__main__':
    unittest.main()

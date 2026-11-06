"""Output-profile length limits must not truncate complete production drafts."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

SCRIPT = Path(__file__).resolve().parents[1] / "seedance_lint.py"
spec = importlib.util.spec_from_file_location("profile_scope_lint", SCRIPT)
lint = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = lint
spec.loader.exec_module(lint)


def production_draft(repeat=90):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from studio_fixtures import prompt as build, segment
    seg = segment('0', '3', '侧面中景', 47, '固定', picture='她坐在屋内桌前，面向布料，窗在画面左侧。',
                  camera='固定，平视。', action='手指压住布面，窗侧柔光照指背。' * repeat,
                  expression='她目光低垂，嘴唇抿紧。', end_state='她的手停在布面上。')
    return build([seg], goal='她在屋内整理布料。', style='窗侧柔光，5600K。', cut=False,
                 audio='本段无对白（设计）。现场声为房间底噪。NO BGM。',
                 consistency='画面中只有 1 人。无字幕、无水印。')


def overlong_draft():
    return production_draft(150)


class ProfileScopeTests(unittest.TestCase):
    def findings(self, text, profile="standard"):
        return lint.structural_lint(text, lint.Settings(), None, profile=profile)

    def test_block_draft_has_no_length_cap(self):
        # The 1,800-character cap belongs to the bilingual-JSON profile only;
        # studio block drafts have no length cap .
        draft = production_draft()
        self.assertEqual(lint.detect_regime(draft), "block")
        self.assertNotIn("zh-overlength", [f.rule for f in self.findings(draft)])
        self.assertFalse(any(f.severity == "FAIL" for f in lint.lint(draft)))
        import director_contract_lint as contract
        self.assertEqual(contract.check_document(draft)[0], [])
        # The studio block format has no length cap .
        self.assertEqual(contract.check_document(overlong_draft())[0], [])

    def test_bilingual_extracted_zh_boundary(self):
        self.assertNotIn("zh-overlength", [f.rule for f in self.findings("字" * 1800, "bilingual-json")])
        self.assertIn("zh-overlength", [f.rule for f in self.findings("字" * 1801, "bilingual-json")])
        self.assertNotIn("zh-overlength", [f.rule for f in self.findings("字" * 1801)])

    def test_paired_json_counts_decoded_zh_only(self):
        pair = [{"lang": "en", "prompt": "English coverage. " * 300},
                {"lang": "zh", "prompt": "字" * 1800}]
        # Escapes and the long English entry must not consume the ZH budget.
        encoded = json.dumps(pair, ensure_ascii=True)
        self.assertGreater(len(encoded), 1800)
        self.assertNotIn("zh-overlength", [f.rule for f in self.findings(encoded, "bilingual-json")])
        pair[1]["prompt"] += "字"
        self.assertIn("zh-overlength", [f.rule for f in self.findings(json.dumps(pair), "bilingual-json")])

    def test_profile_does_not_accept_missing_zh_as_valid_pair(self):
        for pair in ([{"lang": "en", "prompt": "x"}],
                     [{"lang": "en", "prompt": "x"}, {"lang": "zh", "prompt": None}],
                     ["en", "zh"]):
            with self.subTest(pair=pair):
                self.assertIn("bilingual-json-shape", [f.rule for f in self.findings(json.dumps(pair), "bilingual-json")])

    def test_other_structural_failures_are_still_checked(self):
        for profile in ("standard", "bilingual-json"):
            with self.subTest(profile=profile):
                findings = lint.structural_lint("[0-6s] 一段动作。", lint.Settings(duration=5), None, profile=profile)
                self.assertIn("beats-exceed-envelope", [f.rule for f in findings])

    def test_cli_profile_is_explicit(self):
        with tempfile.TemporaryDirectory() as td:
            path = Path(td) / "draft.txt"
            path.write_text(production_draft())
            result = subprocess.run([sys.executable, str(SCRIPT), "--preflight", "--file", str(path)], capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            path.write_text("字" * 1801)
            result = subprocess.run([sys.executable, str(SCRIPT), "--file", str(path), "--profile", "bilingual-json"], capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
            self.assertIn("zh-overlength", result.stdout)


if __name__ == "__main__":
    unittest.main()

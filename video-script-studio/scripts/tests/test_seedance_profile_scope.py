"""Output-profile length limits must not truncate complete production drafts."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "seedance_lint.py"
spec = importlib.util.spec_from_file_location("profile_scope_lint", SCRIPT)
lint = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = lint
spec.loader.exec_module(lint)


def production_draft():
    return ("【参考素材职责】\n纯文字参考。\n【一句话概述】\n她在屋内整理布料。\n"
            "【具体情节】\n0s-3s：侧面中景，" + "手指压住布面，窗侧柔光照指背。" * 140 +
            "\n【全局补充】\n本段无对白（设计）。无字幕、无水印。NO BGM。\n")


class ProfileScopeTests(unittest.TestCase):
    def findings(self, text, profile="standard"):
        return lint.structural_lint(text, lint.Settings(), None, profile=profile)

    def test_complete_four_section_draft_is_not_capped(self):
        draft = production_draft()
        self.assertGreater(len(draft), 1800)
        self.assertEqual(lint.detect_regime(draft), "block")
        self.assertNotIn("zh-overlength", [f.rule for f in self.findings(draft)])
        self.assertFalse(any(f.severity == "FAIL" for f in lint.lint(draft)))

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

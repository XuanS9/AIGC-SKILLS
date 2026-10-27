"""Explicit S-image authoring aliases do not imply uploaded assets."""
import copy
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    "scene_alias_lint", Path(__file__).resolve().parents[1] / "seedance_lint.py")
lint = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = lint
spec.loader.exec_module(lint)


class SceneAliasTests(unittest.TestCase):
    def fixture(self):
        return {"schema_version": 1, "assets": [{
            "type": "S", "name": "山口", "handle": "@山口",
            "file": None, "status": "planned", "view_plan": [{
                "name": "总览", "image_id": "S01", "actual_file": None,
                "generate_separate_image": True}]}], "reference_aliases": [{
            "handle": "@S01", "image_id": "S01", "asset_handle": "@山口",
            "file": None, "status": "planned"}]}

    def load(self, data):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "registry.json"
            p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            return lint.load_asset_registry(p)

    def test_explicit_alias_is_planned_not_bound(self):
        r = self.load(self.fixture())
        fs = lint.asset_registry_lint("场景：@S01", r)
        self.assertEqual([(f.severity, f.rule) for f in fs],
                         [("WARN", "asset-not-ready")])
        self.assertEqual(r["@S01"]["asset_handle"], "@山口")

    def test_legacy_does_not_infer_alias(self):
        d = self.fixture(); del d["reference_aliases"]
        fs = lint.asset_registry_lint("@S01", self.load(d))
        self.assertEqual(fs[0].rule, "asset-handle-not-registered")

    def test_bound_requires_actual_matching_file(self):
        d = self.fixture(); d["reference_aliases"][0]["status"] = "bound"
        with self.assertRaises(ValueError): self.load(d)
        d["reference_aliases"][0]["file"] = "scene.png"
        with self.assertRaises(ValueError): self.load(d)
        d["assets"][0]["view_plan"][0]["actual_file"] = "scene.png"
        self.assertEqual(self.load(d)["@S01"]["status"], "bound")

    def test_duplicate_alias_rejected(self):
        d = self.fixture(); d["reference_aliases"].append(copy.deepcopy(d["reference_aliases"][0]))
        with self.assertRaises(ValueError): self.load(d)

    def test_unknown_or_ambiguous_view_rejected(self):
        d = self.fixture(); d["assets"][0]["view_plan"] = []
        with self.assertRaises(ValueError): self.load(d)
        d = self.fixture(); d["assets"][0]["view_plan"] *= 2
        with self.assertRaises(ValueError): self.load(d)

    def test_reuse_record_not_an_independent_alias_target(self):
        d = self.fixture()
        d["assets"][0]["view_plan"].append({"name": "近景", "image_id": "S01",
            "actual_file": None, "generate_separate_image": False})
        self.assertIn("@S01", self.load(d))
        d["assets"][0]["view_plan"][0]["generate_separate_image"] = False
        with self.assertRaises(ValueError): self.load(d)

    def test_wrong_parent_and_handle_rejected(self):
        for patch in ({"asset_handle": "@不存在"}, {"asset_handle": []}, {"handle": "@Image1"},
                      {"handle": "@S02"}, {"image_id": "S1"}):
            d = self.fixture(); d["reference_aliases"][0].update(patch)
            with self.assertRaises(ValueError): self.load(d)

    def test_invalid_alias_collection(self):
        for value in (None, {}, "@S01", [None]):
            d = self.fixture(); d["reference_aliases"] = value
            with self.assertRaises(ValueError): self.load(d)


if __name__ == "__main__":
    unittest.main()

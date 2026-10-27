import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'proofread_manifest.py'
spec = importlib.util.spec_from_file_location('proofread_manifest', SCRIPT)
proof = importlib.util.module_from_spec(spec)
spec.loader.exec_module(proof)

PROMPT = '# Clip 1-1｜A\ntext A\n# Clip 1-2｜B\ntext B\n'


def manifest_for(text, reviews=None, expected=None):
    units = proof.units_for(text, 'clip')
    if expected is None:
        expected = list(units)
    if reviews is None:
        reviews = {
            key: {'status': 'reviewed', 'summary': '已逐条回读正文与相关接缝。',
                  'findings': [], 'sha256': proof.digest(units[key])}
            for key in expected if key in units
        }
    return {'unit_kind': 'clip', 'expected_units': expected,
            'file_sha256': proof.digest(text), 'reviews': reviews}


class ProofreadManifestTests(unittest.TestCase):
    def run_case(self, text, data):
        with tempfile.TemporaryDirectory() as temp:
            prompt = Path(temp) / 'prompt.txt'
            manifest = Path(temp) / 'proofread.json'
            prompt.write_text(text, encoding='utf-8')
            manifest.write_text(json.dumps(data), encoding='utf-8')
            return proof.validate(prompt, manifest)

    def test_complete_clip_coverage(self):
        self.assertEqual(self.run_case(PROMPT, manifest_for(PROMPT)), [])

    def test_missing_clip_is_not_complete(self):
        data = manifest_for(PROMPT, expected=['1-1'])
        self.assertTrue(any('覆盖范围' in e for e in self.run_case(PROMPT, data)))

    def test_unreviewed_clip_fails(self):
        data = manifest_for(PROMPT)
        data['reviews']['1-2']['status'] = 'pending'
        self.assertTrue(any('不是 reviewed' in e for e in self.run_case(PROMPT, data)))

    def test_summary_required(self):
        data = manifest_for(PROMPT)
        data['reviews']['1-1']['summary'] = ''
        self.assertTrue(any('缺少逐条结论' in e for e in self.run_case(PROMPT, data)))

    def test_modified_clip_invalidates_its_record(self):
        data = manifest_for(PROMPT)
        changed = PROMPT.replace('text B', 'text B changed')
        errors = self.run_case(changed, data)
        self.assertTrue(any('哈希不匹配' in e for e in errors))
        self.assertTrue(any('最终文件哈希不匹配' in e for e in errors))

    def test_extra_review_entry_fails(self):
        data = manifest_for(PROMPT)
        data['reviews']['9-9'] = {'status': 'reviewed', 'summary': 'x', 'findings': [], 'sha256': 'x'}
        self.assertTrue(any('范围外条目' in e for e in self.run_case(PROMPT, data)))

    def test_scoped_review_is_not_misreported_as_complete(self):
        units = proof.units_for(PROMPT, 'clip')
        subset = ['1-2']
        data = {
            'unit_kind': 'clip', 'coverage_mode': 'scoped', 'scope': '只复查Clip 1-2对白改动',
            'expected_units': subset, 'file_sha256': proof.digest(PROMPT),
            'scope_file_sha256': proof.digest(PROMPT),
            'reviews': {'1-2': {'status': 'reviewed', 'summary': '逐句复查改动及接缝。',
                                'findings': [], 'sha256': proof.digest(units['1-2'])}}
        }
        with tempfile.TemporaryDirectory() as temp:
            prompt = Path(temp) / 'prompt.txt'; manifest = Path(temp) / 'proofread.json'
            prompt.write_text(PROMPT, encoding='utf-8'); manifest.write_text(json.dumps(data), encoding='utf-8')
            self.assertEqual(proof.validate(prompt, manifest), [])
        data.pop('scope_file_sha256')
        with tempfile.TemporaryDirectory() as temp:
            prompt = Path(temp) / 'prompt.txt'; manifest = Path(temp) / 'proofread.json'
            prompt.write_text(PROMPT, encoding='utf-8'); manifest.write_text(json.dumps(data), encoding='utf-8')
            self.assertTrue(any('未绑定当前完整文件哈希' in e for e in proof.validate(prompt, manifest)))

    def test_whole_file_mode(self):
        text = 'one complete artifact\n'
        data = {'unit_kind': 'whole', 'expected_units': ['whole'],
                'file_sha256': proof.digest(text),
                'reviews': {'whole': {'status': 'reviewed', 'summary': '逐行审阅完成。',
                                      'findings': [], 'sha256': proof.digest(text)}}}
        with tempfile.TemporaryDirectory() as temp:
            prompt = Path(temp) / 'prompt.txt'
            manifest = Path(temp) / 'proofread.json'
            prompt.write_text(text, encoding='utf-8')
            manifest.write_text(json.dumps(data), encoding='utf-8')
            self.assertEqual(proof.validate(prompt, manifest), [])


if __name__ == '__main__':
    unittest.main()

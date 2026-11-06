"""Cross-file consistency: no doc may teach a rule the contract has replaced.

A conflict between two modules is the failure that phrase-locked tests miss:
each file can contain its own expected sentence while another file still
teaches the opposite. These tests scan every doc for the replaced patterns,
check that the removed modules stay unreferenced, and check that each core
rule has one owning section that the entry links to.
"""
from pathlib import Path
import json
import re
import unittest
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[2]
import sys
sys.path.insert(0, str(ROOT / 'scripts'))
REF = ROOT / 'references'
DOCS = [ROOT / 'SKILL.md', *sorted(REF.glob('*.md'))]

# Seedance 2.0 / upstream history that is loaded only for 2.0 work or as a
# labelled historical source. Replaced studio rules may be quoted there.
HISTORY = {'higgsfield-seedance.md', 'higgsfield-seedance-engine-rules.md',
           'higgsfield-seedance-failure-modes.md', 'higgsfield-seedance-hell-grind.md',
           'higgsfield-seedance-production-patterns.md', 'higgsfield-seedance-vfx.md',
           'higgsfield-seedance-vfx-dialogue-timing.md', 'production-benchmarks.md',
           'higgsfield-shotlist-director-historical-calibration.md', 'seedance-bilingual-json.md'}
# English upstream templates whose skeletons are Higgsfield's original form;
# each opens with a "Studio form" note pointing to the Chinese contract.
UPSTREAM_TEMPLATES = {'template-omni-reference-2-5.md', 'higgsfield-seedance-2-5-mode-playbooks.md'}

REMOVED_MODULES = [
    'higgsfield-soul', 'higgsfield-cinema', 'higgsfield-canvas', 'higgsfield-vibe-motion',
    'higgsfield-apps', 'higgsfield-assist', 'photodump-presets', 'higgsfield-mixed-media',
    'higgsfield-moodboard', 'higgsfield-motion', 'higgsfield-workspaces', 'higgsfield-stack',
    'higgsfield-seedance-vfx-first-frame', 'higgsfield-models-models-deep-reference',
    'higgsfield-recipes', 'prompt-examples', 'higgsfield-pipeline',
    'template-full-performance-example-legacy-xianxia', 'directing-workflow',
]

# Replaced rules: (description, pattern, files allowed to mention it).
REPLACED = [
    ('dialogue as a per-segment 对白： line (now timed lines in [声音])',
     r'当段\s*`?对白|`对白：`\s*行|^\s*对白\s*[:：]', set()),
    ('dialogue tagged by stage (now timed lines)', r'tagged by stage|Stage \d+: speaker', set()),
    ('dialogue in an English [Audio] block', r'go(?:es)? in `\[Audio\]`', set()),
    ('the positioning hm written as Chinese 嗯', r'“嗯”', set()),
    ('a blanket 1,800-character cap', r'1[,，]?800', HISTORY | {'production-checks.md', 'higgsfield-shotlist-director.md'}),
    ('four-section headings', r'【参考素材职责】|【一句话概述】|【全局补充】|Four-section', set()),
    ('a fixed 3-second shot cap', r'常规单镜不超过3秒|默认3秒镜长上限', set()),
    ('a voice-description ban', r'不输出音色描述|不附音色描述|不输出固定音色|Do not output fixed timbre', set()),
    ('a default live-action look', r'默认电影级写实质感', set()),
    ('old seven-section delivery', r"seven-section|七段式|七栏交付", set()),
    ('stale 2.5 720p ceiling', r'2\.5 caps at 720p|capped at 720p|2\.5 has no 1080p', set()),
    ('omni_reference with no reference', r'even with one or no attached references', set()),
]


def lines(path):
    return path.read_text(encoding='utf-8').splitlines()


class NoReplacedRuleTests(unittest.TestCase):
    def test_replaced_rules_do_not_come_back(self):
        for description, pattern, allowed in REPLACED:
            regex = re.compile(pattern)
            for path in DOCS:
                if path.name in allowed:
                    continue
                for number, line in enumerate(lines(path), 1):
                    if regex.search(line):
                        with self.subTest(rule=description, file=path.name, line=number):
                            self.fail(line[:160])

    def test_english_upstream_templates_point_to_the_studio_form(self):
        for name in UPSTREAM_TEMPLATES:
            with self.subTest(file=name):
                self.assertIn('Studio form', (REF / name).read_text(encoding='utf-8')[:600])

    def test_removed_modules_stay_removed_and_unreferenced(self):
        pattern = re.compile(r'\b(' + '|'.join(map(re.escape, REMOVED_MODULES)) + r')\b')
        for name in REMOVED_MODULES:
            self.assertFalse((REF / f'{name}.md').exists(), name)
        for path in [*DOCS, *sorted((ROOT / 'scripts').rglob('*.py'))]:
            if path.name == Path(__file__).name:
                continue
            for number, line in enumerate(lines(path), 1):
                if pattern.search(line):
                    with self.subTest(file=path.name, line=number):
                        self.fail(line[:160])


class SingleOwnerTests(unittest.TestCase):
    # Core rule → (owning file, heading). The entry must link to the owner.
    OWNERS = {
        'Clip 边界与定位秒': ('narrative-planning.md', 'Clip 边界隔离（强制）'),
        '30 秒上限': ('narrative-planning.md', '单个Clip的30秒硬上限与超量处理'),
        '多线叙事': ('narrative-planning.md', '多线叙事与交叉剪辑'),
        '块结构逐项写法': ('template-general-director-2-5.md', '1. 块结构（Higgsfield / Dreamina Seedance 2.5 标准）'),
        '一次交付': ('template-general-director-2-5.md', '1.5 一次交付：导演方案＋提示词＋生成风险'),
        '纯环境场景图': ('spatial-layout.md', '场景资产内容边界'),
        '进出门方向': ('spatial-layout.md', '3.2 进出门：门槛方向锁定'),
        '修改后复查': ('production-checks.md', '修改后标准复查闭环'),
        '统一验收': ('production-checks.md', '统一调用与验收总表'),
        '导演决策': ('directorial-shot-design.md', '导演决策流程'),
    }

    def test_each_rule_has_one_owning_heading_linked_from_the_entry(self):
        entry = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        for rule, (name, heading) in self.OWNERS.items():
            with self.subTest(rule=rule):
                text = (REF / name).read_text(encoding='utf-8')
                self.assertEqual(len(re.findall(rf'(?m)^#{{2,4}} {re.escape(heading)}$', text)), 1)
                slug = re.sub(r'[^\w\- ]', '', heading).lower().replace(' ', '-')
                self.assertIn(f'references/{name}#{slug}', entry)

    def test_entry_is_a_short_router(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertLess(len(text.encode('utf-8')), 14000)
        description = re.search(r'^description: (.+)$', text, re.M).group(1)
        self.assertLess(len(description), 220)
        # Detail that belongs to an owner is linked, not restated in the entry.
        for detail in ('浅暖白灰', '≤8个英文词', '空舱壳体', '类型_中文名_v01', 'source_image_id'):
            self.assertNotIn(detail, text)
        # Every script named in the entry exists.
        for script in set(re.findall(r'scripts/(\w+\.py)', text)):
            self.assertTrue((ROOT / 'scripts' / script).is_file(), script)


class LinkIntegrityTests(unittest.TestCase):
    def slugs(self, path):
        heads = re.findall(r'^#{1,6}\s+(.+)$', path.read_text(encoding='utf-8'), re.M)
        return {re.sub(r'[^\w\- ]', '', re.sub(r'[*`]', '', h)).lower().replace(' ', '-') for h in heads}

    def test_markdown_links_and_anchors_resolve(self):
        for path in DOCS:
            text = path.read_text(encoding='utf-8')
            self.assertEqual(len(re.findall(r'^```', text, re.M)) % 2, 0, path.name)
            for target in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)', text):
                url = unquote(target)
                if re.match(r'\w+://|mailto:', url):
                    continue
                name, _, fragment = url.partition('#')
                destination = path.parent / name if name else path
                with self.subTest(file=path.name, link=url):
                    self.assertTrue(destination.is_file())
                    if fragment and destination.suffix == '.md':
                        self.assertIn(fragment, self.slugs(destination))

    def test_backtick_file_mentions_exist(self):
        known = {p.name for p in REF.iterdir()} | {'SKILL.md'}
        project_files = {'project.md', 'asset-registry.json'}  # user workspace files
        for path in DOCS:
            for name in re.findall(r'`(?:\.\./)?([\w.-]+\.(?:md|json))`', path.read_text(encoding='utf-8')):
                if name in project_files or name.startswith(('models_explore', 'test_')):
                    continue
                with self.subTest(file=path.name, mention=name):
                    self.assertIn(name, known)

    def test_json_examples_parse(self):
        import project_data_lint as project
        for path in DOCS:
            for block in re.findall(r'```json\n(.*?)\n```', path.read_text(encoding='utf-8'), re.S):
                with self.subTest(file=path.name, start=block[:30]):
                    try:
                        data = json.loads(block)
                    except json.JSONDecodeError:
                        if path.name in HISTORY | UPSTREAM_TEMPLATES or '<' in block or '...' in block or '…' in block:
                            continue
                        raise
                    if isinstance(data, dict) and 'video_delivery' in data and 'assets' in data:
                        self.assertEqual(project.validate_data(data)[0], [])


if __name__ == '__main__':
    unittest.main()

"""Text-contract tests; these do not assess generated image realism."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / 'references/template-character-asset-delivery.md'


class CharacterAssetTemplateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.document = TEMPLATE.read_text(encoding='utf-8')
        code = re.search(r'```python\n(def validate_character_sheet\(text\):.*?)\n```',
                         cls.document, re.S).group(1)
        namespace = {}
        exec(compile(code, str(TEMPLATE), 'exec'), namespace)
        cls.validate = staticmethod(namespace['validate_character_sheet'])
        section = cls.document.split('### 标准可复制格式', 1)[1].split('### 定稿、修复与其他资产', 1)[0]
        cls.prompts = re.findall(r'```text\n(.*?)\n```', section, re.S)

    def test_example_and_filled_format_pass_six_line_contract(self):
        self.assertEqual(len(self.prompts), 2)
        for prompt in self.prompts:
            with self.subTest(prompt=prompt[:50]):
                filled = (prompt.replace('[角色姓名]', '测试角色').replace('[年龄]', '30').replace('[性别]', '男性')
                          )
                self.assertEqual(self.validate(filled), [])

    def test_generic_format_is_medium_neutral(self):
        prompt = self.prompts[0]
        self.assertIn('[已选媒介与具体风格]', prompt)
        self.assertIn('[目标媒介]', prompt)
        for term in ('真人', '演员', '摄影', '85mm', '中画幅', '窗光', '胶片', '毛孔'):
            with self.subTest(term=term):
                self.assertNotIn(term, prompt)

    def test_live_action_example_keeps_photographic_guidance(self):
        prompt = self.prompts[1]
        lines = prompt.splitlines()
        self.assertIn('仅示范已选真人实拍方向', self.document)
        self.assertIn('真人演员服装定妆照', lines[0])
        for term in ('完整头部', '面部不刻画五官', '头顶至鞋全部入画', '头身比7头身', '双手空着'):
            self.assertIn(term, lines[3])
        self.assertIn('明暗渐变', lines[4])
        for anchor in ('漫射窗光', '自然衰减', '接触阴影', '中画幅', '85mm', '自然色彩', '可辨'):
            self.assertIn(anchor, lines[5])
        for legacy in ('8k', '高清细节', '电影级边缘光', '工作室灯光', '不要 CG', '3D 渲染', '--no'):
            self.assertNotIn(legacy, prompt)

    def test_non_live_action_formats_pass_without_camera_terms(self):
        for medium, detail, background, light in (
            ('二维赛璐璐动画', '清晰线条与色块', '浅色平涂背景', '两级明暗与统一色块'),
            ('水彩绘本插画', '水彩晕染与笔触', '浅色纸张背景', '透明色层与柔和明暗'),
            ('写实三维游戏 CG', '皮肤粗糙度与材质分区', '浅灰展示背景', '基于物理的渲染光照'),
        ):
            with self.subTest(medium=medium):
                replacements = {
                    '已选媒介与具体风格': medium, '角色姓名': '测试角色', '年龄': '30', '性别': '男性',
                    '五官+发型描述+与媒介匹配的面部细节': '短发、圆脸，' + detail,
                    '中性/冷静等': '中性', '体型+完整服装描述+符合使用状态的材料细节': '中等体型、蓝衣长裤与布鞋，' + detail,
                    '符合年龄与风格的比例': '7头身',
                    '与已选媒介匹配的简洁浅色背景': background,
                    '与内容题材及已选媒介匹配的光影、色彩和材质/画材表现': light, '目标媒介': medium,
                }
                prompt = self.prompts[0]
                for key, value in replacements.items():
                    prompt = prompt.replace('[' + key + ']', value)
                self.assertNotIn('[', prompt)
                self.assertEqual(self.validate(prompt), [])
                for term in ('真人演员', '85mm', '窗光', '胶片颗粒'):
                    self.assertNotIn(term, prompt)

    def test_validator_still_rejects_missing_views_and_text_constraint(self):
        prompt = self.prompts[1]
        self.assertIn('完整三视图', self.validate(prompt.replace('90°左侧面、背面', '90°左侧面')))
        self.assertIn('图面文字限制', self.validate(prompt.replace('、水印', '').replace('或水印', '')))
        self.assertTrue(self.validate(prompt + '\n额外一行')[0].startswith('六行结构失败'))
        lines = prompt.splitlines()
        lines[5] = '角色细节可辨'
        self.assertIn('灯光与质感', self.validate('\n'.join(lines)))

    def test_validator_rejects_old_crop_extra_panels_and_multiple_face_sources(self):
        prompt = self.prompts[1]
        cases = (
            ('全图共 4 格', '全图共 5 格', '四格总数'),
            ('完整头部', '无头', '旧版裁切与多格污染'),
            ('头顶至鞋全部入画', '只展示上半身', '完整三视图'),
            ('面部不刻画五官', '五官清晰', '完整三视图'),
            ('全图唯一清晰面部', '清晰面部', '唯一面部锚点'),
            ('各视图服装结构一致', '右下方补充手部局部特写', '旧版裁切与多格污染'),
        )
        for before, after, error in cases:
            with self.subTest(after=after):
                self.assertIn(error, self.validate(prompt.replace(before, after)))

    def test_validator_rejects_missing_waveform_and_voice_description_pollution(self):
        prompt = self.prompts[1]
        self.assertIn('图底非文字波形', self.validate(prompt.replace('非文字声纹波形', '装饰条')))
        for label in ('音色速览标签「Warm alto」', '英文音色：温暖女中音', 'Voice Description: warm voice', '固定声线：低沉'):
            with self.subTest(label=label):
                lines = prompt.splitlines()
                lines[4] += label
                self.assertIn('无音色描述或标签', self.validate('\n'.join(lines)))

    def test_voice_descriptions_removed_and_variant_identity_preserved(self):
        for guard in ('图底仅保留非文字波形', '不附英文音色描述或音色标签',
                      '不是音频输入', '保持已定稿五官、肤色、年龄、体型与发色',
                      '视频只写当下说话/喊叫/喘息的行为'):
            self.assertIn(guard, self.document)
        for prompt in self.prompts:
            for forbidden in ('音色', 'Warm alto', 'Voice Description', '固定声线'):
                self.assertNotIn(forbidden, prompt)
        self.assertNotIn('### 音色与换装交接', self.document)
        self.assertNotIn('A warm female alto', self.document)


    def test_material_and_style_scope_guards_are_documented(self):
        for guard in ('新衣不强行做旧', '抛光金属保留其真实反射', '剧情新增泥污、破损仍走状态衍生图',
                      '即使工具支持独立负面栏', '已确认未变内容不自动重写',
                      '非人设计不强行转成真人摄影', '不覆盖 C 按所选媒介确定的背景与光影',
                      '用户明确指定 → 项目已确认', '已有风格直接沿用', '题材不等于媒介',
                      '不将“3D 渲染”列为排除项', '不增加独立审批'):
            with self.subTest(guard=guard):
                self.assertIn(guard, self.document)

    def test_style_pollution_is_removed_not_negated(self):
        for file in ('SKILL.md', 'references/template-character-asset-delivery.md',
                     'references/higgsfield-soul.md', 'references/higgsfield-character-design.md'):
            with self.subTest(file=file):
                text = (ROOT / file).read_text(encoding='utf-8')
                self.assertIn('是什么风格就用什么风格', text)
                self.assertIn('即使工具支持独立负面栏', text)
                self.assertIn('删除或替换', text)
                self.assertIn('污染', text)
                for old_policy in ('风格负面词仅放已确认支持', '风格负面词只放已确认支持',
                                   '负面提示词按工具能力分流', '风格负面词仅在已确认支持'):
                    self.assertNotIn(old_policy, text)
        for prompt in self.prompts:
            for unwanted in ('负面提示词', '不要 CG', '塑料感', '过度磨皮', '过度锐化', '蜡像'):
                self.assertNotIn(unwanted, prompt)

    def test_entry_and_character_overrides_agree_on_medium(self):
        for file in ('SKILL.md', 'references/higgsfield-soul.md', 'references/higgsfield-character-design.md'):
            with self.subTest(file=file):
                text = (ROOT / file).read_text(encoding='utf-8')
                for term in ('不默认真人', '根据内容题材', '题材不等于媒介',
                             '真人演员服装定妆照', '接触阴影', '独立负面栏'):
                    self.assertIn(term, text)


if __name__ == '__main__':
    unittest.main()

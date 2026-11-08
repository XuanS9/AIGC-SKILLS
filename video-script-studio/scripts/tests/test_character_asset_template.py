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
                          .replace('[音色标签]', 'Voice: male, low husky baritone, slow drawl'))
                self.assertEqual(self.validate(filled), [])

    def test_first_line_must_lock_one_head_and_each_body_crop(self):
        prompt = self.prompts[1]
        for before, after in [
            ('整张图只有一个头部', '全图唯一清晰面部'),
            ('仅在第一格面部特写出现', '面部清楚'),
            ('正面全身（颈部裁切）', '正面全身'),
            ('90°侧面全身（颈部裁切）', '90°侧面全身'),
            ('背面全身（颈部裁切）', '背面全身'),
        ]:
            with self.subTest(before=before):
                self.assertIn('首行单头与裁切', self.validate(prompt.replace(before, after)))
        self.assertEqual(self.validate(prompt), [])

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
        for term in ('无头全身', '头部不入画', '颈部至鞋全部入画', '身高172cm', '双手空着'):
            self.assertIn(term, lines[3])
        self.assertIn('明暗渐变', lines[4])
        for anchor in ('漫射窗光', '自然衰减', '接触阴影', '中画幅', '85mm', '自然色彩', '可辨'):
            self.assertIn(anchor, lines[5])
        for legacy in ('电影级边缘光', '工作室灯光', '不要 CG', '3D 渲染', '--no'):
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
                    '中性/冷静等': '中性', '服装主轮廓+完整服装层次与部位固有色/材质+标志造型及位置/连接+关键结构的数量/位置/连接+符合使用状态的材料细节': '方短蓝布上衣、宽直灰布长裤与黑布鞋，左肩有深色梯形护肩，前襟三枚纽扣沿中线连接，' + detail,
                    '身高、骨架体量、肩胯与躯腿比例、肌肉/脂肪分布及稳定体态': '身高175cm，中等骨架，肩胯接近等宽，躯干紧凑、腿长适中，前臂与大腿有适度肌肉体积，腰腹自然平直，双肩平放',
                    '按服装明度选的中性背景：深色服装用明亮浅暖白灰、浅色服装用中灰，与服装明度明显拉开': background, '音色标签': 'Voice: female, bright quick alto',
                    '跨资产共用的具体画法、配色倾向与材质表现；本图让固有色和结构可读的光影/色层': '低饱和蓝灰配色，' + light, '目标媒介': medium,
                }
                prompt = self.prompts[0]
                for key, value in replacements.items():
                    prompt = prompt.replace('[' + key + ']', value)
                self.assertNotIn('[', prompt)
                self.assertEqual(self.validate(prompt), [])
                for term in ('真人演员', '85mm', '窗光', '胶片颗粒'):
                    self.assertNotIn(term, prompt)

    def test_basic_asset_skeletons_expose_style_and_color_inputs(self):
        # Template-input coverage only; actual style/readability is a visual review.
        generic = self.prompts[0].splitlines()
        self.assertIn('已选媒介与具体风格', generic[0])
        self.assertIn('部位固有色/材质', generic[3])
        self.assertIn('关键结构的数量/位置/连接', generic[3])
        self.assertIn('跨资产共用的具体画法', generic[5])
        bp_section = self.document.split('## 7. 生物/道具资产的多视图与结构', 1)[1]
        bp = re.findall(r'```text\n(.*?)\n```', bp_section, re.S)
        self.assertEqual(len(bp), 2)
        for prompt in bp:
            with self.subTest(start=prompt[:40]):
                self.assertIn('已确认媒介与具体画法', prompt.splitlines()[0])
                self.assertIn('已确认的整体配色倾向', prompt.splitlines()[-1])
                self.assertIn('颜色', prompt)
                self.assertIn('中性背景', prompt)
                self.assertNotIn('与项目已定媒介匹配', prompt)
        self.assertIn('各部件固有色、材料及反光差异', bp[1])

    def test_skeleton_exposes_body_silhouette_and_signature_without_extra_rows(self):
        # Field coverage, not a score for beauty or silhouette recognition.
        lines = self.prompts[0].splitlines()
        self.assertEqual(len(lines), 6)
        for field in ('骨架体量', '肩胯与躯腿比例', '肌肉/脂肪分布', '稳定体态',
                      '服装主轮廓', '标志造型及位置/连接'):
            self.assertIn(field, lines[3])
        self.assertIn('中性站姿', lines[3])
        self.assertIn('头部不入画', lines[3])

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
            ('无头全身', '完整头部全身', '完整三视图'),
            ('颈部至鞋全部入画', '只展示上半身', '完整三视图'),
            ('头部不入画', '面部不刻画五官', '完整三视图'),
            ('全图唯一清晰面部', '清晰面部', '唯一面部锚点'),
            ('各视图服装结构一致', '右下方补充手部局部特写', '旧版裁切与多格污染'),
        )
        for before, after, error in cases:
            with self.subTest(after=after):
                self.assertIn(error, self.validate(prompt.replace(before, after)))

    def test_validator_rejects_missing_waveform_and_voice_description_pollution(self):
        prompt = self.prompts[1]
        self.assertIn('图底波形与音色标签', self.validate(prompt.replace('声纹波形', '装饰条')))
        self.assertIn('图底波形与音色标签', self.validate(prompt.replace('音色标签', '标记')))
        for label in ('Voice Description: warm voice', '英文音色：温暖女中音', '固定声线：低沉'):
            with self.subTest(label=label):
                lines = prompt.splitlines()
                lines[4] += label
                self.assertIn('完整音色描述不进图片正文', self.validate('\n'.join(lines)))
        long_label = prompt.replace('Voice: female, cool clear mezzo, measured regal cadence',
                                    'Voice: female, cool clear mezzo with a measured regal cadence and soft edges')
        self.assertIn('音色标签长度', self.validate(long_label))

    def test_no_dialogue_is_not_an_asset_voice_exception(self):
        prompt = self.prompts[1]
        self.assertEqual(self.validate(prompt.replace('24岁欧洲皇室女性', '24岁欧洲皇室女性，本段无对白')), [])
        label = 'Voice: female, cool clear mezzo, measured regal cadence'
        self.assertIn('实际音色标签内容', self.validate(prompt.replace(label, '')))
        self.assertIn('实际音色标签内容', self.validate(prompt.replace(label, '无台词角色')))
        missing = prompt.replace('音色标签', '无台词标记').replace(label, '')
        self.assertIn('图底波形与音色标签', self.validate(missing))

    def test_voice_label_states_gender_and_no_age_word(self):
        prompt = self.prompts[1]
        no_gender = prompt.replace('Voice: female, cool', 'Voice: cool')
        self.assertIn('音色标签写明性别', self.validate(no_gender))
        aged = prompt.replace('Voice: female, cool clear', 'Voice: female, young clear')
        self.assertIn('音色标签无年龄词', self.validate(aged))
        for guard in ('紧接性别词', '不靠 mezzo、bass 等音域词暗示', '不写 young'):
            self.assertIn(guard, self.document)


    def test_prompts_print_only_the_voice_label_and_carry_no_negative_style(self):
        for prompt in self.prompts:
            self.assertIn('音色标签', prompt)
            self.assertNotIn('Voice Description', prompt)
            for unwanted in ('负面提示词', '不要 CG', '塑料感', '过度磨皮', '蜡像'):
                self.assertNotIn(unwanted, prompt)


if __name__ == '__main__':
    unittest.main()

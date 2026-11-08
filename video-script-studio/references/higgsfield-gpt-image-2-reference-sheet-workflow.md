# 产品参考表流程（Product Reference Sheet Workflow）

参考表是一张棚拍图，从很多角度记录一件真实产品：正面、背面、侧面、顶面，以及品牌标识、材质和结构的微距近景。向下游生成喂一张参考表（而不是一张照片），给模型多得多的身份几何信息，这正是让产品在图像和视频生成之间保持一致的原因。

这个附属文件覆盖产出这种资产的两个 Higgsfield 流程：

1. **自动产品参考表**：一张产品图 → 一张多视角参考表，通过一条可直接粘贴的提示词。
2. **自动提示词生成器**：多张产品图 → 一条针对该产品、锁定身份的提示词 → 最终结果。

转写自 Higgsfield 官方的参考流程指南，加上配套的复制粘贴提示词包。最好用 **Nano Banana Pro、Nano Banana 2 或 GPT Image 2.0** 跑（模型选择见 `image-models.md`）。代码块里的提示词保留英文原文。

---

## 1. 自动产品参考表：三步流程（Automatic Product Reference Sheet — the 3-step flow）

三步把一张产品图变成一张专业参考表：

1. **上传**一张干净的产品图。
2. **粘贴提供的提示词**（下面 § 2 的 GLOBAL IDENTITY LOCK），让 `@image1` 指向上传的图。
3. **生成**：模型返回一张客观的多视角棚拍表：视情况包括正面 / 背面 / 侧面 / 顶面 / 底面，加上品牌标识、关键材质和一个结构细节的微距近景。

核心是*保留身份，而不是重新设计*：输出必须读起来是同一件真实的实物在棚里拍的照片，而不是重新想象或矢量化的版本。一张图进去，出来一个可复用的高一致性生成资产。

---

## 2. 全局身份锁定：可直接粘贴的提示词（GLOBAL IDENTITY LOCK — paste-ready prompt）

适用于任何产品。摄影/拍摄和背景两块保持不变；模型会按产品类型调整视图列表。

```text
Use @image1 as a strict photographic reference of a real product.

Create a high-resolution studio reference sheet of the EXACT SAME product
shown in @image1. This is not a redesign or reinterpretation. It must look
like the same real physical product was placed in a studio and photographed
from multiple angles.

GLOBAL IDENTITY LOCK (CRITICAL):
Preserve the exact real-world identity of the product from @image1, including
all product-specific characteristics that apply:
- identical overall shape, proportions, silhouette, and structure
- identical dimensions and construction logic
- identical material behavior, thickness, softness, rigidity, and finish
- identical seams, folds, edges, contours, stitching, joins, closures,
  fasteners, hardware, trim, and surface transitions
- identical color relationships and tonal balance
- identical wear, subtle imperfections, manufacturing irregularities, and
  real-world material variation
- identical product-specific features visible in @image1, whatever they may be

BRANDING / GRAPHICS / LABEL LOCK (CRITICAL):
If the product in @image1 includes any logo, text, label, print, patch, tag,
embossing, engraving, packaging graphics, or branding element, preserve it
EXACTLY as it appears:
- preserve exact typography
- preserve exact stroke weight, spacing, alignment, and placement
- preserve exact print, embroidery, emboss, stamp, engraving, or label
  appearance
- preserve slight real-world irregularities
Treat all branding and graphic elements as photographed physical parts of the
product, not as digitally recreated text or artwork.

REFERENCE SHEET LAYOUT:
Photograph the product as a clean multi-view studio reference sheet. Show the
most useful angles based on the product type, including: front, back, left
side, right side, top, bottom/underside where relevant, 3/4 angle if helpful,
macro close-up of the main branding/logo/label area, macro close-up of a key
material or texture area, macro close-up of an important construction detail,
and macro close-up of an important feature specific to the product.
If the product type requires a different angle set, adapt intelligently while
still keeping it a clean, clinical product reference sheet.

BACKGROUND + LIGHTING:
- solid light gray background (#DCDCDC)
- perfectly even studio lighting
- shadowless or near-shadowless presentation
- no gradients
- no reflections
- clean, neutral commercial studio setup

REALISM REQUIREMENTS:
- must look like real product photography, not CGI
- preserve micro surface texture and real material character
- preserve stitching, molding, printing, machining, or assembly
  irregularities where applicable
- preserve realistic edge detail and true product finish
- maintain real-world asymmetry where the physical object naturally has it

CAMERA / CAPTURE:
Canon EOS R5
RF 100mm f/2.8L Macro IS USM
f/8
ISO 100
true-to-life color profile
macro-level material detail
edge-to-edge sharpness

FINAL RESULT:
A clinical, ultra-realistic product reference sheet of the exact product in
@image1, preserving its real-world identity, materials, branding,
construction, and imperfections with professional studio accuracy.
```

**身份锁定纪律：**产品上没有可见的品牌标识，就不要编造。源图里看不到的细节，不要臆造：只精确描述实际存在的东西。

---

## 3. 自动提示词生成器：元提示（Automatic Prompt Creator — meta-prompt）

你有同一件产品的多张图时，这条元提示把上面的全局模板转成一条紧贴该产品的提示词。把它*连同产品图*一起贴进你选的大语言模型；它输出一条最终的生成提示词。

```text
You are a prompt-conversion assistant. Your job is to take the global
product-sheet prompt and rewrite it into a product-specific final prompt
based on the reference image(s) attached to the conversation.

Automatically account for however many reference images are provided. Label
them sequentially as @image1, @image2, @image3, and so on. Your rewritten
prompt must correctly reference all provided images.

Do NOT keep the prompt generic. Analyze the reference image(s) and identify
exactly what the product is, how it is constructed, what materials it uses,
how its branding is applied, what textures are visible, what small details
matter, and which product-specific close-ups and angles are needed. Then
rewrite the global prompt so it is fully tailored to that specific product
while preserving the same studio-reference-sheet purpose, realism standard,
and camera/capture specifications.

Analyze from the image(s): (1) product type; (2) overall identity and
structure — shape, silhouette, proportions, construction logic, parts,
closures/seams/joints/hardware; (3) material and surface qualities —
fabric/metal/plastic/leather/glass/etc., softness or rigidity, thickness,
sheen, grain, finish; (4) branding/graphics/typography/labels — logos,
printed/stitched/embossed/engraved text, patches, tags, color blocking,
stripe placement, exact relative placement, and HOW the branding physically
exists on the object; (5) real-world imperfections — wear, stitching/print
irregularities, slight asymmetry; (6) product-specific shot planning — which
views and macro close-ups matter most for THIS product.

Rules: preserve the same studio-sheet intent, realism level, and capture
specs. Keep the camera/lens package and the background/lighting treatment
exactly consistent unless the user changes them. Convert all generic
statements into specific statements that match the actual product. If the
product has branding, describe it as part of the identity lock. If it has no
visible branding, do not invent any. If a detail is not visible, do not
hallucinate it. The final prompt should read like a refined expert
image-generation prompt, not analysis notes.

Output ONLY the final rewritten prompt — no reasoning, no commentary, no
summary of changes, no multiple versions. One best final prompt.
```

---

## 4. 示例（原样的制作提示词）（Worked examples (verbatim production prompts)）

### 4.1 帽子参考表（单张图）（Hat reference sheet (single image)）

```text
Use @image1 as a strict photographic reference of a real product.

Create a high-resolution studio reference sheet of the EXACT SAME white hat
from @image1. It must look like the same real hat was physically placed in a
studio and photographed from multiple angles.

IDENTITY LOCK (CRITICAL):
- identical hat shape, proportions, and structure
- identical front panel curvature and foam structure
- identical brim curvature, thickness, and stitching rows
- identical navy rope placement and thickness across the front
- identical panel seams and crown construction
- identical perforation pattern on the side panels (match exactly)
- identical wear, subtle fabric variation, and real-world imperfections

LOGO LOCK (CRITICAL):
Use the logo EXACTLY as it exists on the hat in @image1 — do not recreate
typography, re-type text, or "clean up" the logo. Preserve exact stroke
weight, spacing, alignment, and slight print/embroidery irregularities.
Treat the logo as a photographed element printed/stitched on fabric.

REFERENCE SHEET LAYOUT: front, back, left side, right side, top, underside
brim, macro close-up of logo, macro close-up of rope detail, macro close-up
of perforation texture, macro close-up of brim stitching.

BACKGROUND + LIGHTING: solid light gray (#DCDCDC), perfectly even studio
lighting, no shadows, no gradients, no reflections.

CAMERA / CAPTURE: Canon EOS R5, RF 100mm f/2.8L Macro IS USM, f/8, ISO 100,
true-to-life color, macro-level textile detail, edge-to-edge sharpness.

RESTRICTIONS: no redesign, no stylization, no brand reinterpretation, no
added elements, no smoothing or beautification.
```

### 4.2 服装参考表（两种参考职责）（Apparel reference sheet (two reference roles)）

用 `<<<image_1>>>` 作为服装身份参考，`<<<image_2>>>` 作为标识身份/位置参考：

```text
Use <<<image_1>>> as the strict garment identity reference. Use
<<<image_2>>> as the strict logo identity and placement reference.

This is a LOCKED apparel reference sheet. The garment and logo must be
identical to the references with zero redesign, reinterpretation, or
stylistic variation.

GARMENT LOCK: reproduce the exact same women's sleeveless golf dress from
<<<image_1>>> — same white athletic fabric tone and material response, navy
collar shape and thickness, V-placket geometry and depth, armhole trim,
double navy side stripe placement/spacing/taper, skirt length/flare/
silhouette, seam lines and stitch placement, fit proportions.

LOGO LOCK (CRITICAL): use the exact logo from <<<image_2>>> only — same
letterforms, overlap relationship, spacing, weight, proportions, embroidered
thread color, exact position on left chest, and scale. Do NOT recreate,
restyle, vectorize, or reinterpret the logo.

EMBROIDERY REALISM: the logo must appear physically stitched — raised thread
structure, tight embroidery density, visible thread direction, micro
shadowing, slight fabric compression, subtle curvature following the chest
contour.

REFERENCE SHEET LAYOUT on flat light gray (#DCDCDC), even omnidirectional
lighting, no shadows/gradients/reflections: full front (centered), full back,
left profile, right profile, close-up of chest logo, close-up of side-stripe
construction.

MODEL / POSE: neutral mannequin-style stance, arms relaxed, no fashion
posing.

PHOTOGRAPHY SPEC: Canon EOS R5, RF 85mm f/2 Macro IS STM, f/8, ISO 100,
true-to-life color science, no cinematic grading, no stylization LUTs.

RESTRICTIONS: no additional logos, no alternate branding, no text overlays,
no environment, no props, no lighting effects, no beauty retouching.
```

---

## 5. 视频会用到的视图（正 / 侧 / 背，还有底面）（Views the video will need (front / side / back — and the bottom)）

上面的 REFERENCE SHEET LAYOUT 块写的是“bottom/underside where relevant”。Seedance-4K 影片教程准确展示了什么时候算“relevant”，而在那种情况下它不是可选的 [DEMO — Seedance-4K film tutorial, 2026-07]：

- **正 / 侧 / 背是任何摄影机会绕着拍的道具的最低要求**：教程的电视遥控器参考表是同一基线上的三个相同遥控器（正面、真正的侧面轮廓、背壳）。
- **只要物体在视频里会被翻转、翻滚或滚动，就加一个底面 / 底盘视图。**教程的雪地卡车参考表是 2×2 网格：FRONT / SIDE / REAR / BOTTOM-UNDERCARRIAGE，专门这样做是因为卡车在场景里会被掀得车顶着地。模型编不出它从没见过的底面；它会在翻滚中途臆造一个。

按分镜表规划视图，而不是按物体：视频会暴露道具的哪一面，参考表就必须事先拍到那一面。

关于背景：GLOBAL IDENTITY LOCK 的纯浅灰（`#DCDCDC`）落在教程测试过的中性灰规则之内（浅到中灰胜过白或黑；生物设定表用 `#7f7f7f`）。这条是道具/产品表的规则；工作室角色组板的背景按 [角色资产交付规范](template-character-asset-delivery.md) 选。

如果 GPT Image 2 的参考表出来显得扁平或像 2D，在改任何东西之前，先把**同一条提示词原样放到 Nano Banana Pro** 重跑：教程正是这样救回了它的遥控器参考表。演示过的参考表模型顺序是：4K 的 GPT Image 2 → 结果扁平就换 Nano Banana Pro；从零创建的场景或角色用 Soul Cinema。

---

## 6. 红箭头标注：让演员对准正确的控件（Red-arrow annotation — aim the actor at the right control）

针对一个顽固失败模式的修法：不管动作怎么改写，视频里的演员总是和**道具的错误部位**互动：按错按钮、握错把手 [DEMO — Seedance-4K film tutorial, 2026-07]。

这个技巧把指令编码进参考图本身：

1. **在参考表图上画一个红箭头**，指向动作针对的确切控件或区域（任何图像编辑器都行；箭头成为参考的一部分）。
2. **让提示词用文字把箭头读回来。**教程原文，来自按遥控器的那场戏：*“The reference's red arrow points precisely to the CH-UP chevron (˄) directly above the 'CH' label”*：然后 ACTION 块把拇指放在“where the red arrow points”。

带标注的参考表和提示词现在指向同一个无歧义的目标，于是模型不再即兴发挥接触点。为此用参考表的一份副本：干净、没有箭头的参考表留作所有不需要指示的镜头的身份参考。

---

## 7. 参考表流向下游的哪里（Where reference sheets feed downstream）

参考表是可复用的身份资产，不是最终产品。把它喂进：

- **电影感道具连续性**：把参考表绑定为身份参考，然后只描述预期的动作和状态变化（见 `higgsfield-seedance.md` § Reference Roles）。工作室格式在开头 `[参考资产]` 写 `@道具名 对应 道具名。`。
- **角色工作**：同样的身份锁定纪律适用于角色转面表（见 `template-character-asset-delivery.md`）。

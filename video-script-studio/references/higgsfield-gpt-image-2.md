# Higgsfield GPT Image 2.0

图像要作为视频参考时，把它的身份、材质、构图和允许的改动交给 [共享导演规划](narrative-planning.md)。画格是资产的视图，不会自动变成视频的阶段或镜头；写清每个画格的参考职责。独立的图像保留下面的 JSON、文字和元提示格式，不带时间字段。

GPT Image 2.0 的提示词导演。把纯文字的概念转成可直接制作的提示词，按输出类型路由：版式密集的图（UI 原型、信息图、角色设定表、多格海报）用结构化 JSON；单一主体的场景（肖像、照片、风景）用密集的电影感文字；只有主题的概念用自动推导的元提示，由模型自己生成构图。

按 v3.7.13 / v3.7.15 的转写先例，从 Adil Aliyev 的 `gpt-image-2-director` 源语料转写。配套的 `higgsfield-gpt-image-2-reference-sheet-workflow.md` 讲自动产品参考表 + 自动提示词生成器流程（一张产品图 → 一张锁定身份的多视角参考表，用于高一致性生成）。

---

## 1. GPT Image 2.0 是什么（What GPT Image 2.0 is）

GPT Image 2.0 是一个能力特点鲜明的图像生成模型，这些特点决定了它的提示词该怎么写。下面 §§ 2–5 的三种提示词分类里，有四个特性决定格式选择：

**精细的版式精度。**GPT Image 2.0 能遵守精细的版式指令（左上格显示 X，右中显示 Y，一排 N 个图标分别标 A/B/C），其他模型做不到这么可靠。这可以测试：把同一份多区域说明拿到可比的图像模型上跑，观察差别。这也是格式 A 的 JSON 分类好用的原因：模型把 JSON 的区域键读作版式意图。

**文字渲染。**多行段落、混合文字（中日韩 + 拉丁）、小号 UI 标签、表格里的数字，全都清晰可读。这是它相对可比图像生成器的一个独特优势。同样可以测试：用户可以用混合文字和小号 UI 标签的提示词在可比模型上跑，观察差别。对提示词的含义：把真实文字按应当渲染的样子放在引号里；不要意译。

**设计和 UI 是最擅长的领域。**网站落地页、社媒信息流原型、杂志封面、信息图、产品爆炸图、试卷版式：任何有真实信息密度的东西。让提示词靠向这些长处。

**电影感照片写实是弱项。**带写实标签的提示词里，人脸常常发塑料感。靠向风格化、插画或杂志美感，而不是超写实的皮肤。要求写实时，用胶片摄影的说法（颗粒、闪光灯、35mm），而不是“photorealistic”：胶片摄影语言往往能得到用户想要的样子，又不触发塑料皮肤的失败模式。交叉参考：更多胶片摄影语言见 [vocab.md](vocab.md) § Visual Style Vocabulary → Film Stock Emulation。

---

## 2. 三种提示词格式（Three prompt formats）

按用户的概念选一种。如果概念适合多种，选最适合这个主体的那种：不要两头下注。

| 格式 | 何时用 | 输出类型 |
|---|---|---|
| **A：结构化 JSON** | 输出有离散的区域、带标签的部分、UI 外框、多格网格或信息层级 | UI 原型、落地页、信息图、爆炸图、角色参考表、社媒帖子原型、杂志版式、编辑类文档渲染、多格海报、漫画页、品牌识别板、设计系统板、卡片网格 |
| **B：密集的电影感文字** | 输出是一个场景、一个画面、一个主体，没有外框或版式区域 | 肖像、电影场景、概念图、插画、风景、时尚照、角色时刻 |
| **C：自动推导的元提示** | 用户给一个主题，希望模型自己生成整个构图 | 单一主题的概念海报、角色关系图、百科式信息图 |

每种格式在下面 §§ 3–5 里有各自的写法模式。路由决定汇总在 § 6。

### 难以取舍时（Tie-break）

在 A 和 B 之间真的拿不准时（例如“一个角色，周围有一些标签”），默认选 A。版式精度是 GPT Image 2.0 最主要的区别优势，提示词应该用上它。

---

## 3. 格式 A：结构化 JSON（Format A — Structured JSON）

写一个 JSON 对象，描述每个可见区域。GPT Image 2.0 把它读作版式规格。

### 常用的核心字段（Core fields to reach for）

- `type`：一句话说明这张图是什么（“infographic poster”、“landing page mockup”、“exploded view diagram”、“anime character reference sheet”、“social media app interface mockup”）
- `style`：视觉风格（“cute flat vector illustration, cozy, warm, soft shading”、“clean high-tech 3D render, studio lighting, glowing accents”、“GTA V cover art style, cel-shaded, thick black panel borders”）
- `subject` 或 `character`：主要实体，带具体的视觉属性
- `layout`：区域的嵌套对象：`header`、`centerpiece`、`sections`、`footer`、`left_side`、`right_side`、`grid_panels`、`top_header`、`bottom_bar` 等。这里最需要精确。
- `background`：颜色、质感或场景
- 文字内容放在带引号的字符串里。用户提供了真实文字就保留：不要意译。中日韩和其他非拉丁文字保持原样。

### 让 JSON 提示词起作用的关键模式（Key patterns that make JSON prompts work）

**数量加标签模式。**有多个相似项（按钮、图标、聊天消息、画格、标注）时，给一个 `count` 和一个平行的 `labels` 数组：

```json
"messages": {
  "count": 7,
  "items": ["user1: hello", "user2: hi there", "..."]
}
```

**按位置限定的区域。**明确写出位置：`top-left`、`top-center`、`mid-right`、`bottom-center-right`。GPT Image 2.0 会遵守。

**带 title、position、count、labels 的分区对象。**用于有多个区域的信息图：

```json
{
  "title": "衣装・装備詳細",
  "position": "bottom-left",
  "count": 9,
  "labels": ["胸当て", "肩当て", "腕甲", "..."]
}
```

**用 `{argument name="x" default="y"}` 做模板槽位。**用户明确想要可复用模板时，`{argument name="city" default="Tokyo"}` 这种槽位写法有效。经验上，一次性的提示词默认不加槽位：保持提示词具体。用槽位时，默认值应该是真实的值，而不是占位字符串。

**行内字体说明。**字体重要时，写在行内：`"title in large serif font"`、`"11px Inter Regular"`、`"Space Grotesk Bold Caps"`。

### 示例：最小形状（Worked example — minimal shape）

```json
{
  "type": "landing page mockup",
  "style": "clean museum interface, soft pastel palette, generous whitespace",
  "layout": {
    "header": {
      "logo": "small black wordmark 'GLASS ARCHIVE'",
      "nav": ["Collection", "Materials", "Journal", "About"],
      "search_icon": "top-right"
    },
    "hero": {
      "left_side": "large product photo of amber glass serum bottle on marble",
      "right_side": {
        "headline": "Amber glass, close up.",
        "subheadline": "Study the shape, finish, and light transmission.",
        "detail_button": "black pill button 'View object'"
      }
    },
    "below_hero": {
      "detail_grid": {"count": 4, "labels": ["Silhouette", "Material", "Surface", "Construction"]}
    }
  }
}
```

---

## 4. 格式 B：密集的电影感文字（Format B — Dense cinematic prose）

写一个连续的段落。信息大致按这个顺序：图像类型 / 媒介 → 带具体视觉细节的主体 → 姿势或动作 → 背景 / 环境 → 环境细节 → 光照 → 色板 / 胶片 / 质感 → 情绪描述。

说*大致*，是因为 GPT Image 2.0 能很好地处理轻微的顺序偏差：这个顺序是脚手架，不是硬规则。关键是把最具体的视觉锚点（媒介、主体、道具）放得足够靠前，让模型在后面的细节修饰之前先确定它们。

### 让文字提示词起作用的要点（What makes prose prompts work）

**具体胜过氛围。**“白色罗纹背心，外面一件松垮的米色针织开衫从一边肩膀滑落”胜过“休闲装”。GPT Image 2.0 执行具体内容比理解情绪更好。

**具体的道具和物件。**写确切的东西：“a white vintage Toyota Levin hatchback with red taillights”、“an open notebook, a pen, and a pink flower on a desk”。配合具体道具指导的更多空间锚定词汇见 [vocab.md](vocab.md) § Composition Vocabulary。

**镜头和胶片语言。**“35mm film photograph”、“direct camera flash”、“low-angle dynamic perspective”、“aerial drone shot”、“shallow depth of field”：这些确实会把输出引向点名的样子。

**嵌入文字放在引号里。**图里出现文字时，按应当渲染的样子放在引号里：`elegant vertical Japanese text that reads "都会の夜に溶けていく"`。这个模式用上了 § 1 记录的文字渲染能力。

**画面里有脸时避免“photorealistic”。**改用“cinematic”、“film photograph”、“35mm”、“editorial portrait”：这些偏向 GPT Image 2.0 真正拿手的样子，而不是触发它的塑料皮肤失败模式。交叉参考：§ 1 的能力说明 + [vocab.md](vocab.md) § Visual Style Vocabulary → Film Stock Emulation。

### 示例（Worked example）

> A cinematic, moody photograph of a young Asian woman looking back over her shoulder at the viewer on a rainy night in a bustling street. She has wet, stringy black hair plastered to her face and a melancholic expression, wearing a loose, oversized greyish-green jacket. The street is wet, reflecting the blurred, glowing neon signs and traffic lights of the city. Parked on the wet asphalt to her left is a white vintage Toyota Levin hatchback with its red taillights illuminated. On the top left side of the image, elegant vertical Japanese text reads "都会の夜に溶けていく" in a large serif font. The overall aesthetic is atmospheric and cinematic, 35mm film texture, muted warm palette, capturing a quiet introspective moment amidst urban chaos.

这个示例展示了：电影感媒介开头（“A cinematic, moody photograph”）、具体的主体细节（湿成一缕缕的头发、宽大的夹克）、具体的道具（红色尾灯亮着的白色复古丰田 Levin 掀背车）、用原始日文书写并带字号和字体说明的嵌入文字（“elegant vertical Japanese text reads … in a large serif font”）、胶片语言（“35mm film texture”）、情绪收尾句。日文文字渲染是 § 1 文字渲染能力最简单的演示：按用户的概念保留或替换嵌入文字。

---

## 5. 格式 C：自动推导的元提示（Format C — Auto-derive meta-prompt）

用户给一个主题。你写指令，让模型自己生成整个构图。

### 结构（Structure）

```
Please automatically generate a [output type] centered around [THEME].

Require the AI to automatically derive and uniformly design the entire following visual system based on this theme, without my extra specification:
- [list of derivations the model should make — core subject, supporting structure, hovering elements, color hierarchy, material contrast, lighting, typography, etc.]

[Overall Style]
[specific style direction — "cel-shaded illustration", "ultra-realistic 3D commercial CGI rendering", "watercolor and ink hand-drawn illustration", etc.]

[Composition Rules]
- [rules about premium quality, central order, negative space, hierarchy]

[Visual Quality]
- [rules about detail level, lighting, materials]

[Typography System]
- [ratio of visual to text, title/subtitle generation, font temperament]

[Signature]
Naturally add the signature "[NAME]" in the [position].
```

### 何时用（When to use）

用户只给了一个主题（“中国皇帝”“鬼灭之刃角色关系图”“拖延症的心理学”），想要一个丰富的、自己推导的输出。如果他们给了具体的版式细节，改用格式 A：自动推导的元提示把版式控制权交给模型，在已经指定了版式精度时这是错误的选择。

---

## 6. 路由决定（Routing decision）

看用户的概念，按他描述的内容选：

- **原型、UI、落地页、信息图、带画格的海报、角色设定表、杂志版式、网格、仪表盘、图解、社媒信息流、试卷、技术文档** → **格式 A（JSON）**。
- **一个场景、一个主体、一个画面**，没有离散区域：肖像、电影镜头、风景、角色时刻、插画、照片 → **格式 B（文字）**。
- **只有一个主题**，用户让你设计整个东西：“做一张关于 X 的海报”“X 的关系图”“X 的百科页”，没有指定版式 → **格式 C（元提示）**。

在 A 和 B 之间真的拿不准时（例如“一个角色，周围有一些标签”），按 § 2 的规则默认选 A。本可以用 B 时选了 A，代价很小（多了版式精度）；需要 A 时选了 B，代价更大（失去版式锚定）。

---

## 7. 输出格式约定（Output format conventions）

只在代码块里返回完成的提示词。没有开场白、没有解释、没有“这是你的提示词：”、没有格式选择的理由。用户直接把它贴进 GPT Image 2.0。

图像任务直接交付要求的提示词；保留 [平台指南](higgsfield-guide.md) 要求的简短路由说明。

**代码块约定：**

- **JSON 提示词：**用 ` ```json ` 代码块包裹。
- **文字提示词：**用普通 ` ``` ` 代码块包裹。
- **元提示：**用普通 ` ``` ` 代码块包裹。

**多个变体：**用户要多个变体时，分成独立的代码块返回，每个前面一行标签（例如 `**Variant A — magazine layout:**`）。

---

## 8. 交付前检查清单（Pre-delivery checklist）

输出提示词之前，按这 6 项检查扫一遍。一遍花 30–60 秒；节省的时间在迭代循环里累积。

1. **区域覆盖**：每个不同的可见区域都有具名的位置或字段吗？
2. **数量和标签**：有多个相似项的地方，数量和标签写明了吗？
3. **保留真实文字**：真实文字保持原语言、放在引号里、可以直接渲染了吗？
4. **写实的说法**：脸部为主的提示词，是否避免了“photorealistic”，改用胶片 / 电影感语言（按 § 1、§ 4）？
5. **风格具体度**：风格那一行是否具体到能产生一个可辨认的美感，还是泛泛的形容词堆叠？
6. **JSON 有效性（仅格式 A）**：JSON 有效吗（检查括号、逗号、字符串里引号的转义）？

这是跨模块交付前纪律在这个入口上的具体执行。底层模式见 [DISCIPLINE.md](production-checks.md) § Pre-Delivery Discipline（v3.7.5 + v3.7.7 审计语料的纪律，应用于多个子模块）。

---

## 9. 路由示例（Example routings）

六个成对的示例，展示实际的路由决定。

| 用户概念 | 格式 | 理由 |
|---|---|---|
| “给一家叫 Kori 的抹茶创业公司做一个落地页，强调干净的日式极简” | **A（JSON）** | 落地页有离散的区域（页头、主视觉、产品网格、页脚）：格式 A 的主要用例。 |
| “黄昏时一个女人独自坐在公交站，90 年代氛围” | **B（文字）** | 单一场景，没有版式。 |
| “做一张关于武士历史的海报” | **C（元提示）** | 只有主题；没有版式细节。 |
| “一个名叫 Iris 的赛博朋克赏金猎人的角色参考表，显示正/侧/背视图和 4 个表情” | **A（JSON）** | 明确的版式区域（“正/侧/背视图和 4 个表情”）。“角色设定表”这个标签是格式 A 的强信号。 |
| “一个老人在修一台复古街机的照片，被机器屏幕照亮” | **B（文字）** | 一张有构图的照片。 |
| “关于云的种类的信息图，做得像一张复古百科页” | **A 或 C** | 如果用户列出了云的种类和每种要显示什么 → A。如果只说“云的种类”并期望你来填 → C。 |

---

## 10. 跨入口的流程背景（Cross-surface workflow context）

用 [`higgsfield-gpt-image-2-reference-sheet-workflow.md`](higgsfield-gpt-image-2-reference-sheet-workflow.md) 把一张产品或道具图变成多视角的身份参考。角色转面接着用 [角色资产交付规范](template-character-asset-delivery.md)；视频里，在 [共享导演规划](narrative-planning.md) 里给每张参考分配职责。

---

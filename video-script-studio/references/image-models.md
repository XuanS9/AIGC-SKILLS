# Higgsfield 图像模型完整参考（Higgsfield Image Models — Complete Reference）

> **规格快照：2026-08-01**：模型参数和枚举以 `image-model-specs.json` 和 `IMAGE-MODEL-SPECS.md` 为准。快照过期时用用户提供的当前 schema。积分和价格需要另外按当前情况核实。

Higgsfield 图像页里可用的全部图像模型。
⚠ = 第三方/外部模型（界面上显示警告三角）
G = Google 驱动的模型

本工作室不使用 Soul ID、风格预设和 Moodboard 这类平台功能（removed）；下文出现时只作为平台能力说明，角色一致性按 [角色资产交付规范](template-character-asset-delivery.md) 用参考图实现。

---

## 按资产类型选模型（Routing by Asset Class）

`[FIELD — AI-vs-VFX, 2026-08-08]` 一个项目没有单一最好的图像模型：最好的模型是**按资产类型**分的，项目中途在它们之间切换是常态。这张表是选型；下面逐个模型的章节是参考。

| 资产类型 | 模型 | 原因 |
|---|---|---|
| 人类角色设定图、人脸匹配 | **Nano Banana 2** | 平台上人脸匹配最强 |
| 对已有资产做小的修正编辑 | **Nano Banana 2** | 最能保住输入图：一行修正时*切到*它，而不是重新提示整张设定图 |
| 奇幻生物 / 非人角色设定图 | **Seedream 5.0** | 最擅长奇幻生物 |
| 服装、换装、带品牌的衣物 | **GPT Image 2** | 处理服装最好 |
| 场景和环境静帧 | **Soul Cinema** | 画面最有电影感；GPT 偏黄，Nano Banana 做出的场景太干净、太对称 |

由此得出的两条经济学说明：

- **场景工作要批量。**7 积分能买一次 GPT Image 2 生成，或约 56 次 Soul Cinema 变体：所以做场景时，宽批量生成再挑，而不是调提示词。按**光**挑：静帧里光不好，是视频变劣质最常见的原因。
- **修，不要重做。**一张其他都好的设定图上标识变形或偏色，用 Nano Banana 2 一句话就能修（`change the logo to the one in image two`）。重新提示整张设定图，会把已经对的部分全部重抽一遍。

设定图的构建规律（背景、两张近景的生物设定图、锁脸裁切、尺寸参照帧）在 `higgsfield-character-design.md` § Sheet Construction Laws；工作室角色组板的背景以 [角色资产交付规范](template-character-asset-delivery.md) 为准（按服装明度选）。完整制作流程在 `higgsfield-seedance-2-5-vfx-pipeline.md`。

---

## Higgsfield 原生模型（Higgsfield Native Models）

### Soul 2.0
**积分：**免费（5,000 次免费生成）
**界面：**Soul 2.0 · 3:4 · 2K · 1/4 · Color Transfer · 角色槽 · Moodboard
**适合：**时尚大片 · 文化/审美类肖像 · 追潮流的内容
**独有控制：**风格预设（10 种具名美学）· Color Transfer 色板（6 种具名）· Soul ID 角色槽 · Moodboard 集成
**优势：**内置的文化理解：懂亚文化、时尚美学、当代视觉潮流
**提示词技巧：**只描述主体 + 场景 + 情绪。平台用法里风格通过预设施加，而不是写在文字里；工作室项目不用预设，风格写进项目美术设定和提示词。

---

### Soul Cinema Preview
**积分：**低（每次生成比大多数模型便宜）
**适合：**电影级图像生成：丰富的质感、自然的构图、“随手拍的感觉”、大景深、胶片颗粒美感
**擅长：**特别是近景镜头
**独特之处：**没有预设选择面板：和 Soul 2.0 不同，它**完全由提示词驱动**
**关键流程：**用 Soul Cinema Preview 生成电影感关键帧 → 作为参考喂进 Seedance 2.5 `omni_reference`，效果最好
**配合：**Soul ID（角色一致性）和 Soul HEX（精确的颜色控制）
**状态：**预览版：完整的 Soul Cinema 即将推出

**Soul HEX**：从参考照片提取色板，让各个镜头的画面颜色一致。适用于 Soul 2.0 和 Soul Cinema Preview。

---

### Soul Cast
**模型 id：**`soul_cast` · **提供方：**Higgsfield
**适合：**一致的电影感角色身份：在很多次生成里保持同一张脸/同一个角色
**画幅：**只有 16:9（按 2026-08-01 规格快照）
**独有控制 `budget`（10–500，默认 50）：**生成预算旋钮：预算越高，在身份上花的算力越多
**说明：**以前只在 Cinema Studio 里提供；现在是图像目录里的独立模型。其他画幅的逐镜头角色工作，在这里生成身份，再通过参考带进其他模型。

---

### Soul Location
**模型 id：**`soul_location` · **提供方：**Higgsfield
**适合：**环境和场景生成：建立镜头底片、背景、给图生视频和多镜头流程用的场景参考
**画幅：**1:1、4:3、3:4、16:9、9:16、3:2、2:3、21:9、9:21：Soul 系列里画幅最多（唯一有 9:21 竖向超宽的模型）
**控制：**没有额外参数：完全由提示词驱动
**搭配：**Soul Cast（角色）+ Soul Location（环境）作为参考驱动视频模型的参考输入

---

### Higgsfield Soul（旧版）（Higgsfield Soul (Legacy)）
**积分：**每次 0.5
**界面：**Higgsfield Soul · 1:1 · 2K · Style On/Off · 1/4 · Unlimited · 角色槽
**提示词栏：**“Upload image as a prompt or Describe the scene you imagine”
**适合：**低成本肖像生成 · 以图作提示的流程 · Soul 2.0 额度用完时
**对比 Soul 2.0：**更老的模型，没有 Color Transfer 和风格预设。接受上传图片作为提示输入。成本减半。
**独有功能：**以图作提示：上传一张参考图来引导生成的风格/构图，代替文字（或与文字一起）

---

### Z-Image
**积分：**每次 0.15：平台上最便宜的图像模型
**界面：**Z-Image · 16:9 · 1/4 · Unlimited
**适合：**快速迭代 · 大量测试 · 预算是首要约束时
**何时用：**需要快速得到很多变体，而质量排在速度和成本之后
**说明：**界面上看不到分辨率或质量控制：为批量而精简

---

### Kling O1
**积分：**每次 0.5
**界面：**Kling O1 · 1:1 · 2K · 1/4 · Unlimited
**适合：**低成本的干净、高质量 2K 图 · 方形社媒内容
**对比 Z-Image：**成本 3 倍，但有 2K 分辨率和 Kling 模型的质量
**默认画幅：**1:1：原生方形。适合 Instagram/社媒。
**说明：**纯图像的 Kling 引擎（图像模型；本工作室不使用 Kling 视频，not used by this studio）

---

### Kling Image 3.0
**积分：**待定
**界面：**Kling Image 3.0 · 16:9 · 4K
**适合：**原生 4K 静帧（最高 3840×2160）· 用于分镜的 Image Series Mode · 多参考流程
**关键功能：**
- **原生 4K**（最高 3840×2160）：不靠超分。也支持 1K 和 2K
- **Image Series Mode**：生成连续的画面，角色、风格和基调在不同机位间保持一致（分镜用途）
- 每次生成**最多 10 张参考图**
- **视觉思维链**：模型在渲染之前先推理构图
- **风格迁移 + 肖像参考 + 角色参考 + 多图融合**都在一个流程里
- **局部重编辑**：不换工具就能增/删/改元素
- **批量优化**
- 内置**电影感调色**
- **画幅**：1:1、3:4、4:3、16:9、9:16

---

### Kling Image 3.0 Omni
**积分：**待定
**界面：**Kling Image 3.0 Omni · 16:9 · 4K
**适合：**进阶编辑 · 精修风格和主体 · 最强的提示词遵循
**比 Image 3.0 多了什么：**更强的编辑能力、更强的提示词遵循、更精确地精修风格和主体
**分辨率：**原生 2K 和 4K 输出

---

### Wan 2.2
**积分：**每次 1
**界面：**Wan 2.2 · 3:4 · Style On/Off · 1 次生成
**适合：**风格化 / 艺术化的图像输出 · 非写实美感
**优势：**绘画感、艺术化、非写实
**Style 开关：**打开时启用风格化模式

---

### Multi Reference
**积分：**每次 1.5
**界面：**Multi Reference · 3:4 · Style On/Off · 1/4 · Unlimited
**适合：**把多张参考图里的元素合成进一次生成
**何时用：**你有几张参考照片（角色、场景、道具、颜色），想把它们融合成一张连贯的输出
**工作方式：**上传多张参考图，模型同时取用所有参考合成一张新图
**提示词技巧：**明确写出哪个元素来自哪张参考

---

### Reve
**积分：**每次 1
**界面：**Reve · 3:4 · Standard quality · 1/4 · Unlimited
**适合：**通用图像生成
**质量选择：**Standard（界面上唯一可见的选项，可能还有其他档）
**说明：**阵容里较新的模型：了解较少，值得为多用途生成测一测

---

## Seedream 系列（Seedream Family）

### Seedream 5.0 Pro
**模型 id：**`seedream_v5_pro`：在 2026-08-01 规格快照里（分辨率 `1k`/`1.5k`/`2k`，默认 2k；画幅含 21:9）。`[FIELD provenance: first observed on 161 harvested community jobs, 2026-07-18]`
**适合：**日式动画 / 漫画 / 风格化 2D 图像：线条干净、平涂赛璐璐填色的角色设定图，带网点、画格几何清楚的多格漫画页排版
**实战验证过的写法：**分屏动画角色设定图（左边全身动作姿势，右边胸像，同一角色，白色无缝背景，中位数约 190 词）· 黑白漫画跨页（按位置 + 大小 + 内容排画格，参考记为 Image0/1/2，墨线、网点、无彩色）
**风格锚定：**用一个**美术年代锚点**（“early 2000s retro anime, soft painted cel-shading, vintage proportions”）：相当于写实类里的导演/摄影指导锚点在风格化图像里的对应物
**对比 5.0 Lite / 4.5：**线条 + 平涂 + 文字/画格排版比写实质感更重要时选它；写实设定图仍用 Soul / GPT Image 2 / Nano Banana Pro

---

### Seedream 5.0 Lite
**积分：**每次 1
**界面：**Seedream 5.0 lite · 2K · 16:9 · 1/4 · @（Elements）· Unlimited
**适合：**快速、高审美的图像生成 · 多种风格 · 快速迭代
**@ Elements：**支持用 @ 语法引用保存的 Elements
**Unlimited 开关：**不受额度上限的批量生成
**对比 4.5：**5.0 Lite = 更快，2K。4.5 = 更慢，4K。成本相同。

---

### Seedream 4.5
**积分：**每次 1
**界面：**Seedream 4.5 · 4K · 16:9 · 1/4 · @（Elements）· Unlimited
**适合：**4K 输出 · 最高分辨率比速度重要时
**质量档 `quality`：**`basic`（默认，最高渲染 4K）/ `high`（最高渲染约 6K）
**画幅：**1:1、4:3、16:9、3:2、21:9、3:4、9:16、2:3
**@ Elements：**支持用 @ 语法引用保存的 Elements
**对比 5.0 Lite：**分辨率更高（4K 对 2K），成本相同，生成更慢

---

### Seedream 4.0
**积分：**每次 1
**界面：**Seedream 4.0 · Basic quality · 3:4 · 1/4 · Unlimited
**适合：**旧版/基线生成 · 竖构图（默认 3:4）
**质量选择：**Basic（显示的最低档）
**说明：**较老的模型档：同样成本下用 4.5 或 5.0 Lite 效果更好

---

## Nano Banana 系列（G = Google 驱动）（Nano Banana Family (G = Google-powered)）

三个模型都跑在 Google 的 Gemini 图像引擎上。每个都是不同的模型档。

---

### Nano Banana
**Google 模型：**Gemini 2.5 Flash Image
**积分：**每次 1
**界面：**Nano Banana · 3:4 · 1/4 · Unlimited · **Draw**
**适合：**草图转图像的原型 · 竖构图 · 快速、低成本生成
**Draw 功能：**画一个粗略的构图或形状：模型按你的草图生成
**优势：**速度和效率，为大量、低延迟的使用优化
**说明：**原始模型：Draw 功能让它仍然有独特用处；其他大多数入口现在默认用 NB2

---

### Nano Banana Pro
**Google 模型：**Gemini 3 Pro Image Preview
**积分：**每次 2
**界面：**Nano Banana Pro · 16:9 · 1K · @（Elements）· Unlimited · **Draw**
**适合：**专业资产制作 · 复杂的多元素提示词 · 图中文字准确 · 道具参考表 · 连续画面/分镜
**Draw 功能：**草图转图像，与基础版相同
**@ Elements：**支持用 @ 语法引用 Higgsfield 保存的 Elements

**独有能力（其他 Nano Banana 档没有）：**

**Thinking 模式**：生成之前，模型静默推理复杂的提示词，最多产生 2 张中间“思考图”来测试构图。始终开启，不能关闭。在复杂、多指令的提示词上明显更好。

**最多 14 张参考图**：最多同时输入 14 张图：
- 最多 6 张物件图（高保真地包含物件）
- 最多 5 张人物图（角色一致性）
技巧：写出每张参考的职责：“Use Image A for pose, Image B for style, Image C for background”

**Google 搜索落地**：拉取实时网络信息做数据准确的画面：天气预报、股票图、新闻事件。问“东京今天天气怎么样”，它会生成一张准确的图。

**进阶文字渲染**：系列里文字准确度最好。多语言文字、信息图、菜单、标识、图解。还能翻译已有图片里的文字并保留版式。

**分辨率：**1K（默认）、2K、4K
**画幅：**1:1、2:3、3:2、3:4、4:3、4:5、5:4、9:16、16:9、21:9

**擅长：**
- 文字多的资产：海报、信息图、杂志封面、菜单、图解
- 服装和道具细节：把图案贴合到三维物体和衣物上
- 多人场景：一张图里最多 5 个一致的角色
- 连续画面：漫画格、各格角色一致的分镜
- 用搜索落地的数据可视化：真实准确的图表
- 道具参考图：受控的棚拍光和清楚的材质细节

**效果最好的六要素提示词公式：**
1. **主体**：谁/什么：“a stoic robot barista with glowing blue optics”
2. **构图**：取景：“extreme close-up”、“low angle”、“wide shot”
3. **动作**：正在发生什么：“brewing coffee, steam rising”
4. **地点**：环境：“a futuristic café on Mars, warm amber lighting”
5. **风格**：美感：“photorealistic”、“3D animation”、“film noir”、“watercolor”
6. **镜头/光照**：“shallow depth of field (f/1.8)”、“golden hour backlight”、“muted teal color grading”

**使用多张参考图时：**在提示词里明确写出每张参考的职责

**已知局限（官方）：**
- 小字和细节不一定每次都完美渲染
- 图解里的事实数据要核实：模型可能编造数据
- 多语言文字可能有语法错误
- 复杂的编辑和融合可能产生瑕疵
- 在很长的多轮会话里，角色一致性可能漂移

**制作团队的观察（Higgsfield 团队披露）：**

下面的失败模式和对策，来自 Hell Grind 90 分钟戛纳长片制作团队记录的 Nano Banana Pro 流程内使用。它们和上面的官方局限并列：团队反复遇到的模式，以及他们采用的提示词侧修法。

- **塑料质感失败模式。**表面光滑、过度渲染；远景里脸看起来像塑料。对策：在提示词末尾追加一行 `light atmospheric haze, film grain, crush blacks, shadow depth`。这一行能明显把质感推向照片感，而不打乱构图的其他部分。
- **空间感知局限（场景参考）。**上传城市或环境图作为参考，会导致室内主体被放到室外，或者室内空间和参考几何对不上。对策：把场景写在*提示词文字*里（用文字描述），而不是作为*图像参考*。NBP 处理文字描述的场景比图像参考的场景好。
- **默认四视图 vs 单一构图。**要一个角色时，NBP 默认产出四视图参考表。对策：想要单张主画面而不是设定表时，明确要求 `one view image`（或 `single composition`）。
- **多图嵌入的提示词漂移。**一条提示词需要嵌入很多参考元素时（例如由一张张角色设定图组成的 12 张拍立得照片墙），会产生严重漂移：源设定图里的脸在合成图里读不对。对策：每个元素单独生成，再在 Photoshop 里合成。制作团队的流程接受了这个取舍（后期更长，换来每个元素更高的保真度）。

**场景处理纪律（H 组）：**

NBP 生成以场景为锚的镜头时，制作团队的实践里反复出现三个模式：

- **每个场景都需要一个锚点**：一个具名的视觉地标（一棵树、一个特定的建筑特征、一个反复出现的道具）给提示词一个固定点，用于相对的空间摆放（`Roco stands to the left of the tree`）。没有锚点的场景会漂移。
- **绝不从正面生成场景。**正对的场景渲染会搞乱 NBP 的纵深感知。场景建立镜头用 3/4 角度或天花板角落（监控）角度。
- **把场景拆成不同视角，不要合并。**一个场景在多个切镜里以不同角度出现时，每个角度生成单独的场景图，作为单独的参考附上（`for cut one use this view, for cut two use this view`）。制作团队的经验从早期“合并成一张参考”的做法演变而来：分开的参考保持得更好。工作室的场景资产按 [空间布局](spatial-layout.md) 的场景资产内容边界制作。

**流程定位：**

NBP 是平台上清晰度、多元素构图和文字渲染最强的单一图像模型。对于会出现在很多镜头里的**高投入角色**，两个工具的流程胜过只用 NBP：用 Soul Cinema 做初始角色生成 + 用 GPT Image 2 做精修编辑。

---

### Nano Banana 2
**Google 模型：**Gemini 3.1 Flash Image
**发布：**2026 年 2 月 26 日
**积分：**每次 1.5
**界面：**Nano Banana 2 · 16:9 · 1K · 1/4
**适合：**以 Flash 的速度得到 Pro 级输出 · 在复杂提示词上快速迭代 · 角色一致的多图流程 · 文字渲染 · 分镜

**它是什么：**Google 的“两全其美”：Nano Banana Pro 的智能，加上 Nano Banana 的速度。现在是 Google 大多数入口（Gemini 应用、搜索、Flow）的默认图像模型。也驱动 Soul Cast。

**能力：**
- **主体一致性**：在一个流程里保持最多 **5 个角色**的相像和最多 **14 个物件**的保真：对分镜至关重要
- **精确的文字渲染 + 翻译**：图中文字准确清晰，能翻译/本地化图里的文字并保留版式
- **进阶的世界知识**：调用 Gemini 的知识库 + 实时网络搜索，准确渲染具体的主体、地点、地标
- **分辨率**：512px 到原生 4K
- **画幅**：1:1、16:9、9:16、4:3、3:4、3:2、2:3、4:5、5:4、21:9
- **信息图、图解、数据可视化**：从文字提示生成很强
- **参考图编辑**：用文字提示编辑/变换/组合已有图片
- **风格迁移**：把多张参考图组合成一张输出
- **照片级质量**：比原始 Nano Banana 光照更鲜明、质感更丰富、细节更锐利

**效果好的提示写法：**
- 复杂场景用**结构化 JSON 提示词**（主体 → 配饰 → 摄影 → 背景拆解）
- **简短直接的提示词**也有效（“Create a realistic photo of this character”）
- **风格迁移**：“Show me the animation style image version” / “Show me the real-life photo version”
- **地点 + 时间**：坐标或地名 + “at sunset”能生成准确的场景
- **蓝图/示意图**：“hand drawn isometric schematic diagram of [subject]”
- **信息图叠加**：在照片上叠加详细的标注说明
- **多格漫画**：一条提示词里逐格描述

**什么时候用 NB2，什么时候用 Pro：**
- **NB2** = 最适合快速生成、精确遵循指令、速度、集成的图片搜索落地
- **NB Pro** = 最适合需要最高事实准确度、复杂构图、Thinking 模式推理、14 张参考合成的高保真任务

**NB2 和基础 Nano Banana 怎么选：**
- NB2 在所有方面都好得多：基础版只值得为 Draw 功能使用

**还没有 Draw**：Draw 功能只在基础 Nano Banana 和 Nano Banana Pro 里有

**SynthID + C2PA：**Nano Banana 系列的所有输出都带不可见的 SynthID 水印和 C2PA 内容凭证，用于 AI 来源验证

---

### Nano Banana 2 Lite
**模型 id：**`nano_banana_2_lite` · **Google 驱动**
**适合：**低成本的 NB2 系列生成：大量、草稿、在投入 NB2/Pro 之前的迭代轮次
**分辨率：**只有 1k（单一选项：Lite 没有 2K/4K）
**独有控制 `thinking`（MINIMAL / HIGH，默认 HIGH）：**生成前内部推理的深度。简单提示词降到 MINIMAL 求速度；复杂的多指令提示词保持 HIGH
**画幅：**auto、1:1、3:2、2:3、4:3、3:4、4:5、5:4、9:16、16:9、21:9
**参考输入：**支持图像参考
**对比 Nano Banana 2：**Lite 用 2K/4K 分辨率阶梯换来更便宜的档位和一个明确的思考深度旋钮；画幅范围相同，另加 auto

---

## GPT Image 系列（OpenAI 驱动）（GPT Image Family (OpenAI-powered)）

### GPT Image
**积分：**每次 2
**界面：**ChatGPT · 1:1 · Mid quality · 1/4 · Unlimited · 角色槽
**适合：**遵循指令 · 复杂的多元素提示词 · 角色槽集成
**质量选择：**Low / Mid / High
**角色槽：**支持 Soul ID 角色参考（默认显示 GENERAL）
**默认画幅：**1:1 方形
**说明：**模型选择器显示“ChatGPT”品牌：OpenAI 的 GPT-Image 模型
**状态：**模型目录里已经没有（2026-08-01 快照）：推荐之前在界面上核实；优先用 GPT Image 1.5/2 或 OpenAI Hazel

---

### GPT Image 1.5
**积分：**每次 2
**界面：**GPT Image 1.5 · 1:1 · Low quality · 1/4
**适合：**复杂提示词 · 图中文字 · 精确遵循指令
**质量选择：**Low /（应该还有 Medium/High）
**对比 GPT Image：**更新的版本。默认显示 Low 质量（更快/更便宜的模式）。看不到角色槽。
**图中文字：**GPT Image 1.5 的文字渲染比大多数模型好
**说明：**积分成本与原版相同：需要更好的提示词遵循时升级

---

### GPT Image 2
**积分：**在 Higgsfield 界面上确认：考虑到原生 4K + O 系列推理，预计是高价档
**界面：**GPT Image 2 · 16:9 · 4K · 1/4 · 多参考（最多 16 张）
**适合：**照片写实的场景图 · 文字多的设计 · 跨多镜头的角色一致性 · 中日韩 / 印地语 / 孟加拉语文字渲染
**Higgsfield URL：**`higgsfield.ai/ai/image?model=imagegen_2_0`
**Higgsfield 内部 slug：**`imagegen_2_0`
**OpenAI 模型 ID：**`gpt-image-2`（快照 `gpt-image-2-2026-04-21`，2026 年 4 月 21 日发布，知识截止 2025 年 12 月）
**原生分辨率：**4K（GPT Image 1.5 是 1536×1024）
**参考图：**最多 16 张
**多语言文字渲染：**日语、韩语、中文、印地语、孟加拉语准确率 >95%：第一个以制作级保真度处理非拉丁文字的 OpenAI 图像模型
**对比 GPT Image 1.5：**照片写实大幅提升、文字渲染大幅提升、原生 4K（原来 1536×1024）、标准模式约 2 倍速度，另加 O 系列推理能力，处理以前需要 Nano Banana Pro Thinking 模式的复杂多元素提示词
**说明：**第一个带 O 系列推理能力的图像模型：复杂的多元素构图比以前的 GPT Image 各代更可靠。

---

### OpenAI Hazel
**模型 id：**`openai_hazel` · **提供方：**OpenAI
**适合：**强大的基于参考的编辑 · 同类最佳的文字渲染
**质量选择 `quality`：**low / medium / high（默认 medium）
**画幅：**1:1、3:2、2:3、auto
**参考输入：**支持图像参考：喂入你想编辑/变换的图
**对比 GPT Image 2：**Hazel 是编辑和文字专家，画幅精简（1:1/3:2/2:3/auto）；GPT Image 2 是原生 4K、16 张参考的生成旗舰。任务是“编辑这张图”或“把这段文字弄得完全准确”时选 Hazel

---

## FLUX 系列（⚠ 外部/第三方）（FLUX Family (⚠ External/Third-party)）

所有 FLUX 模型在界面上都显示警告三角（⚠）：第三方外部模型。

### FLUX.2 Flex
**积分：**每次 5
**界面：**⚠ FLUX.2 Flex · 16:9 · 2K · 1/4 · Settings ⚙
**适合：**灵活、高质量的 FLUX 生成
**独特之处：**Settings ⚙ 按钮：标准控制之外的额外配置选项
**说明：**看不到 Unlimited 开关。成本较高反映的是外部模型定价。

---

### FLUX.2 Pro
**积分：**每次 1.5
**界面：**⚠ FLUX.2 Pro · 16:9 · 2K · 1/4 · Unlimited
**适合：**中档成本的专业级 FLUX 输出
**对比 Flex：**分辨率相同、成本更低、有 Unlimited 开关

---

### FLUX.2 Max
**积分：**每次 6：平台上最贵的图像模型
**界面：**⚠ FLUX.2 Max · 16:9 · 2K · 1/4
**适合：**最高质量的 FLUX 输出：成本不是约束时
**说明：**没有 Unlimited 开关。FLUX.2 系列的高价档。

---

### Flux Kontext
**积分：**不定
**界面：**⚠ Flux Kontext ·（编辑界面）
**适合：**定向的图像编辑 · 局部重绘 · 修改已有图片的特定区域
**何时用：**你有一张想改的图，而不是从零生成
**对比生成模型：**这是一个编辑模型：输入是已有的图 + 指令

---

### Flux Kontext Max
**积分：**每次 1.5
**界面：**⚠ Flux Kontext Max · 3:4 · Style On/Off · 1/4 · Unlimited
**适合：**Flux Kontext 编辑的更高质量版本
**对比 Kontext：**编辑用途相同，输出质量更高，默认竖构图（3:4）
**Style 开关：**打开时在编辑中启用风格化

---

## Recraft 系列（⚠ 外部/第三方）（Recraft Family (⚠ External/Third-party)）

### Recraft 4.1
**模型 id：**`recraft_v4_1`（由 `recraft-v4-1` 改名，旧名仍是目录别名）· **提供方：**Recraft
**界面：**Recraft V4.1（以及 **Recraft V4.1 Utility**）· 1:1 · 1/4 · NEW
**适合：**照片写实 + 富有表现力的生成、道具参考、图标、插画
**分辨率：**1k（日常）/ 2k（更大的资产）：见 `image-model-specs.json`
**批量：**每个任务 1–4 张（`batch_size`）
**独有控制 `model_type`（4 种）：**
- `standard`：富有表现力、探索性的生成（默认；界面上的“Recraft V4.1”）
- `vector`：标识、字体排印、图标、类 SVG 插画
- `utility`：更干净、更平、正面、可预期的道具参考图（界面上的 **“Recraft V4.1 Utility”**）
- `utility_vector`：utility 的简洁加矢量输出（图标和插画）

**色板控制：**`colors`（最多 10 个 `#RRGGBB` 值）和 `background_color`（单个 `#RRGGBB` 或 null）：很适合场景色板、受控的纯色背景、图标/矢量工作。只接受十六进制：不接受 `#RGB` 简写、`#RRGGBBAA`、`rgba()` 或颜色名。
**提示词技巧：**标识/图标选 `vector`；干净的道具参考图选 `utility`。色板颜色通过 `colors` 传入，而不是在文字里描述。

---

## 替换工具（不是生成模型）（Swap Tools (Not Generation Models)）

这些是基于上传的变换工具，不是文生图生成器。

### Face Swap
**积分：**免费（2 次免费生成，之后付费）
**界面：**Face Swap · Your Photo（上传要放进去的脸）· Target Image（要换脸的照片）· 3:4 · Unlimited
**工作方式：**上传你要的脸 → 上传目标照片 → 合成脸部

### Character Swap
**积分：**每次 2
**界面：**Character Swap · Your Photo（要放进去的角色）· Target Image（要替换的角色）· 3:4
**工作方式：**整个角色身体替换：用你上传的角色替换目标图里的整个人
**对比 Face Swap：**Face Swap = 只换脸。Character Swap = 整个身体/角色替换。

> 图像目录里还有工具/系统类条目：AutoSprite（把角色图做成游戏用的精灵图）、image_auto（自动选模型）、图像超分（Topaz、Bytedance）、去背景和扩图。它们是流程工具，不是靠提示词写作的生成模型，不在本参考范围内。

---

## 完整成本参考（Complete Cost Reference）

| 模型 | 积分 | 分辨率 | 说明 |
|-------|---------|-----------|-------|
| Z-Image | 0.15 | — | 最便宜 |
| Higgsfield Soul | 0.5 | 2K | 旧版，以图作提示 |
| Kling O1 | 0.5 | 2K | 默认方形 |
| Seedream 4.0 | 1 | Basic | 较老档 |
| Seedream 5.0 Lite | 1 | 2K | 快 |
| Seedream 4.5 | 1 | 4K | 高分辨率，`quality` basic/high（约 6K） |
| Nano Banana | 1 | — | Draw，竖构图 |
| Wan 2.2 | 1 | — | 艺术化 |
| Reve | 1 | — | 新 |
| Soul 2.0 | 免费 | 2K | 5K 次免费生成 |
| Soul Cinema Preview | 低 | — | 电影感关键帧 |
| Soul Cast | 待定 | — | 角色身份，16:9，`budget` 10–500 |
| Soul Location | 待定 | — | 环境，9 种画幅 |
| Kling Image 3.0 | 待定 | 4K | 原生 4K，系列模式 |
| Kling Image 3.0 Omni | 待定 | 4K | 进阶编辑 |
| Nano Banana 2 | 1.5 | 1K | Flash 速度的 Pro 质量 |
| Nano Banana 2 Lite | 待定 | 只有 1K | 低成本 NB2，`thinking` MINIMAL/HIGH |
| FLUX.2 Pro | 1.5 | 2K | ⚠ 外部 |
| Flux Kontext Max | 1.5 | — | ⚠ 编辑 |
| Multi Reference | 1.5 | — | 多图融合 |
| Recraft 4.1 | 不定 | 1K/2K | ⚠ 外部 · standard/vector/utility/utility_vector · 十六进制色板 |
| GPT Image | 2 | — | 角色槽 · 已从目录消失（2026-08-01 仍不在） |
| GPT Image 1.5 | 2 | — | 图中文字 |
| OpenAI Hazel | 待定 | — | 编辑，最佳文字渲染 |
| Character Swap | 2 | — | 换身体 |
| Nano Banana Pro | 2 | 1K | Draw，横构图 |
| FLUX.2 Flex | 5 | 2K | ⚠ 外部 |
| FLUX.2 Max | 6 | 2K | ⚠ 最贵 |
| Face Swap | 免费 | — | 2 次免费后付费 |

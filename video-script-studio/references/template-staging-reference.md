# 模板：站位参考图（正面站位图）（Template: Staging Reference (front-on blocking map)）

`[DEMO — Tigran (tig-blocking-map v2), 2026-07-24]` **站位参考图**是一张刻意示意化、按颜色区分的轮廓线稿，和真实的场景、角色参考一起附在生成里。它告诉模型**谁在哪里**，别的什么都不说。

它是 `template-top-down-map.md` 的配套，也是它的另一半。那个模板用于**推理**空间，它的平面图从不附到任何东西上；这一个是视频模型真正看到的参考，并且**从摄影机一侧正面画**，因为视频模型按画面思考，不按平面图思考。

> ## 用它之前先读：它经测量能做到什么
>
> - **它并不能可靠地改变站位。**跨 24 个单元测量：第一轮结果不确定，因为不管哪一臂，12 个单元里有 11 个由模型自己的构图先验主导；第二轮做了**对照平衡**（两张互为镜像的图，两臂先验相同、相互抵消），渲染跟随图上朝向的比例是 **6/12，就是随机水平**。不要向用户承诺它能钉住位置。
> - **它是安全的。**两轮合计 **0/18 串染**：用上下面的三层结构后，图的图形风格没有进入镜头。
>
> 所以：防串染结构已经确定、可复用，站位的说法则没有成立。复杂的多人画面需要一个共享、无歧义的*写作*产物时用它；位置确实必须保持时，用 `higgsfield-seedance.md` 里的文字站位锁定来兜底，而不是只靠这张图。工作室格式里，位置写进第一段定位秒的 `画面：` 行和 `[保持一致]`（左右以镜头为准）。

## 三层防串染结构（The three-layer anti-bleed architecture）

串染正好有三个来源。这是测量结果干净的那一半，而它只在三个来源同时封住时才干净。

1. **图像：只有轮廓，绝不填色。**人形是细的、低饱和颜色的轮廓：不填色、没有实色色块、没有明暗、没有质感。线稿读作*计划*；大面积平涂色块读作*美感*，会被投票进镜头。任何网格都保持很淡。
2. **文字：只用正向形式。**你贴进视频提示词的那一块**完全不提**这张图的图形风格：不写 `flat`、`vector`、`schematic`、`grid`、`diagram`、`illustration`，**连否定形式也不写**。模型不擅长否定，所以“no flat vector schematic look”还是把 *flat*、*vector*、*schematic* 这些词送进了提示词，反而引出被禁止的风格。改为正向地说明风格**真正**来自哪里：场景和角色参考。图形词汇只存在于一个地方：生成示意图的提示词，它永远不碰视频提示词。
3. **结构：最后附上。**先附场景和角色参考，站位参考最后，让照片类参考在风格投票里占主导。

**绝不用信号换隐蔽。**极淡的图能去掉串染，也去掉了站位：模型通过同样那些可能串染的像素读取几何。减少风格的**分量**（轮廓、低饱和、淡网格）；绝不减少信号的**对比度**。

## 字母在提示词里，颜色在图像里（Letters live in prompt-space, colours live in image-space）

图上**只有**彩色轮廓人形：没有字母、没有标签、没有文字。渲染出来的文字不可靠，一个渲染出来的字母可能串进镜头。字母 `A`、`B`、`C` 只存在于提示词文字里，通过颜色绑定到人形（*“@A = the BLUE figure”*）。这样保留了字母的全部价值（可以在整条提示词里使用的稳定、非视觉的调用名：*“@A jerks his head”*），渲染风险为零。

每个人形一种低饱和、最大区分度的颜色：低饱和的蓝、橙、黄、紫、红、绿。**颜色只是字母的身份，绝不是服装。**

工作室项目里，项目调用名是 `@` + 纯中文名，`@A/@B` 只作为这张站位图内部的字母图例，写在块外的站位说明里；复制正文用映射块的 `名字 对应 @名字` 和角色名。

## 第 1 步：生成示意图的提示词（Step 1 — the diagram-generation prompt）

源画面作为构图指引附到*这次*生成上，但必须限定范围，而且助手仍要把每个位置、姿势和朝向翻译成明确的文字：**文字承载站位，图像钉住轮廓。**

```
@Image1 — use the attached image ONLY as the compositional guide: copy its
exact framing, camera angle, crop, and the positions, poses and scale of every person —
but do NOT copy its photographic look: no photo textures, no realistic lighting, no
realistic faces, no colors from the image. Do NOT add anything that is not in the attached
image. Do NOT complete cropped bodies — if a body part is cut off by the frame edge in the
image, cut it off in the drawing. The OUTPUT is a flat schematic:

Flat minimalist technical LINE DRAWING, a staging plan for a film scene — an obviously
schematic, non-photographic drawing on a white background with a very faint, thin,
light-grey graph-paper grid. Figures are drawn as clean THIN OUTLINES in muted colors —
NO fills, NO solid color blocks, NO shading, NO texture, NO realism, NO text, NO letters,
NO labels anywhere.

Front view matching the attached image's framing exactly: [N] outline figures.
[Per figure: POSITION IN FRAME — a MUTED-COLOR outline figure, what is visible (full body /
head and shoulders only / torso and arms only), pose exactly as in the image, facing
direction, any signature prop as a simple outlined shape and exactly where it sits relative
to the body.]
[Anchoring furniture/architecture as simple thin-outline shapes and where — or "no
furniture, open background."]

Nothing else — no ground line, no extra props, no extra figures. Simple, readable,
diagrammatic — flat 2D line drawing, minimal detail, only who is where.
```

**用设置，不用提示词文字。**在图像模型自己的 `aspect_ratio` 参数上设置画幅，与源画面一致（`IMAGE-MODEL-SPECS.md`）。模板里不带 Midjourney 风格的参数（`--ar`、`--style`、`--stylize`、`--no`）：平台目录里没有任何图像模型有这些参数，而不解析它们的模型会把 `--no` 后面的词当作**正向**词读进去：恰恰是这一行想挡在外面的照片写实画面。排除项已经作为“这张图是什么”的陈述写在提示词正文里了。`[fix adopted from OSideMedia/higgsfield-ai-prompt-skill v3.38.0]`

一起交付：分配给**结果**的 `@staging_` 标签、源画面的 `@loc_` 标签，以及一行颜色说明（*“BLUE = the captive soldier, centre-foreground”*）。

**每次都要查的四个画面错配陷阱：**被画框裁掉的身体必须描述为被裁掉，*并且*禁止补全 · 写清头部角度和视线 · 道具高度钉到身体部位上（*“横在喉咙前、下巴下面，不是胸口”*）· 不加任何画面里没有的东西。

## 第 2 步：连接块（Step 2 — the connector block）

自包含、只用正向形式，作为一整块贴进视频提示词的参考部分。下面是原生英文格式；工作室块结构稿里，这些内容编译进 `[动作与声音参考]` 的一行映射（“只用于读取人物位置、姿势和朝向，画面风格、光、人物外观都来自场景和角色参考”），具体位置写进第一段 `画面：` 行。

```
@staging_[PROJECT]_[scene]_[version] — POSITION REFERENCE ONLY
Use this reference solely to read where each figure is placed, its pose, and its facing
direction inside @loc_[PROJECT]_[name]_[scene]_[version]. Every visual quality of the shot
— style, light, color grade, faces, wardrobe, environment, props — comes exclusively from
@loc_[PROJECT]_[name]_[scene]_[version] and the character references. The shot is a fully
photoreal live-action frame.

LETTER LEGEND (letters exist only in this prompt; they do not appear on the reference)
@A = the BLUE figure on the staging reference = [character tag] → [position, pose, facing].
@B = the ORANGE figure on the staging reference = [character tag] → [position].

RENDER RULE: place the real, photoreal characters (from their own references) into the real
location @loc_[PROJECT]_[name]_[scene]_[version] at the positions this reference defines,
and take nothing else from it.

LOCKS: All style, light, and texture come exclusively from
@loc_[PROJECT]_[name]_[scene]_[version] and the character references;
@staging_[PROJECT]_[scene]_[version] defines positions only. The colors on the staging
reference identify WHO IS WHO on that reference only — wardrobe and grading come from the
character and location references. Everyone stays in their staging-locked position until
their scripted action.
```

（“fully photoreal live-action frame”一句只适用于已选真人实拍的项目；其他媒介写项目已确认的媒介。）

**附加顺序：先场景和角色参考，站位参考最后。**

## 标签命名（Tag naming）

`@loc_[PROJECT]_[name]_[scene]_[version]` 和 `@staging_[PROJECT]_[scene]_[version]`。`[PROJECT]` 大写。让站位名和它的场景名看得出是配对的。每次重拍升版本 `_v2`、`_v3`，每个镜头只引用当前有效的版本：过期的标签会造成幽灵站位。工作室项目的正式调用名仍以资产总表为准（`@` + 纯中文名）；这里的英文标签只是站位图的内部工作名，按真实参考绑定。

## 修改示意图（Revising a diagram）

`[FIELD — Higgsfield Studio, ONEIRIC breakdown, 2026-08-13]` 两条规则，第二条是悄悄毁掉一个段落的那条：

1. **每个元素用它分配到的颜色称呼，绝不用物件或人名。***“把蓝色人形移到沙发左边缘”*，而不是*“把 Rudy 移过去”*。颜色是示意图的语言；角色名属于视频提示词。在原示意图提示词写的同一个地方要求修改，让完整的颜色说明和几何仍然在场。
2. **从原始画面重新生成，绝不从上一张示意图。**示意图永远从真实镜头画出来。把一张线稿喂回图像模型，它会开始复制**线稿的缺陷**，而不是画面的几何：每一轮都叠加上一轮的错误。

**镜头覆盖变成一场对话。**一场戏有了示意图之后，新的机位就很便宜：*“给我蓝色的中近景”*、*“现在是绿色的 POV”*：你会得到一张针对新景别或角度重新调度的示意图，颜色绑定保持不变。

**让线稿离开写作循环。**提示词是从画面的*文字*描述写出来的，而不是看着示意图写：这就是为什么第 1 步里每个人形的位置、姿势和朝向都要用文字写清楚。视频提示词由文字构建；线稿只需要和文字一致。

> **把它当作空间数据来谈，而不是一张图。**让它起作用的框架，是把参考当作一套线条、颜色、坐标和方向的系统，而不是一张要复制的图：所以在围绕它下指令时，值得避免用“图像”和“参考”这两个词，而说*位置、姿势、朝向*。

## 已知失败（Known failures）

| 失败 | 原因 | 修法 |
|---|---|---|
| 图的样子进了镜头 | 三个来源中的任何一个：色块填充、视频提示词里的图形词汇（**包括否定形式**），或者图在照片参考之前附上 | 三层都修，然后升版本标签 |
| 颜色 → 服装串染（蓝色人形 → 蓝色上衣） | 填色的人形、饱和的色板、身份没有路由到角色参考 | 用轮廓不用填色，低饱和色板，图例把身份路由到自己的参考负责服装的那个角色 |
| 模型编出画面里没有的东西 | 缺少防护句 | “Do NOT add anything that is not in the attached image” + “do NOT complete cropped bodies”；一旦出现了编出来的东西，正向地写出那个位置实际是什么 |
| 道具漂移（剑从喉咙 → 胸口） | 道具没有钉到身体部位上 | 用一个正向描述**加**一个对比来钉住 |

## 质量检查清单（QA checklist）

**分配标签之前，在示意图上：**只有细轮廓 · 任何地方都没有文字或标签 · 被裁掉的身体保持被裁 · 道具在精确的身体部位高度 · 姿势与画面一致（头部角度、视线、嘴）· 构图和画幅与源画面一致。

**在视频结果上：**符合项目媒介，没有图形化的样子 · 没有白底/网格背景残留或描线边缘 · 服装或调色里没有站位颜色 · 没有文字 · 位置保持到剧本里的动作。任何一项不过，就在提供它的那一层修。

## 时间交接（Temporal handoff）

视频站位使用 [共享叙事规划](narrative-planning.md)。它的八个语义层（资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束）为镜头提供信息；本辅助工具在它已有的示意图提示词和连接块格式里提供空间锚点。保留上面全部三层防串染和附加顺序；不要只为了列举层次就往视频提示词里加规划或图形词汇。

在事件、因果触发、揭晓或状态变化处选择运动边界，然后分配时间。不预设数量，不平均分时。新阶段不一定意味着新图或切镜：在剧本触发之前保持初始位置，描述路径和反应，并把结束位置/接触/道具状态带进下一个镜头。需要时，最后一张图代表计划的结尾画面。上面的测量样本数是关于方法的证据，不是创作上的阶段或镜头配额。

## 扩展（Extensions）

同样的惯例，每条路径一种不同的低饱和颜色，各自在图例里绑定：

- **轨迹图**：一颗子弹、一只鸟、一个被扔出的物体。在淡网格上设计曲线（网格是给**你**的；模型读的是画出来的路径，不是网格单元），以虚线交付。绑定四个事实：起点、路径形状、终点、触发节拍。
- **运镜路径图**：推轨/摇镜用箭头，在图例里声明为*“箭头 = 只表示摄影机路径”*。
- **移动图**：角色穿越用一条虚线，带起点、路径、终点标记，以及移动**何时**发生，绑定到一个节拍上。

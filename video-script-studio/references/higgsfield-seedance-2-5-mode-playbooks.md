# Seedance 2.5 模式手册（Seedance 2.5 — Mode Playbooks）

> **Studio form（工作室格式）。**下面的英文块骨架是 Higgsfield 的原版模板。工作室提示词用中文块结构，对白作为计时行写进 `[声音]`；格式归属：[跨类型导演模板 §1](template-general-director-2-5.md#1-块结构higgsfield--dreamina-seedance-25-标准)。

当前项目的生成对图像/视频/音频输入一律用 `omni_reference`。下面旧的首/尾帧和关键帧写法只作为历史模型背景保留，本项目的视频提示词不得选用。编辑/延伸请求：可以接受重新渲染时，把源视频作为参考；只有在核对了用户对保留时间线的要求和当前平台 schema 之后，才用原生的编辑/延伸模式。不要承诺参考能做到像素级保留。

`higgsfield-seedance-2-5.md` 路由到的各种模式和技法的长模板。这里每个模板都是 `[OFFICIAL — Dreamina]`（字节跳动的 *Seedance 2.5 Prompt Guide* 和 *User Guide*），并按本仓库的约定规范化：正向表述、不用年龄词、参考职责总是配上排除项。

先读 [共享叙事规划](narrative-planning.md)，再读任务需要的章节。它的八层（资产/参考、目标、全局视听与空间、行为/节奏、阶段、连续性、结尾画面/交接、约束）是语义规划。把它们编译进每种模式原生的编辑指令、延伸说明、分镜表、素材顺序或转场指令；不要强加八个输出标题。

分配时长之前，先找出必要的事件、因果转折、揭晓和状态变化。一个阶段不一定是一次切镜或一次生成。不预设数量，不平均分时；已确认的故事、对白、结局、源素材的时间义务和平台限制仍然有约束力。下面示例里的时间和数量只是示意；参数限制、参考数量限制和明确的主体数量锁定保持原有效力。

| 任务 | 章节 |
|---|---|
| 改已有视频里面的某样东西 | § Video editing |
| 在已有视频之后（或之前）加素材 | § Video extension |
| 角色/道具/场景图，参考视频/音频 | `template-omni-reference-2-5.md`（职责映射、排除项、场景阶段） |
| 用分镜网格决定镜头顺序 | § Storyboard grids |
| 用三维预演 / 白模决定镜头 | § Blockout references |
| 把一批静帧变成一条剪好的视频 | § One-click video |
| 在两段完成的片段之间搭桥 | § Seamless transitions |

---

## 自动锁定的参数（Auto-locked parameters）

当前的 `omni_reference` 生成从核实过的平台设置取画幅和时长；参考图的顺序不决定开场画面或画幅。下面的帧锚点一行只作为历史模型指导保留，不是当前项目的路线。原生的编辑/延伸模式有不同的锁定，在严格保留源素材的任务之前必须核实。

| 任务 | 画幅 | 时长 |
|---|---|---|
| 视频编辑 | 锁定为输入视频的画幅 | 锁定为约等于输入的时长（帧处理带来 ±约 0.3 秒） |
| 首帧 / 首尾帧 | 锁定为**第一张图**的画幅（首尾应一致，否则尾帧会被拉伸） | 可设置 |
| 视频延伸 | 锁定为输入视频的画幅 | 可设置 |

在 Higgsfield 上，`video_edit` 还**按源视频的时长计费**，并完全忽略 `duration` 和 `aspect_ratio` 参数（`model-specs.json`，快照 2026-08-07）。

---

## 视频编辑（Video editing）

> **写编辑指令之前先确认通道。**`video_edit` 用于**在一条时间线必须原封不动保留的母片里做限定范围的改动**：4–7 秒墙上的光色、换掉一个道具、去掉音乐。它忽略 `duration`，忽略 `aspect_ratio`，按母片全长计费。*素材变换*任务（替换主体，逐帧继承底片的表演，保留其他每个像素）改走 **`omni_reference` 视频到视频通道**，那里时长可以设置，并且必须等于源素材（这就是为什么源素材必须 ≥ 4 秒）：`higgsfield-seedance-2-5-vfx-pipeline.md` § Stage 4。

把源素材定义为**唯一的编辑母片**，然后写明编辑目标、范围、目标素材和不能改变的内容。检查源素材的实际事件，每个编辑窗口都用源时间坐标。保留它的时间、切点、事件顺序、动作相位和未受影响的起止状态；不要把母片重新切分或重新定时成新规划的阶段。叙事规划确定这次编辑的目的，以及它在已有时间线里的因果位置。视频到视频变换按那个通道的要求，让可设置的时长等于源素材。

```
[Edit Goal]
Edit @Video 1. Within <the entire video or a specific time range>, <add, remove, replace, or
adjust> <visual object, region, or audio category>.

[Source Video Role]
@Video 1 is the sole editing master. It defines <characters, scene, actions, composition,
camera movement, occlusion relationships, audio, and event order>.

[Target Material Role]
@Image 1 or @Audio 1 defines <specified attributes of the target object or sound>.

[Edit Scope]
Modify only <object, region, time range, or audio category>.

[Content to Preserve]
Keep <visual content, motion, audio, and timing relationships that must not change> from @Video 1.
Preserve the source duration, cuts, event order, action timing, and unaffected boundary states.
```

**示例（4–7 秒是示意性的源时间窗口，不是默认）：**

```
[Edit Goal]
Edit @Video 1. Only from 4-7 seconds, change the cool blue light on the right wall to warm
orange light.

[Source Video Role]
@Video 1 is the sole editing master. It defines the character, room layout, actions,
composition, camera movement, audio, and event order.

[Edit Scope]
Change only the light color on the right wall and the area it illuminates. Allow the
character's skin tone to respond naturally to the environmental light.

[Content to Preserve]
Keep the character's identity, clothing, expression, position, motion, room structure, camera
movement, dialogue, and ambience from @Video 1.
```

### 主体替换：时间线继承条款（Subject replacement — the Timeline Inheritance clause）

被替换的物体必须继承原物体的*时间线*，而不只是外观。没有这一条，新物体会按自己的节奏出现、移动和离开。

```
[Edit Scope]
Modify only <specific object and area>. The entire video contains <number> target object(s).
Do not modify <content to preserve>.

[Timeline Inheritance]
<Target object> inherits every appearance, motion, occlusion, and exit of <original object>,
including timing, duration, path, and speed changes.
Except for the object or area explicitly modified above, keep all other people, props, scene
content, camera movements, cuts, and event order from @Video 1 unchanged.
```

明确写出**目标数量**（“Keep exactly one white folding desk lamp throughout the video”）：这是防重复物体锁定在 2.5 里的写法。

### 背景替换：按轮廓限定范围（Background replacement — scope by silhouette）

```
[Target Reference Role]
@Image 1 defines only <target environment>'s spatial layout, materials, depth of field,
ambient color, and lighting direction. Do not use the people or foreground objects in the image.

[Edit Scope]
Modify only <background outside the subject's silhouette>. Do not modify <subject identity,
facial features, hairstyle, clothing, expression, position, size, or motion>.

[Timeline Inheritance]
Keep the character actions and occlusion relationships from @Video 1.
```

### 音频编辑（Audio editing）

对白、说话语言、音色、背景音乐和音效可以分别编辑。写出类别、改动和保持不动的部分。

```
Edit @Video 1. Remove only the original background music. Keep the character dialogue, lip
sync, ambience, and action sound effects; preserve the visuals, camera treatment, and editing
rhythm from @Video 1.
```

```
Edit @Video 1. Change <Presenter>'s spoken language to natural American English while
preserving the dialogue content and speaking times. Keep all other character voices,
background music, ambience, and visuals from @Video 1.
```

### 用文字限定范围的编辑（标注的替代）（Written-scope editing (the annotation substitute)）

Dreamina 基于标记的编辑器不在 Higgsfield 上（`higgsfield-seedance-2-5.md` § Dreamina-Only），所以精度要靠句子来给。厂商自己的文字写法是：

```
[Specific modification object / what] + [action and change description] + [effective time range]
```

```
In the first 8 seconds of the video, replace the courier's jeans with dark black suit
trousers, and keep that change consistent for the rest of the clip.
```

写明改动是作用于**整段片子**，还是只在一个写明的窗口内：没限定范围的编辑，就是片子中途回退的来源。

---

## 视频延伸（Video extension）

**描述任何新内容之前，先对齐边界帧。**这个模式成败全在这条规则上。向后延伸的第一帧接着源素材的最后一帧；向前延伸的最后一帧*落在*源素材的第一帧上。

在 Higgsfield 上，这个模式需要 `extension_mode: forward | backward`，画幅跟随源素材。

只规划新增的素材：确定需要的接点状态，找出之前或之后的事件，然后分配这个模式合法的延伸时长。保持原片的时间线完整。把延伸段的局部时间和源时间、组装后的成片时间分开标注。源长 S、延伸长 E 时：向后延伸的局部 0 接源的 S；向前延伸的局部 E 接源的 0（源素材从组装时间 E 开始）。接缝重叠只算一次。不要把合并后的时长平均分成阶段。

### 向后延伸（在源素材之后）（Forward extension (after the source)）

```
@Video 1 is the source video to extend forward.

Extend @Video 1 forward. The first frame of the extended segment directly continues from the
last frame of @Video 1. Maintain continuity in <subject pose and orientation>, <prop
position>, <background and spatial relationships>, <camera position and composition>,
<lighting>, <motion direction, speed, and action phase>, and <sound and dialogue continuity>.

Then, <describe the new action, event, camera treatment, or audio to add>.

Throughout the extension, maintain continuity in <character identity and clothing>, <key
props>, <background layout>, and <axis of action>.
Keep each subject as the same continuous instance throughout: do not duplicate or split it,
and keep the person's appearance or the object's number of parts stable.
End the added segment on <planned final event, visible state, composition, and audio handoff>.
```

### 向前延伸（在源素材之前）（Backward extension (before the source)）

陷阱：写成“then connect to the source video”。这种写法会让后面的元素漏进前面的素材里，也会让画面在已经到达目标状态之后继续漂移。明确地把源素材的第一帧写成延伸段的结束状态。

```
@Video 1 is the source video to extend backward.

Extend @Video 1 backward. Before the source video begins, <describe the preceding action,
event, camera treatment, or audio>.

The last frame of the extended segment naturally connects to the first frame of @Video 1:
<subject pose and orientation>, <prop position>, and <background and spatial relationships>.
Match the <camera position and composition>, <lighting>, and <motion direction, speed,
and action phase> of @Video 1's first frame, with <sound and dialogue continuity> at the join.
This join is the added segment's final state; the original source then continues on its
own unchanged timeline.

Throughout the extension, maintain continuity in <character identity and clothing>, <key
props>, <background layout>, and <axis of action>.
```

### 带额外的参考素材（With additional reference materials）

**先**定义每个新素材的职责，然后写明源视频仍然控制边界画面。新素材是补充；它们绝不推翻边界。

向前延伸时，还要写明哪些素材属于前面那段，哪些必须**只在**源素材开始之后出现：否则后面的角色、道具和特效会提前出现。

```
<Materials that should appear only after the source video begins> must not appear early in
the backward extension.
```

### 延伸的约定（Extension house rules）

- **边界帧要自然衔接，而不是完全相同。**采用之前，检查接缝两侧和整个延伸段。
- **带切镜的延伸和连续延伸是不同的指令。**连续延伸：要求自然延伸、运动顺滑衔接，不要生硬切镜，不要凭空出现物体。刻意的转场：用切镜设定公式 `[transition type guide] + [basic constraint requirements] + [cut logic requirements]`，写明镜头 A、转场和镜头 B。
- **延伸段的音量可能和源素材略有不同。**
- **链条的经济学：**30 秒以内的源素材每次操作延伸 4–30 秒：60 秒是一条链的上限。超过之后，从原始参考重新锚定，而不是延伸一段延伸。

---

## 分镜网格（Storyboard grids）

网格传达的是**故事、镜头顺序和大致构图**，不是严格的逐格复现。最好 ≤15 格，干净的线稿或简单图示，文字标签尽量少。按事件/揭示的覆盖和空间可读性选格；这个偏好是参考复杂度的限制，不是目标镜头数。保留用户提供的分镜板的顺序和内容。规划之后按每格的动作和反应分配时间；格、镜头和叙事阶段不必一一对应。

```
@Image 1 provides an <N-panel storyboard grid> for shot order and approximate composition.
Read it <left to right, top to bottom>. Do not use the grid's <line-art style, text labels,
or placeholder characters>.
@Image 2 defines <Subject A>'s <appearance and clothing>.
@Image 3 defines <key prop or scene>'s <structure, material, or lighting>.

Shot 1: <shot size, subject action, and scene state>.
Shot 2: <shot size, subject action, camera movement, or transition>.
...
Shot N: <closing action and final visible state>.

The final video uses <visual style>. Audio includes <dialogue, ambience, action sound effects,
or music>.
```

明确写出阅读顺序，并写明要**忽略**网格本身的什么：线稿风格和占位人形是两样会串进去的东西。

分镜板是单色而成片不是时，单独用一句话说明：*“Do not render in pencil, ink, or monochrome — the board's drawing style is not the film's style.”* 通用的排除项覆盖边框和标签；它挡不住分镜板的*媒介*被读成成片的画面，而这种失败一眼就能认出：渲染出来是灰色的、草图感的。工作室中文稿把这句转成正向：“分镜板只提供镜头顺序和大致构图，成片按项目美术设定渲染。”`[EMPIRICAL — third-party Seedance 2.5 field skill, 2026-08-09 evaluation; vendor-consistent]`

### 画格到时间码的映射：可选的遵循度提升（Panel-to-timestamp mapping — the optional adherence raiser）

`[MEASURED — 2026-08-09 A/B, (2.5, Ark), 480p, one pair]` 在网格的职责行里加一个明确的画格→时间映射，改变的是切镜*何时*落下，而不是镜头是否按顺序出现。下面的三格和时间码是那次实验的示意值，不是必须的数量或时间分配：

```
Panel 1 (left) is 0-1.5s, panel 2 (middle) is 1.5-2.5s, panel 3 (right) is 2.5-4s.
Do not reorder the shots. Do not invent shots that are not on the board.
```

A/B 在一张干净的三格分镜板上显示：**两臂都遵守了顺序**：只要顺序就不需要映射。有映射的那一臂，切镜落在声明的时间点上，每格的内容留在自己的镜头里；没有映射的那一臂自己选节奏（中间那个镜头吃掉了一半时长），还让镜头 3 的一个道具漏进了镜头 1。每格的*时间预算*重要，或者道具/演员不能跨格串时，用映射。

两条边界成立：厂商不承诺严格的分镜对齐：网格仍是“高层的情节参考”，映射提高遵循度而不是保证它（时间码分配的是预算；它们不是帧级精确的剪辑点）。需要真正逐格严格时，那是**多关键帧通道**（`higgsfield-seedance-2-5.md` § First/last frame and multi-keyframe control），而不是网格。相比之下，槽位位置不值得争：同一天的 A/B 测了分镜板放第一和放最后，顺序遵循度相同：上传顺序是打破平局的因素，不是语义（SD25-PE 已确认）。

---

## 白模参考（Blockout references）

**先决定粗模还是精模**：它会改变整个提示词结构。

| 类型 | 最适合 | 素材要求 | 提示词重点 |
|---|---|---|---|
| **粗模** | 用简单几何预演动作、路径、站位、运镜、切镜 | 清楚的形体关系 + 完整的动作序列；角色/道具/场景图另外添加 | 映射每个白模主体；写明要继承哪些时间和空间信息 |
| **精模** | 完整的模型，需要新的材质、颜色、角色、场景或风格 | 完整、干净的模型：没有路径线、坐标轴、控制器或摄影机视锥 | 保留结构、动作和运镜；定义要重新渲染什么 |

### 粗模（Coarse blockout）

粗模能承载什么，以及提示词对每一项必须说什么：

| 白模信息 | 在提示词里写明 |
|---|---|
| 路径 | 动作轨迹、运动方向、主体站位、入画/出画顺序 |
| 运镜 | 摄影机位置、路径、方向、速度变化 |
| 光照 | 光的方向、亮度变化，以及何时发生 |
| 切镜 | 切点位置，以及每个切点前后的主体/构图 |
| 音频 | 是否继承对白、音乐、环境声或动作音效 |

```
@Video 1 is a coarse blockout reference. It provides only <motion paths, subject blocking,
camera position, camera movement, cuts, lighting changes, sound rhythm, or spatial
relationships>. Do not use its blockout appearance, materials, or scene.
<Blockout Subject A> in @Video 1 corresponds to <Subject A>.
<Blockout Subject B or geometric prop> in @Video 1 corresponds to <Subject B or key prop>.
@Image 1 defines <Subject A>'s <appearance, clothing, or structure>.
@Image 2 defines <specified attributes> of <Subject B, key prop, or scene>.

<Subject> completes <primary action or event> in <scene>.
Keep <motion path, blocking, camera movement, cuts, lighting, or sound rhythm> from @Video 1.
The final video uses <characters, scene, materials, and visual style>. Audio includes
<dialogue, ambience, or action sound effects>.
```

**附肢警告。**手臂、翅膀和类似的附肢，只有在它们的动作序列*完整*时才应该出现在粗模里；不完整的附肢序列会渲染得僵硬，或者在结构上被误读。厂商自己的最佳做法是在粗模里完全不放四肢和翅膀。

### 精模（Fine blockout）

```
@Video 1 is a fine blockout reference. Preserve <subject structure, action, spatial layout,
camera position, camera movement, and cuts>. Do not use its original gray materials or empty
background.
@Image 1 defines <subject>'s <character appearance, material, color, or surface details>.
@Image 2 defines <scene>'s <space, materials, lighting, or visual style>.

Re-render <subject> from @Video 1 as <final subject>, and re-render the scene as <final scene>.
Keep <structure, action, camera treatment, and spatial relationships> from @Video 1.
Use <materials, colors, and style>. Audio includes <ambience, sound effects, or music>.
```

先清理源素材：去掉轨迹线、坐标轴、控制器和摄影机视锥，否则它们会被渲染成场景内容。

**分段渲染写法**：渲染处理在中途改变时：

在源事件或经授权的处理改变处选择边界，保留所有继承的动作、运镜、切镜和音频时间。`<N>` 从那个边界填，而不是把源素材平均切开。下面 20–25 秒的部分参考窗口是示意；用实际引用的区间。

```
Render the blockout animation of @Video 1 into the final film.
0-<N>s: <background environment, tone, character material, light and shadow>.
At <N>s, <transition trigger point and method>: <rendering description of the new scene>.
Character rendering <remains unchanged / changes with the scene>.
```

**部分参考的纪律。**只用于片子一部分的白模必须说明这一点，否则它会扩展成整片的参考：“@Video 2 is the action reference for the 20-25 second counterattack only; do not use it for other segments, and do not bring its gray scene or original texture into the final footage.”

---

## 一键成片（One-click video）

把一批图片（可选再加一段风格参考视频）变成一条节奏一致的视频。**“把这些素材做成一个视频”永远不够。**

顺序：`Material Roles → Image Order → Motion Amount → Editing Style → Visual Treatment → Audio`

先确定目标和最终画面/状态。围绕事件、流程步骤或揭示给素材分组，然后为运动、阅读时间、对白和转场做预算。保留要求的图片顺序和关系；下面三个图片槽位是示意，不是必须的数量。给每个画面它需要的时间，把产品/角色状态和音频带进下一个；不要默认给每张图分配相等的时长。

```
[Material Roles]
@Image 1 is used for <character, product, scene, or opening image>.
@Image 2 is used for <character, product, scene, or process image>.
@Image 3 is used for <character, product, scene, or ending image>.
@Video 1 is used only for <editing rhythm, transitions, subtitle treatment, or music style>.
Do not use its character identities or scene.

[Arrangement]
Show the images in <upload order, a specified order, or a model-selected thematic order>.
<State the character, product, location, and event relationships that must remain consistent>.

[Image Motion]
Apply <subtle live motion, parallax, push-in/pull-out, lateral movement, or local action> to
each image.
Keep <subject appearance, product structure, text, or background relationships> stable.

[Final Style]
Use <editing rhythm, transition style, subtitle or graphic treatment, and color style>.

[Audio]
Include <dialogue, ambience, sound effects, or music>.
```

图片顺序重要时，写明确切的顺序：模型不会推断。不重要时，说明模型可以按主题安排。有多个角色或产品时，继续分别为每一个命名和绑定。

---

## 无缝转场（Seamless transitions）

在两段视频之间生成连续的**桥接内容**。

顺序：`Before Video → After Video → Trigger Action → Camera Movement → Visual Transformation → Arrival State → Audio`

```
@Video 1 is the before-transition clip. Use its <ending subject, action, composition, camera
direction, and audio>.
@Video 2 is the after-transition clip. Use its <opening subject, composition, camera direction,
and audio>.
Keep <character identity, product structure, scene, and primary action> stable in the original
portions of @Video 1 and @Video 2.

At the end of @Video 1, <subject or foreground object> triggers the transition through <action>.
The camera <movement direction and speed change>, while <shape, material, light, or space>
gradually transforms into <corresponding element> at the start of @Video 2.
The transition ends naturally at @Video 2's opening composition, preserving continuity in
<subject position, camera direction, and motion trend>.
Audio transitions smoothly from <before audio> to <after audio>.
```

### 转场方法及各自需要什么（Transition methods and what each one needs）

| 方法 | 需要写明 |
|---|---|
| 俯冲 / 反向运动 | 运镜方向、速度变化、下一场何时开始 |
| 角色旋转 | 姿势、旋转方向、服装和背景如何连续变化 |
| 前景遮挡 | 前景物体何时填满画面，以及之后的构图 |
| 物体变形 | 对应的形状和材质，以及变形过程 |
| 推 / 拉或焦点变化 | 运镜、对焦目标、连续的空间关系 |

### 具名转场词汇（Named transition vocabulary）

`[OFFICIAL — Dreamina]` 每一种都写成 `[transition type guide] + [basic constraint requirements] + [cut logic requirements]`，每个引导句都带同样的两条禁止：不要生硬切镜，不要凭空出现物体。

| 转场 | 作用 |
|---|---|
| **自然切镜** | 类似硬切、没有特效：但明确点名，让接缝读作一次镜头切换，而不是故障 |
| **淡入 / 淡出** | 镜头 A 变暗到黑，镜头 B 从黑里亮起 |
| **叠化** | 镜头 A 变透明，同时镜头 B 浮现；两者重叠一段写明的时长 |
| **闪白 / 闪黑** | 一个冲击节拍爆发成闪光，然后直接切到下一场 |
| **擦除** | 画面像推拉门一样朝写明的方向擦过，露出镜头 B |
| **遮罩转场** | 一个物体或一面墙填满画面到黑；镜头穿过去进入镜头 B |
| **相似物转场** | 形状的相似承载切镜：一枚硬币变成尺子的末端 |
| **动作转场** | 镜头跟着一个剧烈动作进入模糊；镜头 B 从同一个模糊方向进入 |
| **动态接力** | 一个主体在一个场景里出画，以同样的姿势进入下一个场景，背景是新的 |
| **推近 / 拉远** | 放大进一个细节（瞳孔），直到下一场在里面展开 |
| **水墨** | 镜头 A 像墨在水里一样晕开，同时镜头 B 从晕散中浮现 |

也可以给模型一个短名单，让它自己选：“From natural shot switching, mask transition, ink-wash transition, or similar-object transition, use the one that suits this film's style.”

**上限：**转场的目标是视觉和音频的连续。它是一段生成的桥，不是把两段源素材像素级一致地剪接起来。

### 给桥一个截止时间（Give the bridge a deadline）

`[HOUSE — re-derived from the nutllwhy/seedance-tvc-director evaluation, MIT, 2026-08-09. UNPROVEN HERE: the durations below are that source's practitioner figures, not measured on our material.]`

没写到达点的转场会一直进行下去。上面的词汇安全，是因为每一条都点明了终点；失败出在它周围的自由措辞上：**“drifts through”、“floats across”、“travels into”、“gradually becomes”**说的是一个过程而没有终点，于是桥吃掉了后面的段落，下一场来晚了。

描述离开的状态、桥接动作和到达状态，然后按需要的变化和可读性设定时钟。这些描述的是一个因果连接，不是三个必须的镜头或等长的阶段：

```
Last state of the outgoing scene → one bridging action → target scene fully established at <time>.
```

四条护栏，用的是来源里的示意数字，不是测量过的限制或必须的数量/时长：

- **普通的桥按它的连接来做预算**：来源示意的是大约 0.2–0.8 秒。实际时间取决于触发、变化和可读的到达。
- **主打转场可能需要更长**：来源示意了一个约 1.2 秒的。这个数量和时长是可选的剪辑选择，不是每条片子的配额或上限。
- **转场里不要有空画面。**桥经过一个接近纯色或没有主体的画面超过一个节拍，就会读成掉帧；在桥接元素消失之前，目标场景就应该开始建立。
- **写明目标何时建立完成**，而不只是说它到达了：*“甩镜在 9.0 秒开始；客厅在 9.5 秒完全可读”*。一个具名的到达时间，才能阻止这段过程扩张进下一段的时长。

来源里 30 秒片子共约 2.5 秒的转场预算是示意，不是必须的。在事件规划好之后再分配转场；把它们算进声明的时长，重叠只算一次。保留两段源片段的边界状态和原有部分。

只有当概念本身就是变形时才用变形转场。否则硬切、动作匹配或一次短甩镜既便宜又可靠：而且每一种的名字里就写着它的终点。

---

## 相关（Related）

- `higgsfield-seedance-2-5.md`：模式路由、参考职责语法、分阶段、限制
- `higgsfield-seedance.md`：Seedance 2.0 导演和共享的提示词写作规律
- `higgsfield-seedance-engine-rules.md`：整个系列共享的硬性渲染约束

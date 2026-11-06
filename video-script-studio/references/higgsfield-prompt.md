# Higgsfield 提示词工程（Higgsfield Prompt Engineering）

当前工作室视频生成默认用 Seedance 2.5 `omni_reference`：角色、道具和场景图按职责作参考，动作/运镜视频和声音/音频作参考。哪怕只有一张图，也只是属性参考，从不强制成为开场画面。下面的 I2V 一节描述的是其他模型流程的旧做法，不能用来路由当前工作室的视频任务。开场动作和最终状态用文字描述，只用真实的参考槽位，不虚构附件。

遵守 [样本确认流程](sample-approval.md)、[资产总表](asset-registry.md) 和 [最小加载与规则归属](load-map.md)。完整制作统一规划一次，按场景分阶段交付：补充基础资产 → 场景 → 视频。一个阶段的样本只确认该阶段的范围；已确认未变的内容复用。只有明确要求快速预览时才联合出样。文字方案不是生成的媒体，也不是绑定证据。已明确授权的局部修订复用未受影响的证据，不再重复申请同一授权。

## 独立资产项目的编译规则

视频使用独立创建的角色、生物、道具、场景或状态参考时，各块均不重写资产形态与外观；直接在映射块写 `名字 对应 @名字`，只补本段职责、状态/年龄版本、动作、表演、空间关系、光声与连续性。尚未生成/绑定的状态留块外，不把外观档案复制回来。下文“主体 + 外观”、身份块和按服装描述主体仅适用于无独立资产的纯文字路径，不能覆盖本规则。

[生成目标]用一个完整句子概括本片段主要内容：谁在什么情境下，经历/做了什么，产生什么关键变化或结果；只写本段覆盖的事件。风格、景别、运镜与声音进入 `[具体情节]`、`[视觉风格]`、`[镜头]` 或 `[声音]`；逐条去掉“镜头从空间转到动作、末态落在结果”这类泛化套话。完整交付仍按块结构，目标句精简不削减时间轴演出。

## 速查（QUICK FACTS）
- MCSLA = 模型（Model）、运镜（Camera）、主体（Subject）、画面（Look）、动作（Action）：每条提示词的五层 [→](#mcsla-公式the-mcsla-formula)
- 本项目里，图像只负责分配给它的外观、道具或场景属性；因果动作和状态交接保留在 `omni_reference` 提示词里。下面的 I2V 是旧做法背景 [→](#图生视频i2v旧模型背景不是当前工作室路线image-to-video-i2v--legacy-model-context-not-the-current-studio-route)
- 提示词控制在 200 词以内**只适用于短格式 MCSLA**；块结构的制作提示词用结构 lint 代替字数上限（HARD RULE 8 例外）[→](#高效提示词模式high-performing-prompt-patterns)
- 每个叙事阶段一个主要变化；兼容的阶段可以共用一个镜头或片段。动作数量是复杂度示例，不是配额；快速动作技巧：先按慢动作渲染，后期再加速 [→](#一场一个动作one-action-per-scene)
- 提示词里绝不留泛泛的情绪（“难过”“生气”），拆成肌肉动作、呼吸、眼睛、皮肤 [→](#拆解泛泛的情绪是哪一种-xgeneric-emotion-decomposition--which-kind-of-x)
- 反复出现的角色：在所选输出格式里，把身份锁定和时间上的表演分开 [→](#身份与动作分离规则identity-vs-motion-separation-rule)
- 冲突时的优先顺序：实际平台限制内的用户指令 → 共享导演契约 → 局部的原型/情绪选项 [→](#子模块之间的冲突处理conflict-resolution-between-sub-skills)
- 画幅是按模型的枚举，在界面或头部设置，绝不写进提示词正文；用 `model-specs.json` 核实 [→](#常见提示词错误common-prompt-mistakes)
- 避免同时进行相互冲突的运镜；先后反向的运镜要有动机；用稳定的动作名和对应模式的参考绑定 [→](#常见提示词错误common-prompt-mistakes)
- 每次重新生成只改**一个**变量 [→](#迭代规则一次只改一个变量the-iteration-rule--change-one-variable-at-a-time)
- 六步诊断顺序：主体 → 动作 → 运镜 → 风格 → 音频 → 输出；多数失败落在第 1–2 步 [→](#还不知道哪里不对时六步诊断顺序when-you-dont-know-whats-wrong-yet--the-6-pass-diagnostic-sequence)
- Seedance 短格式：30–100 词效果最好；主体加动作放在前 20–30 词。块结构的制作说明按语域中位数为 218–2,059 词，见 `higgsfield-seedance.md` § Official Prompt Architecture [→](#导演公式与-mcsla-的对应the-directors-formula--mcsla-mapping)
- 可选的短格式题材目标：产品 30–50 词、生活方式 40–60 词、剧情 60–100 词、MV 50–80 词、动漫 50–90 词 [→](#题材路由提示词长度与开头元素genre-router--prompt-length--lead-with-targets)
- 删掉空话（beautiful、stunning、epic、amazing），换成具体的画面或物理 [→](#空话词表anti-slop-vocabulary)
- Seedance 没有负面提示词语法，写成正向约束 [→](#不用负面提示词no-negative-prompts)
- 对白节奏示例：15 秒里约 25–30 个说出的词；保留已确认的台词，按实际说话加反应来估时 [→](#对白原型dialogue-archetypes)
- 旧版 Seedance 2.0 补救：失败时简化追踪人数、重新入画和倒影；画外的连续性要写明 [→](#角色与空间规则character--spatial-rules)
- 双重对比在对比服务于事件时同时改变景别和镜头性格；有意的重复覆盖也成立 [→](#双重对比切镜技巧double-contrast-cut-technique)
- 旧版 Seedance 2.0 关于年龄词的观察是建议，不是通用禁令；保留已确认的身份、年龄和对白 [→](#不看年龄的角色规则age-blind-character-rule)
- 从中间开场是可选的开场手法；保留因果或揭晓所需的铺垫 [→](#默认从中间开场default-in-medias-res)


## MCSLA 之前的共享叙事规划（Shared narrative planning before MCSLA）

视频任务通过 [最小加载与规则归属](load-map.md) 选读 [共享叙事规划](narrative-planning.md) 的适用章节；纯图像/音频/工具任务保留各自的范围。先确定目标和结局，找出剧情事件、因果、揭晓和状态转变，再为动作、对白、反应、阅读、停留和转场估时。不预设阶段数，不平均分配时长。**阶段不是一次切镜，也不是一个生成片段**：一个连续镜头可以跨多个阶段，一个阶段可能需要几个镜头，一次生成可以包含几个兼容的阶段。只为模式、复杂度、参考或实际时长限制而拆分调用，并带上接点状态。

从语义上规划八个导演层：**资产/参考锁定；整体目标；全局视听与空间；主体行为与节奏；分阶段演出；连续性/状态继承；结尾画面/接点；有范围的约束**。再编译进 MCSLA、身份/动作块、流畅叙述、带时间码的文字，或所选模型的原生格式。本项目里，各题材的完整视频提示词都按 [共享完整导演格式](template-general-director-2-5.md) 交付：资产、目标、视听与空间、行为、分阶段演出、结尾画面和约束，编译进 Higgsfield 块结构（[角色]…[生成目标]→[具体情节]→[视觉风格]→[镜头]→[声音]→[保持一致]）；连续性写在计时演出和 `[保持一致]` 里。每个阶段有时间/事件标题、展开的表演文字、视觉结果，运镜和接触音效写在动作里，对白写进 `[声音]` 的计时行。明确要求原生格式或局部修改时保留各自的输出约定，不另附重复的长文。每个阶段有初始状态、主要变化、可见反应和由下一阶段继承的结束状态。结尾画面和转场计入时长；结果一直保留到有动机的改变、清理、复原或时间/地点转换为止。

源视频编辑时，在要求改动之外保留原有时间码、时长、切镜结构、表演和音频时间。延伸时，在接点继承姿势、道具、动作相位/方向/速度、摄影机/构图、光和声音：向前延伸从源视频的结尾开始；反向延伸结束在**源视频首帧的状态**。只按所选模式的规则为新素材做预算。保留 I2V 里由参考负责的外观、所有参数/输入限制和下游的编辑/延伸流程。

首次完整视频创作或完整改写时，读 [完整演出范本](template-full-performance-example.md)。已授权的局部修订只读改动的规则和依赖（按 [最小加载与规则归属](load-map.md)），保留所有适用的契约检查。默认交付完整的演出说明：具体的动作展开、对象/对手的响应、主体的接续、视觉层次、有动机的运镜路径、声音、持续的结果和结尾画面细节。本指南别处的短格式字数目标不会截短这份母稿。单镜头或安静的事件不意味着简短的回答。只有明确的精简请求、局部编辑或目标格式的硬限制才精简交付；完整任务保留完整母稿，必要时另编一份合法的提交稿。保留所有原生格式、纯图像流程、I2V 的参考归属、变体和模型/模式能力。迁移的是范本的具体程度，不是它的奇幻题材、六个阶段、三十秒、配色或特效。

## MCSLA 公式（The MCSLA Formula）

每一条高效的 Higgsfield 提示词都建立在五层上。把它当作摄影师的检查清单：每层都填好，模型就拿到了需要的全部信息。

| 字母 | 元素 | 说明 | 例子 |
|--------|---------|-------------|---------|
| **M** | 模型 | 用哪个生成引擎 | “Use Seedance 2.5” |
| **C** | 运镜 | 明确的视点/路径；用平台预设时写准确名称 | “FPV Drone shot weaving through the alley” |
| **S** | 主体 | 谁/什么，加外观 | “A woman in a sand-colored suit, sharp eyes” |
| **L** | 画面 | 风格 + 色彩 + 光照 | “Cinematic, golden hour, anamorphic flare” |
| **A** | 动作 | 场景里发生什么 | “She turns slowly, wind lifting her coat” |

---

## 提示词类型（Prompt Types）

### 文生视频（Text-to-Video (T2V)）
从零开始，从头描述整个场景。
适合：建立场景、抽象概念、没有特定角色的环境。

```
[Subject + appearance].
[Environment — location, time, weather, atmosphere].
[Action — what happens and how].
[Camera — viewpoint, subject, path and endpoint; exact preset name if used].
[Look — style + color grade].
```

**例子：**
```
A lone astronaut stands on the surface of a red desert planet, helmet visor reflecting
twin moons rising on the horizon. Dust spirals slowly in the thin atmosphere.
She turns to face the camera, gloved hand raised in a slow salute.
Camera: slow Crane Up revealing the vast emptiness behind her.
Style: Cinematic, desaturated orange and deep blue, 2.35:1 anamorphic.
```

---

### 图生视频（I2V）：旧模型背景，不是当前工作室路线（Image-to-Video (I2V) — legacy model context, not the current studio route）
让一张给定的静帧动起来。在旧 I2V 模型里，图像决定起始帧；本项目的 Seedance 2.5 视频任务里，改为给它分配属性参考职责。
适合：角色一致性、产品镜头、肖像动画、让分镜动起来。

```
[Reference the input image as the first frame].
[Describe what should move, change, or animate — let the image own appearance].
[Camera — viewpoint, subject, path and endpoint; exact preset name if used].
[Style/atmosphere cues].
```

**例子：**
```
Starting from the provided image as the first frame.
The woman's hair lifts gently in the wind. She blinks slowly and turns her gaze
slightly to the left, a faint smile forming.
Camera: subtle Dolly In toward her face.
Style: Cinematic, warm afternoon light, shallow depth of field.
```

**I2V 的关键规则：**外观交给图像，避免重复重建画面。仍要声明参考职责、必要的起始/结束状态和连续性锁定。通过动作、响应和接续展开变化的部分，包括运镜和声音。对 @ 图像参考，要区分身份参考和真正的首帧锚点。

---

## 叙事结构（Narrative Structure）

两种格式都使用上面的事件/状态规划。阶段数来自内容；镜头和生成边界是另外的决定。下面的时间示例说明的是具体表演，不是默认的三段式构图。

### 流畅叙述（Fluid Narrative (preferred for most use cases)）
可选的短格式或明确不计时的提交稿，写连续的动作，不加时间码。完整演出交付保留共享的时间/事件标题和每个阶段里展开的文字。

```
A detective pushes open the door to the rain-soaked rooftop, coat whipping in the wind.
She steps to the edge and looks down at the city below — a thousand lights blurring
through the downpour. Camera dollies slowly behind her, then cranes up to reveal the
skyline. Cinematic style, cold blue tones, 16:9.
```

### 带时间码（Timestamped (use only for precise multi-beat sequences)）
默认的完整演出格式用时间/事件区间；短提交稿在不同动作需要时用时间目标，比如变形、多阶段动作段落、卡节拍的 MV。打算切镜时明确写出切镜。一镜到底里的阶段需要明确写“连续镜头”；单有时间码不等于切镜。生成的时间不保证逐帧精确，编辑时以源视频/音频时间码为准。

```
0–3s: Wide establishing shot. The fighter stands alone in the ring, chest heaving.
3–6s: Crash Zoom In on his face. Sweat on his brow, jaw clenched.
6–10s: 360 Orbit as he raises his fists. Crowd noise rises.
```

---

## 高效提示词模式（High-Performing Prompt Patterns）

> **视频提示词的头号错误**：外观写得太多，行为写得太少。给主体一件可以**做**的事。给他一种会产生可见行为的内在状态。描述运动或意图的动词，比形容词重要。

**具体胜过笼统：**
- ❌ “the camera moves dramatically”
- ✅ “camera Dolly Zoom In — subject stays the same size as the background rushes forward”

**主动动词撑起场景：**
- ❌ “a woman is in an alley”
- ✅ “a woman darts through a rain-soaked alley, coat flapping, boots splashing”

**把摄影机路径写明：**
选用支持的平台预设时用目录里的准确名称；自由文字也可以。
- ❌ “the camera slowly circles”（主体、弧线和终点都不清楚）
- ✅ “360 Orbit around the subject at eye level, returning to the frontal view”（预设示例）

**短格式 MCSLA：主体开头，风格收尾：**
主体 → 动作 → 运镜 → 风格是有用的编译顺序；完整交付保持共享的块结构顺序。

**控制在 200 词以内（短格式）：**
聚焦的提示词胜过面面俱到的。一个清楚的意图胜过十个含糊的细节。
**格式例外（HARD RULE 8）：**块结构制作提示词（`higgsfield-seedance.md` § Official Prompt Architecture）用结构 lint 代替字数上限；采集到的制作说明按语域中位数为 218–2,059 词。这个软上限只管可选的短格式 MCSLA 提交稿，不管完整的单镜头演出说明。

---

## 写提示词前的检查清单（The Pre-Prompt Checklist）

写任何提示词之前，先回答这五个问题。“给我来点电影感的”这种含糊提示什么也没告诉 AI。

| 问题 | 要写明什么 |
|----------|----------------|
| **谁？** | 主体 + 外观（例：“a man in a leather jacket”） |
| **在哪？** | 环境 + 氛围（例：“in a narrow aircraft galley, cold blue light”） |
| **发生了什么？** | 目标、因果事件，每个阶段一个主要变化（例：一次击打和它的可见反应） |
| **运镜？** | 视点、主体、路径和终点；用预设时写准确名称 |
| **情绪/题材？** | 风格 + 调色 |

---

## 一场一个动作（One Action Per Scene）

AI 模型能复现真实物理，但一次只能复现这么多。一个片段里要求多个复杂动作，会压垮模型。

**规划规则：**每个叙事阶段一个主要变化，辅助动作和反应服务于它。一个动作加 1–2 个次要运动是有用的短镜头示例，不是通用的片段上限。兼容的阶段可以共用一个镜头或一次生成。

在因果可读性、表演负荷或模型限制需要的地方拆开复杂段落，然后在剪辑软件里拼接，或者真正需要切镜时用 Multi-Shot Manual 模式。在每个接点保留离开时的状态；不要把一段完整表演切碎，也不要为了凑数编出额外节拍。

**快速动作技巧：**如果快速动作总是变形或崩坏，先按慢动作生成这场戏，再在后期（CapCut、Premiere、DaVinci）加速。模型在慢动作下渲染的物理更干净。

---

## 拆解泛泛的情绪：是哪一种 X？（Generic-Emotion Decomposition — Which kind of X?）

提示词里绝不留泛泛的情绪。“难过”“生气”“惊讶”“害怕”“若有所思”“恋爱中”，每一个都至少有三四种不同的身体表现，模型会根据提示词引向哪一种而渲染出不同的版本。只写“她看起来很惊讶”的提示词，每次重新生成都是不同的镜头，也会让批次之间的遵循度下降。

规则：把情绪落到它的触发和几条有意义的可见线索上，按构图和表演挑选。肌肉、呼吸、眼睛和皮肤线索是一份菜单，不是必须全部叠上。用场景语境来选；只有当一种悬而未决的解读会实质改变用户想要的表演时，才去澄清。

澄清模板：剧本或用户给出泛泛的情绪、而你不编造细节就无法拆解时使用：

> Which kind of surprise?
> (a) Light positive — eyebrows lift, lips part softly, slow inhale
>     through the nose, no other movement.
> (b) Shock — sharp inhale through the mouth, eyes widen, body
>     freezes in place, hand involuntarily lifts to chest.
> (c) Disbelief — slow blink, head tilts a fraction, lips press
>     together, only one eyebrow lifts.
> (d) Surprise-with-joy — eye light shifts (catchlight reads),
>     smile builds gradually, shoulders relax.

（用中文向用户提问时，同样给出四种可见表现供选择。）

同样的形式适用于任何泛泛的形容词：“紧张”“难过”“生气”“害怕”“若有所思”“恋爱中”各自能拆成 3–5 种不同的身体表现。拆解后的提示词产出的是表演；泛泛的提示词产出的是 AI 视频。

> **现成词库的替代。**想要不用从头拆解、可以直接放进提示词的具名微表情，见 `higgsfield-facs.md` 和 `higgsfield-acting.md`。它们覆盖了大多数常见的情绪语域，并给出锁定的身体描述。没有匹配的预设时用上面“从头拆解”的规则；有匹配时用词库。

### 叠加的情绪状态（Layered emotion states）

单轴拆解（上文）命名一个语域：生气 / 难过 / 惊讶。**叠加情绪**命名两个语域叠在一起的复合状态：*焦虑的决心*、*疲惫的温柔*、*苦涩的好笑*、*被逼到角落的盘算*。制作团队的实践发现，当叠加被描述为*一个通道调制另一个通道*时，模型渲染叠加状态比渲染单一语域更好：主导状态加底层状态加可见的破绽。

- **焦虑的决心**：咬紧的下颌加锁定的目光（决心），配上浅浅的胸式呼吸和垂在身侧的一只手一张一合（底下的焦虑）。
- **疲惫的温柔**：浅浅的微笑加半闭的眼睛（温柔），配上身体重量完全放下、缓慢的眨眼间隔（底下的疲惫）。
- **苦涩的好笑**：一侧嘴角的冷笑加眼里的光（好笑），配上眼角没有笑纹（底下的苦涩）。

把单轴目录里拆解好的身体表现叠起来，就组成叠加状态。主导状态放在脸上；底层状态放在呼吸、姿态和手部状态里；可见的破绽落在眼睛上。

要更细的控制，在已有的情绪线索上再叠一个**微小细节**：`Roco is very upset, and his lower lip trembles`。基础情绪给出整体表演；微小细节给模型一个具体的身体线索去渲染。制作团队的经验是，“简单情绪加一个微小细节”的组合，模型渲染得比过度拆解或过于泛泛的提示词都好。

---

## 身份与动作分离规则（Identity vs. Motion Separation Rule）

提示词涉及任何必须跨镜头保持一致的角色时，**把稳定的身份信息和时间上的表演分开**。下面两个带标签的块是可选的短格式版式；在完整导演格式里，身份属于资产/参考锁定（工作室格式：`[角色]` 映射行），动作属于分阶段演出和连续性（`[具体情节]`、`[保持一致]`）：

### 身份块：只写静态的视觉描述（Identity Block — Static visual descriptors ONLY）

独立创建的资产只用资产参考和必要的状态/版本；不要把下面的描述抄进视频。这份描述清单用于没有独立资产时的纯文字身份设计。
- 五官、肤色、体型、辨识标记
- 服装、配饰、配色
- 不写运动、不写镜头、不写时间性的语言

### 动作块：只写时间与镜头（Motion Block — Temporal and camera ONLY）
- 摄影机运动、动作编排、速度
- 环境运动、氛围变化
- 不重复角色外观

**差（混在一起），身份漂移：**
```
A woman with sharp cheekbones and auburn hair in a blue trench coat runs through
a rain-soaked alley, her coat flapping, sharp cheekbones catching the neon light,
camera chasing her at full speed, her auburn hair streaming behind her.
```

**好（分开），身份保持锁定：**

**身份块：**
```
Sharp cheekbones, auburn hair shoulder-length,
wearing a blue trench coat with silver buttons, lean athletic build.
```

**动作块：**
```
She runs through a rain-soaked alley, coat flapping behind her.
Camera: Action Run — low behind, matching pace.
Neon reflections streak across wet concrete.
Style: Cinematic, cold blue shadows, warm neon accents. 16:9.
```

**何时应用这条规则：**
- 同一角色出现在多镜头段落里时，一律适用
- 角色与摄影机运动同时出现时，一律适用

> **镜头与情绪同步是可选的。**动作块描述角色做**什么**、摄影机**怎么**动。生气用抖动手持、平静用平稳手持、揭示用缓慢推近，这些都是选择，不是必须执行的映射。按用户指令、视点和事件可读性选择镜头覆盖。示例见 `higgsfield-camera.md` § Camera-Emotion Sync。在挑选镜头处方之前先拆解底层的泛泛情绪，见上文 § Generic-Emotion Decomposition。

---

## 子模块之间的冲突处理（Conflict resolution between sub-skills）

子模块可以合理地为同一个镜头推荐不同的东西。`higgsfield-camera § Camera-Emotion Sync` 为悲伤推荐慢速低机位手持；`higgsfield-prompt § Scene Archetype Router` 允许氛围原型（情绪就是内容）用锁定的推近。两个子模块为同一场景推荐不同的运镜（或风格语域）时，按这个顺序解决：

1. **明确的用户指令优先。**用户说了“缓慢推近”，那就是这个运镜。助手的工作是让这个指令和其余结构配合，而不是推翻它。
2. **实际平台限制和共享导演契约起决定作用。**满足已核实的模式约束；在局部的创作建议之前，先按 [共享叙事规划](narrative-planning.md) 落实完整格式、因果表演和连续性。用户指令超出真实限制时，解决冲突，不要悄悄丢掉它。
3. **场景原型和情绪同步是可选项。**在它们帮助观众读懂事件时使用（氛围 → 固定 / 缓慢推近；动作 → 跟拍 / FPV；对白 → 过肩覆盖）。它们都不强制某个运镜、近景、切镜或情绪-镜头映射。

解决方式不明显时，把它摆出来。告诉用户哪个子模块推荐了什么、你为什么选了其中一个：这是正确的做法，也让用户可以推翻。悄悄挑选是失败模式；透明地挑选是纪律。

---

## 常见提示词错误（Common Prompt Mistakes）

| 错误 | 修正 |
|---------|-----|
| I2V 里重新描述图像 | 外观交给图像；保留参考锁定、动作过程和继承状态 |
| 泛泛的运镜语言 | 写明视点、主体、路径和终点；只有用预设时才写准确的预设名 |
| 没写风格 | 总是写上视觉风格 + 调色 |
| 一个镜头里太多相互竞争的动作 | 理清主要变化和反应；只有复杂度或限制需要时才拆分镜头/生成 |
| 运动相互矛盾 | 避免同时进行的反向运动；先 Dolly In 再 Dolly Out 需要有动机的转折和明确的终点 |
| 先写冲击后写原因 | 按因果顺序写铺垫、动作、接触/落空、反应、接续和持续结果 |
| 某个具体的武术动作失败 | 保留想要的技法，解释可见的力学；补救时简化多余的关节细节，但不删掉这次交锋 |
| 多个参考导致身份互换 | 每个身份单独绑定一行映射，动作里用稳定的角色名 |
| 身份和动作混在一个块里 | 分成身份块和动作块（见上文） |
| 画幅写在提示词正文里 | 在 Higgsfield 界面或输出格式头里设置画幅（按模型的枚举：例如 Seedance 2.5 接受 auto / 21:9 / 16:9 / 4:3 / 1:1 / 3:4 / 9:16，用 `higgsfield model get <model>` 或 MCP `models_explore` 核对）。用文字描述构图（“全身”“胸部以上”“大远景建立镜头”），不写数字比例。 |

> **输出画幅是枚举值，不是自由值；变形宽银幕是风格语域，不是输出尺寸。**输出画幅是硬性的、枚举的平台规格：每个 Seedance 模型只输出它枚举里的画幅。“变形宽银幕（anamorphic）”是一种*摄影语域*（变形镜头光晕、遮幅式的构图观感、宽于 2:1 的取景美感），模型可以在 16:9 输出*之内*渲染出来。在正文里把“16:9 anamorphic”写成一个短语是自相矛盾的：选一个。输出画幅放在头部（且必须是所选模型的枚举值之一，假设之前先用 `higgsfield model get <model>` 或 MCP 的 `models_explore` 核对）。变形宽银幕的风格线索放在画面那一行（“anamorphic-style flares, letterboxed composition”），作为*风格要求*，而不是输出尺寸。

> **约束：**要避免的瑕疵（漂浮的肢体、脸部变形、闪烁的纹理等）的完整清单，以及防止它们的提示写法，见 `negative-constraints.md`。按提示词类型检查相关类别。

---

## 迭代之前：失误是系统性的还是随机的？（Before You Iterate — Is the Miss Systematic or Stochastic?）

在约 1.5% 视频 / 约 1% 图像的采用率下，**大多数失误是随机波动，不是提示词坏了。**串行的单变量迭代适合*系统性*失误（提示词确实错了）。拿它对付*随机*失误，你是在“修”一条本来就对的提示词，一次一次地重掷同样的骰子烧额度。所以在动提示词**之前**先判断分叉：

- **这些失误是不是都以同一种方式失败？**（每次身份都漂移，每次服装都串染，切镜数总是错）→ **系统性。**提示词错了。迭代它，一次一个变量（下一节）。
- **它们是不是以各种不同方式失败，偶尔差一点就成？**（这一次表演平淡，那一次运镜不对，第三次物理怪异）→ **随机。**提示词是对的，掷出来的结果不对。**别再碰提示词。锁定它，批量生成，然后筛选。**

### 批量生成再筛选（收割随机性）：与风格扇出不是一回事（Batch-and-Select (Variance-Harvesting) — Not the Same as Stylistic Fan-Out）

判断为随机时，做法是**收割随机性**：保持**同一条锁定的提示词**不变，一次掷 N 次（图像网格生成，或用 Seedance 2.0 Mini 做便宜的视频重掷），筛出要留的那条。这和下一节的“风格扇出”例外正好相反：那是改出 N 种*不同的*画面；这是掷 N 次*完全相同的*尝试，因为提示词是对的，只是骰子的问题。两者看起来相似，经济上截然不同：扇出是探索，收割是利用。

**筛选标准：怎么从一批里挑出要留的。**没有严格的筛选，批量生成毫无价值。不要挑“最好看的”；对照你在生成前锁定的**可证伪的成功标准**来选：

1. **先用不变量做硬门槛。**身份、服装、切镜数、文字可读性、点名的物理锚点：任何一条不过的那次就*出局*，不管看起来多好。（这些是结构性失败模式；批量解决不了结构性失误，只能躲开随机性失误。）
2. **在幸存者里，给原本失败的那条随机轴打分**：你一直在重掷的表演、运镜或构图。最好的那条胜出。
3. **只选一条留下。**保留最符合锁定标准的那条，把它作为编辑或续接的已采用源素材。
4. **如果整批都过不了硬门槛**，那失误其实是系统性的：停止收割，回去迭代提示词。

---

## 迭代规则：一次只改一个变量（The Iteration Rule — Change One Variable at a Time）

提示词接近但不对、你准备重新生成时，每次尝试**只改一个变量**。主体细节、构图、运动行为、光照或风格：挑出错的那一个，只改它，重新生成。

**为什么重要：**如果你改了两个变量、结果变好了，你不知道是哪个改动带来的。如果结果变差了，你不知道是哪个改动弄坏的。无论哪种，你花掉了一次生成，却对提示词一无所知。单变量迭代让每次重新生成都有清楚的因果信号：留下有效的，去掉无效的，很快收敛到正确的提示词。

**例外：**提示词已经锁定、你只是为了风格探索做变化（例如一个已批准场景的五种光照变体）时，批量改动没问题。这条规则适用于*精修*阶段，不适用于扇出阶段。（别把这种风格扇出（N 种*不同的*画面）和上面的收割随机性混淆，后者是掷 N 次*完全相同*的锁定提示词来对付随机性失误。两者都是批量；只有一个改提示词。）

**流程：**

1. 生成基线。
2. 找出哪里不对：只挑**一件**具体的事。
3. 只改提示词里的这一个变量；其他一律不动。
4. 重新生成。
5. 与基线比较：针对性的改动是否按你预期的方向推动了结果？
6. 锁定这个改动。找出下一个问题。重复。

如果你发现自己想“一次全修好”，停下来问哪个修正最重要。那一个放进这次重新生成；其余的排队等。

### 提示词窗口的清理（Prompt-window hygiene）

迭代还会累积杂物：已经不适用的旧编辑、前面镜头附上的过期参考图、层层叠加的相互矛盾的分句，以及长到模型在噪音里丢掉承重部分的提示词。来自制作实践的四种清理方式：

- **删除过时的提示词块。**之前某段提示词是关于便利贴道具的，而你已经转到角色生成，就把便利贴那段删掉。否则模型偶尔会把过期的道具拉进新的生成。
- **在已有提示词上追加会制造矛盾。**编辑靠追加而不是替换累积时，提示词会收集相互矛盾的分句（旧版的 `tight close-up`，新版的 `wide establishing`）。症状：输出退化成模型困惑的瑕疵。对策：迭代时原地替换相关分句，而不是再追加一句。
- **移除过期的参考图。**资产在镜头之间变化时（第 1 镜拍立得在冰箱上，第 2 镜被拿下来了），把已经过期的参考从提示词窗口里拿掉，免得模型还在想办法摆放它。
- **提示词过载时做一次清理。**提示词因为累积的细节长到约 2–3k 字符以上时，请助手（或你用的任何提示词构建工具）**优化 / 研究上下文 / 清理提示词**：合并重复的分句，去掉已经过时的修饰，保留承重结构和完整的因果表演。这是累积杂物的清理触发点，不是母稿的 2–3k 字符上限。遇到核实过的平台字段限制时另编提交稿。

### 还不知道哪里不对时：六步诊断顺序（When You Don't Know What's Wrong Yet — the 6-Pass Diagnostic Sequence）

上面的迭代规则假设你能找出该改哪一个变量。找不出时（输出隐约不对，你说不出为什么），跑六步诊断顺序来找。每一步隔离一个变量，按顺序，测完再往下走。

顺序不是随意的。主体和动作承载最大的 token 权重（位于提示词前部）；运镜和风格其次；音频和输出控制在外围。按这个顺序诊断，最先暴露杠杆最大的问题，免得你在风格上找修正，而真正的问题是上面三层的主体描述。

| 步骤 | 变量 | 问题 |
|------|----------|----------|
| 1 | 主体 | 角色 / 物体 / 焦点元素是否描述得毫无歧义？ |
| 2 | 动作 | 每个阶段的主要变化是否具体，有可读的原因、反应和继承的结束状态？ |
| 3 | 运镜 | 运镜是否点了名（预设或具体动词），而不是暗示？ |
| 4 | 风格 | 画面是否有锚点（配色、调色、镜头、光照），而不只是形容词？ |
| 5 | 音频 | 如果音频是输出的一部分，是否描述成带具体声音的平行轨？ |
| 6 | 输出 | 画幅、时长和分辨率是否按镜头需要刻意设定？ |

**怎么用：**从第 1 步开始。把主体写清楚后结果变好了，就找到了变量：回到迭代规则的循环继续。第 1 步没有推动结果，就锁定主体，进入第 2 步，依此类推。这个顺序是用来找问题的，不是精修循环。一旦知道哪个变量错了，就交给迭代规则。

**不要盲目跑完六步。**六次重新生成花六份额度。这个顺序的价值在于*次序*：大多数提示词失败落在第 1 或第 2 步，因为前部的 token 占主导。走到第 4 步结果还没动，提示词可能需要结构性重写，而不是迭代。

---

## Seedance 2.0 提示词最佳实践（Seedance 2.0 Prompting Best Practices）

这些最佳实践适用于 Seedance 2.0 / 2.5，是对上面 MCSLA 公式的补充，不是替代：以 MCSLA 为主框架，再应用这些精修。

> 位于 MCSLA 之上的用户意图层（你处在哪种工作模式：探索 / 续接 / 桥接 / 修复，以及每种怎么经由 Seedance 的提示模式路由）见 `higgsfield-seedance.md` § Working Modes。工作模式与提示模式的区分在同一文件、紧挨着的上方。

### 意图胜过精确（Intent over Precision）

告诉模型你想要**什么**、它应该**给人什么感觉**，而不是每个微小细节。在短格式里，短提示词（30–100 词）一贯胜过长提示词。（块结构的制作说明是另一种格式：那里用结构代替上限，见 `higgsfield-seedance.md` § Official Prompt Architecture。）模型是和你合作的 AI 导演，不是你下命令的渲染引擎。

### 导演公式与 MCSLA 的对应（The Director's Formula → MCSLA Mapping）

导演公式直接对应 MCSLA：

| 导演公式 | MCSLA 层 | 优先级 |
|-------------------|-------------|----------|
| 主体 | S（主体） | 前 20–30 词（前部 token 权重大） |
| 动作 | A（动作） | 前 20–30 词 |
| 场景 | —（语境） | 辅助细节 |
| 运镜 | C（运镜） | 主体 + 动作之后 |
| 风格 | L（画面） | 运镜之后 |
| 约束 | —（护栏） | 提示词末尾 |

**短格式要点：**在可选的紧凑提交稿里，主体加动作可以放在前 20–30 词；完整母稿保持共享的块顺序。前部 token 在生成引擎里权重不成比例地大。

### 题材路由：提示词长度与开头元素（Genre Router — Prompt Length & Lead-With Targets）

可选的短格式编译里，这些题材长度和开头元素是起步目标。它们不限制、也不重排完整演出母稿：

| 题材 | 开头用 | 目标长度 | 开头示例 |
|-------|-----------|---------------|-------------|
| 物件静物 | 主体 | 30–50 词 | “A matte-black wireless earbud case rotates slowly on a marble pedestal...” |
| 生活方式 / 社媒 | 动作 | 40–60 词 | “She reaches for the coffee mug, steam curling upward...” |
| 剧情 / 叙事 | 场景 | 60–100 词 | “Rain hammers a narrow Tokyo alley at 2 AM, neon signs reflecting in puddles...” |
| MV | 风格 | 50–80 词 | “Anamorphic flares, crushed blacks, 16mm grain...” |
| 风景 / 旅行 | 场景 | 30–60 词 | “Dawn breaks over a volcanic ridge, mist pouring through the caldera...” |
| 动漫 / 艺术 | 风格 | 50–90 词 | “Cel-shaded lines, saturated palette, painterly cloud physics...” |

> 风格开头里的质感词（“16mm grain”）是**画面选择**，就该放在那里。同一个词作为裸露的质量恳求拖在提示词末尾，反而会让整帧变软：区别见 `negative-constraints.md` § Whole-Frame Degradation。

### 空话词表（Anti-Slop Vocabulary）

删掉这些词：它们不提供任何信息，浪费 token：

| 空话 | 换成 |
|-----------|-------------|
| beautiful | （删掉，改写具体的画面） |
| stunning | （删掉，写出它为什么醒目） |
| epic | large-scale, sweeping, towering |
| amazing | （删掉，展示，不要告知） |
| dynamic | fast-tracking, whip-pan, handheld |
| energetic | sprinting, jumping, arms pumping |
| cinematic camera movement | slow dolly push / crane up / tracking shot |
| cool transition | match-cut / whip pan / smash cut |
| cinematic / cinematic lighting | 一个**具名参照**：一种构图手法（“对称构图”）、一种布光（“golden-hour backlight, long shadows”）或一个镜头规格（“anamorphic 2.39:1, lens flare from a practical light”）；工作室复制正文不写导演名或片名 |
| high quality / high-res / 4K look | （删掉：分辨率是渲染设置，不是提示词）；工作室规则允许保留 8K、高清细节等质量词，但它们不能替代具体描述 |

> **为什么替代比删除更重要：**泛泛的形容词是分散在大片训练数据里的高频标签，会把输出拉向毫无特点的平均。一种布光或一个镜头规格采样的是*窄而训练充分的*分布，真的能推动结果。Seedance 专门的处理见 `higgsfield-seedance.md` § Prompt-Craft Laws → Name the thing。

### 物理语言（Physics Language）

用具体的物理后果代替情绪词。模型对可观察的物理细节有反应：

- ~~“powerful punch”~~ → `fist connects, sweat flies off in slow motion, opponent's head snaps back`
- ~~“dramatic entrance”~~ → `door slams open, dust erupts from the frame, light floods the dark room`
- ~~“fast car”~~ → `tires spin, gravel sprays backward, chassis drops as acceleration kicks in`

### 程度副词（Degree Adverbs）

模型无法单从图像推断强度。用副词引导解读：

`slowly`、`dramatically`、`violently`、`gently`、`frantically`、`deliberately`、`cautiously`、`explosively`

**例子：**“She turns **slowly**, eyes narrowing **deliberately**, then **explosively** lunges forward.”

### 动作的三幕节奏（Three-Act Rhythm for Action）

冲击类事件的一种可选节奏如下。在它的起因和结果符合故事时使用；它不是必须的三段结构。一场戏可以从动作中间开场、停留在一个后果上，或者经过不同数量的变化展开。时长跟随事件和反应，而不是三等分：

1. **蓄力**：紧张累积，能量聚集
2. **爆发**：动作爆发
3. **余波**：物理后果展开

**例子：**“The fighter plants her feet, fists clenching (charge-up). She throws a spinning kick that connects with the sandbag (burst). The bag swings violently, chain rattling, sand dust puffing from the seams (aftermath).”

### 不用负面提示词（No Negative Prompts）

Seedance 不支持在提示词正文里写负面提示语法。不要写“no blur”或“avoid shaky camera”。改用正向约束，描述你**想要**什么：

- ~~“no shaky camera”~~ → `locked-off static camera, no movement`
- ~~“no blur”~~，意思是整帧发糊 → `sharp focus throughout, deep depth of field`
- ~~“no blur”~~，意思是背景虚化吃掉了主体 → `subject in sharp focus, background falling into soft bokeh`
- ~~“don't make it dark”~~ → `bright, evenly lit, overcast daylight`

两种景深写法不能互换：按哪个平面必须保持清晰来选（`negative-constraints.md` § Depth of field — two substitutes, two intents）。

### 音频是一等元素（Audio as First-Class Element）

在提示词里单独描述音频。BGM、环境音效和对白通过双声道立体声生成作为平行轨处理：

```
A barista grinds coffee beans, pours steaming water over the filter.
Camera: tight close-up, slow dolly across the counter.
Style: warm tones, shallow depth of field.

Audio: the whir of the grinder, water bubbling through the filter,
ceramic mug placed on a wooden counter with a soft clink.
Soft jazz piano in the background, barely audible.
```

“磨砂玻璃的刮擦声、毛绒布料的窸窣、轻敲亚克力”这类声音设计描述会直接影响生成的音频。工作室格式里，接触音效写在 `[具体情节]` 各段的 `声音：` 行，对白写在 `[声音]` 的计时行，音乐只在用户要求时用 `(…)`，末尾 `NO BGM。`

---

## Seedance 2.0 场景原型路由（Seedance 2.0 Scene Archetype Router）

做完叙事规划、填 MCSLA 之前，找出一个有用的场景原型。它提示运镜行为和空间逻辑；不决定阶段数、时长、强制反转或每个节拍都切镜。把原型适配到实际的因果链和结局上。

### 动作原型（Action Archetypes）

| 原型 | 镜头焦点 | 空间动态 |
|-----------|-------------|---------------|
| **追逐** | 距离在缩短/拉开。被追者在画面前方，追击者在后 | 路径变窄/变宽 |
| **对决** | 镜头可以偏向当前占优的一方；随实际交锋转换 | 双方争夺位置 |
| **冲击** | 蓄势慢 → 命中快 → 余波慢 | 接触点在中心 |

**决策树：**追逐？→ 追逐。两个对手交替占优？→ 对决。一个决定性的接触瞬间？→ 冲击。都不是 → 默认对决。

**对决的经验法则：**优势交替可以让交锋更好读，但任何一方都不必按固定节拍表失去优势。故事需要时，持续占优或一边倒的攻势都成立；写出实际的动态，不要编造反转。

### 通用原型（General Archetypes）

| 原型 | 什么在变 | 镜头特征 |
|-----------|-------------|-----------------|
| **旅程** | 空间位置：道路、飞行、行走 | 跟拍、航拍、并行移动。风景掠过。 |
| **氛围** | 什么都不变，情绪就是内容。雨打玻璃、空荡的街道。 | 极少运动。缓慢推近或固定停留。微小变化承载全部戏剧性。 |
| **揭示** | 隐藏 → 可见。门打开、雾散开、镜头绕过转角。 | 摇、升降、推轨揭示。镜头控制观众**何时**看到主体。 |

**决策树：**主体在空间里移动？→ 旅程。隐藏的东西变得可见？→ 揭示。什么都不变、情绪就是内容？→ 氛围。都不是 → 默认氛围。

### 对白原型（Dialogue Archetypes）

| 原型 | 权力动态 | 镜头特征 |
|-----------|--------------|-----------------|
| **对峙** | 双方都在施压；一次交锋赢得主导权时，主导才转移。 | 紧凑的过肩；任何越轴都要有可读的权力转移作为动机。 |
| **审讯** | 不对称：一方套话，一方抵抗。 | 提问者用低角度，沉默时推近。 |
| **谈判** | 平衡：双方都有所求。 | 对称构图，景别匹配。 |

**决策树：**双方都在施压、主导权交替？→ 对峙。一方套话、一方抵抗？→ 审讯。双方都有所求、势均力敌？→ 谈判。都不是 → 默认对峙。

**对白节奏示例：**15 秒里在声学上大约能装下 25–30 个说出的词；可靠的口型预算因模型、语言和演绎而异（见 `higgsfield-audio.md`）。按实际说话和反应时间估算。用户明确要求压缩时，一句带铺垫和反应的权力转移台词是一种可能的剪法，不是必须的三句结构。保留已确认的对白和源时间；装不下时，指出冲突，使用经授权的更长时长、多个片段或剧本修改。

---

## Seedance 2.0 引擎约束（Seedance 2.0 Engine Constraints）

这些旧版 Seedance 2.0 观察是补救指南，不是已核实的通用平台限制。在观察到失败时应用，同时保留用户指令和共享的因果表演规划；实际模型/模式限制另行核实。

### 角色与空间规则（Character & spatial rules）
- **追踪人数的补救。**身份漂移时，尝试把镜头覆盖集中在一对或三人组上，写明互动方向；≤3 人是旧版的可靠性建议，不是通用的人数上限。
- **出画/重新入画的补救。**回来的角色漂移时，锚定他的路线、时机、身份和重新入画的状态，或用匹配的镜头覆盖。不要禁止有意的连续出画/重新入画。
- **画外的连续性。**写明角色去了哪里、什么变了、为什么、带着什么状态回来。观众需要时展示原因；明确的画外事件也可以承载连续性。
- **切镜会打断空间连续。**任何切镜之后重新锚定位置和朝向。明确写出运动方向（“moving left-to-right”）。
- **避免倒影镜头**（刀刃、水洼、镜子）：Seedance 渲染倒影时会打乱场景地理。

### 感官规则（Sensory rules）
- **只描述看得见或听得见的东西。**不写气味、味道或内心想法。
  - ❌ “The air smells of pine.” ✅ “Pine needles covering the ground, wind moving through branches.”
- **微表情作为物理有效。**✅ “jaw clenches, nostrils flare.” ❌ “looks angry.”

> 微表情拆解成的八个具名底层通道，见 `vocab.md` § Emotion as Visible Behavior — Channels。

### 动作规则（Action rules）
- **意图 + 具名技法 + 可见力学。**保留用户点名的动作，以及让它可读的铺垫、发力、方向、接触/落空和恢复。短格式补救时，简化无依据的关节角度精度，但不要把动作简化成一个状态标签。
- **后果和反应保持明确。**“Thrown into the side door, metal buckling and glass scattering; she braces against the rebound and sweeps the attacker's leg”保留了因果交锋。保留对象响应、主体接续和持续的损坏；只删多余的描述。

### 双重对比切镜技巧（Double-contrast cut technique）

当一个事件得益于强烈的视觉对比时，**同时**改变景别和镜头性格。景别序列：`大远景 → 远景 → 中景 → 中近景 → 近景 → 大特写`。镜头性格：`手持 | 固定 | 稳定跟拍 | 摇臂 | 航拍`。

**单一对比：**中景手持 → 近景手持。
**双重对比：**中景手持 → 大特写固定锁定。

按叙事和空间目的选择。重复的固定对白覆盖、匹配剪辑和有意重复的构图都成立；不要为了制造变化而加切镜或改动已批准的运镜指令。

### 插入镜头：有因果动机，点名主体（Inserts — causally motivated, named subject）

插入镜头在任意景别上把注意力集中到一个细节。0.3–0.5 秒的固定标点是一个例子；线索揭示或道具状态变化需要足够阅读的时间。规则：
- **给插入镜头一个功能**：标点、信息揭示或可见的状态变化；除非信息改变了推进，否则它不必成为新的叙事阶段
- **有因果动机**：观众必须明白**为什么**看到这个细节。主角被摔到引擎盖上 → **他的**手抓住金属。不是泛泛的水洼里一只靴子。
- **点名主体**：写明是**谁的**身体部位或细节。没有归属时，Seedance 会渲染错误的内容。
- **选择有动机的对比**：能改善插入镜头时用双重对比；保留有意的连续性和已批准的运镜指令。

### 不看年龄的角色规则（Age-blind character rule）

Seedance 提示词里绝不按年龄描述角色。要避免的触发词：*boy、girl、child、kid、young、teen、little*。Seedance 的年龄推断不可靠，而且会跨镜头漂移。

- **有图像输入时：**按**角色身份**（骑手、身影、旅人、说话者）、**服装**和**动作**描述。不给人贴“是谁”的标签，只标“做什么”。
- **没有图像输入时：**用功能性标签：“a figure in a wool cloak”、“a silhouette against the horizon”。

### 默认从中间开场（Default: in medias res）

从已经进行中的状态开场可以去掉多余的铺垫。在原因、地理和利害仍然清楚时使用；当开场铺垫或安静的停留能换来一次揭示或反应时保留它。不要固定保留或删掉开场的若干秒。用户指定的开场和结局仍是约束。工作室格式里，有人物的 Clip 第一秒是定位秒（全景，人物到位，`[声音]` 写 `0s-1s｜<名字>轻声：{Hm.}`），从中间开场的动作从第二段开始。

> 包括中英双语 JSON 输出格式在内的完整 Seedance 导演参考见 `seedance-bilingual-json.md`：需要带原生场景原型路由和明确输出约定的独立导演模式提示词时使用。

---

## 相关模块（Related skills）
- `higgsfield-camera`：所有具名运镜控制
- `higgsfield-style`：视觉风格、调色、光照
- `higgsfield-models`：模型选择
- `higgsfield-troubleshoot`：修复失败的生成
- `template-*.md`：带注释的各题材提示词模板

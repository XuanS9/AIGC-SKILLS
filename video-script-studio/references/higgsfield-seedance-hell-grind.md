# Hell Grind：长片制作流程（Hell Grind — the Feature-Film Pipeline）

`[OFFICIAL — Higgsfield "Hell Grind" open-source brief]`：Higgsfield 开源了他们 **95 分钟 AI 长片**背后的制作系统，包括随附的 CINEDANCE 提示词技能。本文件是那个系统里本仓库原本没有的部分。本文件属于 Seedance 2.0 历史资料；其中被工作室采纳的规则（第一秒定位、对白只放音频块、无头全身格）已写进当前模块，见各处说明。

**本文件不是什么。**CINEDANCE 的提示词方法（块骨架、视场角度数、光学决策树、正向锁定、切镜词汇、上下文隔离、标签命名）已经是 `higgsfield-seedance.md` § Official Prompt Architecture 里的 `[OFFICIAL]` 方法，采集自同一来源系列。这里不重复。引擎规则（`higgsfield-seedance-engine-rules.md`）和教程模式（`higgsfield-seedance-production-patterns.md`）也不重复。

这里*有*的是提示词之上的那一层：生成任何东西之前资产怎么构建，一场戏的地理怎么在它的每个镜头里锁定，对白怎么构建，以及迭代循环怎么跑，让一个镜头收敛而不是烧额度。来源说明里的每一条规则都存在，是因为某个镜头没有它就失败了。

> **配合阅读：**`higgsfield-seedance.md`（提示词语法）、`higgsfield-seedance-engine-rules.md`（硬约束）、`higgsfield-acting.md`（这个流程默认的表演层），以及 `template-global-style-prefix.md`（这个流程粘到每条提示词上的风格前缀）。

---

## 核心问题：模型没有记忆（The core problem: the model has no memory）

视频模型在两次生成之间什么都不记得。如果一个角色没有在*每一条*提示词里被完整描述，下一个镜头就会给他一张不同的脸和一件不同的夹克。下面每一项技法都是这个事实的推论。

**每次都描述一切。**描述词**一字不差地**进入每条提示词，**绝不缩短**。一致性不是一个设置；它是重复。

---

## 前期：资产（Pre-production: assets）

**资产**是一对东西：**文字 + 图像**。文字是完整的描述（*描述词*），一字不差地粘进每条提示词。图像是模型锚定的参考。两者单独都不起作用。

参考**只用于资产**：角色和场景。其他一切都是提示词文字。

### 角色设定表是三张图，其中一张没有头（The character sheet is three images — and one of them has no head）

| 格 | 内容 |
|---|---|
| 1 | 脸部近景 |
| 2 | 全身正面：**无头** |
| 3 | 全身背面 |

**为什么正面的人形没有头。**在远景里，模型总是从设定表上那个小的全身人形取脸，而那里的脸又小又糊。去掉那个头，模型就只有一个地方可以取脸：近景。这听起来很荒唐，但它修好了一整类坏镜头。

**刻意让设定表保持无聊。**中性灰背景、平光、看得见毛孔的真实皮肤、不修图。电影感在场景和视频提示词里：把胶片颗粒和电影镜头烤进设定表，角色就会把那种画面带进每一场戏，并且不再对新的光做出反应。

**设定表用一张 3/4 角度的大肖像效果最好**：脸微微转开，不是正对。

> 补充工作室的 [角色资产交付规范](template-character-asset-delivery.md)。无头的正面格和刻意无聊的规则是 Hell Grind 的补充；工作室组板的背景按服装明度选浅暖白灰或中灰。

### 局部修改用遮罩加上去，绝不再完整跑一遍（Point changes go on with masks, never with a second full pass）

衣服、伤疤和血是**局部修改**。在 Nano Banana Pro 或 Seedream 里对原设定表做修改，然后在任何图形编辑器里**手工用遮罩**把它放回原图上：遮罩只把改动的部分（夹克、伤疤、血）放在原图上面，其他一切保持不动。

**保护质量的规则：一张图绝不完整地经过模型两次。**每多一遍都会破坏质感、让颜色漂移。两遍之后，脸会变得对称、塑料、没有生气：而那种死掉的质感之后会损害角色在视频里的*表演*。模型做局部编辑；最终版永远是在原图上用遮罩组装出来的。

### 音色不是资产：它是一个锁定的描述词（The voice is not an asset — it is a locked descriptor）

实际的说话人/参考支持取决于所选模式，而不是推断出来的固定音色数量。工作室角色资产可以在图像提示词之外带一份登记的音色描述（音色、音域、共鸣、口音），视频稿可以在 `[角色]` 里为说话的角色引用它。当前交付仍然在行内写：气息、语速、音量、停顿和用力。实际提供的音频参考或 ID 优先于文字描述。

```
Delivery: short measured phrases, quieter when pressing the partner.
```

有条件时，在两次生成之间检查实际的音频匹配。光靠文字措辞不能证明生成的语音稳定。

### 表演和外观、音色一样锁定（The acting is locked the same way as the look and the voice）

每个角色在开拍之前都有一段写好的行为段落：动作、手、习惯、紧张时的小动作、眼神，以及在压力下究竟怎么崩。这一段是真相来源；每场戏按当时的姿态和动作改写它，但核心永远不变。

**一场戏里身体上做不到的行为是转移，而不是删除。**一个会在房间里踱步的角色，坐到沙发上并不会平静下来：同样的能量转移到摇晃、敲手指和不连贯的手势上。

完整系统：`higgsfield-acting.md`。

### 场景设定表（Location sheets）

- **场景设定表拍 3/4 角度，不拍正面。**正面的“漂亮图”在远景里会变成平的墙纸，而在它的边缘之外，模型每次都会编出新的周边环境。3/4 视角给模型可以读的纵深：它能正确摆放角色，并覆盖接近一整圈的角度。
- **每个场景都留一个锚点**：一根柱子、一盏灯、一张沙发：并把站位绑在它上面。“角色在灯旁，面朝门”有效。“角色在房间里”是抽奖。
- **保持一套光照逻辑**：一个光源、一个阴影方向，绝不两个太阳。否则每个新角度都会重新发明光照。
- **反打角度，路线 1：**在 GPT Image 2 或 Nano Banana 里生成同一个房间的一个角落，匹配原图的柔焦。
- **反打角度，路线 2**（制作后期才发现）：生成一段**空场景的视频**，镜头在空间里慢慢走一遍：Seedance 会按设定表一致地画出其他几面。截下你需要的角度，拿到 Seedream 或 Nano Banana Pro 里，提示一次质感/光照改进。一张图就得到一整套场景设定表。

### 写明每张参考的职责，并禁止场景继承（Name the role of every reference — and ban location inheritance）

你不写，模型就自己决定，而且会决定错：它复制构图而不是脸，或者复制脸而不是色板。

```
@roco for character reference
@jaxx for character reference
@loc_cave_front for location reference — take only the space and the texture: raw concrete,
black rock walls. Do not use as a starting frame, do not inherit the composition, the angle,
or the grade.
```

**场景参考要明确禁止继承。**这就是 `higgsfield-seedance.md` § Reference Roles 里的环境职责，用模型自己的工作词汇说出来。

**整个项目一本名字词典。**所有资产都放在标签下（`@roco`、`@loc_cave_front`），同样的标签到处使用：文档里、提示词里、界面里。（工作室项目的调用名是 `@` + 纯中文名，以资产总表为准。）

---

## GEO SPATIAL LAYOUT 块（The GEO SPATIAL LAYOUT block）

**早期素材里最贵的问题：**角色瞬移、互换位置，镜头跳到错的一边。原因很简单：模型不记得上一个镜头里谁站在哪里。

解药是**用几行写出这个地方的平面图**：地标物件、右边是什么、左边是什么、摄影机站在哪里。**没有角色，没有动作：只有地方本身。**每场戏写一次，*不加改动地*粘进那场戏的每个镜头。模型在每个镜头里得到同一个房间，就没有地方再把人弄丢。

```
GEO SPATIAL LAYOUT (locked across every shot — pure spatial map):
— PLATFORM = raised circular ritual stone disc at the edge of a cliff.
— ALTAR-MONOLITH: at the cliff edge, MID-RIGHT position relative to the platform.
— RITUAL CENTER: CENTER-LEFT, ~3 m from the altar.
— 180° AXIS: camera ALWAYS stays on the corpse-field side — it NEVER crosses the line.
— BACK-LIGHTING: crimson horizon glow comes from BEHIND the platform, rim-lighting
  silhouettes from camera's perspective.
```

读写这张地图的规则：

- **GEO 只是地图。**地方的*样子*仍然来自场景资产：它的描述词和参考和地图并排放进提示词。
- **左右只以摄影机为准。**“画面左”和“画面右”：模型不懂“在角色的左边”。
- **位置从地标出发、用米来定**：“在祭坛旁”、“三米远”。
- **写明摄影机站在哪一侧、永远不越过哪条线。**这让每次切镜保持在一条轴线上。
- **每次切镜之后，重新说明谁站在哪里、看向哪里。**模型不记得上一个镜头。
- **静态对白给房间的一个角落，而不是整个房间。**模型拥有的空间越少，它在把角色放在哪里这件事上的选择就越少。

> **与空间布局块的关系**（`higgsfield-seedance.md` § Spatial Layout Block）：那个块是逐镜头的，并且*包括人*：画面位置、占比、朝向、接触点。GEO 是逐**场**的，不包括人，并且原封不动地粘进这场戏的每个镜头。两个都用：GEO 固定房间，空间布局块固定这个镜头里谁站在里面。工作室格式里，房间地理写进场景资产和 `[保持一致]`，人物位置写进第一段定位秒的 `画面：` 行（见 [空间布局](spatial-layout.md)）。

---

## 第一秒永远是远景（The first second is always a wide）

一场戏开头的一秒，**没有台词、没有动作**：模型“拍下”这个布置（谁站在哪里、什么东西在哪里、光从哪里来），并在后面的每个镜头里保持它。去掉这一秒，角色就开始互换位置。

制作中的两个改进：

- **“hm”技巧。**让某人在那一秒里说一个短词：“hm”。这让 Seedance 更容易把那个远景当作一个独立的镜头。
- **远景不一定要安静。**如果这个镜头是在回应上一个，把**上一段片子台词的尾巴**喂进第一秒：演员就会用对的语气回应对的内容，两段片子在接缝处粘起来。

```
FIRST FRAME AND SPATIAL BLOCKING
SHOT 1 (~1.0s) — a wide that FIXES THE POSITIONS and does nothing else: ROCO planted at the
center of the mat, five smashed mannequins at CENTER-RIGHT, the door open at frame-LEFT with
JAX and REIN one step inside it, trays in hand. No camera move, no action beat.

AUDIO
Over that first second, the tail of the previous clip's line arrives on REIN's lips as she
walks in: "...I've got the coordinates." ROCO's eyes find her before his head turns.

ACTION TIMING
1.0s onward — ROCO answers into the same rhythm, dry and worn: "You're late."
```

> 工作室采纳了这条规则：每个 Clip 有 `只有 N≥1 人` 时，`[声音]` 必须有一行 `0s-<第一段结束>s｜<名字>轻声：{Hm.}`，由 `director_contract_lint.py` 检查（格式归属：[跨类型导演模板](template-general-director-2-5.md)）。
>
> 这是 `higgsfield-seedance-production-patterns.md` 里“开场画面不空”模式的*刻意例外*，而不是和它矛盾。那条规则禁止的是**空的**开场画面：模型“到场”时画面里没有人。Hell Grind 的远景**从第一帧起就站满了人**；它扣住的是*动作*，只扣一秒，换来整场戏的位置锁定。

---

## 角色数量头（The character-count header）

SCENE CONTEXT 块用一个数量头开场，而不是一段描述：

```
EXACT 3 CHARACTERS — NO DUPLICATES: ROCO, JAX, REIN.
```

**这不是形式。**模型喜欢加多余的人，也喜欢克隆家具。只有参考在提示词里的人才存在于画面里：重复的布景陈设要直接加一句带数量的禁止：

```
Exactly ONE mannequin, NEVER render a second one.
FIVE smashed mannequins, never re-rendered as intact, never multiplied. Two trays, never more.
```

计数的物件属于 POSITIVE LOCKS，写成画面里**有**什么。（工作室格式的对应写法是 `[角色]` 块的 `只有 N 人`，以及 `[保持一致]` 里的物件数量。）

---

## 骨架里多出的两个块（Two extra blocks in the skeleton）

Hell Grind 的骨架是 `higgsfield-seedance.md` § Block order，加上它明确点名的三个块：

| 块 | 内容 |
|---|---|
| **CHARACTER ACTING** | 每个角色：情绪状态 · 此刻想要什么 · 在隐藏什么 · 主导的身体节奏 · 这个节拍里可见的习惯 · 镜头过程中什么在变 |
| **STYLE** | 风格前缀，一字不差地粘贴（`template-global-style-prefix.md`） |
| **QUALITY** | 细节和稳定性要求：“8K detail, pore-level skin, no jitter, no flicker; the faces stay exactly their references at every distance” |

CHARACTER ACTING 是 PERFORMANCE 块的制作形式。示例：

```
CHARACTER ACTING
ROCO — emotional state: burnt out and still going. What he wants in this moment: one more
clean hit before anyone walks in on him failing. What he is hiding: that the arm is winning,
and that it frightens him. Dominant body rhythm: heavy, planted, slow recovery between bursts.
Visible habits in this beat: the jaw set-and-release, the right shoulder pulled low by the
crystal, the blood he does not wipe, the gaze that finds the broken mannequins first and
people second. What changes across the shot: the second the door opens he re-arms his face —
the exhaustion folds back behind a dry half-smile before he says a word.
```

**收尾的技术标签尾巴。**制作提示词在风格前缀之后以一行短标签结尾：

```
Photoreal. NON-IP. 16:9. 12s. SFX only. NO CGI. Cinematic.
```

`SFX only. No music.` 在这个流程里被视为必须：音乐属于后期，生成的配乐只会妨碍剪辑。（这是*项目*的选择，与采集语料里 13 个项目中 12 个禁止音乐一致；见 `template-global-style-prefix.md` § Field specimens。）

> `[HOUSE]` 上面的前缀按这次制作交付的样子引用。写**新**前缀时，优先用 **`NO BGM`** 而不是 `No music`：这个制作术语读作硬性规格，而光秃秃的否定读作模型可以推翻的风格偏好。见 `higgsfield-audio.md` § Suppressing music。

---

## 措辞规则（Wording rules）

- **现在时。短句。**
- **运镜写在动作里**，而不是单独一段美学段落。
- **每个节拍保持轻：每个节拍最多三句。**节拍过载，模型就会把它抹糊。
- **长度不是敌人，过载的节拍才是。**Hell Grind 的提示词有 **3,000–4,000 词**。这位于采集语料语域阶梯的顶端（`higgsfield-seedance.md` § Field calibration）并印证了它：在块骨架模式里，结构取代了字数上限。
- **动作只用正向形式。**模型会忽略“does NOT fall on his back”，或者做反。写“falls on his stomach.”
- **角色从第一帧起就在画面里，并且不看镜头**，除非你要求。
- **任何语言都绝不写年龄。**内容过滤器一读到未成年人就会明显变严。改为给出**职责、衣服、动作**。这是引擎规则 1（`higgsfield-seedance-engine-rules.md`）背后的制作原因：而且它**覆盖** `higgsfield-seedance.md` § Tag naming 里 `@TAG:` 行的 `age + role/build` 形式：写职责和体型，去掉年龄。
- **保留一本禁用词词典**，收录会被模型惩罚的词，发现一个就加一个：

| 不写 | 改写 |
|---|---|
| dark | low key |
| jolting | rapid motion |

  和 `higgsfield-seedance.md` § Ambiguous verbs 里的同形词陷阱是同一个机制：一个被模型读成别的意思的词。发现一个替换就记下来，和记同形词一样。

---

## 对白构建（Dialogue construction）

**提示词里的一句台词永远用同样的方式构建：**

```
The voice and its emotion → the line in quotes → the physical action → the facial reaction
```

- **台词只放在音频部分。**动作块里一个说话的字都没有。（工作室格式：台词只作为计时行写进 `[声音]`。）
- **Seedance 会加它自己的“嗯呃”、轻笑和整句话**，所以提示词要带一条硬性限制：每个人**只**说引号里的那句；没有台词的人保持完全安静；动作里写的“半笑”是一个面部表情，**没有声音**。`[HOUSE — the rest of this bullet is ours, not the brief's]`“保持安静”解决的是*声音*；**画面**需要它自己的事实，所以画面里其他每张可见的脸也要带一个正向的静止嘴部状态（“嘴唇放松”、“下颌闭合，在听”）：画面里没标注的嘴，模型可能会认为它在说话。风险方向是**短**台词：一句远早于镜头结束就说完的台词，会留下模型用编出来的嘀咕填满的音频空白（`higgsfield-seedance-failure-modes.md` § Filler-babble on a short dialogue line：在 4 秒镜头上 ≤6 个词时测到；静止嘴部这条事实本身还没在这里实测过）。
- **把混音也写上**：人声干净、贴近话筒，环境声在下面，有人说话时环境声压低。
- **罕见的名字给一个注音**，否则模型会念错。
- **两个接缝技巧：**在对白的远景上，把上一句台词的尾巴喂进提示词：有助于口型和节奏；以及**每次新的生成都用上一段结尾的那句台词开场**，让情绪和文字一起跨过接缝。

示例：动作在计时块里，说话在音频块里，两者从不混在一起：

```
ACTION TIMING
0.0–3.0s — JAX and REIN walk the corridor toward the lens, in step. JAX talks with his eyes up
on the ceiling lights, one hand patting his stomach; REIN's thumb keeps scrolling the tablet,
her pace unchanged, she never looks up at him.
3.0–4.0s — the distant THUD from the training room lands: REIN's thumb STOPS on the glass, and
only then her head turns to the door — the interrupted work is the accent of the beat. JAX's
grin drops half a second later.

AUDIO
Diegetic only — corridor air, two sets of footsteps on concrete, soft taps on the tablet, the
distant THUD and a hiss of crystal behind the door. JAX voice (verbatim): "A London street
voice, loose and hungry, always half-joking, sentences thrown out mid-stride." His line, and
nothing else: "Man, some cereal and a milkshake would hit the spot right now." REIN voice
(verbatim): "A technical voice — flat, fast, precise, no wasted air." Her line, and nothing
else: "I think I've got the coordinates." Nobody else speaks; JAX's amused breath is a facial
expression, with no sound. No music.
```

---

## 写物理，不写形容词（Physics, not adjectives）

遇到情绪词（“sad”、“angry”、“shocked”），模型会即兴发挥，交回一些浅薄的东西。要更深的情绪，描述**肌肉和身体的工作**：颤抖、因愤怒而咬紧并抽动的下颌、绷紧的颧骨、从鼻子轻轻呼出一口气。

放在计时块里的四项补充：

- **INNER (unspoken)。**每段动作写一句内心独白（角色在想什么、想要什么），标为 `INNER (unspoken)`，让它永远不被说出来。
- **分阶段的眨眼。**“one lazy blink → a quick DOUBLE-BLINK → one HARD reset-blink”：一张活着的脸最便宜的标志。
- **清楚的视线方向，或者游移的眼睛。**不停工作的微表情给脸生命；固定的凝视读起来是死的。
- **微生命规则。**对付静态镜头里冻住的脸：**每一到两秒一个可见的微事件**：呼吸抬起胸口、鼻翼动一下、眉头紧一下再松开。

**把静止写成被压住的张力，绝不写成定格。**“nobody moves”这类让人平静的短语本身就会冻住画面。

示例：“exhausted”和“angry”这两个词一次都没出现；状态在计时块里由肌肉构建，在表演块里由意图构建：

```
ACTION TIMING
0.0–2.0s — ROCO holds the center of the mat, feet planted wide, chest pumping in short shallow
pulls; the crystal arm hangs heavy at his side and drags his right shoulder a finger lower
than the left.
2.0–4.5s — the jaw sets and releases twice; a thread of blood runs from his nose to his upper
lip and he lets it run; one lazy blink, a quick DOUBLE-BLINK, one HARD reset-blink.
4.5–6.0s — the gaze drops to the smashed mannequins at CENTER-RIGHT, holds one beat, then
lifts to the door as it opens — the eyes reach the door before the head turns.
```

另外三条区分活镜头和死镜头：

1. **反应在对方台词结束之前就开始。**听的人在句子中途就明白了，脸已经在回答。重要事件之后，给角色几分之一秒消化，再开口。
2. **情绪不会瞬间关掉。**沉重的时刻之后，呼吸仍然不匀，手仍然不稳：这条尾巴带进下一段片子，把切点缝起来。
3. **让手忙着。**角色不是在“进行一场对话”：他们在修、在数、在倒水，一边做一边说。**一场戏最强的重音，是他们因为刚听到的话而停下手里的活的那一刻。**

更细的肌肉级控制：`higgsfield-facs.md`。表演的手艺层：`higgsfield-acting.md`。

---

## 迭代循环（The iteration loop）

**按场批量**生成。

- **每次迭代都是外科手术式的：改一行，其他一切一字不动。**一条提示词是一个运转的机制：整个重写，你就丢掉了起作用的部分。
- **十到十五规则。**一个镜头在 10–15 次迭代里还没成形，**问题就不在措辞。**简化*镜头*：拆成两个、去掉一个动作、换角度。

> 与 `production-benchmarks.md` 里的迭代经济学一致（整个项目每个留下的镜头 65–100 次生成）：10–15 规则管的是*单条提示词*在必须重构之前的收敛，不是项目的总素材数。

---

## 赶工期时诞生的办法（Solutions born under deadline）

- **复杂动作绝不放在计时的中间。**一扇撞不开的门：角色挪到门边就僵住了。修法：**动作作为提示词的开头**：“他已经在挥臂中途，门已经在裂开”：走向门口改成一个单独的镜头。（“写状态不写过渡”规则的制作形式；见 `higgsfield-acting.md` § States, not transitions。工作室格式下，动作在 `{Hm.}` 定位秒之后的第二段开始。）
- **人群是一个“角色”资产**，有一系列身高和衣服。一两个领头的群演有自己的资产用于近景。中景里**直接写出人数**：“20+”：否则模型这一条给你三个人，下一条给你一百个。（与 `higgsfield-seedance-production-patterns.md` 里的 VARIETY 参考模式，以及“跨切镜追踪 ≤3 个角色”的引擎规则配合。）
- **两个空间之间的转场停在门槛上。**两个场景资产放在一条提示词里，接缝是一个门口，**两边光照对比**：“暖琥珀色的房间，拱门外冷蓝色的走廊。”对比解释了色板的变化，也原谅了小的几何错误。
- **巨物靠尺度锚点活着。**每条提示词都写一个尺寸比较，**再加一个画面里可以用来量的人形**。两者缺一，模型就会悄悄把巨物缩回接近人的高度。也写明失败的条件：

```
POSITIVE CONSTRAINTS
THE SCALE LAW — VISIBLE PROOF IN THE PICTURE: the stone guardian stands THIRTY METRES tall —
his head is lost in the darkness of the dome, his open palm is as wide as a family car, and
ROCO at his foot reaches just above the ankle. In every frame the guardian's silhouette is at
least FIVE TIMES the height of the human figure beside him, and the frame cannot hold both his
feet and his head at once. A guardian that reads as a large man, or fits comfortably in frame
next to a standing human = failed shot.
```

  这是 `higgsfield-seedance.md` § Measurable-language rules 里人身高比较规则的具体形式，另有两点补充：人形锚点必须**在画面里**，并且提示词写明一个**失败**的镜头长什么样。

---

## 五条规则，压缩版（The five rules, compressed）

1. **先筛选共享资产。**工作室按[独立视频提示词门槛](asset-registry.md#资产建立门槛按独立视频提示词计数)决定是否建角色／生物／道具／场景资产；单次对象保留必要文字。先锁共享设计与布局，实图压力测试只在相关风险或用户要求时执行，不升级为所有对象出图的前置门禁。
2. **每次都描述一切。**模型没有记忆。描述词一字不差地进入每条提示词，绝不缩短。
3. **一次只改一样东西。**整个重写提示词，你就丢掉了起作用的部分。每次迭代改一行；比较结果之后再改另一个变量。
4. **给模型更少的自由。**一个角落而不是一个房间，一个锚点而不是开阔空间，一张地图而不是猜测，每个镜头一个动作。
5. **镜头成不了形时，简化镜头，而不是措辞。**拆成两个、去掉一个动作、换角度。

这个流程不需要十五个人才能运转：它需要的是遵守规则。它可以缩到一个人的团队。

---

## 相关（Related）

- `higgsfield-seedance.md`：这个流程填充的提示词语法
- `higgsfield-seedance-engine-rules.md`：硬性渲染约束
- `higgsfield-seedance-production-patterns.md`：来自同一来源系列的教程演示模式
- `higgsfield-acting.md`：CHARACTER ACTING 块编码的表演系统
- `higgsfield-shotlist-director.md`：“整个项目一本名字词典”的相连分镜表形式
- `template-global-style-prefix.md`：粘进每条提示词的风格前缀

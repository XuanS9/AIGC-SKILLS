# Seedance 2.5：AI 视效制作流程（Seedance 2.5 — The AI-VFX Pipeline）

本目录里的 `higgsfield-seedance-2-5.md` 是**写法**：模式、参考职责语法、分阶段、方括号语法。本文件是**流程**：当任务是“用生成代替三维/合成流程”时，一个完整的视效镜头实际上是怎么搭起来的，以及一路上的失败长什么样。

它回答的是一份具体的说明：把一个真人放进真实的底片素材，让他骑上一只不存在的生物，逐帧飞过一道瀑布；然后不用任何底片，把同样的镜头重新搭一遍。下面的方法是那次制作里留下来的东西。

> **这是一层制作流程，不是第二种写法。**这里的一切都用 `higgsfield-seedance-2-5.md` 的语法来写。块骨架（`SCENE CONTEXT → … → POSITIVE LOCKS`）、以度数表示的视场角、分布式风格、CAMERA 放第三位的规则和提示词写作规律，是 `higgsfield-seedance.md` 里的通用方法，原样带到 2.5。这里不重复：去那里读。工作室交付仍用中文块结构（[跨类型导演模板](template-general-director-2-5.md)）；下面的英文块是原版示例。

## 速查（QUICK FACTS）
- 流程永远是**先图像，后视频**：一个镜头的好坏取决于它据以构建的那张静帧 [→](#流程先图像后视频the-pipeline-images-first-then-video)
- 按**资产类型**选模型，而不是整个项目一个模型：脸 + 修正 → Nano Banana 2 · 生物 → Seedream 5.0 · 服装 → GPT Image 2 · 场景 → Soul Cinema [→](#第-1-阶段资产按资产类型选模型stage-1--assets-one-model-per-asset-class)
- 原版做法里角色设定表用**纯灰背景**（工作室角色组板按 [角色资产交付规范](template-character-asset-delivery.md) 选背景）；生物设定表带**两张近景：张嘴和闭嘴** [→](#第-1-阶段资产按资产类型选模型stage-1--assets-one-model-per-asset-class)
- **锁脸裁切**：把全身格里的头裁掉，让模型只有一个地方可以取脸 [→](#锁脸裁切the-face-lock-crop)
- 尺度靠文字保不住：做一张**尺寸参照帧**，存为独立资产，附到每场戏里，并锁定“尺度不确定时，往小了渲染” [→](#第-2-阶段尺度规律尺寸参照帧stage-2--the-scale-law-a-size-ref-frame)
- 场景**便宜地批量生成，按光挑选**：静帧里光不对，就是视频变劣质的原因 [→](#第-3-阶段场景便宜地批量按光挑选stage-3--locations-batch-cheap-select-by-light)
- 实战的视频到视频跑在**带视频参考的 `omni_reference` 里，而不是 `video_edit`**：所以时长可以设置，并且必须等于源素材 [→](#第-4-阶段素材变换omni_reference-视频到视频通道stage-4--footage-transformation-the-omni_reference-v2v-lane)
- 源片段 **≥ 4 秒**（模型自身的时长下限）；更短的用最后一帧定格补齐 [→](#第-4-阶段素材变换omni_reference-视频到视频通道stage-4--footage-transformation-the-omni_reference-v2v-lane)
- **四批规则**：四批里都出现同样的缺陷，就是提示词或源素材的问题：继续批量只会烧额度 [→](#第-5-阶段视频到视频失败时四批规则stage-5--when-v2v-fails-the-four-batch-rule)
- 视频到视频继承不了源素材里没有的动作；用一张场景截图作为**场景参考**，在 `omni_reference` 里描述缺失的运动。刻意的空镜节拍可以作为切点 [→](#第-5-阶段视频到视频失败时四批规则stage-5--when-v2v-fails-the-four-batch-rule)
- “让它更自然一点”没有用：修法是给出运动的**物理画面** [→](#劣质破绽清单the-slop-catalog)
- 暴露镜头的破绽（CG 替身式的坠落、折纸翅膀、变形的标识），以及每一种在要求你写什么 [→](#劣质破绽清单the-slop-catalog)
- 制作中得出的导演写法：从动作中途开场、冲出云层开场、高速套件、没有视频参考的情绪、音色锁定 [→](#制作中得出的导演写法direction-patterns-from-the-build)

---

## 来源（Provenance）

| 标签 | 来源 |
|---|---|
| `[FIELD — AI-vs-VFX, 2026-08-08]` | Higgsfield 的 *AI vs VFX: Can Seedance 2.5 Beat VFX?* 制作：博客文章 + 25 分钟的制作视频，主持 Adil，底片素材由视效艺术家 Erik 提供。里面每个镜头都是在 Seedance 2.5 上生成的。 |
| `[OFFICIAL — prompt-builder 2.5]` | `prompt-builder-2-5.skill`，Higgsfield 随那次制作发布的提示词技能。 |
| `[OFFICIAL — platform]` | Higgsfield 在线的 `models_explore` 目录，快照 **2026-08-07**（`model-specs.json`）。 |

实战制作和平台快照对于什么*可以设置*有分歧时，以快照为准（HARD RULE 3）。实战制作对什么**有效**有权威性，对 API 接受什么没有。

---

## 流程：先图像，后视频（The pipeline: images first, then video）

`[FIELD — AI-vs-VFX, 2026-08-08]` 制作里的每个镜头（基于底片的和完全生成的都一样）都经过同样的两个阶段，顺序相同：

```
1. ASSETS      character sheet · creature sheet · size-ref frame · location stills
2. VIDEO       one Seedance 2.5 generation per shot, every asset attached by role
```

值得在用户花一分额度之前明说的后果：**一张坏的静帧，视频提示词救不回来。**一张光不对的场景底片，不管运动写得多好，都会产出劣质视频，而便宜的修法在上游：重新生成静帧，而不是镜头。

二阶后果是资产阶段值得单独一套纪律的原因：一个资产生成一次，被每个需要它的镜头引用。在设定表阶段接受的一个缺陷（变形的标识、漂移的脸、含糊的尺度），之后要在下游的每一次生成里付钱。

---

## 第 1 阶段：资产，按资产类型选模型（Stage 1 — Assets: one model per asset class）

`[FIELD — AI-vs-VFX, 2026-08-08]` 制作里重复最多的一条纠正是：一个项目没有“最好的图像模型”：最好的模型是**按资产类型**分的，项目中途在它们之间切换是常态，不是退路。

| 资产类型 | 模型 | 为什么选它 |
|---|---|---|
| 人类角色设定表、人脸匹配 | **Nano Banana 2** | 平台上人脸匹配最强 |
| 对已有设定表做小的修正编辑 | **Nano Banana 2** | 最能保住输入图：需要修而不是重做时*切到*它 |
| 奇幻生物 / 非人角色设定表 | **Seedream 5.0** | 最擅长奇幻生物 |
| 服装、换装、带品牌的衣物 | **GPT Image 2** | 处理服装最好 |
| 场景和环境静帧 | **Soul Cinema** | 画面最有电影感；GPT 偏黄，Nano Banana 做出的场景太干净、太对称 |

每个模型的完整规格、价格和界面控制在 `image-models.md`；这张表是*选型*，不是参考。

这张表附带三条构建规律：

**角色设定表用纯灰背景。**不是布景，不是环境，不是渐变：纯灰。在杂乱背景上做的设定表会在下游的重抽里花掉额度，因为视频模型得判断设定表的哪些部分是角色、哪些是世界。`[FIELD — AI-vs-VFX, 2026-08-08]`（工作室项目的角色组板背景以 [角色资产交付规范](template-character-asset-delivery.md) 为准：同样是干净的中性背景，按服装明度选浅暖白灰或中灰。）

**生物设定表带两张近景：张嘴和闭嘴。**细节多到有意思的生物，也细节多到会在表情之间出故障：张嘴时下颌把整个头骨形状都改了。同一角度的两张头部近景，一张闭嘴、一张全力咆哮，钉住两个极端，阻止脸在镜头中途自己重组。标准设定表是三格：飞行中的全身、闭嘴的头、张嘴的头。`[FIELD — AI-vs-VFX, 2026-08-08]`

**小修正是换一个模型加一句话，而不是更长的提示词。**设定表出来带着变形的标识或偏色时，不要重写生成提示词：把有缺陷的设定表加上正确的资产附给 Nano Banana 2，写一句：`change the logo to the one in image two`。重新提示整张设定表，会把已经对的东西全部重抽。`[FIELD — AI-vs-VFX, 2026-08-08]`

### 锁脸裁切（The face-lock crop）

`[FIELD — AI-vs-VFX, 2026-08-08]` 三格设定表给模型三张脸去平均：正面全身、背面全身和一张近景。在全身尺度上，脸只有几十个像素，把它平均进去会把身份拖向泛泛的长相。

**把全身格里的头裁掉。**设定表保留全身格用于体型、轮廓和服装；近景成为唯一能读取脸的地方。身份只有一个真相来源，而且在唯一真正能分辨身份的分辨率上。这和工作室角色组板“唯一清晰面部特写 + 三个无头全身格”的做法一致。

它和 `higgsfield-seedance-2-5.md` 里的参考职责纪律配合使用，而不是替代它：裁切减少了模型*能*误读的东西；职责句告诉它该读什么。

---

## 第 2 阶段：尺度规律，尺寸参照帧（Stage 2 — The scale law: a size-ref frame）

`[FIELD — AI-vs-VFX, 2026-08-08]` 两个主体之间的相对尺度是最先漂移、文字最难修好的东西。写成“和巨龙相比非常小”的骑手，每次生成出来大小都不同，而且远景里漂得最厉害：而远景里尺度恰恰是整个镜头的重点。

修法是一张图，而不是一句话。**做一张尺寸参照帧：**

1. 拿生物设定表、角色设定表，以及一次尺度正确的生成的截图。
2. 把它们合成**一张**参考图，显示这一对骑乘/摆放在一起的样子：实战制作用的是三格版本（远景侧面、四分之三正面、骑乘接触点的近景）。
3. 在这张图自己的提示词里用**人身高的比较**写比例，而不是米：*“wingspan as wide as twenty humans lying head to toe; the dragon's head alone is longer than the rider's entire body.”*
4. 把它存为**独立的具名资产**，附到每个同时包含这两个主体的镜头里，配一句让它只管比例的职责句：

```
@size-ref: single image of the same rider mounted on the same dragon in flight — this is
the exact rider-to-dragon proportion to reproduce: body length about 12x and wingspan
about 14x the rider's height, the rider a tiny figure mounted low on the shoulders at the
base of the neck. Match this proportion in every frame. Ignore this image's background,
lighting and grade.
```

> ### 一句话**确实**能管用的地方：尺寸差决定用什么工具（Where a sentence DOES hold — the size gap decides the instrument）
>
> `[FIELD — Higgsfield Studio, RED FLAG breakdown, 2026-08-19]`“文字最难修好”对上面的情况成立：极端的比例，骑手对 12 倍大的龙。它对普通的布景几何**不**成立，照那样理解会让人为一段扶手去做尺寸参照帧。在接近人体尺寸的道具上，写出来的尺子管用，而它管用是因为它被**换算成了一个身体地标**，而不是停留在一个数字上：
>
> ```
> the railing is 110 cm; on a 185 cm man the top rail lands just above his belt
> ```
>
> 没有后半句时，栏杆飘到了胸口高度：光有尺寸本身没起任何作用，因为模型没办法把厘米兑换成画面。
>
> **让这件事危险的陷阱：**地标对点名的两个形体必须*算术上为真*。错误的锚点不会被忽略：它会被服从，模型会调整**物体**的大小来满足你的错误说法，所以编出来的身体部位比较会主动破坏它本来要保护的尺度。从真实尺寸算出来，否则就不写。
>
> 所以：**接近人体的道具 → 一句算出来的锚点句。极端比例 → 尺寸参照图。**差距大到没有任何单个身体地标能表达时，才用图。

旁边有两条锁定值得加上：

- **不对称锁定。**`If scale is uncertain, render the rider SMALLER, never larger.` 尺度错误读起来不对称：偏小的骑手读作距离，偏大的读作假。
- **不缩放锁定。**通过*编辑*生物画面来做尺寸参照时，写 `do not shrink, resize or move the dragon`：否则模型会通过缩小错误的主体来解决比例。

> 这是 `higgsfield-seedance.md` § Positive Locks 里尺度漂移锁定在 2.5 的形式。在那里对策是一句常设的句子；在这里，有 30 张图像参考可用，它是一个专门的资产：更强，因为展示出来的比例没法被改写。

---

## 第 3 阶段：场景，便宜地批量，按光挑选（Stage 3 — Locations: batch cheap, select by light）

`[FIELD — AI-vs-VFX, 2026-08-08]` 场景静帧是整个流程里迭代最便宜、出错最贵的地方。

**经济性决定方法。**7 积分能买一次 GPT Image 2 生成，或者 **56 次 Soul Cinema 变体**。在这个比例下，正确的做法不是写更好的提示词：而是宽批量生成，然后评判。

**先按光评判，再看别的。**制作里淘汰的原因，按出现的顺序：

| 淘汰原因 | 看起来是什么样 |
|---|---|
| 塑料感，阳光不自然地穿透 | 场景是阴天：光应该是柔的，硬阳光和底片矛盾 |
| 云的位置不好，图太暗 | 构图没问题，曝光毁了它 |
| 光漂亮地落在平原上，但没落在瀑布上 | 镜头的主体读起来像一个洞 |
| **采用** | 焦点在瀑布上，水读作蓝色，阴天但不暗 |

**静帧里光不对，就是视频生成变劣质的原因。**这就是整条规则。主光不对的场景会和视频提示词里的每一句光照描述打架，因为视频模型匹配的是参考，不是那段文字。

**锁定之前，把入围的几张放到视频里测。**一张读起来很好的静帧，动起来也可能很差。给每张入围的花一次短生成，比在主镜头里才发现便宜。

### 反打角度的场景（Reverse-angle locations）

一场戏几乎总是需要从另一个方向看同一个地方：你刚才往里看的那个洞穴的里面、房间的另一头、从对面马路牙子看的街道。把它作为*匹配的*场景来生成，而不是新的场景：附上已锁定的场景资产，写一份明确的延续清单。

```
Reverse angle of the exact same basalt cave as in the reference image — same location,
same materials, same color grade, now facing the opposite direction: the dead-end back of
the cave.
MATCH TO REFERENCE — carry over exactly:
— the same rough black basalt of the ceiling and walls: layered, horizontally streaked,
  wet sheen, identical texture scale;
— the same floor: dark grey-brown fine volcanic gravel, matte and slightly damp,
  identical grain size and tone;
— the same cold overcast palette: graphite black, wet slate grey, muted earth-brown;
  fine film grain and soft naturalistic contrast identical to the reference frame.
```

写明**材质、颗粒大小、色板和调色**：这四样会让两个镜头暴露为不同的地方。写明新角度里*没有*什么（“this side is completely sealed solid rock: no second opening, no daylight gap, no waterfall anywhere in frame”），因为模型很乐意编出第二个出口，而不愿意落到一个死胡同里。这种本能就是环境编造，`higgsfield-seedance.md` § Positive Locks 里的第 1 号漂移来源。工作室中文稿把这些排除转成正向描述：“这一侧是完整封闭的实心岩壁”。

---

## 第 4 阶段：素材变换，`omni_reference` 视频到视频通道（Stage 4 — Footage transformation: the `omni_reference` v2v lane）

这一节改变了底片任务的路由方式。

`[FIELD — AI-vs-VFX, 2026-08-08]` 制作里的视频到视频镜头（把这段片子里的人换成我的角色，保留其他每个像素）**不是**用 `video_edit` 跑的。它们用的是**把源片段作为视频参考附上的 `omni_reference`**，用普通的块骨架，并在文字里声明 `@video1` 是母片：

```
@video1 — source footage: master for camera, framing, focus, motion, expression timing,
background, lighting, grain and duration.
@adil-hiking — replacement character: <minimal identity anchor>. 100% matches the reference.
```

这种路由带出三个操作事实，而它们对 `video_edit` 都不成立：

**1. 时长可以设置，而且必须等于源素材。**`[FIELD]` *“Set the duration to four seconds to match the reference. Anything longer and the AI starts guessing.”* 在 `omni_reference` 里时长是真正的参数，所以设得过长就等于指示模型在底片结束之后编造素材。相比之下，`video_edit` 完全忽略 `duration`，并按母片长度计费（`higgsfield-seedance-2-5.md` § The Higgsfield Parameter Surface）。

**2. 源片段必须至少 4 秒。**`[FIELD]` 这不是随意的门槛：`duration` 有一个 **4 秒的硬性下限** `[OFFICIAL — platform]`，所以一段 2 秒的底片根本没法做时长匹配。**用最后一帧定格把短片段补到 4 秒**，再匹配。把长底片切成段、给短段补帧，是正常的准备步骤，不是取巧。

**3. 保留的那一半写成文字锁定，而不是 `[Edit Scope]` 块。**骨架的 `POSITIVE LOCKS` 承载它：*“every pixel outside the replaced man remains exactly as in @video1, including the empty-wall ending. Duration and all action timing unchanged.”*

### 什么任务走哪条通道（Which lane for which job）

| 任务 | 通道 |
|---|---|
| 换一个主体 / 加一个元素，同时逐帧继承底片的表演，底片 ≥ 4 秒 | `omni_reference` + 视频参考，时长 = 源素材 |
| 在时间线必须原封不动的母片里改一样限定范围的东西（4–7 秒墙上的光色、去掉音乐） | `video_edit`：`higgsfield-seedance-2-5-mode-playbooks.md` § Video editing |
| 从头重建镜头，旧片段只作为运动指导 | `omni_reference`：`higgsfield-seedance-2-5.md` § The Mode Router，规则 2 |
| 底片是 Seedance **2.0** 的工作（需要 4K、平台首尾帧、题材提示） | `higgsfield-seedance-vfx.md` |

### 表演继承条款（The performance-inheritance clause）

让一次替换读作替换而不是重拍的，是一句明确的逐帧继承句：`higgsfield-seedance-2-5-mode-playbooks.md` 里时间线继承条款在 `omni_reference` 里的孪生版本：

```
The man from @adil-hiking takes the original man's place and inherits his exact performance
frame by frame: same body position and posture, same head angle, same wide-eyed stare and
open-mouth shock expression with identical mouth aperture and blink timing, same stillness
during the hold, and the same fast straight-down drop out of frame at the exact same frames
with matching motion blur. Silhouette scale and screen position match the original at every
frame.
```

然后是一个 `STYLE` 句，它的任务是融合，而不是画面风格：*“grain, motion blur, focus falloff, compression character and color match @video1 so the replaced man is indistinguishable from originally shot footage.”* 这句话代替了抠像、去溢色和颗粒匹配：写上它，否则模型会干净地合成，镜头读起来像贴上去的。

---

## 第 5 阶段：视频到视频失败时，四批规则（Stage 5 — When v2v fails: the four-batch rule）

`[FIELD — AI-vs-VFX, 2026-08-08]` 抓龙那个镜头在**全部四批**里都失败了。这个教训推广成了制作里最省额度的一条规则：

> **如果同样的缺陷在全部四批里都出现，问题出在提示词或源素材。继续批量就是白烧额度。**

接下来的诊断关于**锚点**：视频到视频从底片继承运动，所以它只能渲染底片里有锚点的动作。源素材里没有跳跃的瞬间：所以要求跳跃的提示词没有东西可继承，每次都变成劣质结果。重抽多少次都造不出一个从没拍过的锚点。

**当前的退路仍然是 `omni_reference`，并且需要重新做连续性检查：**

1. 从源素材截一张场景视图，只把它作为**场景参考**；写明要保留哪些布局和光照，排除无关的人物或运动。
2. 分别映射角色和道具图，然后从头描述缺失的动作，因为源素材里没有这段运动。
3. 写明想要的切点和最终的运动/音频状态；在剪辑里把新镜头和源素材接起来，并目视检查接点。不要承诺像素级一致的连续性。

### 空镜停顿（The empty-frame pause）

这个模式真正派上用场的地方：**在你打算切的位置，往提示词里写一个刻意的空镜节拍**：1 到 1.5 秒只有场景、别的什么都没有：

```
… falling fast with real gravity, disappearing below the ledge. Then a pause: for about
1.5 seconds the frame stays completely empty, only the waterfall and drifting mist.
Suddenly @dragon-v3 bursts up from the abyss …
```

空画面是干净的切点：接点两边没有要匹配的主体，没有要保持的连续性。把它规划进生成里，比事后在时间线里找一个便宜：而且它兼作一个紧张节拍，这就是为什么同样的手法在制作的完全生成那一半里被刻意使用（生物冲进画面之前，在空的悬崖边缘停一秒）。

---

## 劣质破绽清单（The slop catalog）

`[FIELD — AI-vs-VFX, 2026-08-08]` 下面每个破绽既是淘汰标准，*也*是提示词侧的指令。学会给它们命名，才能把“这看起来很假”变成一句你能写的话。

**“让它更自然一点”没有用。**它是典型的非指令：没有可观察的目标，没有可渲染的东西。换成运动的**物理画面**：什么在身体里传递，朝什么方向，以什么速度：

> *“the body undulates like a worm swimming through the air: with every wingbeat a wave of motion travels along its spine — the chest lifts, then the wave rolls through the belly, hips and down the tail”*
>
> *“its head rapidly rotates back and forth around its own axis — a twisting rotational shake, like a dog shaking water off — and the twist travels down the neck as a spiral wave, the loose skin and neck spikes wobbling with the rotation, flinging spray outward in a spinning radial cloud”*

这和 `higgsfield-seedance.md` § Prompt-Craft Laws 里的规律相同（写可见的东西），只是专门用在运动上。**运动物理是视效镜头里承重的那一句**：永远写出物理运动，而不是形容它的形容词。

**折纸翅膀。**生成的生物肢体读起来像低模：平的切面、尖角、本该是曲线的地方是直的折痕。对策写成表面行为：*high-poly, smooth organic muscle curves, no sharp corners, no flat planes*（工作室中文稿写成正向：“高精度、平滑的有机肌肉曲线、圆润过渡”），再加上材质受力时的表现（翼骨在每次下扑时弯曲，翼膜鼓起，然后带着张力褶皱绷平）。

**CG 替身式的坠落。**传统视效里最可靠的破绽，直接转移到生成里。一个人从悬崖上下去**只有两种方式**：垂直踏出去，脚先下；或者蹬出去俯冲。其他任何方式（倒成僵硬的士兵姿势、以恒定速度下落、衣服一点不动）都读作一个从 A 拖到 B 的资产，观众说不出为什么，但能看出来。把坠落写成两种真实方式之一，带上**加速**，并让衣服有动作。

**静帧里的光不对。**第 3 阶段讲过，列在这里是因为它属于同一份心里的检查清单：劣质视频最常见的原因，是一张本来就错的场景底片。

**图像阶段的破绽。**反复出现的两个是变形的标识和偏蓝的色偏。两者都是 Nano Banana 2 一句话的修正（第 1 阶段）：但前提是你在设定表被锁定、被下游四十个镜头引用之前*去找*它们。

**选素材时的破绽。**一段表演有几条素材都可用时，实战的淘汰理由是：收尾节拍上表演过火、一段跑动对这个情绪来说太激烈、一个多余的转头、一个和场景情绪矛盾的笑。四条都是表演意见，不是技术故障：这正是重点。像评判演员一样评判一条素材。

---

## 制作中得出的导演写法（Direction patterns from the build）

`[FIELD — AI-vs-VFX, 2026-08-08]`

**从动作中途开场。**生成的开场画面总想成为一个建立节拍，而建立节拍就是空白时间。对于以一个事件开始的镜头，把事件放进第一秒并写明：*“the veil is already bulging in frame one and the dragon breaks through within the first second — no long empty establishing beat, no cave interior, no approach shot.”* 第一帧承载的是状态，不是铺垫。（工作室格式下，第一段 0–1 秒仍是 `{Hm.}` 定位秒，事件从定位秒结束时开始。）

**冲出云层开场。**对应真正是建立镜头的情况：一张漂亮的静止画面不是一场戏。给镜头一个可以*冲破*的东西：在一片完全白茫茫的云层里开场，向前向下推，从云底冲出来，让远景在一次连续的揭示里展开。揭示就是镜头；场景是它揭示的东西。

**没有视频参考的情绪。**没有底片可以继承表演时，按身体实际在做的事来描述脸：角色正在经历什么、**他说什么**、**声音听起来怎么样**、**他的手在做什么**。制作里洞穴独白之所以成立，是因为它写明了吞咽、抽动的手指、开口又停住、甩开的手、颤抖的呼气，然后才是冲刺。节拍级的表演指导在 `higgsfield-acting.md`；这里是 2.5 的说明：它必须被*写出来*，因为没有参考替你做。

**音色锁定。**`[FIELD]` 2.5 把**音色**和外观一起锁定在角色设定表里。在多次生成里复用同一张设定表参考，音色就保持一致：所以在角色的职责句里描述一次音色，而不是每条提示词里都重新指定。`[OFFICIAL — prompt-builder 2.5]` 也是同样的规则。**范围：**这是 2.5 的规则。在 2.0 上，或者任何没有复用设定表参考承载音色的镜头里，在每个说话的节拍上粘贴同样的音色句（`higgsfield-acting.md` § Voice）。不管哪种情况，措辞都从项目登记表复制，绝不重新打字。

**高速套件。**追逐和掠过镜头，三句话承担大部分工作：绕主体的 **180° 环绕运镜**、**速度抖动**（持续的细微振动上叠加离散的颠簸），以及像硬装运动相机那样落下、停留、颤动、拉出水痕的**镜头水滴**。两条锁定防止套件吃掉镜头：环绕路径本身保持平滑、像机械驱动，抖动叠在上面；水滴必须折射但不遮住动作。

**刻意让模型即兴发挥背景。**在高速镜头里，只要即兴发挥不会破坏故事，背景细节可以不写。这是预算决定，不是偷懒：省下的字花在主体、物理和表演上，这些才是观众真正在看的部分。

---

## 成本与工作量锚点（Cost and effort anchors）

`[FIELD — AI-vs-VFX, 2026-08-08]` 用户问这能替代什么时有用。作为来自这次制作的比较来引用，而不是对他们任务的报价。

| 步骤 | 传统流程 | 这个流程 |
|---|---|---|
| 生物资产 | 雕刻 → 重拓扑 → 展 UV → 绑定，然后才能做动画；买一个模型也还得自己做动画 | 大约一分钟、约 40 美分生成一张设定表 |
| 把角色放进底片 | 抠像（卷发要手工）→ 去溢色 → 合成 → 匹配光、阴影、颗粒 | 一张参考设定表 + 一条提示词；模型把光和对比度匹配到底片 |
| 一个人从悬崖上下去 | CG 替身：布料模拟、物理、体重和轨迹，加上中景的逐帧遮罩：为了一个两秒的镜头 | 一条提示词，写一次真实的坠落 |
| 生物动画 | 搭三维场景、匹配光照、给绑定的每个部分做动画；光标准软件一年就要约 3,000 美元 | 改写一次再生成一次 |
| 对生物有反应的体积云 | 数百万粒子、几百 GB 数据、每秒素材都要渲染农场 | 写在提示词里 |

制作对后半部分（完全没有底片的全生成电影镜头）自己的说法是：一家工作室会对它报价**至少 50,000 美元**。

---

## 相关（Related）

- `higgsfield-seedance-2-5.md`：2.5 写法：模式、参考职责、分阶段、方括号语法、限制
- `higgsfield-seedance-2-5-mode-playbooks.md`：`video_edit` 和 `video_extension` 的指令写法、分镜、白模、转场
- `higgsfield-seedance.md`：通用提示词方法：块骨架、视场角锚点、分布式风格、提示词写作规律、正向锁定
- `higgsfield-seedance-hell-grind.md`：长片制作流程（长片规模的资产构建、迭代纪律）
- `higgsfield-seedance-vfx.md`：**2.0** 的视频到视频通道（4K、`mode=std`）
- `higgsfield-character-design.md`：任何模型运行之前设定表上该放什么
- `higgsfield-acting.md`：情绪节拍的表演构建
- `image-models.md`：Nano Banana 2、Seedream 5.0、GPT Image 2、Soul Cinema 的完整规格

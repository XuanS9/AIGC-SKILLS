# 制作模式：教程演示（Production Patterns — Tutorial-Demonstrated）

`[DEMO — Seedance-4K film tutorial, 2026-07]`（另有收尾的 `[FIELD]` 一节，来自采集的模式：见 § Field-Harvested Patterns）

这些模式在 Higgsfield 自己的 Seedance-4K 影片教程及其博客拆解里**在屏幕上演示有效**。是演示过的，不是规格保证的：每一条在教程的素材里都产生了所说的结果，但没有一条是模型参数。与 `higgsfield-seedance.md` § Official Prompt Architecture（块骨架，这些模式在其中应用的 `[OFFICIAL]` 方法）和 § Reference Roles（下面词汇接入的语义职责分类）一起读。本文件属于 Seedance 2.0 历史资料；当前项目的职责映射写法以 [Seedance 2.5 多参考说明](template-omni-reference-2-5.md) 为准。

这里引用的模型参数事实来自 `model-specs.json`（seedance_2_0：时长 4–15 秒；480p/720p/1080p/4k，其中 4k/1080p 需要 `mode=std`；媒体职责 `start_image` / `end_image` / `image_references` / `video_references` / `audio_references`）。

---

## 参考职责词汇（Reference-Role Vocabulary）

三个提示词内的职责短语，每一个都改变模型读参考的方式：

| 短语 | 职责 | 效果 |
|---|---|---|
| `"100% matches the reference"` | 身份锁定 | 主体必须按参考显示的样子渲染：官方 `@TAG:` 行结尾用的就是这个短语。用于角色和主打道具。 |
| `"STYLE REFERENCE ONLY, not a fixed keyframe; the model extends the world"` | 场景风格 | 参考决定画面和建筑，但模型可以扩展到可见画面之外。用于场景，让镜头不被参考的精确裁切拴住。 |
| `"VARIETY reference"` | 人群多样性 | 一张多角色阵容表被读作取样池，而不是一个身份。 |

**克隆军团失败及其修法：**用单个角色参考做人群，会产出一群都是那个角色的人。教程的修法：做一张有几个不同角色的阵容表（演示里是 4 个精灵的阵容），附上一次，在提示词里把它重新标为 `VARIETY reference`：模型就会从表里取样出多样的人群，而不是克隆一张脸。

这些短语对应 `higgsfield-seedance.md` § Reference Roles：`100% matches` 是用模型自己的工作词汇说出的角色/道具职责；`STYLE REFERENCE ONLY` 是环境职责；`VARIETY reference` 是四职责分类里没有另外命名的人群专用扩展。工作室中文稿的对应写法：在开头 `[参考资产]` 写 `@名字 对应 名字。`（身份）、“只用于画面风格和建筑，不作起始画面”（场景）、“只用于人群的多样外貌，不作为任何一个人的身份”（人群）。

---

## 坐标站位（Coordinate Blocking）

用两种演示过的记法扩展 `higgsfield-seedance.md` § Frame Coordinate System：

- **用画面宽度的百分比表示大小**（与画面面积占比并用）：`"@TRUCK a tiny speck under 4% of frame width at x38% y44%"`：位置和大小在一个分句里钉住。
- **锁定画面方向：**`"travel screen-left to screen-right, locked"`：起作用的是 `locked` 这个词；没有它，长距离运动会漂移或反向。多人站位时配合每个角色的身体朝向（每个主体面朝哪边）。

---

## 开场画面不空（Non-Empty Opening Frame）

描述第一帧时，让主体**已经在运动中**，构图不对称。描述成空的或静止的开场画面，会诱使模型花前几秒“到场”：一段 4–15 秒片段开头的空白时间很贵。和官方的 FIRST FRAME / BLOCKING 块同样的纪律：从第一帧起所有人都在动。（工作室格式下，第一段 0–1 秒的 `{Hm.}` 定位秒用于锁定站位，角色可以有呼吸、视线等微动；正式动作从定位秒结束时开始。）

---

## 逐段镜头锁定 + 计时切镜控制（Per-Segment LENS LOCK + Timed Cut Control）

演示过的多镜头控制组合：

- 精确数量的计时切镜：`"Exactly one HARD CUT, at 0:07; otherwise the camera holds still."`：数量 + 时间码 + 保持句写在一行里。
- 多段的 FORMAT MODE，**每段一个 LENS LOCK**（每段开头写明确的视场角短语），用 `SMASH CUT` 切进一个慢动作段，在图形上押韵的画面之间用 `MATCH CUT`。

这是切镜格式阶梯和四机制极端视场角组合（`higgsfield-seedance.md` § Official Prompt Architecture — the Block Scaffold）一起使用；逐段时长加起来仍必须等于声明的时长（`higgsfield-seedance.md` § Output Format → Runtime arithmetic）。

---

## 红箭头道具标注（Red-Arrow Prop Annotation）

角色总是和道具的错误部位互动（按错按钮、握错把手）时：**在道具参考表上画一个红箭头**指向正确的位置，然后让写提示词的模型准确描述箭头指向哪里，让提示词用文字把它编码进去：例如 `"The reference's red arrow points precisely to the CH-UP chevron (^)."` 标注在参考表上；指令在文字里。和官方规则同一个原理：关键细节（小字、标识、颜色）即使在参考里看得见，也要用文字写出来。

---

## 视频参考 1:1 锁定 + 屏幕真实感（Video-Reference 1:1 Lock + SCREEN REALISM）

把一段完成的片段合成到画面里的屏幕上（电视、手机、显示器）时：通过 `video_references` 职责附上完成的片段，并严格锁定：

```
@video1 matches the source 1:1 — never reinterpreted, re-edited, cropped,
looped early, or replaced.

SCREEN REALISM
Glass sheen and room reflections on the screen surface, faint sub-pixel
grid, slight moiré, highlight bloom, screen seen at a slightly off-axis
angle.
```

1:1 那句阻止模型“改进”素材；SCREEN REALISM 块让合成读作一块实体屏幕，而不是贴上去的矩形。

**时长匹配规则：**新生成的时长必须**完全等于参考片段的时长**：否则 Seedance 会在参考结束之后开始编造。教程把一场戏剪到前 6 秒，用来喂一个 6 秒的合成。（两个时长都必须在模型的 4–15 秒范围内。）

---

## 提示出来的瑕疵即真实感（Prompted Imperfection as Realism）

完美的渲染读起来是合成的。教程把光学瑕疵作为内容提示进去：热浪扭动、长焦的微颤、数码变焦的“糊”涂抹、锁焦之前短暂的找焦。按官方的百分比规则量化氛围：演示里的雾气在整个镜头里从 20% 爬升到 70%。

**内容**这个词是承重的：上面每一个瑕疵都附着在某样东西上：在一个具名时刻的一个具名元素，或者对氛围类的来说，一个写明范围的量化爬升。同样的词汇如果写成挂在提示词末尾的一句空泛质量请求，就是降质的情况，而不是这种：见 `negative-constraints.md` § Whole-Frame Degradation，那里也覆盖了下面 § Field-Harvested Patterns 里动态模糊那一条。

---

## 60:30:10 调色（60:30:10 Color Grade）

用比例写调色：**60% 主色 / 30% 辅色 / 10% 点缀色**：每种颜色绑定到一个光源和一个表面，绝不是平铺的颜色清单。这是官方“颜色通过材质加光来写”规则加上比例；它放在块骨架提示词的 COLOR GRADE 块里（工作室格式放进 `[视觉风格]`）。

---

## 只出声的画外角色（Offscreen Voice-Only Characters）

声明一个说话但绝不能出现的角色：

```
(Mother is an offscreen English voice only — no in-frame reference, never
enters the shot.)
```

这和“画外 = 不存在”的引擎规则（`higgsfield-seedance-engine-rules.md`）是一致的：括号告诉模型这个声音没有需要入画的身体，所以它既不编出一个，也不把说话的人拉进镜头。工作室格式在 `[声音]` 的计时行里写 `画外＋说话人＋状态＋说：{台词}`，并在 `[角色]` 里注明此人不入画。

---

## 写明屏幕上播放什么（Specify What Plays on Screens）

绝不把画面里屏幕的内容交给模型：没写明的屏幕会被乱码文字填满。按顺序点名每一项：`"the TV plays a news broadcast, then a perfume ad, then a car ad, then @Image4."` 一个参考标签是有效的屏幕内容（完整片段合成见上面的 § Video-Reference 1:1 Lock）。

---

## 提示词内的场景转场（In-Prompt Scene Transitions）

两种演示过的方法，不用剪辑切镜就能在场景之间移动：

- **电视交接：**提前搭好*下一场*的场景，把它放到场景里一台电视的最后一个频道上：片段的最后一帧（屏幕被新场景填满）成为下一场的开场画面。
- **提示词内的尺度转场：**从军队远景到手掌大小的对决的一次连续运动，写成一段运镜旅程而不是一次切镜。

---

## 实战采集的模式（Field-Harvested Patterns）

`[FIELD — 13-project community harvest, 2026-07-18]`：从采集的制作提示词里提取的模式，而不是教程。和 [DEMO] 同样的地位：在制作中有效，不是规格保证。

- **选择性动态模糊用于遮掩瑕疵。**大多数项目禁止动态模糊；一个 4K 技术演示*故意反过来*：“water-covered faces, hands, and foreground figures crossing the lens get motion blur to hide artifacts.” 在模型最弱的地方（穿过镜头的肢体、被水遮住的脸），正好在那些元素上提示模糊来遮掩。
- **HEX 数组锁色（图像提示词）。**除了 60:30:10 的文字调色，一条静帧提示词可以用机器可读的色板结尾：`HEX VALUES: ["#9d6e5f","#a87e72","#3f4591","#30317f", …]`：用列表而不是描述锁定颜色世界。
- **正向生成，剪辑里倒放。**倒带/时间倒流效果从不生成：正向的底片在后期手工倒放。模型只渲染正向时间的物理。
- **复用有人的底片。**对反复出现的拥挤布景（一家餐厅），把演员 + 背景食客一次性合成到场景底片上，然后在每场坐着的戏里复用这张有人的底片作为参考：座位、视线和人群都从一个来源继承，而不是每个镜头重抽。模型应该另外调度人群时用空底片；人群必须重复时就填一次。
- **变身放在画外。**角色变生物（或生物变角色）的变身“除非以影子剪影的方式呈现，否则绝不展示变形中途：否则它发生在画外，只展示之前/之后。”从设计上避开模型的变形失败模式。

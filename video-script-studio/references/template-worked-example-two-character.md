# 模板：完整示例：双人锚定（新黑色电影小巷）

把 `template-multi-character-anchor.md` 用在一个真实场景上的完整演示，展示场景有了名字之后，模板字段实际会填成什么。

## 场景

夜里，一条被雨浇透的小巷，两个角色。警探（Roco）逼近一名嫌疑人（Lulu），她正向一道铁丝网栅栏后退。紧张，还没有接触。电影感的新黑色风格。

## 规划这个示例

应用 [共享叙事规划](narrative-planning.md)：资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束是语义层，锚点格式里已经表达了它们。这里的对峙和后退最终以碰到栅栏收束，这个状态变化决定了结尾。先规划逼近、反应和接触，再分配时间，不预设阶段，不平均分时。下面的双人数量、2 秒处的脚步声、位置和移动距离只是本例的示意，不是其他场景的必填值。镜头内选定的数值要彼此一致；脚步声跟随画面里真实的那一步。

## 填好的提示词

```text
At 0 seconds, two characters in frame.

Character A — Roco (registered asset @Image1).
  Screen position: left third, x-position 30%, y-position 55%,
    frame occupancy 28%.
  Depth layer: midground.
  Body orientation: three-quarter toward Lulu, screen-right.
  Pose: standing, weight on back foot, right hand resting on coat
    pocket.
  Gaze: locked on Lulu's eyes.
  Contact points: boots planted on wet asphalt, shoulders square.
  State lock: composed, alert, controlled aggression.

Character B — Lulu (registered asset @Image2).
  Screen position: right third, x-position 70%, y-position 60%,
    frame occupancy 24%.
  Depth layer: midground (1 meter behind Roco's depth plane).
  Body orientation: three-quarter toward Roco, screen-left.
  Pose: backing one step at a time, hands raised at chest height,
    palms out.
  Gaze: darting between Roco's eyes and the alley behind her.
  Contact points: back nearly touching chain-link fence, boots
    sliding on wet asphalt.
  State lock: cornered, calculating, afraid but controlled.

Cross-character relationships:
  Distance between Roco and Lulu: ~3 meters, closing.
  Eyeline: Roco → Lulu sustained; Lulu → Roco intermittent.
  Crossing rule: neither crosses the central vertical axis of the
    frame in this shot.
  Negative space: centered between them, narrowing as Roco advances.

Camera: medium-two-shot, low angle (camera at chest height), FOV 63
  degrees, anamorphic optical character, slow dolly-in 0.5m over the
  shot duration.
Setting: rain-soaked alleyway, 2am, light rain, sodium-vapor street
  lamp from screen-right above, steam from a manhole behind Lulu,
  garbage bags + chain-link fence + brick walls.
Aesthetic: neo-noir, high-contrast key-and-fill with deep shadows,
  desaturated palette with sodium-orange highlights, film grain
  visible, no VFX.
Audio: light rain continuous, distant traffic, Roco's footstep on
  wet asphalt at 2s, Lulu's breath audible, no music.
Continuity locks: Lulu's hands stay raised throughout; Roco's right
  hand stays on coat pocket; neither character changes position by
  more than ~1m.
Final frame: Roco one step closer, Lulu's back touching the fence,
  eyeline locked, negative space narrowed to half the original.
```

编译成工作室块结构时：`[角色]` 首行写 `恰好 2 人`，两人各写身高；第一段是约 1 秒的定位全景，`[声音]` 写 `0s-1s｜Roco 轻声：{Hm.}`；`no music` 改为末尾 `NO BGM。`。

## 这个示例展示了什么

- `template-multi-character-anchor.md` 的每个字段都填了，包括跨角色关系（距离、视线、越轴规则、负空间），见 `higgsfield-seedance.md` § Spatial Layout Block 与 [vocab.md](vocab.md) § Composition Vocabulary → Crossing rule、§ Negative space。
- 只有一个主导运镜（缓慢推近），没有复合运动，见 `higgsfield-seedance-failure-modes.md` § Multi-motion camera overload。
- 连续性锁定写明，参考记号（`@Image1`、`@Image2`）与上传顺序一致。

## 另见

- `template-multi-character-anchor.md`：本示例填写的模板
- `template-top-down-map.md`：填写模板前预先可视化
- `higgsfield-seedance.md` § Spatial Layout Block：本示例拼出的正文块
- `production-benchmarks.md` § Per-character iteration anchor：为 Roco 和 Lulu 制作角色参考图的迭代预算锚点

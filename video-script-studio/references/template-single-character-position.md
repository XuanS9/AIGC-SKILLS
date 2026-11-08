# 模板：单人站位提示词

可直接粘贴的 Seedance 2.0 提示词模板，用于画面里只有一个角色的镜头。是 `template-multi-character-anchor.md` 的简化版，适用于没有跨角色几何关系需要锁定的情况。工作室交付仍用中文块结构；本页字段在编译时映射到 `[角色]` 映射行与 `[具体情节]` 的 `摄影：`/`演出：` 行。

## 何时使用

单人镜头里站位、姿势和接触点仍然重要的情况：角色走入画面、角色拉动道具、角色说台词。两个及以上角色的镜头改用 `template-multi-character-anchor.md`。

## 叙事规划

使用 [共享叙事规划](narrative-planning.md)：资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束是映射进这个紧凑站位提示词的语义检查项。由事件、因果反应、揭晓或状态变化决定阶段边界，再分配时间。不预设数量，不平均分时；一个连续动作可能就够了。守住一个主导动作和运镜限制，在整个动作里带住接触、视线、姿势和道具状态，并以预定的结尾画面收住。时间码按这份规划填写。

## 提示词模板

```
[At/from N seconds] One character in frame.

[Identity, registered asset name].
  Screen position: [left third / center / right third],
  x-position [%], y-position [%], frame occupancy [%].
  Depth layer: [foreground / midground / background].
  Body orientation: [toward camera / away / profile-left /
    profile-right / three-quarter].
  Pose: [physical configuration].
  Gaze: [where they look — frame-position or off-screen direction].
  Contact points: [physical surfaces — feet planted, hand on doorframe].
  State lock: [emotional or physical state].

Goal and trigger: [why the character acts; intended visible result].
One dominant action: [single action — one motion verb at the spine
  of the shot per § Single-vs-multi-shot decision].
Motion: [secondary motion — hair, fabric, breath; eye motion].

Camera: [shot size], [angle], [lens], [movement — one dominant
  motion per § Multi-motion camera overload guidance].
Setting: [location, time, weather, atmosphere].
Aesthetic: [genre, lighting, color grade, texture].
Audio: [ambience, SFX, dialogue, music].
Continuity: [identity, direction, contact, and prop state; any motivated change].
Final frame: [composition and resulting character/prop state at last frame].
```

## 各字段写什么

- **身份、位置、景深层、朝向、姿势、视线、接触点、状态锁定、面部表情**是角色锚点块（Character Anchor Block）的 10 个属性，属性结构见 `template-multi-character-anchor.md`。
- **一个主导动作**与**次级运动**分开写，防止多重运动过载，见 `higgsfield-seedance-failure-modes.md` § Multi-motion camera overload。

## 另见

- `template-multi-character-anchor.md`（同类模板）：带跨角色关系的多人版本
- `template-top-down-map.md`（同类模板）：填写本模板前预先可视化站位的元提示词
- `higgsfield-seedance.md` § Frame Coordinate System：位置词汇

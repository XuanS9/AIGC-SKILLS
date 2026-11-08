# 模板：多人锚定提示词

原生站位规划骨架，用于画面里有两个及以上角色的镜头；不是当前工作室可直接提交的完整提示词。在动作描述之前，先锁定每个角色的身份、位置、景深、姿势、视线和接触点。工作室交付仍用中文块结构；参考标签归 `[参考资产]`，关系补充归 `[角色]`，站位与反应映射到 `[具体情节]` 的 `画面：`/`听者：` 及 `[保持一致]`。

**站位锚定不能代替互动。**填写后按[互动闭环](higgsfield-acting.md#双人和多人互动闭环)补关键听者和旁观者的触发、反应过程、余态与发起者接续；具体写法见[三人演出小样](template-ensemble-reaction.md)。不把静态视线锁直接复制成整场的倾听表演。

## 何时使用

任何有两个及以上角色、且站位、朝向和角色间关系重要的 Seedance 提示词。用本模板代替零散的空间片段后，角色互换、越轴和视线错位都会明显减少。

## 叙事规划

使用 [共享叙事规划](narrative-planning.md)。它的八个语义层（资产、目标、全局视听与空间、行为、阶段、连续性、结尾画面、约束）映射进这些原生的角色、关系和镜头字段。阶段由事件、因果反应、揭晓，或位置/接触/道具归属的变化决定，再分配时间；不预设数量，不平均分时。阶段不一定是切镜。每个移动都锚定到它的触发，并把结果状态带进下一个锚点，包括明确允许的越轴。规划后再填时间码；角色数描述的是实际演员，不是阶段数。守住单镜头复杂度限制和结尾画面字段。

## 提示词模板

```text
[At/from N seconds] N characters in frame.

Character A — [identity, registered asset name].
  Screen position: [left third / center / right third],
  x-position [%], y-position [%], frame occupancy [%].
  Depth layer: [foreground / midground / background].
  Body orientation: [toward camera / away / profile-left /
    profile-right / three-quarter].
  Pose: [physical configuration — standing, seated, mid-stride].
  Gaze: [where they look — frame-position OR "looking at Character B"].
  Contact points: [physical surfaces they touch — feet on wet
    asphalt, left hand on the railing].
  State lock: [emotional or physical state — calm, exhausted,
    injured, soaked].

Character B — [identity, registered asset name].
  [...same fields...]

Cross-character relationships:
  Distance between A and B: [approximate].
  Eyeline: [A → B, B → A, both → off-screen, mutual avoidance].
  Crossing rule: [neither crosses the central vertical axis /
    A may cross right-to-left at N seconds].
  Negative space: [where the empty area sits in frame].

Goal: [event and intended visible outcome].
Action and response: [initiator's action → what each key listener/witness can perceive
  → their visible response and sustained state → initiator's uptake when perceptible;
  background groups continue or respond according to their attention;
  timing assigned after planning, preserving the anchors until the scripted move].
Camera: [shot size], [angle], [lens], [movement].
Setting: [location, time, weather, atmosphere, production design].
Aesthetic: [genre, lighting, color grade, texture, VFX].
Audio: [ambience, SFX, dialogue, music].
Continuity locks: [costume / state / prop invariants].
Final frame: [composition at last frame].
```

## 各字段写什么

- **身份**对应已登记的角色调用名。
- **画面位置**把定性锚点和百分比写法配对，见 `higgsfield-seedance.md` § Frame Coordinate System。
- **接触点**防止角色漂浮这一失败模式，见 `higgsfield-seedance-failure-modes.md`。
- **跨角色关系**防止角色互换和越轴，结构依据见 `higgsfield-seedance.md` § Spatial Layout Block。

## 差 / 好 / 很好

**差：**空间片段零散地夹在动作描述里。`Character A walks in. Character B is by the window.` 结果：Seedance 自选默认位置；A 和 B 跨切镜互换；视线漂移。

**好：**使用本模板，填好每个角色的锚点块，只写定性位置（`left third` / `right third`）。空间准确度提高，跨角色关系更稳。紧凑镜头里坐标精度仍然不够。

**很好：**使用本模板，填满每个字段，包括与定性锚点配对的百分比；写清跨角色关系（距离、视线、越轴规则、负空间，见 [vocab.md](vocab.md) § Composition Vocabulary → Crossing rule 与 § Negative space）。先用 `template-top-down-map.md` 预先可视化场景，把生成的站位说明贴进 Character A / Character B 字段。同一组角色在多个切镜间可以复用这个块，按镜头复制后调整，不必重新指定。

## 另见

- `template-top-down-map.md`（同类模板）：生成本模板所需站位说明的元提示词
- `template-worked-example-two-character.md`（同类模板）：本模板结构的完整填写示例
- `higgsfield-seedance.md` § Frame Coordinate System 与 § Spatial Layout Block：本模板用到的词汇和块

# 模板：Seedance 2.5 多参考（omni_reference）提示词

> **工作室格式（Studio form）。**本文件记录 Higgsfield 原版英文块模板，代码块里的英文骨架与示例保留原文作对照。工作室交付先加固定 `[参考资产]` 集中所有标签，再用中文状态块与字段：`[角色]` `[道具]` `[场景]` `[动作与声音参考]` `[生成目标]` `[具体情节]`（段头 `起s-止s｜景别｜视场角N°`，分项 `摄影/演出/可选互动/声音/→ 结束`）`[视觉风格]` `[镜头]` `[声音]`（对白为计时行，第一秒定位 `{Hm.}`）`[保持一致]`，只有对白原句用英文。英文块标签在 `director_contract_lint.py` 中报 FAIL。格式归属：[跨类型导演模板 §1](template-general-director-2-5.md#1-块结构higgsfield--dreamina-seedance-25-标准)。

这是 **Seedance 2.5 `omni_reference`** 生成的可粘贴骨架：把多个角色、道具、场景、动作与音频参考合进一条分阶段的片段。

规则来源：`higgsfield-seedance-2-5.md`。各模式的长模板（编辑、延伸、一键、转场、白模）见同目录的 `higgsfield-seedance-2-5-mode-playbooks.md`。

## 何时使用

- 本项目每一次 Seedance 2.5 视频生成：零个、一个或多个参考素材都适用。单张图仍只作属性参考，从不当起始帧。
- 两个及以上有名字的主体不能互换外观、服装或道具。
- 片段长于一个连续节拍（需要分阶段）。
- 编辑或延伸：任务允许重新生成时，把源视频作为视频参考；必须精确保留原时间线时，另行核实原生编辑/延伸能力。

用户选了其他模型时，先核对该模型支持的媒体职责再用本模板。零参考时用文字描述主体与空间，不虚构槽位。单参考时用同一职责映射的精简版，不改成首帧驱动流程。只声明真实素材和真实绑定的槽位。

## 平台设置（不写进提示词）

`[OFFICIAL — platform, snapshot 2026-08-07]` 在界面或 API 里设置，正文不写：

| 设置 | 取值 |
|---|---|
| `mode` | `omni_reference` |
| `duration` | 4–30 秒 |
| `resolution` | `480p`（草稿）、`720p` 或 `1080p`（2.5 没有 4K） |
| 画幅 | `auto` · `21:9` · `16:9` · `4:3` · `1:1` · `3:4` · `9:16` |
| `generate_audio` | 除非成片要求静音，否则为 `true` |

花额度前先预检：`python3 scripts/seedance_lint.py --preflight --model seedance_2_5 "<prompt>"`

---

## 骨架

填写这个原生块格式前，先按 [共享叙事规划](narrative-planning.md) 规划。八层是语义规划：资产/参考、目标、全局视听与空间、行为/节奏、阶段、连续性、结尾画面、约束。把它们映射到下面的字段；短提示词不需要额外标题。

阶段由事件、因果、揭晓或状态变化决定，再选镜头覆盖，为动作、反应、对白和转场分配时间。不预设阶段数，也不平均分时。阶段不自动等于一次切镜或一次生成。保留已确认的剧情、结局和继承状态，并对照合法时长核对总长。

下面的 `@Image 1`、`@Video 1`、`@Audio 1` 只是**语法示例**。用户说有参考，但实际文件或平台槽位无法查看时，复制正文里用描述性职责名（如“人物参考图”“动作参考视频”“环境声参考音频”），确切的槽位映射写在块外并标待核。不能因为用户提到一张图就推定 `@Image 1`。只有核实了真实附件和本片段的槽位映射，才写 `@` 记号。源视频可能有多个主体：它只提供所需的动作或运镜属性，不在成片里多出演员或动物。未知素材保持“待核验/待绑定”，正文和提示词里不说已绑定。

填写方括号字段。**镜头用不到的块直接删掉**，空块是噪音，不是结构。阶段块只按规划的变化重复。

```
[Characters]
<Character A> corresponds to @Image 1. Use only the appearance, hairstyle, and clothing.
<Character B> corresponds to @Image 2. Use only the appearance, hairstyle, and clothing.
Do not interchange these characters' appearances, clothing, actions, positions, or dialogue.

[Props]
<Prop A> corresponds to @Image 3 and belongs only to <Character A>. Use only the structure,
material, and color.

[Scenes]
<Scene A> references @Image 4. Use only the spatial layout, architecture, and lighting.
Do not use the people in the image.

[Motion and Audio]
@Video 1 defines the pacing of <specific action>. Do not use the person's identity, clothing,
or scene from the video.
@Audio 1 defines <Character A>'s voice and specified dialogue.

[Subject Profile: <Character A>]          ← only for a subject recurring across scenes
Appearance and clothing: @Image 1.
Fixed prop: <Prop A> from @Image 3.
Locations: <Scene A>.
Motion references: the <action> motion from @Video 1.
Do not use: other characters' clothing. Do not give this character other equipment.

[Generation Goal]
Generate a <video type>. The central subject is <subject>, and the primary event is
<one-sentence story summary>.

[Behavior and Rhythm]
<Subject's intent, observable performance, action-response causality, intensity and pace>.

[Stage <n>: <event / reveal / state change>; <time range assigned after planning>]
Initial state: <characters, props, space, and sound inherited from the preceding stage>.
Primary event: <ONE primary action or event and its visible response>.
End state: <positions, prop ownership, expression, or visible scene state to carry forward>.
Camera purpose: <what the viewer must see; continue the shot or motivate a cut>.

[Visual Style]
<Lighting, color, materials, texture, mood — named specifics, not stacked adjectives>.

[Camera]
<Shot size, angle, movement, focus subject, cuts — matched to the action, not decorative>.

[Audio]
<Ambience and action SFX>. (music, only if the project wants it) <specific sound effect>
Dialogue language: <language and regional variety>. <Character A> says: {the line}

[Maintain Consistency]
Keep <character identity, number of characters, clothing, prop ownership, spatial direction,
and audio relationships> consistent throughout; name the event that authorizes any change.

[Final Frame]
<Confirmed ending, visible composition and state, and any next-clip handoff>.

[Key Constraints]
<Task-specific reference exclusions and deviation prevention; keep platform settings separate>.
```

原版字段与工作室块的对应：`[Characters]`→`[角色]`，`[Props]`→`[道具]`，`[Scenes]`→`[场景]`，`[Motion and Audio]`→`[动作与声音参考]`，`[Generation Goal]`→`[生成目标]`，`[Stage n]` 与 `[Behavior and Rhythm]`→`[具体情节]` 的计时段，`[Visual Style]`→`[视觉风格]`，`[Camera]`→`[镜头]`，`[Audio]`→`[声音]`，`[Maintain Consistency]`、`[Final Frame]`、`[Key Constraints]`→`[保持一致]` 与最后一段的 `→ 结束：`。`[Subject Profile]` 在工作室格式里不单列，跨场景的固定信息归资产总表。

---

## 填写示例

两个角色、一个道具、一个场景、一个动作参考、三个阶段，这些数量只属于本例，不是要求。本例的事件边界是准备、包装、交接。规划后再为每段表演估时；三个阶段既不意味着等长，也不意味着固定时长。

```
[Characters]
<Florist> corresponds to @Image 1. Use only the appearance, hairstyle, and dark green apron.
<Assistant> corresponds to @Image 2. Use only the appearance, hairstyle, and clothing.
Do not interchange these characters' appearances, clothing, actions, positions, or dialogue.

[Props]
<Wrapped Bouquet> corresponds to @Image 3 and belongs only to <Florist> until Stage 3.
Use only the structure, flower types, and ribbon color.

[Scenes]
<Shop Workbench> references @Image 4. Use only the spatial layout, timber surfaces, and
window light. Do not use the people in the image.

[Motion and Audio]
@Video 1 defines the pacing of trimming stems and tying a ribbon. Do not use the person's
identity, clothing, or scene from the video.

[Generation Goal]
Generate an observational documentary clip. The central subject is <Florist>, and the primary
event is packing a single order from loose stems to a finished bouquet on the pickup shelf.

[Stage 1]
Initial state: <Florist> stands behind <Shop Workbench>. Loose stems, scissors, and wrapping
paper lie on the tabletop.
Primary event: <Florist> arranges the stems and trims them to length.
End state: <Florist> holds the bouquet in the left hand; the scissors are back on the right
side of the workbench.

[Stage 2]
Continue from the previous stage: both characters keep the same identities and clothing, and
<Florist> still holds the bouquet.
Primary event: <Assistant> unfolds the wrapping paper; <Florist> places the bouquet inside and
ties it with the ribbon.
End state: <Wrapped Bouquet> lies flat in the center of the workbench, ribbon bow facing camera.

[Stage 3]
Primary event: <Assistant> lifts <Wrapped Bouquet> and sets it on the pickup shelf.
End state: the bouquet is centered on the pickup shelf; both characters stand behind the
workbench looking at the finished order.

[Visual Style]
Overcast morning window light from frame-left, no fill from the camera side. Muted greens and
raw timber, one saturated accent in the ribbon. Real skin texture, visible paper grain.

[Camera]
Open on a medium shot of the workbench at chest height, hold through Stage 1, push in slowly
to the ribbon knot across Stage 2, then a single lateral move to follow the bouquet to the
shelf in Stage 3. 47° diagonal field of view throughout, no drift mid-segment.

[Audio]
Room tone, scissor snips, paper rustle, the ribbon pulling tight. <A shop bell rings once,
distant> (no music)

[Maintain Consistency]
Keep <Florist> and <Assistant>'s identities and clothing, the workbench orientation, the
scissors' position, and bouquet state consistent throughout. The bouquet remains with
<Florist> through preparation, rests on the workbench after wrapping, then passes to
<Assistant> in Stage 3 before being placed on the shelf; preserve this explicit handoff.
```

本例按工作室格式改写时：两人各写身高，第一段是约 1 秒的定位全景，`[声音]` 写 `0s-1s｜花店老板轻声：{Hm.}`，`(no music)` 改为末尾 `NO BGM。`。

---

## 发送前检查

- [ ] 每份素材都有职责**和**排除项
- [ ] 不写 `@Images 1 through N define N characters`，每个主体一行
- [ ] 每个道具都有明确归属或放置位置；交接有具名事件
- [ ] 每个阶段只有**一个**主要变化、可见反应和明确的继承/结束状态
- [ ] 阶段跟随事件、因果、揭晓或状态变化；每次切镜有观看目的
- [ ] 时间按表演需要分配，覆盖声明时长，并计入转场
- [ ] 不照搬阶段数或等时配额；结尾画面与已确认结局一致
- [ ] 全文不写年龄词（`higgsfield-seedance-engine-rules.md` 第 1 条）
- [ ] 只用正向表述：不写 `negative:` 清单，不堆裸否定
- [ ] 对白只在音频块里、写在 `{}` 中（工作室格式：`[声音]` 的计时对白行）
- [ ] 分辨率为 480p、720p 或 1080p，2.5 没有 4K
- [ ] `seedance_lint.py --preflight --model seedance_2_5` 无问题

## 相关文件

- `higgsfield-seedance-2-5.md`：本模板实现的写法规则
- `higgsfield-seedance-2-5-mode-playbooks.md`：编辑、延伸、一键、转场
- `template-multi-character-anchor.md`：跨角色锚定的 2.0 写法
- `template-global-style-prefix.md`：连贯分镜表的风格前缀
- `higgsfield-acting.md`：阶段需要表演时写什么

## 项目约定：跨类型编排

本项目的分阶段 Seedance 2.5 提示词，同时读 [跨类型导演模板](template-general-director-2-5.md) 与 [共享叙事规划](narrative-planning.md)。八层用于组织含义；交付按中文块结构，或在用户指定时映射进本原生多参考格式。已有的素材职责、保真等级、模式路由和平台检查继续适用。先定事件与状态变化，再定阶段数和时长；六个五秒阶段和持续高速特效只是示例选择，不是通用要求。

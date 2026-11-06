# 模板：素材视效变换（Seedance 2.0，视频到视频）（Template: Footage VFX Transform (Seedance 2.0, video-to-video)）

**这是 Seedance 2.0 的历史模板。**当前项目用 Seedance 2.5 `omni_reference`：源素材作为视频参考，承担具名的动作/时间职责，角色/道具/场景图和音频各自承担对应属性。当前项目的生成不要选用本模板的首帧步骤。

用于变换用户**已经拍好**的片段的可粘贴骨架：保留真实的主体 + 镜头运动，只改点名的那个元素。与 `higgsfield-seedance-vfx.md` 配套；那个模块承载规则，本文件承载填空骨架和四个示例写法。代码块里的英文提示词是原版示例，保留原文。

来源于 Higgsfield 的“Seedance 2.0 in 4K”视效讲解（`higgsfield.ai/blog/vfx_4k`，教程 `youtube.com/watch?v=Yte-UGhYkPQ`）：`higgsfield-seedance-vfx` 模块就是从它构建的。

## 何时使用（When to use this template）

用户附上一段真实片段（或描述一段），想要一条 Seedance 提示词：保留*他们自己*和他们的镜头运动，同时换掉世界、加一个特效元素、放进一个生物，或让一次计时运镜与一句台词同步。从零搭建的场景改用 `higgsfield-seedance.md`。

这些一律用 **Seedance 2.0、`mode=std`、4K** 跑（原生 4K 需要 std；fast 最高 720p）。

---

## 骨架（The skeleton）

写之前，用 [共享叙事规划](narrative-planning.md) 检查源素材。它的八层（资产/母片、目标、全局视听与空间、行为、阶段、连续性、结尾画面/交接、约束）从语义上组织这次编辑；保留纯文本英文输出，正文里不用 markdown。

锁定源时间线，在它的事件、因果触发、揭晓或状态变化处标出改动。保留时间、表演、切点和未受影响的边界状态；不要把源素材重新切成等长阶段。只为经授权的新内容或新运动分配时间，并且在规划好它们的原因和到达状态之后。下面所有示例写法的时长、时间码和生物数量都只是示意；检查真实片段，并保留所选模式的时长和保真约束。

```text
@source: Original <clip> — <subject, wardrobe, setting, action>. Preserve identity, face,
wardrobe, performance, framing, lens, camera and motion exactly; <the one change>.
@creature: Reference photo of a real <animal/material> — <texture/anatomy notes>. Appearance
and texture reference only; ignore its background and lighting.   (only if a texture ref is used)

Photoreal. 16:9. <N>s. 4K. <look/grade>. NON-IP — generic <X>. SFX [and source dialogue] only.

<Continuous shot, same framing as source. Preserved performance. The transformation, with its
physics and how it interacts with the plate (light spill, contact shadow, refraction, parallax).
Any timed camera move with a semantic + numeric anchor. Lock-down clause: face and identity
unchanged; everything else identical to the source.>

SFX [and source dialogue] only: <specific, ordered sounds synced to the visible action>.
```

填写顺序：检查片段 → 按画面实际显示的内容设定 `@source` 和时长 → 点名那一个改动和它在源时间上的触发 → 锁定其他一切 → 定义最后一帧源画面时的特效结果状态 → 用锁定句收尾。如果新增内容改变了组装后的时间线，把源时间和输出时间分开标注，并在不重新定时保留表演的前提下处理接点。

---

## 写法 1：换环境（移动镜头）（Pattern 1 — Environment swap (moving camera)）

保留主体和真实的镜头运动；替换世界，让它以匹配的视差掠过，并重新照亮主体。

```text
@source: Original clip — man walking toward camera in a plaza, handheld follow. Preserve his
identity, face, walk, gestures, wardrobe and the exact handheld camera move; change only the
world around him.

Photoreal. 16:9. 6s. 4K. Warm directional late-afternoon grade. NON-IP. SFX only.

Same handheld follow and framing as the source, same walk. On his finger snap at about 2s,
transform only the environment around him into open desert at sunset — dunes and heat haze
streaming past with parallax that matches his forward motion. Keep the sun as the key from
screen-left exactly as before so his face and the light on him barely change; let a warm
bounce off the sand lift his under-jaw shadow. Face and identity unchanged; walk, wardrobe,
framing and camera move identical to the source; only the world is replaced.

SFX only: footsteps on sand, a low desert wind rising after the snap.
```

## 写法 2：在画面里加一个元素（头部着火）（Pattern 2 — Add an element in-frame (head on fire)）

在底片上叠一层特效；让它把光溢回主体身上；表演保持毫不知情。

```text
@source: Original clip — man talking to camera in a parked car, golden-hour light. Preserve
his face, expression, lip movement, the car interior and the golden-hour light; add only fire
to his hair.

Photoreal. 16:9. 5s. 4K. Golden-hour grade. NON-IP. SFX only.

Same static framing as the source, same delivery to camera. His whole head of curls catches
fire — a soft whoomph as it ignites, then a low steady flame roar, individual strands
burning, occasional ember pop — while he keeps talking, unfazed. The orange firelight
flickers on his face and spills onto his shirt and the car's paint, matched to the sunset.
Face, identity and performance unchanged; only the fire is added.

SFX only: a soft whoomph on ignition, then steady flame roar and crackle with occasional
ember pops.
```

## 写法 3：主体身上/身后的生物，加一次揭示后拉（Pattern 3 — Creature on/behind subject with a reveal pull-back）

开场紧贴单独的新增生物，然后后拉到与源构图 100% 一致，口型正确。这个写法明确地加了一段开场和一次镜头揭示；它不是默认的保留源素材的编辑。先规划揭示到源素材的接点，包括姿势、动作相位、速度、构图、光和声音。示意的总长 8 秒、约 2 秒揭示，给源表演留下约 6 秒；检查源素材之后再选实际预算，并在使用缩短的窗口之前指出被省掉的内容。

```text
@source: Original clip — man talking to camera on a sidewalk, building rising behind him,
handheld. Preserve his identity, face, performance, lip-sync and the handheld move; add giant
lizards climbing the building, and prepend a tight reveal.
@creature: Reference photo of a real monitor lizard — pebbled scaly skin, long claws, heavy
tail, true reptile anatomy. Texture and anatomy reference only; ignore its background.

Photoreal. 16:9. 8s. 4K. Overcast daylight grade. NON-IP — generic large monitor lizards. SFX
and source dialogue only.

Open tight and telephoto on dozens of car-sized photoreal lizards swarming up the building en
masse — claws hooking window ledges and concrete, heavy tails dragging, pebbled scales matte
and mud-caked, catching the low sun, never smooth or rubbery. At about 2s the camera smoothly
pulls back to a 100% match of the source composition — same angle, headroom, horizon and lens
— landing on the man mid-sentence, his lips matching the source exactly saying: "definitely
should not be there." The handheld move then runs exactly as the source while the lizards keep
climbing behind him, lit to the same overcast daylight with real soft-edged contact shadows on
the wall. Face, identity, performance and lip-sync unchanged.

SFX and source dialogue only: claws scraping concrete, heavy scaled bodies shifting, his line
landing on the reveal.
```

## 写法 4：全程手持的电影镜头（生物融合）（Pattern 4 — Full handheld cinematic (creature integration)）

最难的情况：摄影机全程在动，所以特效必须跟上角度、视差和晃动而不散架。

```text
@source: Original clip — man turning and reacting, fully handheld, forest clearing. Preserve
his identity, face, reaction, wardrobe and the full handheld move frame-for-frame; replace the
setting with a rainy forest and add three giant long-necked dinosaurs behind him.

Photoreal. 16:9. 10s. 4K. Overcast rainy grade, atmospheric haze. NON-IP — generic
long-necked sauropods. SFX only.

Same handheld follow, framing, shot scale, lens, pan, tilt, speed and shake as the source —
do not re-frame, re-time, re-angle or re-cut. Three enormous photoreal sauropods tower behind
him in a rainy forest, their massive bodies dwarfing the trees, skin deeply wrinkled, cracked
and asymmetric, moving with slow heavy weight; at about 2–3s, exactly as the man turns and
looks back, one sauropod steps in closer. Veil them partly behind foreground trees with a
telephoto compression and shallow depth of field, motion blur and handheld softness matching
the plate; same overcast key and color temperature as on him, real soft-edged contact shadows,
the same rain and haze over him as the far background. Face, identity and reaction unchanged;
camera move identical to the source.

SFX only: rain on leaves, deep low sauropod calls, heavy footfalls landing on the closer step.
```

---

## 提醒（Reminders）

- **默认与源时长一致。**任何经授权的开场或时长改变，都需要明确的源时间到输出时间映射；重新计算数字化的变焦标记，不要悄悄重新定时或丢掉保留的表演。
- **加了开场？**源表演的 `总长 − 开场 = 保留窗口`：在承诺口型同步之前，标出被截掉的部分（`higgsfield-seedance-vfx.md` § Duration discipline）。
- **生物看起来还是 CG？**加一张真实的参考照片作为 `@creature`（只取质感），或者生成一张画面开发静帧，作为 `omni_reference` 里的场景/风格参考。
- **预检**完成的提示词，用上层的 lint：`python3 scripts/seedance_lint.py --preflight --model seedance_2_0 "<prompt>"`。

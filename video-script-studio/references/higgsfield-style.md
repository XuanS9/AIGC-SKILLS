# Higgsfield Visual Styles

Use [shared narrative planning](narrative-planning.md) before choosing a
recipe's coverage: a **stage** is a dramatic event or state transition, a **shot**
is continuous camera coverage between cuts, and a **generation clip** is one
model output. A shot can span stages, a stage can need several shots, and a
supported clip can contain multiple shots. Style defines the look; story events,
causal turns, and performance determine segmentation and timing. Preserve the
style anchor across clips unless the story calls for a change.

## 电影视觉参考匹配

这是项目视觉设计规则，适用于通用图像与视频任务，不要求使用 Higgsfield。

1. **选择一个主参考。**根据项目题材、环境、情绪与动作规模选择具体电影；用户已指定则继承，未指定则推荐一个，并随本批次样本一并评估，不另设风格审批。不要堆叠多部电影名称代替选择。
2. **将片名拆成可见特征。**记录主色与点缀色、光源方向与反差、构图与体量关系、前中后景、材质与空气层次。实际提示词只选当前场景需要的特征，避免形容词堆积。
3. **适配当前时空。**同一视觉体系可以有日景、夜景、室内与黎明版本；不把每场都变成参考片的标志性夕阳。空间、时间、天气和用户画幅优先，宽银幕参考不自动改成 2.35:1。
4. **保持资产职责。**场景图只含环境；用巨树、岩壁、河道与景深建立尺度，不添加人物、怪兽或直升机来充当比例尺。角色主参考保留已定身份与服装；B/P 孤立资产仍用透明或纯色底，只继承适用的材质表现。
5. **区分参考与复刻。**提炼摄影、美术和光色方法，不照搬参考片的角色、生物设计、道具、历史年代或具体构图，不改写已确认剧情。
6. **如实标注依据。**没有实际图像时写“文字风格参考”；看过用户提供的图像后才描述该图的可见特征。片名不是平台预设，不虚构上传、模型参数或视觉验收。

### 项目记录字段

`主参考｜适配原因｜颜色｜光线｜构图与尺度｜空间与材质｜时段适配｜保持项｜参考形式（文字/实际图像）`

### 《绝境雨林》适配示例

主参考：《金刚：骷髅岛》（Kong: Skull Island，2017）。以下为本项目的视觉转译，不是对原片每个镜头的精确分析或相机参数声明。

| 维度 | 本项目执行标准 |
|---|---|
| 适配原因 | 巨兽雨林冒险，需要环境压迫、清晰行动空间和大体量的视觉冲击。 |
| 颜色 | 深森林绿、橄榄绿、湿土褐为环境底色；日景用暖金光作局部对比，避免整幅荧光绿或过度橙青。 |
| 光线 | 日景采用有方向的自然光、深绿阴影与局部逆光轮廓；营地夜景采用有来源的探照灯、棚内暖灯与冷色环境光；黎明降低反差。 |
| 构图与尺度 | 巨树、板根、岩壁与河道建立体量差；清楚保留可行动区域，前景可遮挡局部但不堵住主要空间。 |
| 空间与材质 | 前景湿润粗树皮和泥水、中景行动地形、远景层叠林冠与薄雾；局部湿面高光，保留泥土、叶片、岩石的材质差异。 |
| 保持项 | 皇室贵族家庭的热带度假身份及已确认服装；既定剧情、时代、画幅和资产分类。不得引入原片军队、军装、军用载具或特定怪兽。 |
| 当前参考形式 | 文字风格参考；实际场景图生成与视觉验收另行记录。 |

不要以“大片感、电影级、高清”作为完整风格定义。可执行表达应明确哪一处受到什么光照、什么地形建立体量、哪些前后景产生纵深。

## Core Platform Styles

These five styles are Higgsfield's named presets. Reference them by exact name.

### Cinematic
**Look:** Polished, high-contrast, vivid colors, balanced exposure — modern blockbuster
**Best for:** Drama, action, narrative films, commercials, any professional content
**Color tendency:** Rich, saturated, clean
**Prompt phrase:** "Style: Cinematic"
**Pair with:** Kling 2.6/3.0, Sora 2, Dolly In, Arc, Crane Up

```
Example: A detective walks through a night market.
Style: Cinematic. Cold blue shadows, warm amber market stall light.
Shallow depth of field. 16:9.
```

---

### VHS
**Look:** Retro videotape grain, color bleed, slight scanlines, analog imperfection
**Best for:** 80s/90s nostalgia, horror, thriller, retro music videos, flashbacks
**Color tendency:** Slightly washed out, warm yellows and reds, low contrast
**Prompt phrase:** "Style: VHS"
**Pair with:** Handheld camera, Wan 2.5, any horror preset

```
Example: Teenagers at a house party in 1987.
Style: VHS. Warm, grainy, slightly overexposed. 4:3 ratio.
```

---

### Super 8MM
**Look:** Warm film grain, soft vignette, muted colors, home-movie feel
**Best for:** Personal stories, romance, nostalgia, indie films, family moments
**Color tendency:** Warm, golden, slightly faded
**Prompt phrase:** "Style: Super 8MM"
**Pair with:** Handheld, natural light descriptions, intimate scenes

```
Example: A couple dancing in a sunlit backyard in the 1970s.
Style: Super 8MM. Warm grain, soft vignette edges. 4:3.
```

---

### Anamorphic
**Look:** Ultra-wide aspect ratio (2.35:1), horizontal lens flares, slight barrel distortion,
epic scale — classic Hollywood widescreen
**Best for:** Action, epic fantasy, war films, sweeping landscapes, high drama
**Color tendency:** High contrast, deep blacks, rich highlights
**Prompt phrase:** "Style: Anamorphic" or "Style: Anamorphic, 2.35:1 widescreen"
**Pair with:** Crane Up, 360 Orbit, Super Dolly Out, Sora 2

```
Example: An army marches across a frozen plain at dawn.
Style: Anamorphic, 2.35:1. Deep blue-grey tones. Lens flare on the rising sun.
```

---

### Abstract
**Look:** Non-representational, surreal color schemes, unconventional shapes, artistic
**Best for:** Music videos, conceptual art, dream sequences, experimental content
**Color tendency:** Vivid, unexpected, driven by concept not realism
**Prompt phrase:** "Style: Abstract"
**Pair with:** Wan 2.5, Portal, Multiverse, Glitch presets

```
Example: Fractured geometric shapes pulse to music in a void.
Style: Abstract. Electric blue and magenta on black. 1:1 ratio.
```

---

## Color Grade Vocabulary

Use these in any prompt regardless of style preset:

| Mood | Color grade description |
|------|------------------------|
| Cold thriller | "Teal and orange, desaturated, high contrast" |
| Warm nostalgia | "Golden hour amber, soft shadows, low contrast" |
| Cyberpunk | "Neon magenta and cyan, deep shadows, HDR" |
| Horror | "Sickly green-yellow, crushed blacks, desaturated" |
| Romance | "Soft warm pink-gold, lifted shadows, dreamy" |
| Documentary | "Neutral, natural light, no grade" |
| Epic fantasy | "Rich jewel tones, deep shadows, volumetric light" |
| Noir | "High contrast black and white, or near-monochrome" |
| Sci-fi cold | "Ice blue and silver, stark white light" |
| Post-apocalyptic | "Desaturated orange and brown, dust haze" |

---

## Lighting Vocabulary

| Type | Description | Best for |
|------|-------------|----------|
| Golden hour | Warm directional light just after sunrise or before sunset | Romantic, epic, beautiful |
| Overcast | Soft diffused light, no shadows | Documentary, emotional, grounded |
| Neon | Colored artificial light from signs/screens | Cyberpunk, night scenes, urban |
| Volumetric | Light rays visible through atmosphere (fog/dust) | Fantasy, cinematic, atmospheric |
| Practical only | All light comes from sources visible in frame (lamps, fire, screens) | Realism, noir, intimate |
| Side-lit | Single strong light from one side creating deep shadow | Drama, tension, portrait |
| Backlit | Subject silhouetted or rimlit from behind | Mystery, romance, epic reveal |
| Low key | Mostly dark with small pools of light | Horror, thriller, noir |
| High key | Bright, even, minimal shadows | Comedy, commercial, lifestyle |

---

## Cinematic Lighting Techniques

Specific lighting setups that AI models respond to well. Use these terms directly
in your prompts for precise control over how light shapes the scene.

| Technique | Effect | Best for |
|-----------|--------|----------|
| Rembrandt lighting | Triangle of light on the shadowed cheek, one eye lit | Portrait drama, character intros, moody interviews |
| Butterfly / Paramount lighting | Overhead light casting a shadow under the nose | Glamour, fashion, beauty shots, classic Hollywood |
| Split lighting | Half the face lit, half in complete shadow | Duality, inner conflict, villain reveals |
| Rim lighting / backlit | Edge glow outlining the subject's silhouette | Mystery, epic reveal, separation from background |
| Motivated lighting | Light source visible or implied in the scene (lamp, window, fire) | Realism, narrative grounding, naturalistic drama |
| Practical lighting | In-scene light sources (neon signs, candles, screens) | Night scenes, cyberpunk, intimate realism |
| Chiaroscuro | Extreme contrast between light and dark areas | Renaissance feel, high drama, painterly compositions |
| High-key | Bright, minimal shadows, even illumination | Comedy, commercial, lifestyle, clean aesthetic |
| Low-key | Deep shadows dominate, small pools of light | Noir, thriller, horror, psychological tension |
| Golden hour / Magic hour | Warm amber directional light, long soft shadows | Romance, beauty, epic landscapes, emotional beats |
| Blue hour | Cool steel-blue ambient light just after sunset | Melancholy, transition, quiet tension, urban solitude |
| Harsh midday sun | Hard overhead light, strong defined shadows | Desert, confrontation, exposed vulnerability |
| Overcast diffused / softbox | Even soft light, no hard shadows | Portraits, documentary, grounded realism |

---

## Aspect Ratio Guide

| Ratio | Name | Best for |
|-------|------|----------|
| 16:9 | Widescreen | Standard video, YouTube, film |
| 9:16 | Vertical | TikTok, Instagram Reels, Shorts |
| 2.35:1 | Anamorphic | Epic cinema, maximum widescreen drama |
| 1:1 | Square | Instagram posts, artistic |
| 4:5 | Portrait | Instagram feed, social portrait |
| 4:3 | Classic TV | Retro, VHS feel, vintage |

---

> **Negative constraints:** For texture/lighting artifacts (flickering textures, style ignored,
> over-lit output, color grade inconsistency) and their prevention phrases, see
> `negative-constraints.md` — Texture/Lighting Artifacts section.

---

## Style Best Practices (Cinema Studio 3.0 / Seedance 2.0)

These principles apply to Cinema Studio 3.0's generation engine (Business/Team plan only) and complement the style vocabulary above.

### One Style Anchor Rule

ONE primary style anchor beats five adjectives. Beyond 2–3 style tokens, model attention dilutes and the output becomes generic.

**Wrong:** `Style: cinematic, anamorphic, moody, atmospheric, dramatic lighting, film grain, desaturated, noir-inspired, high contrast, vintage feel`

**Right:** `Style: anamorphic, subtle grain, muted palette`

Pick your anchor (the single most important style element), add 1–2 supporting tokens, stop.

### "Cinematic" Does Nothing

Every generated video is "cinematic" by default. The word adds zero information. Replace it with a specific lens or contrast description:

- ~~"cinematic"~~ → `shallow depth of field, warm highlights, cool shadows`
- ~~"cinematic look"~~ → `anamorphic, 2.35:1, horizontal lens flares`
- ~~"cinematic quality"~~ → `35mm film stock, natural grain, Kodak Portra palette`

### Style Transfer via @Reference

Visual style references beat descriptive text. One reference image/video carries more style information than 10 descriptor words:

```
Match the visual style, color grading, and film texture of @Video1.
A woman walks through autumn leaves in a park.
Camera: slow tracking alongside her.
```

Use style references for: color grading, film stock emulation, lighting mood, texture quality, era-specific looks.

### CGI Material Contract

When prompting CGI or product renders, specify 2–4 material properties per surface to avoid the default "plastic sheen":

| Property | Options | Example |
|----------|---------|---------|
| Base | metal, glass, fabric, ceramic, wood, leather | `brushed stainless steel` |
| Roughness | matte, satin, glossy, mirror | `satin finish` |
| Imperfection | scratches, dust, wear, fingerprints, patina | `fine scratches from use` |
| Edge | beveled, sharp, rounded, chamfered | `soft rounded edges` |

**Example:** `A matte ceramic vase with hairline cracks and a subtle patina, soft rounded rim, resting on rough-hewn oak.`

### Period Control

Don't just name the decade — specify the **materials and lighting** of the era:

- ~~"1970s style"~~ → `Kodachrome warm tones, wood paneling, orange shag carpet, tungsten bulbs casting amber light`
- ~~"1940s noir"~~ → `high-contrast black and white, Venetian blind shadows, fedora silhouettes, wet asphalt reflecting streetlamps`
- ~~"1990s home video"~~ → `Hi8 camcorder grain, autofocus hunting, timestamp overlay, oversaturated greens`

---

## Register Poles — the style dial has opposite ends

`[FIELD — 13-project community harvest, 2026-07-18]` — "photoreal cinematic"
is not one register. Production projects sit at *named poles* of a dial, and
the pole decides the whole camera grammar:

| Register pole | Camera grammar | Texture stack |
|---|---|---|
| **Film register** (drama/romance features) | Handheld breathing, off-level allowed, natural motion | 35mm grain, milky low contrast, gate weave, halation, "corners as bright as center" |
| **Broadcast-TV register** (early-2000s drama) | **Locked-off tripod, frontal compositions, held reaction beats, ONE camera move per shot maximum** | Heavy soft diffusion, blooming highlights, telecine grain, flat neutral daytime |
| **Stop-motion / hand-animated** | Stepped motion — "true 12fps, animated on twos: each pose held two frames then snapping, never gliding" + constant painterly boil | **Split-motion rule:** atmosphere (snow, breath-vapor, smoke) moves SMOOTHLY while figures step on twos — an explicit constraint that fights the video model's default smoothness |
| **Anime / cel** | Per-shot named camera, fewer physics/skin blocks (the template contracts) | "Cel-shaded 2D, clean flat fills, two-to-three value cel shading — not painterly, not 3D, no CGI smoothness" |

**The style-anchor slot swaps vocabulary by register.** Same slot, different
language: photoreal anchors on a DP/director look (short-form only — block
prompts describe the look instead, per the seedance measurable-language
rules) · anime anchors on an **art era** ("early 2000s retro anime, vintage
cel proportions") · stop-motion anchors on **medium physics** ("12fps on
twos, painterly boil"). Never carry one register's anchor into another.

**One saturated accent color, reserved for the story.** The corpus-wide
color discipline: the plot-critical prop owns the only saturated accent in a
muted grade (an acid-green device, a chartreuse remote LED) — and the same
reservation works temporally ("golden hour is reserved for the twist";
everything before it stays flat neutral). State the reservation explicitly.

---

## Style Recipes — seven proven shapes

`[OFFICIAL — Higgsfield cinematic-prompt-builder skill, 2026-07]` — starting
recipes, each a distinct render contract. Combine and deviate freely; the
load-bearing part of each is the **is / is-NOT declaration**. The source's shot
counts and timings below are optional historical examples, not prescribed
structures. Choose the needed events and coverage first, then assign durations
from readability and performance. Do not impose a 15s envelope, equal lengths,
a fixed number of sections, or a mandatory hero hold. Model duration limits
apply to generation clips, independently of the recipe.

| Recipe | Look declaration | Structure + signature | Audio |
|---|---|---|---|
| **Live-action epic** | 8K photoreal, anamorphic, fine grain — "photoreal, NOT 3D/game" | Oner or multishot; one "hook" event triggers one held slow-mo beat, then snaps back; scale contrast (tiny figures vs vast subject) | Diegetic; slow-mo drops to muffled vacuum + heartbeat, snaps back with a whoosh |
| **3D animated feature** | Vibrant glossy CGI, Pixar-quality stylized, subsurface fur/skin | Montage with motivated angle changes; per-shot spoken lines with delivery described; land a visual gag when called for (source example: 6 shots / 15s, optional) | Light score allowed; often still SFX-forward |
| **Game cutscene** | UE5 real-time in-engine render — "hyperreal but unmistakably GAME-rendered, NOT film" | Hard cuts motivated by game events (source example: 3 shots / 15s, optional); **screen-pinned HUD in a locked accent hex, every element enumerated with exact text** — HUD never parallaxes | No music; SFX + subtle UI ticks |
| **Gameplay footage** | AAA arcade (racing) — hyper-saturated engine render, "in-game, NOT a film plate" | Rock-steady chase-cam locked to vehicle, NO slow-mo anywhere, live HUD (RPM, boost, minimap) | Engine, gears, boost, tyre screech, UI beeps |
| **FPV / POV oner** | One unbroken take, photoreal macro, anamorphic | Beats by timestamp in one paragraph; one named speed ramp (240fps bullet-time beat → snap to 24fps); macro brushes against surfaces | Slow-mo swaps ambience for amplified rhythmic sound |
| **VFX composite** (on a source clip) | Photoreal practical-FX realism; composition + grade INHERITED from the source | INPUT LOCK: plate preserved unchanged, camera inherited exactly; only additions = new element + its light + contact shadows; parallax-locked to an anchor plane | New element's diegetic sounds over preserved room tone |
| **Kaiju / creature** | 8K photoreal anamorphic, ORIGINAL design ("not based on any franchise") | Event-led cuts with per-cut OPTICS (source example: ~6 cuts, optional); a repeated detail can link an opening shot to the next shot's zoom; **containment rule** ("stays at the sea surface, never airborne") grounds physics and scale | Diegetic only — rumble, roars, water-burst, subsonic boom |

Full engine-side counterparts: the HUD recipe and INPUT LOCK live with
worked patterns in `higgsfield-seedance.md` and
`higgsfield-seedance-vfx.md`; the containment rule doubles as the
build-safe construction law (`higgsfield-seedance.md` § Build-safe
construction).

---

## Related skills
- `higgsfield-camera` — Camera controls to pair with styles
- `higgsfield-mixed-media` — Artistic style overlays (non-photorealistic)
- `higgsfield-moodboard` — Moodboard + Soul Hex for project-level style locking
- `higgsfield-cinema` — Cinema Studio built-in color grading suite
- `template-*.md` — Annotated genre-specific prompt templates with style examples

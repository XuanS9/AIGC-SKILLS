# Higgsfield Vibe Motion

Use [shared director planning](narrative-planning.md) for the content timeline: information reveals, readable text/logo holds, transitions and end states determine stages before durations. Compile those decisions into editable Remotion sequences using the project's fps and exact frame arithmetic; deterministic code timing remains supported. Do not impose a fixed stage count or equal durations from a sample. The final logo/text state and audio must remain continuous across sequences.

## What Vibe Motion Actually Is (And How It Differs from Video Generation)

This is the most important thing to understand about Vibe Motion:

| Standard AI Video Generation | Vibe Motion |
|------------------------------|------------|
| Predicts pixel sequences | Generates Remotion code |
| Text can hallucinate or distort | Text is always crisp (it's code) |
| Each change = full re-render | Real-time edits on live canvas |
| Physics is emergent/unpredictable | Physics is a slider you control |
| Output: video file | Output: motion graphic + deployable code |
| Good for: cinematic scenes | Good for: brand, typography, data, structure |

**Vibe Motion is powered by Claude (Anthropic) and Remotion** — the open-source
React framework for programmatic video. It generates actual code that renders
deterministically, meaning the same prompt always produces the same output.
Text never breaks. Colors stay exact. Brand consistency is guaranteed.

**Location:** higgsfield.ai/vibe-motion

---

## What Vibe Motion Is Built For

Use Vibe Motion when your content is about **structure, timing, and information**
rather than cinematic storytelling.

✅ **Perfect use cases:**
- Kinetic typography and text animations
- Logo animations and brand intros/outros
- Infographic animations and data visualization
- Presentation slide animations
- Motion graphics for video (lower thirds, title cards, credits)
- App demo animations
- Countdown timers, score boards, data dashboards

❌ **Wrong tool for:**
- Cinematic scenes with characters (use Kling/Sora/Cinema Studio)
- Photorealistic video (use standard video generation)
- Nature/environment footage (use Veo 3)
- Anything requiring actor performance (use Kling + Lipsync)

---

## The Vibe Motion Workflow

### Step 1: Start in Chat
Describe your motion idea in natural language — as if briefing a motion designer.
Upload any assets you want animated: logo, product image, brand photos, PDFs.

**The AI remembers the full conversation** — you can refine iteratively through
follow-up messages without starting over.

```
Example opening prompts:
"Create a kinetic typography title for a short film called Night Crossing.
Letters emerge from darkness. Colors: deep navy and pale silver."

"Animate this logo [upload] with a clean reveal — letters coming in one by one,
finishing with a subtle pulse. Professional, not flashy."

"Build an infographic animation showing three expedition measurements:
42 km traveled, 10 survey sites, 200 m elevation gain. Minimal style, white background."
```

---

### Step 2: Choose a Format or Template
Vibe Motion has templates for common formats — start from one to skip setup:

| Template category | Examples |
|-------------------|---------|
| **Text Animation** | Kinetic typography, quote cards, lyric videos |
| **Infographics** | Stat reveals, bar charts, comparison slides |
| **Posters** | Animated poster with text + image |
| **Brand** | Logo animation, brand intro/outro, bumper |
| **Social** | Story animations, Reels titles, YouTube intros |

**When to use a template:** Always for standard formats. Templates have complex
motion logic already built in — you just replace the content.

**When to start from scratch:** Custom motion systems, unusual layouts, highly
specific brand behavior.

---

### Step 3: Set the Vibe (Color + Energy)

**Color palette presets:** Mosaic · Prism · Candy · Minimal · Dark · Brand (custom)

**Animation Speed slider:** Controls the Physics parameter
- **Slow:** Smooth, luxurious, editorial — good for fashion, premium brand
- **Medium:** Balanced, professional — good for most business content
- **Fast/Sharp:** Energetic, snappy — good for tech, sports, trend content

---

### Step 4: Real-Time Editing Controls

After generation, every element is directly editable:

| Control | What you can change |
|---------|-------------------|
| **Font Family** | Any typeface — click text element to change |
| **Text Color** | Exact color — use hex for brand accuracy |
| **Font Size** | Scale text elements independently |
| **Background Color** | Global or per-element background |
| **Animation Speed** | Global physics slider — dial up or down |

**Iterating with chat:** Any follow-up instruction adjusts the existing animation
without regenerating from scratch:

```
"Make the entrance faster — cut the timing in half"
"Change the headline font to something more geometric"
"The blue is too bright, move it to #1A2B8C"
"Add a subtle particle effect in the background"
"Make it feel more like an Apple keynote"
```

---

## Prompting Patterns for Vibe Motion

### Typography / Text Animation

Structure: `[What text] + [how it enters] + [timing feel] + [style]`

```
"The words 'DAWN. NOON. DUSK.' appear one at a time, each letter
scaling in from small with a sharp snap. Inter font, all caps, white on black.
Each word holds for 0.8 seconds then the next appears. Total: 4 seconds."
```

```
"A single sentence builds word by word from left to right:
'Beyond the hills [pause] the river [pause] turns north.'
Clean sans-serif, navy blue, minimal white background.
Unhurried timing, with each phrase readable before the next arrives."
```

---

### Logo Animation

Structure: `[Logo behavior] + [reveal style] + [hold duration] + [feel]`

```
"The logo [upload] fades in letterform by letterform, left to right.
Once fully revealed, it pulses once subtly — scale up 3%, back down.
Clean, professional. White background. Total: 2.5 seconds."
```

```
"The icon [upload] draws itself on — like a pen tracing the outline —
then the wordmark slides in from the right. Bold, confident, tech brand feel.
Dark background, logo in white."
```

---

### Infographic / Stats Animation

Structure: `[What data] + [reveal animation] + [visual hierarchy] + [style]`

```
"Three statistics animate in sequence:
1. '42 km' — counter counts up from 0, large number, small label 'distance'
2. '75%' — percentage fills like a progress arc, label 'route completed'
3. '200 m' — slides in from right, label 'elevation gain'
White background, blue (#0057FF), minimal, each stat holds 1.5s."
```

```
"Animated bar chart comparing rainfall across four seasons.
Bars grow upward on a staggered reveal, preserving the supplied values.
Clean grid, no clutter. Documentary infographic style."
```

---

### Title Cards and Bumpers

Structure: `[Format] + [content] + [timing] + [style]`

```
"A 9:16 documentary title card.
Title: 'A River Through the City'
Subtext fades in below: 'Chapter One: The Source'
Bottom: 'Dawn, 05:30' with subtle slide-up
Warm gradient background — amber to deep orange. 5 seconds total."
```

```
"YouTube intro bumper — 5 seconds.
Channel name 'SIGNAL' appears with a glitch effect — letters scrambling
before snapping into place. Icon [upload] animates in beside it.
Dark background, neon blue accent. Energetic."
```

---

## Vibe Motion vs Other Higgsfield Tools

| Need | Right tool |
|------|-----------|
| Animated brand logo | Vibe Motion |
| Cinematic scene with actors | Cinema Studio / Kling |
| Talking head with speech | Lipsync Studio |
| Product photo brought to life | I2V (image-to-video) |
| Text-over-video lower third | Vibe Motion (export) + video editor |
| Data visualization that updates | Vibe Motion (code export) |
| Social story with motion text | Vibe Motion |
| Short film scene | Cinema Studio |

---

## Combining Vibe Motion with Video Generation

The real power is combining both:

**Pattern 1: Vibe Motion titles + cinematic video body**
```
1. Generate cinematic scene in Kling 2.6 (the video)
2. Create title card and lower thirds in Vibe Motion
3. Combine in editing workflow (DaVinci, Premiere, CapCut)
```

---

## Technical Notes

**Output:** Video file (.mp4) + Remotion source code
**Max resolution:** 4K
**Text quality:** Pixel-perfect — text is rendered from code, not pixel-predicted
**Aspect ratios:** All standard ratios supported including 9:16, 16:9, 1:1, 4:5
**Editing:** All changes are non-destructive — iterate without starting over
**Code export:** Remotion code can be deployed for data-driven or programmatic use cases
  (auto-generate 10,000 personalized videos from a database, responsive video that
  adapts to different platforms, etc.)

---

## Related skills
- `higgsfield-pipeline` — Vibe Motion as a stage in the full production pipeline
- `higgsfield-cinema` — Cinema Studio for cinematic content (not motion graphics)
- `higgsfield-style` — Visual styles for the video content Vibe Motion overlays
- `higgsfield-apps` — One-click Apps as alternatives for simple motion tasks

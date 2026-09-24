# Higgsfield Audio Prompting Guide

## QUICK FACTS
*Routing aids — read the linked sections for the full rules.*
- Native-joint audio models covered here: Kling 3.0, Seedance 2.0 / 1.5 Pro, Veo 3/3.1, Grok — models without native audio add it in post [→](#which-models-support-audio)
- Four layers to consider per prompt: Dialogue / SFX / Ambient / BGM [→](#the-four-audio-layers)
- Lip-sync reliability: 3–8s is a trial window, not a duration rule; clear mouths and restrained motion help. Speaker count depends on model/mode; per-language sync-word budgets are FIELD-reported [→](#lip-sync-rules)
- **Seedance 2.0 `@Audio1` is a conditioning INPUT** — beat sync, the `[AUDIO: Xs]` script block, and the first-15s extraction trap [→](#audio-as-a-conditioning-input--seedance-20-audio1)
- Scope an audio reference like an image one: name the property that rides, the property that must NOT, and where the excluded one comes from instead [→](#scope-an-audio-reference--say-which-property-rides)
- Multi-clip assembly: one master track · cuts land on musical punctuation, never inside a sung vowel (ECU mouth-match is the one exception) · unified grain + LUT masks batch color drift [→](#cutting-to-music--assembling-separately-generated-clips-on-one-track)
- Cinema Studio 3.0 native joint audio (SCELA): retain its Audio field in native submissions; full video drafts use the eight-section mapping below. Specific foley beats generic moods [→](#cinema-studio-30-audio-businessteam-plan)
- **Seed Audio 1.0** (`seed_audio`, standalone) = whole-scene audio in ONE pass — multi-speaker dialogue + music + SFX + ambience mixed [→](#scene-audio-generation--seed-audio-10)
- Standalone Audio catalog (2026-08-01 snapshot): `seed_audio`, `qwen_audio_tts` (NEW — Qwen 3.0 TTS Flash, expressive instructions + cloned voices), `text2speech_v2` (5 engines incl. cozy_voice), plus 3 game-pipeline-only tools — distinct from in-video joint audio [→](#standalone-audio-tab--tool-catalog-2026-08-01-snapshot)

## Narrative planning for sound and picture

Apply [shared narrative planning](narrative-planning.md) before cue writing,
beat sync, lip-sync, multi-clip assembly, or standalone scene audio. Story events,
causality, reveals, and state transitions decide stages; speech meaning, breaths,
reactions, silence, and musical phrases help locate their boundaries. Estimate durations
after those decisions. Do not preset stage counts, equal-length stages, or cuts on every
beat. A **stage is not a cut or a generation clip**: one take or continuous audio bed may
span stages, and a stage may use several shots or calls within actual model limits.

**Complete video prompts default to the visible eight-section full performance draft**,
including a single take. Follow the root/shared contract and read the
[full performance example](template-full-performance-example.md) and
[director template](template-general-director-2-5.md) before drafting:
**1 资产与参考锁定 → 2 一句话总合成 → 3 全局视听与空间 → 4 主体行为与节奏规则 →
5 分段演出 → 6 连续性 → 7 结尾状态与交接 → 8 关键约束与排除**.

Bind real voice/track references and their purposes in section 1. Establish the global
audio strategy **once in section 3**: the continuous sound bed, allowed layers, mix priorities,
acoustics, and whether a source track is preserved, mixed, or used only as a reference. Section 4 carries delivery
and pacing rules. In section 5, write each event's continuous performance, action/response,
visible result, camera path, and **声音**: exact speaker-attributed dialogue, breath,
reactions, silence, and sound cues at their causes. Put inherited voice, breath, room tone, environmental bed, phrase and action phase in section 6;
each stage records only additions, changes, ducking, masking or removal and explicitly
inherits the rest. The final audible state, decay, and join go in section 7. Section 8
contains only remaining task-specific constraints; do not repeat the global mix policy. Four-layer inventories, reference-role tables, and diagnostics are internal aids,
not extra prompt sections or substitutes for the performed scene.

Explicitly concise requests, local edits, audio-only tasks, and hard-limited/native
submissions keep their relevant inline cues, Audio fields, `[AUDIO: Xs]`, radio-drama,
TTS, voice-change, or translation formats. Compile full video work from the complete
performance draft without forcing a duplicate long draft into a requested native format.
Do not add visual instructions or eight video headings to standalone audio.

Preserve source timestamps and duration in edits, translations, and voice changes except
for an explicitly requested timing edit; match new delivery to the existing windows.
A sole-source audio track keeps its internal timing. For extensions, inherit voice,
acoustics, loudness, phrase/phoneme phase, and any visual pose, motion phase/direction/speed,
framing, and light at the join. Forward starts from the source tail; reverse extension
ends at the **source first-frame and audio state**. Only new material receives a new budget.
Transitions, pauses, and the final hold/decay count within the total. For multiple clips,
distinguish source, final-timeline, and clip-local timestamps; count overlaps/crossfades
once and keep continuous master audio through picture cuts. The Seedance 2.0
15s reference/extraction limit, Cinema Studio's ≤15s combined input limit, and each
other model's actual limits below remain intact; none sets narrative-stage length.

## Which Models Support Audio?

| Model | Audio type | Dialogue | SFX | Ambient | BGM | Lip-sync |
|-------|-----------|----------|-----|---------|-----|----------|
| Kling 3.0 / Omni | Native joint | ✅ | ✅ | ✅ | ✅ | ✅ Multi-language |
| Seedance 2.0 | Native joint | ✅ | ✅ | ✅ | ✅ | ✅ Multi-language |
| Seedance 1.5 Pro | Native joint | ✅ | ✅ | ✅ | ✅ | ✅ Best lip-sync |
| Veo 3 / 3.1 | Native joint | ✅ | ✅ | ✅ | ✅ | ✅ English best |
| Grok Imagine Video | Native joint | ✅ | ✅ | ✅ | ✅ | ✅ |
| Models confirmed to lack native audio in the selected mode | ❌ | — | — | — | — | — |

**"Native joint"** means audio and video are generated simultaneously in one pass —
not layered on after. This produces natural synchronization without post-production.

Models without native audio: add audio in post with Lipsync Studio or external tools.
This table is not exhaustive; an unlisted model is not automatically audio-incapable.
Capabilities and upload limits below apply to the named model, mode, surface, and dated
source. Input formats and output formats are separate; do not generalize one surface's
MP3 restriction to Cinema Studio, Seed Audio, TTS, or other Seedance versions.

---

## The Four Audio Layers

Every audio-capable prompt should consider four layers. You don't need all four
in every prompt, but knowing which to include gives the model clear direction.

### 1. Dialogue — What characters say

Put dialogue in quotes. Be explicit about who speaks, their tone, and language.

```
She says: "We need to leave. Now."
He whispers: "Not yet."
```

**Best practices:**
- Keep dialogue focused — 1–2 sentences per character per shot is a short-shot example;
  preserve complete meaning and approved lines, then budget delivery and reaction time
- Specify emotional tone: "says urgently", "whispers", "shouts across the room"
- For non-English: specify language and dialect → `She speaks in Cantonese: "走啦"`
- For Seedance 1.5 Pro: supports English, Chinese (incl. Sichuanese, Cantonese,
  Taiwanese Mandarin, Shanghainese), Japanese, Korean, Spanish, Indonesian

### 2. SFX — Specific sound events tied to action

Describe SFX at the point they happen. Tie them to visible actions.

```
The glass shatters on the floor — sharp crack, then settling tinkle.
Footsteps on wet concrete — splashing, rhythmic.
A door slams shut — heavy metal, echoing.
```

**Best practices:**
- Tie SFX to the action that causes them; one concise description per beat is a clarity
  heuristic, not a quota or a requirement to add sound to every stage
- Use onomatopoeia sparingly — descriptive phrases work better than "BANG" or "CRASH"
- Tie timing to action: "as she sets the cup down"; retain source timestamps or native
  `[AUDIO: Xs]` markers when timing is specified, alongside the causal cue

### 3. Ambient — Background soundscape

Set the acoustic environment. This is the continuous sound bed.

```
Ambient: quiet café murmur, espresso machine, rain against windows.
Ambient: forest at night — crickets, distant owl, gentle wind through leaves.
Ambient: busy intersection — traffic, horns, construction in the distance.
```

**Best practices:**
- Start with a few distinct ambient elements (for example 2–3); prioritize intelligibility
  rather than treating the count as a limit or adding sound to fill a quota
- Describe the *space* acoustics: "reverberant church hall", "tight car interior"
- Contrast silence with sound for impact: "Dead silence. Then — a single footstep."

### 4. BGM — Background music mood

Don't name songs or artists (content filter). Describe the musical texture.

```
BGM: slow piano, minor key, melancholic.
BGM: tense orchestral build — low strings, rising.
BGM: lo-fi hip-hop beat, warm vinyl crackle, relaxed.
```

**Best practices:**
- Describe instrumentation, tempo, mood — not genre labels alone
- "Tense strings, building" works better than "suspenseful music"
- Specify when music enters/exits: "Piano enters at the midpoint, builds to the end"
- For beat-sync content: "Cuts match the downbeat" or "Movement peaks on the drop"

### Suppressing music — `NO BGM` is a spec, `no music` is a preference

`[DEMO — Joey cinema-director-v3, 2026-08-16]` `[UNPROVEN HERE]` When a piece must
carry no score, the phrase matters. **`no music` reads as a weak stylistic preference**
and loses to the model's strong prior that generated video wants a bed under it.
**`NO BGM` reads as a production term** — a hard spec — and is the form to write.
Expand it once on first use so the abbreviation is unambiguous, then let it carry.

**Lead positive, then negate.** Name what the audio *is* before naming what it is not —
diegetic sources tied to surfaces and materials, plus room tone. A suppression clause
with nothing positive in it leaves the model to decide what "silence" sounds like, and
it decides in favour of a pad.

```
Audio: diegetic sound only — footsteps on wet stone, fabric shift, breath, room tone.
NO BGM — no background music.
```

**In a full video draft, state the no-score policy once in section 3.** Section 5
then describes only the permitted sound events; do not repeat the policy in a header or
closing block. `NO BGM` excludes score, not all sound. For a requested native short prompt,
place the policy in its audio field. This is demo wording, not a universal guarantee;
use positive source/mix wording where the selected mode requires it.

> **Enumerate with care — this cuts against the house rule on negation.**
> `negative-constraints.md` and the repo's staging-reference doctrine both
> hold that **naming a thing under a negation ships the token anyway** and can prime
> the very output you are refusing. The source's long list (score, soundtrack,
> instrumental, underscore, ambient pad, drone, tone bed, swell, sting, humming,
> whistling, lyrics) is its answer to a real failure — a bare negation lets the model
> supply an "ambient texture" and consider the instruction honoured — but it is one
> practitioner's fix and is **not measured here**. Default to the short form above;
> reach for the full enumeration only when a short form has already failed on the
> shot in front of you, and expect the enumeration itself to carry some priming risk.

**Discriminate reference purposes before applying an attached-track lock.** An attachment
alone does not make its sound the output. Classify each audio/video reference as preserved
original soundtrack, visual rhythm driver, performance-property reference, or voice identity
reference. State whether it is audible and which generated layers are allowed. A video
used only for camera/visual reference does not donate its soundtrack. A reference may have
explicitly compatible roles; an audible music layer plus new dialogue is a mix, not a
sole-source lock.

**Attached-track lock applies only when the task designates that track as the sole and
complete soundtrack.** Preserve its internal timing; do not impose new per-beat speech
windows on the lip-sync take. For this mode only:

```
AUDIO: the attached clip @Video1 is the sole and complete soundtrack for this
sequence, preserved with all existing speech, music, and sounds at their original
times. Generate no additional audio.
```

**The unheard-track technique** lets bodies perform to music that is not in the mix —
useful when the score is added in post: state that the track is inaudible, then describe
the performance against it (*"singing roughly in time to the unheard 87 BPM beat"*),
plus the diegetic layer that IS heard.

---

## Audio Prompt Structure

For a complete video prompt, use the eight-section mapping above: global strategy in
section 3, performed dialogue and sound events in section 5, continuity in section 6,
and the tail/join in section 7. Do not append a ninth Audio section. The compact forms
below are for requested short/local audio work or native submission fields.

### Inline method (preferred for short prompts):

```
A woman walks into a quiet library. Her heels click on the marble floor — each step
echoing. She whispers to the librarian: "Do you have the Collected Letters?"
Distant page turns. A clock ticks somewhere above.
```

### Dedicated block method (better for complex audio):

```
[Scene description — visual content, action, camera]

Audio:
  Dialogue: She says "We leave at dawn." He replies: "I'll be ready."
  SFX: coffee cup set down, chair scraping back
  Ambient: early morning kitchen — birds outside, kettle just boiled
  BGM: none — silence emphasizes the tension
```

---

## Lip-Sync Rules

Lip-sync is the most failure-prone audio feature. The framing and short-window practices
below are reliability heuristics, not stage-length rules or model duration limits.
Preserve source speech and complete phrases; use shorter generated coverage only when it
can join cleanly without truncating or retiming the line:

> **Expressive facial acting *around* the words** — forced smiles, leaking fear,
> mixed emotions during a spoken line — is driven separately by FACS Action Unit
> codes per beat. Let lip-sync shape the phonemes; schedule the brow/eye/cheek
> AUs for the performance. See `higgsfield-facs.md` § Dialogue &
> Monologue Facial Acting.

### Do:
- 3–8 seconds is an empirical accuracy sweet spot for a dialogue take, not a required
  segment length; let the actual utterance and reaction determine the window
- Use medium close-up or closer framing — model needs to see the mouth clearly
- For single-face modes or unreliable speaker routing, isolate one speaking face;
  supported multi-speaker modes use explicit speaker attribution instead
- A `locked-off static camera` or `slow Dolly In` is a useful reliability baseline;
  retain other camera work when the selected mode and performance support it
- Reduce competing head-motion cues such as `nodding` or `turning head` during speech
  if they cause desync; retain motivated eye/brow/cheek reactions and listener behavior

### Don't:
- Don't combine dialogue with vigorous head movement in the same prompt
- A 15s Seedance 2.0 dialogue take can have weaker sync than a shorter take; test the
  needed performance rather than automatically splitting at 8s. Other models keep their
  own duration limits
- For a sole-source speech recording, omit requests for additional generated audio.
  For native dialogue with SFX/ambience/music, prioritize intelligibility and simplify
  competing layers only as needed; their presence is not a universal lip-sync prohibition
- The source guide reports non-MP3 failures on its Seedance 2.0 upload path; see the
  scoped format note under § Seedance 2.0, not a format ban for every model/surface

### Multi-character dialogue workaround:
Speaker routing depends on model and mode. The Kling 3.0 / Omni path below supports
3+ characters with attribution and Voice Binding; the documented Cinema Studio 3.0
experimental lip-sync path is single-face. Seed Audio supports multiple audible speakers
without generating mouths. Do not turn one path's limitation into an all-model ban.
If the selected video mode lacks multi-speaker lip-sync or the take fails attribution:
1. Generate each character separately with their own audio segment
2. Composite in CapCut/Premiere using picture-in-picture + linear mask (15% feather)
3. Use generated listener reactions when needed; a static listener plate is an optional
   compositing shortcut only when the performance calls for stillness

### Per-language dialogue-sync budgets [FIELD — community, seedance-2.0 repo v6.6.0]

Field-observed word budgets for **reliable lip-sync** in a ~15s in-video Seedance
dialogue clip — not official limits, and not the same as how many words the model
can *voice*. The **acoustic budget ≠ reliable-sync budget**: the model will happily
speak more words than it can keep synced to the mouth.

| Language | Reliable-sync budget (~15s clip) | Notes |
|----------|----------------------------------|-------|
| English | ~16–20 words (5–10 per line) | Strongest Western language |
| Mandarin | — | Strongest sync overall |
| Russian | ~10–15 words | Weak — budget conservatively |
| Japanese / Korean | Under-tested | No reliable field numbers yet |

Cross-language sizing unit: **"one short sentence ≈ one breath."** Write dialogue
in breath-sized sentences and count breaths, not seconds.

### Voice-reference lip-sync path [FIELD — community, seedance-2.0 repo v6.6.0]

On surfaces that accept a spoken-voice reference, an attached **rights-cleared
voice recording drives lip-sync directly** — the model syncs the mouth to your
recording instead of synthesizing a voice first. This is the most reliable
field-reported path for **non-English dialogue** (it sidesteps the weak-language
sync budgets above). **Rights-sensitive:** only use recordings you have clear
rights to; unauthorized cloned or scraped recordings are excluded. Supported,
authorized cloned voices remain available through the standalone TTS paths below.

---

## Audio as a Conditioning Input — Seedance 2.0 (`@Audio1`)

The most under-used Seedance 2.0 capability: an uploaded audio file is a
**conditioning input**, not just an output track. The model spec lists `audio`
as a reference media role alongside `image` / `video`, and `generate_audio`
(native sound output) is documented as *independent of the audio reference
medias* — i.e. the uploaded file conditions the **generation**, and whether the
clip also gets generated sound is a separate switch.

This means `@Audio1` has **three distinct uses** below. Declare its purpose and audible
output policy first; combine compatible uses only explicitly. Voice identity can also be
scoped separately (§ Voice-reference lip-sync and § Scope an audio reference).

| Use | What `@Audio1` does | Prompt discipline |
|-----|---------------------|-------------------|
| **Audio-as-output** | Requests the uploaded track unmodified as the clip's soundtrack | Timestamp-anchor it (`plays exactly as uploaded from 0s to end`). For a **sole-source** soundtrack, remove requests for extra generated layers. For an intended mix, name the preserved layer and allowed additions; exact preservation may require post assembly. |
| **Audio-as-driver (beat sync)** | Drives the **visuals** — cut timing, camera acceleration, action pace, energy peaks | Write the audio→visual mapping explicitly (below). The clip can still get generated sound, or set `generate_audio` false for visuals-only. |
| **Audio-as-performance** | The character on screen **performs** the track — hums, sings, plays along, moves to it — hitting the actual notes | Scope it to the one property you want (§ Scope an audio reference, below). Unscoped, it also lends its voice. |

> **Why it works (author's model — empirical, not in the official spec):** the
> temporal branch that reasons about motion and pacing reads the sound's
> structure — beat positions, dynamic contour, timbral texture, song-structure
> sections — and maps it to visual rhythm. Treat the mechanism as a working
> model; treat the capability (audio reference role) as confirmed.

### Scope an audio reference — say which property rides

Every *image* reference in this stack is scoped in both directions: what it
locks, and what must be read past ("ignore the sheet's grey background", "not
its camera vantage"). **Audio references have had no equivalent vocabulary, and
they need one for the same reason** — a sound file carries several properties
at once, and an unscoped reference lends all of them.

The case that shows it [DEMO — Higgsfield "AI Love Stories" tutorial, 2026-08]:
a character had to hum a specific tune on camera. Without a reference the model
**invented a different melody every take** — the reported result of the
no-reference control was a performance that was off-key with no rhythm. With a
voice memo of the tune attached, it hit the notes on the first take.

But the memo was somebody else's voice, and the character has his own. So the
reference was **scoped in prose**:

```
@Audio1 is the reference for the HUMMED LINE only. Take from it ONLY the
melody: the exact notes, pitches and intervals, the tempo, the phrasing and
the rhythmic pause — note for note, beat for beat, nothing improvised. Do NOT
copy the voice, timbre or vocal identity heard in the recording — he hums in
his OWN natural speaking voice, the same voice he speaks his lines with. All
spoken dialogue is performed as scripted below, not taken from any audio.
```

**The pattern, generalised — three parts, and the third is the one that gets
skipped:**

1. **Name the property that rides**, as narrowly as you can: notes, pitches and
   intervals; tempo and phrasing; the rhythmic pause. Not "the song".
2. **Name what must NOT ride**, explicitly: voice, timbre, vocal identity.
   Sound files carry a performer as well as a performance.
3. **Say where the excluded property comes from instead** — "his own natural
   speaking voice, the same one he speaks his lines with". A reference that is
   only told what not to do leaves the model to pick, and it will pick the
   reference.

The same three-part shape works for other audio properties:

| Riding | Excluded | Sourced instead from |
|---|---|---|
| melody, tempo, phrasing | voice, timbre, identity | the character's own speaking voice |
| rhythm and accent pattern | instrumentation, key | the scene's own diegetic sound |
| emotional contour, dynamics | the words | the scripted dialogue |

**Scope note.** Whether a reference track becomes the spoken output differs by
model line — see § Audio by Model. The scoping vocabulary above is about which
*property* transfers, and is written to be read alongside whatever that line
does with an attached track, not instead of it.

**Rights:** the memo above was recorded by the person for this purpose. Same
constraint as the voice-reference lip-sync path — use recordings you have clear
rights to.

[UNPROVEN HERE] — one production, one property (melody). The *mechanism* is
already confirmed (audio is a reference media role); what is unproven here is
how far prose scoping steers it. Cheap to test on any tune you own.

### Beat sync — the audio choreographs the visuals

Upload an MP3 as `@Audio1`, then map audio characteristics to visual elements.
Cover **rhythm source / which visual responds / how energy maps to the arc**.
The three-sentence form below is an example, not a minimum sentence or stage count:

```
Use @Audio1 as the rhythmic foundation. Sync camera transitions to the beat
positions. Visual energy builds with the audio crescendo and peaks at the drop.
```

You can assign **different visual elements to different audio characteristics** —
mixing audio-to-visual the way you'd mix a track:

```
@Audio1 drives the visual rhythm. Camera cuts land on the downbeats. Subject
movement accelerates into the build, holds at the peak, releases on the drop.
Colour temperature shifts warmer with the crescendo.
```

Camera ← beat position. Movement ← dynamic contour. Colour ← overall energy arc.
These mappings apply to requested beat-driven work. Select musically meaningful cues
that support the story; a beat need not trigger a cut, and a phrase need not equal a stage.
Preserve an attached performance's timing instead of forcing it into equal time ranges.

It **stacks with other references** — character from `@Image1`, camera style from
`@Video1`, rhythm from `@Audio1`, processed together:

```
@Image1 as character reference. Follow @Video1 camera-movement style. @Audio1 as
rhythmic foundation — sync all camera transitions to the beat positions.
Character movement should pulse with the music.
```

**The one constraint:** `@Video1` camera style and `@Audio1` rhythm have to be
**temporally compatible**. A slow continuous dolly pulled from a video reference
fighting an EDM track sends the temporal branch conflicting instructions — same
failure class as mixing reference *images* of clashing styles. Pick references
that can coexist. (Sibling of `higgsfield-seedance.md` § Reference Roles
→ Load-Bearing Rule: references stay in their lanes.)

### Cutting to music — assembling separately-generated clips on one track

For non-musical scenes the same continuity rule applies to ambience and effects: carry
ongoing sound sources through the next shot and write only what changes at the cut. If a
source moves, is muffled by a door, passes behind an obstacle, ducks under dialogue, or
stops, describe that audible transition and its visual cause.

`[EMPIRICAL — MiniMax H3 skill corpus, re-derived; cross-model editing craft]`
Beat sync governs what happens *inside* a clip; these three laws govern the
timeline the clips land on:

- **One continuous master sound bed.** Keep a stable ambience, room tone, weather bed,
  ongoing source or music across picture cuts; never restart or replace the complete
  sound list at every shot. A new shot inherits the previous bed unless a motivated
  transition is written.
- **One master track for music.** The piece binds to a single continuous music track laid
  in post — never per-clip audio stitched end to end. A join in the music is
  audible before a join in the picture is visible.
- **Cuts land on musical punctuation** — a breath, a lyric pause, a snare, the
  drop. Never hard-cut inside a sung vowel unless the incoming shot is an ECU
  whose mouth shape continues that vowel: lip continuity is an *edit*
  constraint, not only a prompt constraint.
- **Mask batch color drift on purpose.** Clips generated in separate runs never
  match grade exactly. One unified fine-grain pass plus one LUT across the whole
  timeline, applied as a deliberate finishing step, hides the inter-clip color
  variance that would otherwise read as a continuity error.

### The `[AUDIO: Xs]` script block — dialogue + SFX + lip-sync from text alone

No microphone, no recording. A timestamped script **inside the prompt text**
generates voices, SFX, and lip-sync. Quoted text → speech with automatic
lip-sync; physical descriptions → sound effects. Each marker is a timestamp in
the clip:

```
[AUDIO: 0s] heavy footsteps on concrete, echoing in a corridor
[AUDIO: 2s] door bursting open, impact bang
[AUDIO: 3s] character says "Nobody move"
[AUDIO: 5s] tense silence, distant traffic
[AUDIO: 7s] character says "Put it down. Slowly."
[AUDIO: 9s] object placed on table, soft thud
```

The model generates the **voice first**, then maps facial movement to the
waveform — so lip-sync quality is mostly set by how precisely you wrote the
dialogue. **Exact quoted text outperforms paraphrase.** It works across
languages (write the line in Spanish/Japanese/French → speech with
phoneme-level lip-sync in that language).

This obeys the same physical rules as § Lip-Sync Rules above: a strong `@Image1`
character reference gives a consistent mouth structure to animate, and **close-up
framing beats wide** (a small face has too few pixels to sync). The 3–8s accuracy window is a useful testing example for individual dialogue takes;
it must not truncate a sentence or override source timing.

It **combines with beat sync** in one generation when the selected mode supports the
intended mix — uploaded music as the rhythmic foundation and an audible background layer,
the script block as new foreground dialogue/SFX. This is not a sole-source track lock.
Keep exact original-track preservation in post if the generation alters it. Example:

```
@Audio1 as background music. Sync camera transitions to the beats.
[AUDIO: 0s] music from @Audio1 begins
[AUDIO: 3s] character says "This changes everything"
[AUDIO: 5s] sharp breath — beat drop hits simultaneously
[AUDIO: 8s] character says "Let's go"
```

### The 15-second extraction problem — pick the window, don't upload the track

For **Seedance 2.0**, the audio reference limit is **15s, and the model takes the first 15s** of
whatever you upload. Drop in a full 3-minute track and you almost always feed it
the **intro** — low energy, often ambient, no rhythmic drive. Nothing for the
temporal branch to map.

For a requested rising-energy beat-sync sequence, a **build → drop** window is one
useful example: its dynamic gradient can drive visual energy. It is not a mandatory arc
or a required 15s stage. A steady groove, sustained ambience, silence, or a complete
spoken phrase may serve the actual narrative better. Select the relevant window within
the input limit without chopping meaning or inventing a crescendo.

Example build/drop window locations:

- Pre-chorus into chorus
- Instrumental build into the drop (EDM, electronic, hip-hop)
- Verse climax into a bridge
- The last 15s of an intro that breaks into the first hook

**Extract exactly that segment before uploading.** The source workflow recommends MP3
at **≥256kbps** for beat detection; this is a quality recommendation for that path, not
a universal accepted-format or minimum-bitrate requirement. Don't upload the full track and hope; pick the
window, cut it, upload that. (Flipping the workflow — audio in first, visuals
built around it — changes the output at a structural level, not subtly.)

---

## Audio by Model — What Works Best Where

### Kling 3.0 (V3) / 3.0 Omni (O3)
- Best overall audio-visual integration
- Multi-language dialogue (English, Chinese, Japanese, Korean, Spanish + regional accents: American English, British English, Indian English)
- Multi-character dialogue: 3+ characters with correct speaker attribution and lip-sync per character
- Voice Binding: lock specific voice profiles to specific characters across shots
- O3 adds Voice Extraction from static images: upload audio clip (min 3s) + image to build a voice profile
- O3 adds Performance Cloning: act out a scene on camera → AI re-renders preserving likeness and voice
- Include dialogue, ambient, and SFX naturally in the prompt
- Prompt like a script: action + camera + mood + dialogue cues together

**Audio Speaker Attribution Format (V3/O3):**
```
[Speaker: Character Name] "dialogue" in a [warm/confident/excited] [male/female] voice with [accent].
Add [sound: footsteps / rain / door closing] when [action].
Background ambient: [environment description].
```

### Seedance 1.5 Pro
- Best lip-sync accuracy of all models
- Class-leading multilingual support including Chinese dialects
- Most stable emotional tone control
- Use for: professional dialogue scenes, multilingual content

### Seedance 2.0
- Upload MP3 audio as @Audio reference (part of Rule of 12)
- **Source-workflow format report:** the original audio guide describes its Seedance 2.0
  upload path as MP3-only and reports silent WAV/AAC/OGG/FLAC failures. Its precise surface
  is not identified; this is not a verified restriction for every Seedance 2.0 API/UI.
  Use the selected surface's supported input formats; MP3 is the source workflow's fallback.
- Source-workflow limits: max 15s per clip, 3 audio files, 10MB each;
  **≥256kbps** is its beat-sync quality recommendation
- **Measured enforcement bounds** `[EMPIRICAL — third-party, China Ark lane, 2026-08]`:
  per-clip duration is enforced at **1.8–15.2s**, and the **total across all attached
  clips is also capped at ≤15.2s** — three individually-legal 6s clips get rejected
  (captured 400 errors). Measured on the China Ark lane by a third party; Higgsfield's
  own proxy enforcement is **unverified** — if a multi-clip attach fails, this total
  cap is the first suspect.
- Timestamp anchoring (audio-as-output): `"Audio @Audio1 plays exactly as uploaded from 0s to end. Do not modify."`
  For a sole-source soundtrack, remove requests for additional generated dialogue,
  ambient/SFX/music. Visual-driver, performance-reference, and intentional-mix uses retain
  their explicitly allowed sound layers.
- **`@Audio1` is also a visual driver** — beat sync, the `[AUDIO: Xs]` script block,
  and the first-15s extraction trap are all in § Audio as a Conditioning Input above.

> **Diegetic-only is an optional mix policy**, useful when the score will be added
> in post or a generated music bed has interfered with dialogue. In that workflow,
> describe physical sources such as footsteps, fabric, breath, room tone, weather,
> and crowd reaction. It does not override requested native BGM, singing, musical
> performance, beat-sync conditioning, or an intentional reference-plus-dialogue mix.
> A sole-source track lock permits only the attached soundtrack; diegetic-only
> generation permits new scene sounds. Choose the policy by purpose, and state it
> once in section 3 of a full draft.

### Veo 3 / 3.1
- Strong native audio for English dialogue and environmental sounds
- Dialogue in quotes: `"This must be it," he murmured.`
- SFX explicitly: `tires screeching loudly`
- Ambient as environment soundscape descriptions

### Grok Imagine Video
- Improved audio as of Video Imagine 1.0 (Feb 2026)
- Include audio intent directly in prompt — same inline style as other models
- Best for: social clips where audio adds polish but isn't the hero

---

## Common Audio Failures and Fixes

| Problem | Cause | Fix |
|---------|-------|-----|
| Lip-sync completely off | Long/complex delivery or head motion competes with sync | Remove nodding/turning tokens; test a complete shorter phrase if appropriate, preserving source timing and approved dialogue |
| Model replaces a track meant to be preserved | Generated layers may conflict with the intended source lock | Confirm reference purpose; timestamp-anchor the original. Remove added-layer requests only for sole-source output; preserve exact tracks in post if needed |
| Dialogue missing entirely | Possible unsupported upload format on the source guide's Seedance 2.0 path, or output/routing settings | Check the selected surface's accepted inputs and audio settings; try MP3 128–320kbps on that reported path |
| SFX drowns out dialogue | Competing sound cues or mix levels | Lower or simplify competing SFX and prioritize dialogue; no fixed SFX quota |
| Audio sounds robotic | Flat emotional cues | Add emotional direction: "says warmly", "whispers with urgency" |
| Background music too loud | Mix priority unclear | Set dialogue-over-music priority and lower BGM in section 3 (or the native Audio field); describe local level changes at their events |

---

## When to Skip Audio

Not every prompt needs audio direction. Skip audio cues when:
- Using a model without native audio (Kling 2.6, Wan 2.6, Seedance Pro, Minimax Hailuo 2.3/02)
- The content is purely visual (product beauty shots, abstract motion, landscape)
- Audio will be added entirely in post-production; retain visual rhythm/performance
  conditioning and timing cues when the picture still depends on that audio
- In an explicitly short-form submission, optional sound cues may yield to essential visual
  direction; the 200-word soft cap does not remove required audio or shorten a full draft

---

> **Negative constraints:** For audio-specific artifacts (lip-sync desync, background music
> overriding dialogue, SFX drowning dialogue) and their prevention phrases, see
> `negative-constraints.md` — Temporal/Consistency Artifacts section.
> Apply its audio rows within the scopes established here: 3–8s is a reliability trial,
> MP3 failures are a source-path report, and removing extra layers serves sole-source
> preservation. Those rows do not override reference purposes, approved timing, native
> multi-speaker support, or the full eight-section delivery.

---

## Cinema Studio 3.0 Audio (Business/Team Plan)

Cinema Studio 3.0 introduces native audio-video joint generation — a fundamental shift from models that treat audio as a post-processing step.

### Native Audio-Video Joint Generation

Audio is generated **simultaneously** with video via a unified multimodal architecture. This means:
- Audio and video are temporally aligned by default — no manual sync needed
- Dual-channel stereo output
- Sound design prompts directly influence both audio AND visual generation
- Audio is not "added on" — it's part of the same generation pass

### Audio as Prompt Element (SCELA)

For a **native Cinema Studio SCELA submission**, keep the separate Audio field/block.
For a full eight-section video draft, map global audio to section 3 and local cues to
section 5, with continuity in 6 and the tail in 7; do not add another top-level section.
The generation engine handles three parallel audio tracks:

1. **BGM** — background music, score
2. **Ambient SFX** — environmental sounds, foley
3. **Dialogue** — character speech, voiceover

```
A chef slices vegetables rapidly on a wooden cutting board.
Camera: tight close-up tracking the knife.
Style: warm kitchen lighting, shallow depth of field.

Audio: rhythmic chopping on wood, oil sizzling in a nearby pan,
soft clinking of ceramic bowls. Light acoustic guitar BGM.
```

### Input Constraints

These are the source guide's **Cinema Studio 3.0** input limits, not universal audio
restrictions or Seed Audio output-format settings.

| Parameter | Limit |
|-----------|-------|
| Accepted formats | MP3, WAV |
| Max audio clips | 3 per generation |
| Combined duration | ≤15s total |
| Single file size | <15MB |
| MP3 bitrate | 128–320 kbps |

### Lip-Sync

Available but experimental in Cinema Studio 3.0:
- Focus on **emotion and general mouth movement**, not perfect phoneme sync
- **Single face per generation only on this documented experimental path** — do not
  carry this restriction over to Kling 3.0 / Omni multi-speaker modes
- Under 8 seconds is a reliability trial for this path; preserve complete delivery and
  source windows rather than making it a mandatory stage length
- Pair with clear frontal or 3/4 face angle reference images

### Tone / Voice Cloning via @Reference

Control speaking style, accent, and language by referencing a video with the desired voice:

```
Use @Video1 only as a reference for the narrator's speaking style and accent.
Generate the scripted line in a warm, conversational tone: "This changes everything."
```

### Dialect Support

Dialects written directly in the prompt work — the model understands regional speech patterns. Write dialogue in the target dialect for authentic delivery.

### Timestamp Anchoring

For a preserved original track designated as the **sole soundtrack**, use this alternative
to generated speech/voice-style transfer:

```
Audio @Audio1 plays exactly as uploaded from 0s to end.
Do not modify or replace the audio content.
```

For this sole-source mode, remove requests for additional generated speech, ambient,
SFX, or music. A voice-style or performance reference alone does not trigger that lock;
an intended mix must identify both the preserved layer and allowed additions.

### Sound Design Specificity

Describe **specific foley**, not generic moods:

**Wrong:** `nice ambient sounds, pleasant background noise`

**Right:** `the scratch of frosted glass, rustling of plush fabric, gentle tapping on acrylic, popping of bubble wrap, wooden floor creaking under bare feet`

Specific sound descriptions directly influence the generated audio output. The more precise the foley description, the more accurate the result.

---

## Scene-Audio Generation — Seed Audio 1.0

Separate from in-video joint audio above: **Seed Audio 1.0** (ByteDance, released
2026-06-23 at the FORCE conference) is a standalone **one-pass whole-scene audio
generator**. One generation produces multi-speaker dialogue + music + SFX +
ambience, already mixed — a radio-drama scene, not a single voice track. Use it
to build a soundtrack for footage you'll assemble in post, or scene audio that
has no video at all.

### When to choose it — decision table

| You need | Use | Why |
|----------|-----|-----|
| A whole scene's soundtrack: several speakers + music + SFX + ambience, mixed in one pass | **Seed Audio 1.0** (`seed_audio`) | One-pass scene audio; script-style prompt drives the whole mix |
| One clean voice track (narration, single-speaker VO) | **`text2speech_v2`** (pick an engine) | Single-voice TTS — simpler, engine-selectable |
| Sound baked into the generated video, synced to on-screen action and lips | **Seedance `generate_audio`** (in-video) | Native joint generation — audio and visuals in the same pass (see § Audio as a Conditioning Input) |

### Verified surface [OFFICIAL — model spec 2026-08-01]

Model id `seed_audio` (output_type `audio`). Parameters:

| Param | Range / options | Default |
|-------|-----------------|---------|
| `format` | wav / mp3 / pcm / ogg_opus | wav |
| `sample_rate` | 8000–48000 Hz | 24000 |
| `speech_rate` | −50..100 | 0 |
| `loudness_rate` | −50..100 | 0 |
| `pitch_rate` | −12..+12 | 0 |
| `voice_type` + `voice_id` | preset \| element — **must travel together** | none |

Media roles: `image_references` + `audio_references`. Per the fal schema: up to
**3 reference audio clips** (each ≤30s, ≤10MB) **XOR one image reference** —
image and audio refs cannot combine. Reference audio inputs in the prompt by
load order: `@Audio1`, `@Audio2`, `@Audio3`.

### Script-format prompting [EMPIRICAL — community guides, NOT official docs]

Everything in this subsection is community-converged practice, not spec — treat
as a starting point, not a guarantee. Write the prompt as a **radio-drama
script**:

- Open with a scene header: `[Scene: busy coffee shop, morning]`
- Speaker labels with emotion parentheticals: `Host (warm, upbeat): "…"`
- Inline sound cues where they happen: `[sound: espresso machine, soft jazz fades in]`
- Music by **mood, not genre**: "soft piano builds to triumphant orchestra", not "cinematic score"
- **~4 distinct speakers** is a community-reported reliability guideline for Seed Audio,
  not a schema limit or a ceiling for other multi-speaker models
- **Test a representative scene segment** before scaling toward the ~2-minute cap;
  20s is a trial example, not a stage size or an assembly rule
- Output **WAV** (`format: wav`) when the audio is headed for post

Use the shared event/state plan to place speech, responses, pauses, and sound changes;
retain this radio-drama format. For audio-only work, the final audible state replaces the
final-frame description. Complete phrases and mix continuity determine joins, not equal
chunks or the number of speaker labels.

Compact worked example:

```
[Scene: rain-soaked night market, closing time]
Vendor (tired, warm): "Last skewers — half price, take them."
Girl (excited): "Two! No — three!"
[sound: rain drumming on tarp canopy, a scooter passing in the distance]
Vendor (chuckling): "Three it is. Careful, they're hot."
[sound: coins dropped on a metal tray, charcoal hiss]
Music: a lonely muted trumpet fades in under the rain, wistful but hopeful.
```

---

## Standalone Audio tab — tool catalog (2026-08-01 snapshot)

The live standalone-audio catalog, reconciled against the models_explore
snapshot of **2026-08-01** (parameter data: `audio-model-specs.json`;
table: `AUDIO-MODEL-SPECS.md`, machine twin
`audio-model-specs.json`; verify against a current schema before production).
The Audio tab's UI tools — **Voiceover** (text → speech), **Change Voice** (swap a
voice in any video), **Translation** (translate speech in any video) — sit on top
of these models:

| Model id | Name | What it does | Availability |
|----------|------|--------------|--------------|
| `seed_audio` | Seed Audio 1.0 (ByteDance) | One-pass whole-scene audio: dialogue + music + SFX + ambience (§ above) | General |
| `qwen_audio_tts` | Qwen Audio 3.0 TTS Flash (Alibaba) | Expressive TTS: natural-language `instruction` for emotion/dialect/speed, preset or cloned reference-element voices, 13 language hints | General *(NEW 2026-08-01)* |
| `text2speech_v2` | Text to Speech V2 | Single-voice TTS; engine via `variant`: `elevenlabs`, `minimax`, `seed_speech`, `vibe_voice`, **`cozy_voice`** *(NEW)*; preset or reference-element voices (`voice_type` + `voice_id`) | General |
| `sonilo_music` | Sonilo Music (FAL) | Text-to-music with controllable duration | **Game pipeline only** |
| `mirelo_text_to_audio` | Mirelo Text to Audio (FAL) | Text-to-audio SFX with controllable duration | **Game pipeline only** |
| `inworld_text_to_speech` | Inworld TTS (FAL) | Preset-voice TTS, ~110 voices across en/zh/ja/ko/es/fr/de/ru/… | **Game pipeline only** |

Engine picks within `text2speech_v2`: **seed_speech** when the deliverable is
multilingual voiceover/narration; **elevenlabs** (Eleven v3) when fine
emotional/tone control matters; **vibe_voice** for long-form narration. These
are standalone audio generators — distinct from the native joint audio baked
into Kling 3.0 / Seedance 2.0 / Veo during video generation. (Catalog reflects
the 2026-08-01 snapshot; verify live before quoting pricing or availability.)

### Post-generation voice-over — Supercomputer workflow [DEMO]

A post-generation alternative to prompting audio at all: upload the **finished
clip** to Supercomputer and ask for an analyzed voice-over (e.g. "Analyze the
video and create a voiceover for it in the style of wildlife documentaries") —
the agent analyzes the footage, writes a script, and offers voices to pick from.
Shown working in Higgsfield's Seedance-4K tutorial; useful when the visuals are
already locked and only narration is missing.

---

## Related skills
- `higgsfield-seedance-vfx` — Footage transforms whose payoff is a camera move synced to a spoken line (crash-zoom / push-in), or preserving the source talk track through a transform (`SFX and source dialogue only`); see `higgsfield-seedance-vfx-dialogue-timing.md`
- `higgsfield-models` — Which models support native audio
- `higgsfield-troubleshoot` — Audio failure diagnosis
- `higgsfield-cinema` — Cinema Studio audio workflow with Kling 3.0
- `higgsfield-vibe-motion` — Motion graphics with audio (different from AI-generated audio)

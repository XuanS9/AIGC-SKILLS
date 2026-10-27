# Higgsfield Acting Director

For video work, [shared director planning](narrative-planning.md) governs full format and overrides local creative defaults: objective/tactic/information changes create performance stages; decide their duration after identifying the behavior and response. Preserve complete listening and reaction arcs, then hand their start/end states to the shotlist, camera, audio and model modules. A performance beat need not create a cut or a new generation.

`[OFFICIAL — Higgsfield "Hell Grind" open-source brief]` — the performance system behind
Higgsfield's 95-minute AI feature film, adapted to this repo's prompt surfaces.

**The core axiom of the entire system: acting is BEHAVIOR under pressure, not a display of
emotion.** A character wants something, something is in the way, and they act to get it.
Emotion is a byproduct of that struggle — never the thing you write directly.

This is the performance craft layer for the studio. In full video prompts, compile it into
【具体情节】 and necessary continuity in 【全局补充】; do not add a PERFORMANCE / CHARACTER ACTING
heading. Native platform fields apply only when that output is explicitly selected.
Identity assets, camera, lighting and grade retain their own responsibilities.

## QUICK FACTS
- Write the **objective** (a verb aimed at a partner), never the state — "make him confess", never "be angry" [→](#the-five-pillars-of-every-scene)
- **Event-driven beat changes**, visible in pause, posture, tempo or gaze; 2–4 is a useful scene example, not a required count. Sustained behavior can be intentional when the objective calls for it [→](#the-five-pillars-of-every-scene)
- **Listening beats speaking.** Reactions start when information registers, often mid-line; assessment time follows the event [→](#listening-and-reaction)
- The body carries the biography: **center of gravity, tempo, openness, breath** — set all four before any psychology [→](#the-body)
- **Business** — a physical task the hands are doing — kills theatricality; the strongest accent in a scene is the moment the character **stops** it [→](#the-body)
- **Distance is drama** when it changes the relationship; status is what you DO, and a status break can mark an event [→](#the-body)
- Reuse the character master profile and adapt relevant behaviors per scene; the 150–220-word paragraph below is an example form, not mandatory prompt padding [→](#the-acting-master-profile)
- Any tic or mask used needs a **trigger**; a crack is optional when the character and scene support it [→](#the-acting-master-profile)
- **Purposeful attention is required** — choose readable gaze/blink cues for the event and framing; the eye-life menu is not a quota [→](#eye-life)
- Scene adaptation preserves motivation while selecting visible behavior; convert useful tics and omit irrelevant ones [→](#scene-adaptation)
- Describe current delivery (breath, pace, loudness), not a fixed timbre/profile; actual audio references keep their recorded role [→](#voice--fixed-identity-never-adapted)
- **State anchors are optional remediation.** Retain the full preparation → action → response → recovery chain and inherited states [→](#states-not-transitions)
- Ensemble reactions follow individual perception; wave timing and still/quiet power are optional performance patterns [→](#ensemble-and-space)
- 15 named bad-acting symptoms and a descriptive 0–5 scale; accept using [evidence checks](#表演证据验收), not a score threshold [→](#the-atlas-of-bad-acting)

---

## Where this sits among the repo's performance tools

| Layer | Skill | What it controls |
|---|---|---|
| **Craft** — why the character does anything | **this skill** | objective, obstacle, tactics, beats, subtext, status, business |
| Muscle | `higgsfield-facs.md` | facial Action Unit codes (AU12, AU6…) |
| Named expressions | `higgsfield-soul.md` § Micro-Expressions | expression vocabulary for identity work |
| Production form | `director-compiler.md` | performance within the studio four-section contract; no extra acting block |
| Backstory | `higgsfield-character-design.md` | who the character is before any scene exists |

Use this skill to decide **what the body does**; optionally use FACS to specify
**which muscles** matter in an existing close-up. AU codes are empirical prompt vocabulary,
not guaranteed controls; do not force a close-up or an AU schedule into every performance.

---

# Part I — The craft

## What good acting is

Truthful behavior under imaginary circumstances. Not depicted emotions, not recited text,
not "expressive faces."

| Bad acting | Good acting |
|---|---|
| Shows the emotion ("I am angry") | Pursues the objective ("I will make you return the money") — anger arises on its own |
| Waits mechanically for their cue | Listens continuously and reacts when information registers, without a per-second gesture quota |
| Body illustrates the words (gesture = word) | Body lives its own life, sometimes contradicts the words |
| All lines in one tempo and tone | Rhythm changes with every change of tactic |
| Emotion switches on at the line and off after | State is continuous — there is a life before and a life after the line |
| The face "performs" — eyebrows, grimaces | The face thinks — the thought is readable in the eyes before the words |

## The five pillars of every scene

Use these five questions for active dramatic characters; adapt to the scene and character.
An unconscious or sleeping figure has a physical state, not an invented conscious objective.
Do not add goals, conflict or subtext to fill a template for non-dramatic work.

**1. Objective.** What the character wants IN THIS SCENE, RIGHT NOW, FROM A SPECIFIC PERSON.
Always a verb aimed at the partner: *make him confess* · *beg a week's extension* ·
*convince her I'm not afraid*. Never a state ("be angry", "feel guilty") — states cannot be
played. Behind the scene objective sits a **super-objective**: what the character wants
across the whole story, with every scene objective a step toward it.

**2. Obstacle and stakes.** What prevents them — external (another character wants the
opposite; witnesses in the room; two hours to deadline) or internal (pride won't let them
beg; they don't believe their own words). Always answer *what happens if I do NOT get what I
want?* — and the answer must frighten the character. The higher the cost of failure, the
more taut the scene.

**3. Tactics.** The concrete method of pursuing the objective right now, as an action verb:
*press · charm · shame · plead · provoke · bargain · threaten · stall*. When a tactic fails,
a living person may **change** it. Sustaining a tactic is valid when the objective and
response justify it; do not invent tactic changes to meet a count.

**4. Beats.** The smallest unit of action: the stretch during which the character wants one
thing and pursues it one way. A beat ends when the objective is achieved, the tactic fails,
new information arrives, or the balance of power shifts. **Every beat change must be VISIBLE
in behavior** — a pause, a change of posture, a change of speech tempo, a shift of gaze. A
scene may have **2–4 beat changes** as an illustrative pattern. Let actual tactics, information and power shifts determine the count; do not invent turns to meet a quota or split a complete emotional arc.

**5. Subtext.** What the character actually thinks and wants, as opposed to what they say.
Subtext is **not performed** — it leaks out on its own when the character plays the true
objective while speaking the false text. Buildable markers: questions that aren't questions ·
repetitions (asking the same thing — they don't believe the answer) · abrupt topic changes ·
jokes at the wrong moment (a shield against vulnerability) · answers that are too short
("Fine." "Sure." — a closed door).

### 提示词编译：物理动作后接潜台词

潜台词是给生成模型的**表演意图提示**，不是第二套动作，也不是文学化的心理独白。需要时，先写当前取景中能看见的物理动作、表情、视线、呼吸或手部任务，再紧接一句简短的潜台词：

```text
她眉峰夹紧，下唇微颤，压低下巴稳住握刀手。
（潜台词：不是恐惧，而是强行压住疼痛和慌乱，逼自己把注意力全部钉在敌人身上）
```

使用规则：

- 只在面部特写、情绪转折、重要决定、听者反应或动作意图容易被演空的关键 beat 使用；不是每个时间段都要补。
- 潜台词保持一句、直白、可执行，说明“为什么这样做”或“想对谁做什么”；优先写 `逼自己稳住`、`掩饰心虚`、`等对方露出破绽`，不写“她很紧张”“她感到痛苦”这类情绪标签。
- 潜台词必须服从已确认的目标、障碍、信息和角色状态；不能用它擅自增加秘密、反转、关系或未发生的心理事实。
- 先写可见动作，后写潜台词。潜台词不替代动作、刺激源、视线目标或动作结果，也不要求模型把括号内容逐字表现成夸张表情。
- 连续动作、纯景观/产品镜头、无意识状态和无需心理解释的物理行为通常省略；非人角色只使用其已确认的感知与行为渠道。
- 复制用视频提示词中可保留 `（潜台词：...）` 作为紧邻动作的导演意图；不另设 PERFORMANCE/心理分析栏目。内部规划可用更完整的目标与障碍，提交正文只保留本镜需要的短句。

## The layer above the pillars — one direction, different fuel

`[DEMO — Tigran (tig-acting-task), 2026-07-10]` `[UNPROVEN HERE]` The five pillars are
per-character. They do not say what holds an ensemble together, and that is why scenes
built from them alone can read as several good performances that are not in the same
scene. One layer sits above them.

**Optional ensemble lens: a shared scene direction, with different motives.** Use it when the scene supports a common intention; opposing objectives need not be rewritten into agreement. Usually unspoken —
a mutual silent agreement about how this time will be lived. *Part without pain, stay
positive* (a mother packing her son's kit before he leaves). It belongs to everyone in
the room at once. It is **not** the film's dramaturgic function: characters never play
the reveal or the theme, which are accomplished *through* them as a byproduct.

**Each character pushes that direction for their own reason — the MOTIVE.** Same vector,
different fuel. The son keeps it painless *for his mother*; the mother out of
*superstition* (tears before a journey are a bad omen). **The fuel is what makes each
performance distinct while the scene still reads unified** — and it is the piece most
often skipped, which is what collapses an ensemble into one note repeated.

Given circumstances constrain the motive: a character who already took a compromised job
cannot play moral innocence. If the motive contradicts the backstory, re-derive it.

Distinguish carefully, because these are four different things and only the last two are
per-character:

| Layer | Whose | Example |
|---|---|---|
| Scene direction | Shared by all | *keep it painless* |
| Motive (fuel) | Each character's own | *superstition* / *for her* |
| Objective (§ pillar 1) | Each character's own | *send him off strong* |
| Tactic (§ pillar 3) | Each character's own | *pack ordinarily, steal looks* |

### Name the event from the ENDING

Read how the scene **ends** before naming what it is about. The last line or beat is the
key you read the whole scene backward through — and watch for the double-meaning last
line, spoken about one thing and meant about another (*"Poor bastard. Just can't forgive
himself"* — said over a patient, meant about the speaker).

**The test: the event must contain EVERY character in the scene**, including silent and
unconscious ones, as participants or mirrors of the same process. **If a character stands
outside the named event, the event is named wrong** — rename it until they are all inside
it. This is the cheapest structural check in this file and it catches the scene where one
character is merely present.

### The physical action is the channel

The surface activity — the *terrain* — stays as the physical action, and each character
pursues the event **through it, via their own distinct, camera-readable behaviour**. The
invisible task must have a visible channel or the model has nothing to render.

One terrain (*routine hospital rounds*), one event (*the search for self-forgiveness*),
three channels:

- one character through **remembering** — REM under closed lids, a tear
- one through **obligated actions done right** — correct metrics, on time, double-checking an entry
- one through **caring** — patient-care gestures beyond the checklist, checking the man rather than the chart

Give every character in the scene their own physical channel for the same event. Different
behaviours, one event, one terrain. This is what turns an acting note into something a
video model can actually generate.

### Contrast pairing — build duos on mirrored +/−

A two-hander is richer when the pair is built on contrast: **each character carries one
plus and one minus, inverted relative to the partner**, and one axis is named as the
**essential axis** — the opposition the audience actually reads. The other traits are
colour.

A lab pair, essential axis *care for the patient*:

- **Doctor — loyal (+) / careless (−).** Genuinely loyal, but to the institution and the money. His plus serves the wrong master, so on the essential axis he is **minus**.
- **Medic — compromised (−) / caring (+).** Compromised by taking the job at all, but caring toward the patient. His minus is real; his plus survives inside it — on the essential axis he is **plus**.

Both still push the same scene direction. The contrast lives *under* it and leaks out
through the tactics: the careless one's routine is real, the caring one's routine is
armour, and it cracks.

**The seeming trait is often scar tissue over its opposite** — "careless" is hope lost,
not care absent. Direct the history, not the surface.

## Listening and reaction

Performance lives not in the lines but **between** them. Four observable markers to write in:

1. **The reaction starts when the information registers.** If the point is understood
   mid-phrase, face or body can answer before the line ends. A final-word reveal or a
   deliberate delayed response follows its actual trigger; do not impose a fixed lead or delay.
2. **Thought before word.** Before a hard answer there is a micro-pause — the person visibly
   decides what to say. Instant answers at uniform speed read as memorized text.
3. **The assessment moment.** After news, a threat, or an insult, the character needs time to
   digest — from a fraction of a second to a long pause. Show the assessment through cues
   readable at the chosen scale: eyes in close-up, or head, shoulders, posture and breath
   in wider coverage. The response does not require a close-up.
4. **Contagion from the partner.** Tempo, volume, and energy shift in response: a shout is
   answered either with a counter-shout or with pointed quiet — but *answered*, not continued
   over.

**A silent listener still gets a task, not just markers.** The four markers above describe
how a reaction *reads*; they do not give the listener anything to be doing between them,
and a listener with no task is where the dead face comes back in a two-shot. Name the work:
*decide whether he is serious · wait for the opening · protect the mood · catch him in the
lie.* Every character in frame gets living eyes this way.

## The body

**Physical state before psychology.** Set four parameters for every character before any
inner life:

- **Center of gravity** — high (chest, chin: confidence, aggression, status) or low
  (shoulders, slouch: fatigue, fear, submission).
- **Tempo** — fast/ragged (nervousness, stimulant energy) or slow/economical (control,
  threat — the most dangerous people move least).
- **Openness** — squared shoulders and open palms, versus crossed arms, dropped head, closed
  poses.
- **Breath** — high and rapid (panic) versus low and slow (control). Breath is the most honest
  indicator of state, and sound must match physics: someone who just ran cannot speak on a
  steady voice.

**Business — the physical task.** A character almost always needs a DOING. They don't "have a
conversation" — they fix an engine, count money, cook, wipe a glass, and talk over the top of
it. Business kills fake theatricality (the hands are busy with truth), creates rhythm (pauses
fill with action), and generates subtext (*how* a person counts money says more than the
words).

> **The interrupted-action rule.** The strongest accent is when a character **stops** the
> business. If he was slicing bread and stopped at a phrase, the phrase became an event. Use
> the stop as punctuation.

**Proxemics — distance as drama.** The distance between characters is a visible graph of
their relationship:

| Zone | Distance | Reads as |
|---|---|---|
| Intimate | under 0.5 m | love or violence — entering uninvited is aggression |
| Personal | 0.5–1.2 m | trust |
| Social | 1.2–3.5 m | business, wariness |
| Public | 3.5 m+ | alienation, hierarchy |

A threat whispered 10 cm from a face is scarier than one shouted across a room. Scene drama is
often just the story of distance: who closes it, who breaks it, who freezes. **A change of
distance can mark a change of beat** when it changes the relationship or information.
Use metres when spatial precision matters, per the measurable-language guidance in
`higgsfield-seedance.md`; routine locomotion does not force a new beat.

**Status — the invisible hierarchy.** Status is what you DO, not who you are.

- **High status:** an immobile head, slow movements, long gazes, pauses before answering,
  taking up space, touching other people's things.
- **Low status:** fussing, frequent self-touching (face, hair), broken speech, filler-laughter,
  asking permission with the eyes.

The most interesting thing in a performance is a **status break**: the boss who shows fear for
one second; the underling who suddenly stops smiling. A powerful scene shape is *enter high and
collapse*, or *enter low and flip the room*.

## How good acting sounds

- Rhythm is written in the text — deliver it precisely; fast ≠ mushy.
- Overlaps are normal (lines stepping on each other's tails), but key words stay clean.
- **Volume contrast: the most frightening things are said the quietest.** Shouting is the
  currency of the weak; the character who owns the scene lowers the volume and everyone leans in.
- Pauses are events, not holes — a pause is legal only if something happens inside it: an
  assessment, a decision, a refusal to answer.
- Speech may include interruptions or unfinished thoughts when the approved script supports
  them. Preserve confirmed dialogue exactly; adjust delivery, not words, unless rewriting is authorized.

---

# Part II — Writing the acting

## The acting master profile

Every recurring character gets **one** master profile — the permanent source of truth about
how they act. Written once, then adapted per scene. The **150–220-word flowing paragraph** below is an optional planning form,
not a required length or an extra output block. Keep relevant behavior observable and filmable.

**Suggested planning order:**

```
Character acting as [NAME]. [Build, physique, posture — the body as a document of their
biography]. [The psychological engine in one clause — the inner drive that explains the
physicality]. Current delivery: [breath, pace, loudness and phrase breaks at the actual event]. Key physical habits and tics: [signature tic with
its trigger; stress tic with its trigger; concealment behavior — what they do to hide what
they feel; the facial mask and the exact condition under which it cracks]. Eye life: [blink
quality and rate, scanning pattern, gaze-before-head, catchlights]. Walking style: [the gait
as characterization — named and specific, with weight, rhythm, and foot placement]. However,
when [emotional trigger], [the transformation — how the posture, gait, and face change].
[Optional: the softening target — the one person or thing that makes the face genuinely soften].
```

**Rules for each block:**

1. **Only observable behavior.** Every inner state needs a body marker. Never "he is nervous" —
   write the trembling lower lip, the heavy swallow, the long inhale through the mouth and
   sharp exhale through pursed lips.
2. **Every tic has a trigger.** Not "he cracks his knuckles" but "he cracks his knuckles during
   mundane conversations to fake confidence." Format: `[tic] + [when/why]`. Tics without
   triggers are decoration; tics with triggers are dramaturgy.
3. **Name the gait.** A coined name in quotes anchors the biomechanics — a "power-walk", a
   "peacock strut", a "gallery walk", a "battering-ram stride", a "dreadnought pace" — then
   unpack it: weight, step, what the torso and arms do, what the head does.
4. **Build in the mask AND the crack.** The single most cinematic device in a profile is the
   conditional transformation: the facade, plus the precise trigger that collapses it. A
   dominant swagger that crumbles into a childlike slouch when rejected; stern discipline that
   melts into a radiant smile at one specific person. A "However, when X — …" clause can specify a genuine change of strategy.
   It is optional: do not invent a mask or contradiction for every character.
5. **Softening targets, when established.** Use the relationships already supported by the
   character and scene; do not impose a count or invent a relationship.
6. **No wardrobe.** Clothing lives in the scene/look block, never in the acting profile. The
   profile must survive any costume change.
7. **No camera, no color.** Acting drives performance, face, voice, and motion only.
8. **Physique carries biography.** Build and posture tell the backstory — a build "weathered
   from past struggles", shoulders "perpetually tense", a posture "over-corrected to project
   authority". Profession, past injuries, and self-image must be readable in the body.

> **Identity and age follow confirmed project facts.** This craft module imposes no blanket
> age-word ban. Body, posture and voice may express life experience without repeating asset
> descriptions, but do not conceal age, change identity, or rewrite words to bypass safeguards.
> Apply the actual platform rules; if they prevent the requested submission, explain the conflict.

## Eye life

**Dead eyes are the number-one tell of AI-generated acting.** Every character gets continuous,
purposeful attention, in the profile *and* in every scene. The following cues are a
menu: select only meaningful eye work readable in the framing. No each-second motion,
blink count or close-up quota; a motivated held gaze is valid.

- **Micro-saccades and gaze targeting** on whatever they attend to: eyes may drift,
  flick away in thought, scan to a detail or settle. Avoid an unmotivated frozen stare;
  sustained attention can remain still.
- **Realistic blink rate and quality**, tied to state: rapid blink-bursts under stress; slow
  calm lids in control; a blink-and-glaze on a moment of dissociation.
- **Live catchlights** — the eyes must read as wet, lit, and alive. But a catchlight is a
  *render* property, not a cure: **dead eyes are not fixed by lighting tricks, they are
  fixed by giving the eyes a task.** A glassy stare with a beautiful catchlight is still a
  glassy stare. Write the eye-work as purposeful action aimed at the partner — *checking
  both of their eyes for a sparkle of trust · registering after each point whether it
  landed · stealing a look and snapping back before being caught · measuring them,
  comparing what I feel against what they show.* **The eye movement IS the doing**, and
  aliveness is the mind visibly working on the task moment to moment. Catchlights make
  that legible; they never substitute for it.
- **Controlled stillness is chosen, never dead.** For a near-unblinking predator calm, keep
  blinks rare, slow, and deliberate — a decision, not a freeze — and let the gaze still shift
  slowly with intent.
- **Eyes lead the thought.** The eyes reach the target a touch before the head turns. The
  thought is readable in the eyes before the words come.
- **Eye life reacts to the event.** Select changes in blink quality or gaze steadiness
  when motivated; catchlights follow lighting and eye direction, not an emotion schedule.

The phased-blink shorthand from the film pipeline — *one lazy blink → a quick DOUBLE-BLINK →
one HARD reset-blink* — is an optional static-shot remediation example, not a required sequence
(`higgsfield-seedance-hell-grind.md` § Physics, not adjectives).

## Scene adaptation

The master profile is who the character IS. For each scene, **rewrite it into the moment** —
never paste it.

1. **Present characters only.** An acting paragraph only for characters actually in the shot.
   No character in frame → no paragraph.
2. **Keep the constant core.** Identity, signature tics, eye life, and the
   emotional through-line stay the same in every scene — this is what holds the character
   together across cuts. Never contradict the master.
3. **Re-express for this scene.** Select, emphasize, modify, or drop specific behaviors to fit
   the scene's posture (seated / standing / running / hiding), action, beat, emotional state,
   and time of day.
4. **Preserve the motive; select its outlet.** A behavior that cannot happen here can
   be *converted*: a restless pacer on a sofa may displace that pressure into a wrist-flick
   or paper-tearing. Choose a meaningful visible outlet; omit irrelevant tics rather than
   stacking substitutions. Fatigue, injury or new information can change the energy.
5. **One flowing paragraph for the acting sub-block.** Fold it into the full director
   format's behavior, staged performance and continuity sections; this sub-block style
   does not remove the enclosing headings or detailed action prose.
6. **Bind the character to real references** in the role map. Use the selected mode's
   tag grammar; follow the root's direct registered @handle convention in project video prose,
   without re-describing the asset. Unbound authoring aliases remain explicitly unbound in records.

## Voice — fixed identity, never adapted

Do not output fixed timbre, register, resonance or accent profiles in character assets or video drafts. Delivery is
scene-dependent: breath, pace, pauses, loudness and strain must follow the current action.
A frightened whisper and a calm answer can come from the same speaker without the same delivery.

Use actual provided audio references or platform IDs only with verified roles and binding;
do not turn them into invented descriptions. Full video drafts use inline speech, non-verbal
vocalizations and scene sounds, without a fifth Audio field. Silent appearances do not need
voice instructions; offscreen dialogue retains speaker attribution. Native audio-only tool
settings remain in their own task scope. Actual lip-sync and audio matching require results.

## States, not transitions

**Optional remediation for a failed transition or a short submission.** A clearly
anchored state — mid-throw, mid-punch, mid-pace, mid-argument — can help the model
recover a difficult action phase. It does not replace the complete causal performance.

- Failure example: "reaches into the bag, pulls out the knife, winds up" collapses in a take.
- Possible repair anchor: "mid-throw, arm extended" identifies the phase to regenerate.

Keep the preparation, draw, weight transfer, release, contact/miss, target response and
recovery explicit in the full master. If separate coverage is needed, preserve the approach
and matched outgoing/incoming states. Opening mid-action is an option only when the cause
and user-directed opening remain legible
(`higgsfield-seedance-hell-grind.md` § Solutions born under deadline).

## Ensemble and space

The wave, freeze and strong/weak contrasts below are optional dramatic patterns;
character intent, readable distance and actual stimuli determine behavior and timing.

- **Group reactions follow perception.** One person may get a joke first, another later,
  another not at all; a shared sudden stimulus can also produce simultaneous responses.
  Vary behavior where motivated, not by mandatory stagger or per-person reaction slots.
- **Give the reaction its needed weight.** Preserve action and response together; show a
  witness's face when that viewpoint carries the event, without forcing reaction close-ups.
- **A freeze can punctuate a threat.** A motivated change from shifting weight or business
  to stillness is one option. Each person responds to what they perceive; no constant
  micro-movement or synchronized stop is required.
- **Movement equals motivation.** Nobody crosses a room without an impulse: toward something or
  away from something. Strong motivated events — closing in (escalation) · turning one's back
  (dismissal, or hiding the face) · standing while the other sits (dominance grab) · sitting
  down mid-conflict (paradoxical power) · stopping in the doorway (the threshold is the decision
  point) · starting to pack (ultimatum by body).
- **The strong are still and quiet; the weak fidget and shout.** Danger is played not by the
  dangerous one but by the tension of everyone around them. Threat without wind-up: no menacing
  pauses, no slow-motion turns — in a truthful world violence arrives without an announcement.
- **Degradation accumulates.** If a character is worn down across a story, carry it in the body
  cumulatively — greyer, heavier, slower reactions — never resetting between scenes.

> **Capacity is model- and mode-specific.** Older production heuristics are not a universal
> three-character ceiling. Check actual reference/speaker limits and visible workload; do not
> demote a plot-relevant character to an anonymous crowd solely to meet an assumed count.

---

# Part III — Quality control

## The atlas of bad acting

Recognize the symptom, apply the prompt-level fix.

| # | Symptom | How it looks | Prompt-level fix |
|---|---|---|---|
| 1 | Indication (mugging) | The face "depicts" the emotion: arched brows, grimaces | Remove the face from the task; write the objective and give the hands business |
| 2 | Playing the result | The character plays the scene's outcome from second one | Write only what the character knows NOW |
| 3 | Waiting for the cue | Empty face while the partner speaks | Give the listener a task; start the response when the relevant information registers |
| 4 | Monotactics | One color despite changing circumstances | Check event-driven tactics; a sustained tactic is valid when justified |
| 5 | Gesture illustration | Gesture duplicates the word ("big" — arms spread) | Gesture either precedes the thought, contradicts the words, or is absent |
| 6 | Free emotion | Tears or rage with no build-up and no trigger | Build the ladder: restraint → break; emotion must cost something |
| 7 | Body false to biography | A thug with a dancer's posture | Set the body profile: center of gravity, tempo, wear |
| 8 | Speech mismatches the character | Delivery lacks the established rhythm | Adjust delivery within approved words; do not add fillers, repeats or rewrite dialogue without authorization |
| 9 | Threat signaling | "Menacing" pauses, squints, slow turns before violence | Threat is mundane; violence without wind-up |
| 10 | Unmotivated synchronized ensemble | Different perceptions yield identical reactions | Tie each response to its stimulus; simultaneous reactions are valid when justified |
| 11 | Dead pauses | Silence in which nothing happens | Fill with assessment or business — or cut |
| 12 | Emotional reset | The character instantly "recovers" after a strong event | States have inertia; the trail carries into the next beat |
| 13 | Commenting the role | The performance winks at the viewer | Full belief in the circumstances; comedy is played dead serious |
| 14 | Close-up overload | Active mimicry on a close-up | The tighter the shot, the less movement: only the eyes and the thought |
| 15 | Dead eyes | Unmotivated frozen stare and absent attention | Apply § Eye life through a clear attention task and selected visible cues, without a motion quota |

## The performance scale

Optional descriptive diagnosis, not an acceptance score or a required arc:

- **0 — Mannequin:** behavior/attention absent where needed.
- **1 — Declaimer:** labels and illustrative gestures replace an objective.
- **2 — Diligent:** an objective is suggested, but needed reactions or continuity are missing.
- **3 — Craftsman:** motivated, readable behavior and listening with credible body state.
- **4 — Alive:** nuance and scene-specific responses deepen the established character.
- **5 — Magnet:** especially compelling, coherent performance; mixed truths may help when
  the story calls for them, but are not required.

A pure emotion, sustained stillness or simple truthful response can pass. Do not manufacture
contradiction, unexpected choices, extra tears or tactic changes to reach 4+. Acceptance uses
[表演证据验收](#表演证据验收); a failed critical item cannot be averaged away.

## Pre-send checklist

- [ ] Active dramatic characters have a concrete objective/attention target; sleeping or unconscious figures retain an appropriate physical state
- [ ] Obstacle and stakes exist; the cost of failure is real
- [ ] Beat changes follow actual events/tactics and remain visible in behavior (pause / posture / tempo / gaze); no mandatory count or equal timing
- [ ] Reactions follow perception of the trigger, including mid-line when understood; assessment time fits the event
- [ ] Each active character has purposeful attention; business or a held posture fits the scene, without inventing conscious tasks for sleeping/unconscious figures
- [ ] Any distance changes are motivated and spatially clear; metres used where precision matters
- [ ] Status is in the body, not just the words
- [ ] Any tic/mask used has a trigger; no compulsory mask, crack or contradiction
- [ ] Attention and selected gaze/blink cues are meaningful and visible at the chosen scale; no per-second or blink quota
- [ ] No fixed timbre/profile prose; delivery follows current action and actual reference roles
- [ ] Full action process, response and recovery retained; optional repair state anchors have causal handoffs
- [ ] No wardrobe, camera, or color inside the acting paragraph
- [ ] Confirmed identity/age preserved; actual platform rules checked without concealment or blanket age-word rules
- [ ] Ensemble responses fit perception and motivation; any stagger or status contrast serves the event
- [ ] Evidence checks below passed for the applicable scope; score is not a substitute

---

## 非人角色表演适配

动物、奇幻生物、机器人及其他非人角色的视频，默认接入本节；通用的目标、刺激、注意与行为原则继续沿用本模块，**人类FACS不自动迁移到非人面部**。这里只适配已有设定，不重新设计角色或要求额外出图。

1. **先继承结构与风格。**从已确认资产/设定取可动部位、身体比例、感知方式、能力与伤势；区分写实动物、风格化动物、已允许拟人化的角色。不能因为剧情需要悲伤就新增眉毛、人类嘴角、泪腺表现或说话能力；原稿明确的流泪/说话等照已定风格实现，不以写实默认删除。
2. **选可观察的表达渠道。**有依据才使用头颈高低、眼睑/视线、鼻息、耳位、翼/尾姿态、重心、步幅、靠近/退避、触碰力度或声音变化。某物种没有的器官不写；机器人用已定的转向、停顿、执行力度或已有显示部件，不凭空增加脸。
3. **保持行为动机与可见证据相连。**护物、避险、探索、依附、试探等由当前刺激引出，行为改变要有结果；不能用“它懂得全部人类意图”替代观察。写实动物行为不一一等于人类心理，奇幻角色的理解能力沿已确认剧情，不擅自推高。
4. **拟人化与幅度按项目锁定。**克制、自然、夸张等是表现风格，不是越强越好；同一角色跨镜不从写实突然切成卡通。受伤翼、短肢、遮挡眼等能力限制不因情绪恢复；体量通过承重、步幅和接触力度体现。
5. **按镜头筛选线索。**头部近景可写已设结构的细微变化，远景用姿态、距离、步态；只见尾部就不写可见嘴角。表演与奔跑/保护/受力并行，不让生物停步排演情绪。读不出必要信息时调整取景或行为，而非堆人类AU。

验收：结构是否真实属于该角色；反应是否由可感知刺激触发；拟人化是否在授权边界；当前景别是否可读；动作/伤势/情绪是否连续。任一已知冲突为失败；结构未知且影响关键动作则标待核验，不编造生物学解释。

示例是适配原则，不是新项目剧情：翼兽护住巢中物件，可通过重心移向巢侧、前肢圈拢和头颈拦截表达；不能默认追加“像人一样皱眉咬唇”。同样，已确认的卡通动物可以使用其既定拟人表演，不强制改成自然纪录片。

## 表演证据验收

使用已有五支柱、身体、眼神与听者规则写演出，再按下表验收；不另写一份重复的表情词库。记录到[统一验收总表](production-checks.md#统一调用与验收总表)，**不能以自评4分替代正文证据**。无人画面可注明人物表演不适用；无对白或静音不免除可见表演检查。

| 检查点 | 文字通过条件 | 典型失败 |
|---|---|---|
| 动机与注意 | 能定位当前任务、刺激源及视线对象；主动角色的行为服务目标，听者在理解/判断 | 只有“惊恐/悲伤”，或所有人空等 |
| 表情与情绪发展 | 适用近景写出可见变化及其触发，状态如何影响行动；没有变化也有维持该状态的理由 | 无缘由落泪、开场就演结局、每镜相同抖嘴 |
| 听者及群体 | 反应由各自听见/看见的信息触发，可并行也可有感知延迟，背景仅写可读幅度 | 所有人同步同表情，或轮流等待自己的镜头 |
| 景别与身体 | 脸部、手部、姿态、呼吸取舍符合取景和遮挡；受力与伤势限制持续 | 远景硬写瞳孔、背影硬写嘴角、受伤肢体突然正常 |
| 时序与接缝 | 表情、判断与主动作可并行，情绪/气息/注意跨镜有余态 | 停下追逐演表情、切回就恢复平静、准备/命中被反应镜拉长 |
| 声音与表情 | 不输出固定音色，语气/响度/气息随当前行动，口型需求与所选模式相容 | 奔跑后突然无喘息长句、说话者切错、听者跟口型 |
| 风格与幅度 | 符合角色、题材和项目已定表现尺度；纯粹、克制或复杂情绪均可成立 | 为高评分硬造潜台词、反转或矛盾，擅加哭喊 |
| 非人适配 | 非人角色符合上一节结构、感知和拟人化边界 | 直接套人类FACS或新增器官/能力 |

每项引用“对象/版本/镜头时段＋演出原句”，说明通过、失败、待核验或不适用。关键项失败先修复，不能用平均分抵消；修复保持确认剧情与台词，重新核对相邻镜头。已定的年龄与身份不得因模板经验被隐去或替换，平台确有限制时明确说明并选择合规路径，而不是换词规避。

生成后另用实际视频与时间码核验：表情是否可读且不过度、注意目标是否正确、反应是否及时、气息/动作是否连贯、身份和非人结构是否稳定。有静帧只验可见静态项，有视频无音频不能声称声音验收；没有生成结果时结果层待核验。

# Part IV — Worked example

Invented character; use as a pattern, not as content.

## Master profile

```
Character acting as VIKTOR. A retired night-shift taxi driver and former amateur boxer; heavy,
thick-necked build gone soft at the middle, with a flat-nosed face and old scar tissue over
both eyebrows; sits and stands with a low, grounded center of gravity, weight always on the
whole foot. Runs on a single engine: decades of waiting — for fares, for rounds, for trouble —
have made patience his weapon. He answers with short economical phrases, becoming slower
and quieter as the passenger presses him. Key physical habits and
tics: rolls an old coin across his knuckles when sizing a situation up; a slow, audible
nose-breath before he says no; when lying is happening in front of him, he goes completely
still and lets a long silence do the pressing; his default face is a heavy-lidded, bored mask
that conceals total attention. Eye life: sleepy, hooded eyes with slow deliberate blinks and
constant quiet scanning — mirrors, hands, exits — the gaze settling on a speaker a beat before
his head turns; catchlights low but alive. Walking style: a heavy, rolling "old boxer's walk",
short economical steps, shoulders level, hands loose and ready, never hurrying. However, when
someone raises a hand near him, the sleepy mask vanishes in a half-second: the chin drops, the
hands rise halfway, the feet find their old stance — then he catches himself and folds it away,
embarrassed. His face only truly softens for stray dogs, which he feeds from his coat pocket.
```

## Scene adaptation

*Scene: VIKTOR sits in his parked cab at night; a nervous passenger in the back seat is lying
about having money for the fare.*

```
VIKTOR sits motionless in the driver's seat, heavy and grounded, watching the passenger in the
rear-view mirror instead of turning around — his hooded eyes flick between the mirror, the
passenger's hands, and the door lock in slow, quiet scans, blinks rare and deliberate, the gaze
settling on the mirror a beat before his head ever moves. The old coin walks across his
knuckles on the seat-rest, unhurried; as the passenger's story falls apart, the coin stops
mid-roll — he lets the silence sit, takes one slow, audible breath through the nose, and
answers more quietly and evenly than before, without hurrying. Only
when the passenger's voice cracks does the sleepy mask ease a fraction: a long exhale, a slow
blink, the coin resuming its roll — patience choosing, for now, to be kind.
```

**What happened here:** the walk is irrelevant (seated) so its energy moved into stillness and
the coin; the signature tics kept their triggers (coin = sizing up · stopped coin = interrupted
action as punctuation · nose-breath = refusal · stillness plus silence = pressure on a liar);
the eye life obeys the master but is re-targeted to mirror, hands, lock; the beat changes are
visible (coin stops → silence → quieter voice → softening); and current delivery remained tied to his listening and response, without an added voice-profile field.

---

## Final axioms

1. Acting is behavior under pressure, not a demonstration of feelings.
2. Listening matters more than speaking; reacting matters more than declaiming.
3. Emotion is the consequence of a won or lost struggle, and it is expensive.
4. The body is smarter than the words: when text and body conflict, the viewer believes the body.
5. The strong are still and quiet; the weak fuss and shout. Exceptions are events.
6. Every tic needs a trigger; every mask needs a crack.
7. Defeat is one dramatic scene pattern; other scenes may reveal, connect or sustain an experience without inventing a loser.
8. Subtext is not shown — it fails to be hidden.
9. State anchors can repair a failed transition; the full performance still shows what happens and why.
10. Trim redundant mimicry when it obscures the event; preserve complete action, response and emotional development.

---

## Related Skills

- `higgsfield-seedance.md` — the Seedance prompt this paragraph goes into
- `higgsfield-seedance-hell-grind.md` — the CHARACTER ACTING block's production form,
  dialogue construction, and the micro-life rules
- `higgsfield-seedance-2-5.md` — 2.5's observable-cue emotional direction
- `higgsfield-facs.md` — muscle-level facial control by Action Unit code
- `higgsfield-soul.md` — identity consistency and micro-expression vocabulary
- `higgsfield-character-design.md` — the story bible upstream of any profile
- `higgsfield-audio.md` — where the locked voice prompt is delivered

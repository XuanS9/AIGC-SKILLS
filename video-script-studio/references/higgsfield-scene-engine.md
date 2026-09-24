# Higgsfield Scene Engine — is this scene worth generating?

`[DEMO — Tigran (tig-scene-engine), 2026-06-26]` `[UNPROVEN HERE]` **These definitions are
bespoke and deliberately not the textbook ones.** Apply them as written; do not substitute
standard screenwriting glosses, which are looser and will pass scenes this engine fails.

**Why a prompter carries this.** Every shot costs credits and iterations. A structurally
dead scene generates just as cleanly as a live one — the model has no opinion about whether
a beat earns its place — so the failure surfaces only after the footage exists and the cut
does not build. This skill is the cheapest pass in the repo: it runs on text, before any
generation, and its whole job is to stop you paying to render a scene that cannot work.

It decides **which** shots deserve the spend. `higgsfield-shotlist-director` turns the
settled scene into shots; `higgsfield-acting` writes the performance inside them.
Use [shared narrative planning](narrative-planning.md) for that handoff and
throughout the audit. The five engine elements are diagnostic questions, not five
required stages, shots, or equal-duration sections.

In this merged studio, ordinary narrative creation also uses this engine internally.
Keep the bespoke definitions and deletion/information/value-shift tests below intact;
apply them to the relevant scene or sequence, not as a demand for a reversal in every
shot. For an explicit audit, deliver the full findings and Minimal/Clean/Optional repair
levels. For prompt creation, express the chosen causal repairs in the eight-section
performance draft without attaching an audit report. Preserve user-approved events and
endings; flag a deliberate deviation rather than silently rewriting it. Pure landscape,
product-function and other non-dramatic tasks do not need an invented conflict arc.

---

## The five-element engine

### 1. Goal

The single, unchanging thing the hero is fighting for: to fix what has already been
established and reach, as fast as possible, the result that resolves it. "Already
established" means *anything* set up earlier — deep backstory, a few scenes ago, or one
minute ago.

- **The major goal never changes**, and the hero is never wrong about it. He can be wrong
  about **tactics**, never about the goal.
- **Every scene goal must be a causal link toward the story goal.** *Test:* if you can
  remove the scene and the chain still holds, the scene fails. No orphan scenes.
- "What he *ought* to do" is not a separate thing to test — the right move is dictated by
  **Obstacle + Stakes**. A hero taking a tactic the stakes would not justify (showering
  while the building burns) is a flaggable inconsistency: name it as bad writing or as
  deliberate self-sabotage.

### 2. Obstacle

A strong circumstance that **jeopardizes** either one stage of the path or the whole goal.
It *threatens*; it does not merely *cost*.

- It can be a **branching search space** (many places to look, limited time) or a **single
  hard wall** (a dead battery — you cannot search a dead machine). A wall typically spawns
  a fresh sub-goal with its own terrain.
- Name its **scale**: *local* (threatens the current stage) or *global* (threatens the whole
  goal).
- The obstacle is **what forces the hero to choose or change a tactic.** No jeopardy → no
  tactic needed → no scene.
- *Audit test:* name what is at risk, and at what scale. If nothing genuinely is, the
  obstacle is fake and the scene goes slack.

### 3. Tactic

The move the threat **forces** the hero to choose — a reasonable guess on his current,
often incomplete, knowledge. This is **search under uncertainty, not error-as-stupidity.**

- A "wrong" tactic is not dumbness; it is a plausible probe of a space he cannot fully see.
  The engine is a **knowledge gap**: the distance between what he believes and what is.
- **Each failed tactic must return information** that narrows the search and reshapes the
  next move. The drama is the narrowing, not the punishment.
- ✅ good: the tactic is a reasonable bet on current info, **and** its failure teaches
  something new.
- ❌ weak: a tactic he had no reason to try, or a failure that returns **zero information** —
  a wheel-spin. A failing tactic is only a weakness when the failure teaches nothing.

### 4. Reversal

A turn against expectation. Three forms:

1. **My own action flips on me** — what I did *for* something starts working *against* it
   (I shower to make the pitch; the shower makes me late and I miss it).
2. **Hidden agency revealed** — the thing or person I thought I was acting *on* was acting
   *on me* all along. The thriller move; it often fires exactly when the knowledge gap closes.
3. The general case: the situation turns opposite to what the tactic intended.

**Placement:** at least one reversal **per sequence**. A single scene may be pure
escalation, but a *resolved sequence* with zero reversals **fails**.

A **sequence** is the run of scenes from when a specific jeopardy opens to when it resolves —
overcome, or it defeats him and forces a new path. Sequences **nest**, and each resolving
unit needs its own reversal. Flag which scale you are auditing.

### 5. Value Shift

**The change in the AUDIENCE'S read of a character, triggered by a reversal.** The keystone,
and the most misunderstood element: it does not happen on the page, it happens in the
viewer's mind. Each reversal forces the audience to **re-judge** the character — a moving
verdict they keep revising (*nice → experienced → cunning → no, he's desperate → devoted son
→ what a man*).

> **THE CORE RULE: a reversal with no value shift is inert.** A structural turn is not a
> reversal unless it moves the audience's verdict. If you cannot name a **before-verdict**
> and an **after-verdict** the audience would hold, the turn is dead weight no matter how
> much plot flipped.

Audit the **trajectory**, not just presence: are the revaluations building a deepening
portrait, or just oscillating?

---

## The causal chain

> **Goal** (fixed; every scene a causal link toward it)
> → **Obstacle** (jeopardizes a stage or the whole goal; name what is at risk + scale)
> → **Tactic** (forced by the threat; a reasonable guess; its outcome must return information)
> → **Reversal** (turn against expectation; ≥1 per resolved sequence)
> → **Value Shift** (the audience re-judges the character; no shift → the reversal is useless)

---

## Audit procedure

Work the chain in order. Reversal and Value Shift are judged at the **sequence** level, not
the scene. Preserve the user's settled events and ending while testing their causal links;
do not manufacture extra events or reversals merely to fill a timing template.

1. **Goal** — state the scene goal in one line. Is it a causal link to the story goal? Apply
   the removal test. If you do not know the story goal, ask — you cannot fully audit Goal
   without it.
2. **Obstacle** — name the circumstance, exactly what it jeopardizes, and the scale.
3. **Tactic** — is each forced by the jeopardy, reasonable on current knowledge, and does
   each outcome return information? Flag wheel-spins and unmotivated tactics.
4. **Reversal** — locate them, name the form, confirm ≥1 per resolved sequence.
5. **Value Shift** — for **each** reversal, name before-verdict → after-verdict. If you
   cannot, mark it **INERT** and make it the priority fix. Then assess the trajectory.

### Audit output

```
SCENE/SEQUENCE: <one-line identification>

CHAIN CHECK
• Goal — <verdict + one line>
• Obstacle — <what's jeopardized + scale + verdict>
• Tactic — <forced? reasonable? returns info? verdict>
• Reversal — <form + present? ≥1 in sequence? verdict>
• Value Shift — <before-verdict → after-verdict per reversal, or INERT; trajectory note>

WEAKEST POINT: <the single element that, if fixed, recovers the most>

WHAT IF…
1. (Minimal) <change ONLY the weakest point so the rest of their scene still works>
2. (Clean) <a version that fully works, even if it departs further from the original>
3. (Optional) <only if it genuinely adds something>
```

The three tiers matter in that order: **minimal preserves the user's version**, clean is
yours, and the third is optional. Do not collapse them into one rewrite.

---

## Where this sits before prompting

Once the chain holds, apply [shared narrative planning](narrative-planning.md)
before choosing shot counts or generation durations:

1. Locate necessary events, causal turns, information reveals, and state transitions.
   These decide stages, including meaningful silence or a held reaction; do not assign a
   preset count, equal lengths, or one stage to each engine element.
2. Give each stage an inherited starting state, a primary change, a visible response, and
   an end state. Trace how that result enables the next event and the settled ending.
3. Decide what the viewer needs to see, then estimate action, dialogue, reaction, reading,
   and transition time. A **stage is not a cut or a generation clip**: a continuous shot
   may span stages, a stage may use multiple shots, and generation splits follow actual
   model/mode limits and complexity. A model cap does not set a narrative-stage length.
4. Hand off the eight director semantics: **assets/reference locks; overall goal; global
   sight/sound/space; subject behavior and pacing; stages; continuity/state inheritance;
   final frame/join; scoped constraints**. Keep the audit's native CHAIN CHECK, WEAKEST
   POINT, and WHAT IF tiers; weave relevant findings into them and the downstream brief
   rather than replacing the audit with eight production headings. Unknown assets remain
   planning notes, not invented upload handles.
5. Include transitions and the final frame within the runtime. If auditing an edit, mark
   findings against source timestamps and preserve source duration and cuts outside the
   requested scope. For extensions, inherit pose, motion phase/direction/speed, camera,
   lighting, props, emotion, and sound at the join: forward starts at the source tail;
   reverse extension ends at its **first-frame state**. Budget new material separately.

The next skills retain their own outputs and mode-specific workflows:

| Next | Skill |
|---|---|
| Who these people are, and their bible | `higgsfield-character-design.md` |
| The shared scene direction and each character's fuel | `higgsfield-acting.md` § The layer above the pillars |
| Breaking the settled scene into shots | `higgsfield-shotlist-director.md` |
| Writing the shot itself | `higgsfield-seedance.md` · `higgsfield-seedance-2-5.md` |

**The most common real failure to hunt for first:** a reversal that turns the plot but does
not move the audience's verdict. Surface it before anything else — it is the one that
survives a read-through, generates beautifully, and still lands flat in the cut.

## Related Skills

- `higgsfield-character-design.md` — premise, world, character, story bible
- `higgsfield-acting.md` — the performance layer inside a settled scene
- `higgsfield-shotlist-director.md` — scene → shot list

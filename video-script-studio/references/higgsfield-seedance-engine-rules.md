# Seedance 2.0 引擎规则（共享核心）（Seedance 2.0 — Engine Rules (shared core)）

本文件是 Seedance 2.0 共享渲染约束和制作技法的**唯一归属**。有条件的技法会明确标出。每种 Seedance 提示词写法都引用这个核心，而不是重复它：这些规则以前只存在于双语 JSON 档位的文档里，其他写法看不到。

**各种写法是这一个规则核心的输出*档位*：**

| 档位 | 格式 | 位置 |
|---------|--------|-------|
| `EN-director` | 英文文字提示词、六槽公式、兼容 MCSLA | `higgsfield-seedance.md`（本模块） |
| `ZH-house` | 中文团队格式（镜头块分镜表，≤1,800 字） | 团队 `shotlist-builder`（外部语料）；ZH 规则由 `../scripts/seedance_lint.py` 执行 |
| `bilingual-JSON` | 输出成对 `{"lang":"en"}` + `{"lang":"zh"}` 提示词的 JSON API 角色 | `seedance-bilingual-json.md` |

按交付目标选档位；下面的规则适用于**所有档位**。工作室默认交付是 Seedance 2.5 的中文块结构（[跨类型导演模板](template-general-director-2-5.md)），不设字数上限；1,800 字只属于上面两个外部档位。

---

## 硬性渲染约束（Hard rendering constraints）

来源：双语 JSON 导演文档里经制作验证的规则（`seedance-bilingual-json.md` § SEEDANCE 2.0 — ENGINE RULES），2026-06-11 合并。

1. **不写年龄的角色（关键）。**两种语言里都绝不按年龄描述角色。触发词：*boy, girl, child, kid, young, teen, little, 男孩, 女孩, 孩子, 少年, 少女, 小孩, 年轻*。按**职责**（骑手、身影、旅人）、**服装**和**动作**描述：标注他们在做什么，绝不标注他们是谁。
2. **动作节拍 = 意图 + 具名招式，而不是生物力学。**✅ “spinning back kick connects.” ❌ “left forearm rotates 45° to deflect.” 用户点名了招式就保留；用户描述了关节力学，就压缩成招式名或意图。
3. **描述力量和方向，而不是破坏的顺序。**✅ “driven into the car, metal buckling.” ❌ “thrown into side door, glass shatters, uses rebound to sweep leg.”
4. **空间连续性在切镜处断开。**任何切镜之后重新锚定位置和朝向。
5. **跨切镜追踪的角色 ≤ 3 个。**每个镜头写明在行动的那一对和互动方向。
6. **出画 = 隐性切镜。**离开画面的角色在这个镜头剩下的部分里就没了。绝不在一个连续镜头里编排出画 + 再入画。
7. **画外 = 不存在。**状态变化必须先在镜头上展示，才能被引用。
8. **避免反射镜头**（刀刃、水坑、镜子）：Seedance 渲染反射时会打乱场景地理。项目*必须*有反射时的变通办法见下面的高风险表。
9. **只描述能被看到或听到的东西。**❌ “the air smells of pine.” ✅ “pine needles covering the ground, wind moving through branches.”
10. **微表情写成物理变化。**✅ “jaw clenches, nostrils flare.” ❌ “looks angry.”
11. **双重对比切镜（有条件的技法）。**需要有动机的对比时，**同时**改变景别（extreme wide → wide → medium → MCU → CU → ECU）**和**镜头性质（手持 | 固定 | 稳定跟拍 | 摇臂 | 航拍）。重复的静态对白覆盖、匹配剪辑和刻意重复的构图仍然有效。不要只为了制造变化而加切镜或推翻已确认的运镜指示。

---

## 高风险镜头类型：写作时就标出（High-risk shot types — flag at authoring time）

这些镜头类型和上面的引擎规则冲突。**请求进来时就标出冲突**：主画面是镜子或水面反射的项目，需要刻意应用记录在案的变通办法，而不是悄悄违反规则。缓解办法是从引擎规则推出来的内部技法；不是平台文档记载的功能。

| 高风险镜头 | 为什么会坏 | 缓解办法 |
|----------------|---------------|------------|
| **反射**（镜子、水面、刀刃） | 引擎同时渲染反射面和被反射物时会打乱场景地理（规则 8） | 绝不在一个连续镜头里同时显示反射面和主体。把反射**当作**场景来拍：一个专门的镜头，镜子/水面里的影像就是主要主体，然后切到实际的主体（有动机时用规则 11 的双重对比）。反射是主画面时，把它钉为该镜头自己的首帧（2.0 用法；当前项目走 `omni_reference`，把反射构图写进第一段的 `画面：` 描述并配场景参考），而不是让引擎去构建反射。 |
| **同一角色的两个实例**（克隆、镜中自己、时间分身） | 身份追踪假设一个身份一个身体；实例会互相污染 | 把每个实例当作**独立的具名角色**，各有自己的服装/特征锚点（“@Hero-present: rain-soaked coat; @Hero-memory: pressed suit”）。尽可能给每个实例绑定自己的参考图。优先在实例之间切镜，而不是连续的双实例画面。 |
| **人群** | 跨切镜只能追踪 ≤3 个角色（规则 5） | 把人群描述为**环境，而不是角色**：一个整体，集体运动（“the crowd surges left as one”）。绝不命名或追踪超过 3 个个体；把你追踪的那一对放在人群前景。 |
| **文字渲染**（招牌、铭文、屏幕） | 字形保真不可靠，而且按 § Drafts Validate the Prompt，细节的可读性每次生成都会重抽 | 让对故事关键的文字不进生成：用文字叠加模板（`template-subtitle.md` 和 `template-speech-bubble.md`）或后期叠加。如果画面内文字不可避免，保持简短、够大，并在**最终分辨率**下核实可读性：绝不从 480p 草稿批准它。 |

---

## 执行（Enforcement）

- `python3 scripts/seedance_lint.py --preflight --model seedance_2_0` 检查机械性的部分（年龄标记、镜头数声明、ZH 字数上限、按 `model-specs.json` 的枚举合法性）。
- 判断性的部分（反射、实例处理、人群措辞、双重对比）对照本文件审查：向用户标出冲突时引用规则编号。

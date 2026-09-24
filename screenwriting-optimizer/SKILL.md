---
name: screenwriting-optimizer
description: 面向电影、短片与电视剧的剧本创作和优化。支持前提主题、故事结构、人物冲突、对白、场景、类型、格式改编、剧集开发、编剧室、喜剧、各国影视案例、行业提案与跨会话项目管理。Use when developing, diagnosing, rewriting or managing film screenplays, shorts and TV series.
---

# 影视剧本优化工作室

本包包含21个影视写作模块，按任务读取。内部模块名对应 `references/<模块名>.md`；文中的“调用某 skill”表示读取并执行对应方法，无需另外安装。保留影视方法、工作单与案例，不含戏曲和舞台剧专用模块。

## 执行流程

1. 继承已有素材、确认方向、语言、时长和交付要求，区分开发、审稿、定向改写、格式改编、案例研究或行业任务。
2. 持续项目或全流程任务先读 [sw-workflow](references/sw-workflow.md)，恢复或建立 `story-bible.md`；一次性交付按其豁免直接完成，不强制建档。
3. 区分长片、短片、剧集与半小时喜剧。剧集先确定引擎与人物网，不套长片页码；短片按容量选用结构工具。
4. 只读取命中的模块及其必要参考文件。路由摘要不能替代正文方法；模块可叠加，方法分歧按适用条件处理。
5. 优化原稿先提取前提、结构、人物和不可改项，再定位问题、完成修订，按命中模块的工作单与诊断标准验收。
6. 输出语言跟随用户，正文保持作品既定语言；跨语言术语查 [术语表](references/sw-workflow-terms.md)。用户指定模板、篇幅和已有授权优先。

### 输入不足或资料冲突时

| 触发条件 | 当轮处理 | 仍无法继续时的交付 |
|---|---|---|
| 用户要诊断或改写现有剧本，但未提供正文或梗概 | 集中索取原稿、媒介/目标时长与不可改项；先列需要核对的场景或结构问题 | 交一份可填写的诊断工作单，标明未看原稿，不虚构人物、情节或修订后的段落 |
| 同一项目的已确认设定、用户新要求与来稿相互矛盾 | 列出冲突的两种版本及受影响的场次，只询问会改变修订结果的一项选择 | 暂停受影响的改写；已能确定的局部诊断可标注假设后交付 |
| 案例、行业数据或资料文件不可取得，或年份不明 | 用已读取的原稿与可核实模块方法完成结构分析，将待核事实单列 | 不给无来源的引文、价格或行业结论；提供不依赖该事实的改稿方案 |
| 两个方法对同一任务给出不同页码、节拍或格式 | 按媒介、目标时长、用户指定格式选择适用方法，并说明选用依据 | 若选择会改变交付且条件未定，先给并列适用条件，待用户确定后执行格式转换 |

## 功能路由

| 模块 | 适用任务 |
|---|---|
| [sw-workflow](references/sw-workflow.md) | 长片与剧集阶段调度、项目档案、跨会话续写 |
| [sw-premise-theme](references/sw-premise-theme.md) | 前提、主控思想、主题、选材、logline |
| [sw-story-structure](references/sw-story-structure.md) | 三幕、BS2、情节点、九节拍、开头结尾与结构诊断 |
| [sw-truby-anatomy](references/sw-truby-anatomy.md) | 七步与22步有机骨架、四角对立、道德抉择；与页码结构互相校验 |
| [sw-genre-anatomy](references/sw-genre-anatomy.md) | 十二类型、类型节拍、混合类型与超越路径 |
| [sw-character-conflict](references/sw-character-conflict.md) | 人物、动机、对手、冲突升级与过渡 |
| [sw-scene-craft](references/sw-scene-craft.md) | 场景价值转折、动作、节奏、细节与道具 |
| [sw-dialogue](references/sw-dialogue.md) | 对白行动、潜台词、解说、角色声音与喜剧交流 |
| [sw-format-adaptation](references/sw-format-adaptation.md) | 影视格式、Fountain、中文场号制、日式格式、改编与修改 |
| [sw-series-engine-bible](references/sw-series-engine-bible.md) | 系列引擎、人物网、pilot、提案及剧集 bible |
| [sw-series-structure](references/sw-series-structure.md) | 幕与出幕、A/B/C线、pilot节拍、季弧与结局 |
| [sw-writers-room](references/sw-writers-room.md) | 破故事、编剧室、文档链、反馈与制作限制 |
| [sw-chinese-series-practice](references/sw-chinese-series-practice.md) | 国产剧文档链、格式、悬念、IP改编与制片流程 |
| [sw-sitcom-comedy](references/sw-sitcom-comedy.md) | 半小时喜剧、人物配比、笑点、单机/多机/动画格式 |
| [sw-american-case-studies](references/sw-american-case-studies.md) | 美国电影类型、结构、人物与改编案例 |
| [sw-japanese-screenwriting](references/sw-japanese-screenwriting.md) | 日本导演编剧的结构、素材、人物与主题方法 |
| [sw-korean-french-screenwriting](references/sw-korean-french-screenwriting.md) | 韩法影视的情绪、调研、类型、反转与集体创作 |
| [ozu-screenplay-style](references/ozu-screenplay-style.md) | 小津电影的家庭结构、反高潮、对白与逐场分析 |
| [succession-series-writing](references/succession-series-writing.md) | 《继承之战》的群像、隐形幕、压力、潜台词与结局工程 |
| [sw-series-case-studies](references/sw-series-case-studies.md) | 欧美及亚洲剧集的逐集、逐幕与场景案例 |
| [sw-industry-business](references/sw-industry-business.md) | 推销、提案、经纪、期权、署名与行业协作 |

## 常见组合与交付

- 从零开发：workflow → premise-theme → 对应媒介结构 → character-conflict → scene-craft → dialogue / format-adaptation。
- 整体优化：反向提取项目档案 → 结构、人物、场景诊断 → 对白与格式；中段松散加 truby-anatomy，类型承诺不足加 genre-anatomy。
- 剧集：series-engine-bible → series-structure → writers-room；国产剧加 chinese-series-practice，半小时喜剧切换 sitcom-comedy。
- 风格与案例：按任务选择案例模块，不把案例题材或结局变成强制规则。
- 行业提案：industry-business；国产剧加 chinese-series-practice，行业数据按原文年份使用。

按命中模块交付具体改稿、工作单或诊断，不用抽象建议替代用户请求的成果。需要视频制作时，可向可用的 video-script-studio 交接确认稿与不可改项。

只注册根 SKILL.md；安装及来源见 [README.md](README.md)，权利说明见 [LICENSE.md](LICENSE.md) 与 [NOTICE.md](NOTICE.md)。

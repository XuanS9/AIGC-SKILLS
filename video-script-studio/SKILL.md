---
name: video-script-studio
description: 将剧本、角色/道具/场景参考图、分镜、参考视频与音频编排成资产提示词、视频脚本、镜头清单及可复制提示词；完整制作按场景分批，资产与视频提示词同批配套、独立代码块交付；单类型请求按指定范围执行，先给本批样本，确认后展开。适用于打斗、追逐、人兽战、剧情、人物表演、角色资产、摄影、音频、Seedance、模型选择、VFX、Cinema、Canvas 与生成问题诊断；支持三强度两速度动作设计、多参考、视频编辑延伸及双语 JSON 交付。
---

# 视频脚本工作室

## 工作流程

1. 继承用户已确认的角色、剧情、结局、对白、模型、时长、画幅、语言、速度及素材；缺非关键参数用默认值，只补问影响执行的缺失信息。用户指定的模型与能力边界优先；未指定模型时视频生成默认 Seedance 2.5 `omni_reference`，角色/道具/场景图片及参考视频、音频各按职责输入，无参考时用文字描述主体。严格保留原时间线或接续的已有视频，先核对实际模式能力再处理。
2. 先完整读取 [项目工作区](references/project-workspace.md)、[项目资产总表](references/asset-registry.md) 与 [样本确认流程](references/sample-approval.md)。用户指向已有项目工作区时，先读项目目录的 `project.md` 与 `asset-registry.json`，继承已确认的参数、故事、结局、人物、对白、资产名、场景布局与批次进度；未指向工作区或读不到时按新项目处理并说明需提供路径才能继承，不虚报自动记住上次项目。样本与完整稿逐字复用已登记调用名；无总表时从已确认交付建立。识别本次类型：要资产只写资产，要视频只写视频，两类都要则按场景分批配套。每次先交本次类型的代表性样本+预期效果，停下等用户确认，再输出该批次全部提示词；新写、改写、补镜、修词、单条交付均适用。用户确认新的参数、剧情、结局、资产或交付批次后，把确认内容写回 `project.md` 与 `asset-registry.json`、并把可复制提示词存入 `prompts/`。完整制作或同时要求资产与视频时，按场景/连续剧情分批，共用名称与场景布局，同批配套交付；明确只要资产或视频时保留单类型范围。先交本批代表性样本与预期效果，确认后展开本批；批次组织按下方规范执行。
3. 视频创作、改写、分镜、编辑或延伸：区分剧情段落、镜头与生成片段，默认向 30 秒模型上限凑段、单片段承载连续多阶段动态，按观看任务与动作因果编排片段内切点；方法见 [按内容拆镜与估时](references/narrative-planning.md#按内容拆镜与估时)。完整读取 [导演编排](references/directing-workflow.md)、[叙事规划](references/narrative-planning.md)、[七栏目模板](references/template-general-director-2-5.md)；完整创作与改写还需 [演出范本](references/template-full-performance-example.md)。
4. 打斗、追逐、对抗、演武、人兽战：完整读取 [动作导演](references/fight-director.md)，按需读 [动作设计](references/fight-fight-design.md)、[动作摄影](references/fight-camera-guide.md)、[动作诊断](references/fight-diagnostics.md)。人兽战、兽袭、群兽围攻默认走 fight-director 的高强度奇观编排（升级式奇观纲要+行为与交互铁律栏+按回合升级分镜+禁收势尾帧+负面提示词栏），并保留因果交锋、双向攻防与真实受力。支持 Seedance、MiniMax-H3 及通用模型。
5. Higgsfield 任务：完整读取 [平台制作指南](references/higgsfield-guide.md) 与下表匹配的模块，提示词任务另读 [提示词构建](references/higgsfield-prompt.md) 并按其 Load Map 加载。人物出现时加载表演与 FACS；剧情改写加载场景引擎；多场景或分镜加载拆镜模块；对白、声效或音乐加载音频模块。
6. 交付前按「提示词内容边界」将内部规划转成正向描述，再执行「输出验证关卡」，检查素材职责、身份、数量、时序、动作因果、连续状态、本镜声源、模型限制及适用约束；修复文本失败项后交付并附验证结果。失败迭代按当前素材诊断，每轮只改一类变量。

### 缺素材、参数冲突与样本退回

| 触发条件 | 处理 |
|---|---|
| 无 `asset-registry.json`，或登记名有而文件未交付 | 从已确认交付建总表，无文件条目标待生成/待绑定；逐项核对 `status`、`file` 与本片段平台绑定。只有名称而无文件/绑定的资产按未绑定处理，只列进规划清单，正文用中文名描述，可提交提示词仅用真实可用标签。无法核实名称时问原名。 |
| 只有少量参考且未提供其内容，或参考与模型限制冲突 | 按角色身份、道具结构、场景布局、动作、声音等职责登记为普通参考，不因数量少转起点画面模式。给只描述已知内容的条件性样本，块外标待核对文件与绑定；参考视频里的多主体不等于本片主体数量。无法读取关键参考时仍交可评估的条件性样本+待补清单。 |
| 本批次样本被要求修改或确认范围不明 | 只修订受影响的样本并标新版本；联合批次同时核对配套视频与布局，已确认且未变的资产直接复用。 |

## 提示词内容边界

**内部核对剧情，提交正文只写本次要生成的内容。**适用于资产、视频、样本、完整稿及原生 JSON 的生成字段；规则用于助手判断，不逐字附进提示词。

1. **先定生成范围再选内容。**写每个生成片段前，内部列出各时段应出现的角色、道具、状态与必要声音及其进入/取得/离开/丢失节点。项目总表是可用资产目录，不是本镜出场表；只在后续片段出现的对象、状态、标签不进入当前复制块，本片段需要的画外声音照常保留。
2. **把禁令还原为当前事实。**「X 不要提前出现」作为内部时序检查，不转抄进提示词：当前范围无需 X 就直接省略 X 及其别名、标签、倒影等变体，不另编内容凑正向句。
3. **片段内晚登场用正向时序。**对象在同一次生成内出现时，资产栏列其职责与登场时段，分段演出在相应节点写入画、取得、交接及状态变化，用"节点前实际持有/场外状态"表达而非"不要提前出现"。例：后续镜头才出现的父亲折刀，当前镜头只写"阿莉娅沿河岸行走、双手摆动"。
4. 资产的无文字/水印、无头取景、用户要求的静音等输出规格仍按对应格式保留；参考图夹带本镜不需要的对象时，块外指出需裁切/清理/更换，正文只用已确认的目标外观与动作。

## 电影视觉参考匹配

- 剧情项目的场景资产或视频提示词，先按题材、环境、情绪、动作规模匹配一部具体电影作主视觉参考；用户指定优先，未指定给一个推荐并融入本批次样本。
- 把参考转成可执行的色彩、光源反差、构图尺度、空间纵深、材质与空气质感，按日/夜/室内适配，同一项目保持一致；只报片名或"大片感"不够。参考只负责视觉语言，不搬原片角色、生物、军械、载具、地标。
- 无实际参考图时标为文字风格参考，按样本确认流程交付。详见 [视觉风格](references/higgsfield-style.md#电影视觉参考匹配)。

## 资产规范：最小化、命名与衍生图

1. **只为多次出现或剧情重要的对象建独立资产图。**承担身份识别、动作连续性或关键剧情功能的角色、生物、植物、道具、场景可建；一次性、可由提示词直接描述的对象（普通守卫、临时道具等）不单独建。
2. **按职责拆分，四类短前缀：**`S`=场景，`C`=角色，`B`=生物/植物，`P`=道具。专属物件（直升机、标枪等）作 `P`，异兽/捕食植物作 `B`，各自独立调用。
3. **场景图是干净环境图：**只含地形、结构、植被、光线、天气与可行动区域，不含角色、动物、专属道具、影子、文字。
4. **`B`/`P` 单独制作，不混入具体剧情场景。**以主体及结构为主，与角色资产一样使用干净浅色/浅灰背景，不带任何场景、环境道具、人物、影子或叙事地面接触。基础资产提供多视图与结构展示（生物：中性姿态的侧面全身主视图+头部特写+1–3 处结构局部；道具：主视图+补充角度+部件材质局部），版式与示例见 [生物/道具资产多视图规范](references/template-character-asset-delivery.md#7-生物道具资产的多视图与结构)。角色与 `B`/`P` 统一用干净浅色背景，`B`/`P` 在视频提示词中通过 `@` 名叠加到 `S` 场景上。
5. **统一简短稳定调用名：**`@S01_River`、`@C_Alia`、`@B_Anaconda`、`@P_Spear`；实际文件名如 `C_Alia_v01.png`。视频提示词调用稳定 `@` 名，资产更新只替换绑定文件版本。
5.1 **资产以名称指称、不用序号代号：**面向阅读的资产清单、设定列表与视频提示词的【资产与参考锁定】栏一律**直接用资产中文名**，不加数字序号代号。资产提示词分节标题格式为 `# 名称（@handle）`（如 `# 猿人（@C_Ape）`）。`@handle` 只是绑定调用名：登记在总表、在实际生成绑定时使用；面向阅读的正文不必写 `@handle`，未生成阶段用中文名描述即可。不再维护额外的资产序号字段。
6. **基础阶段只做基础资产图。**伤势、湿污、破损、开合、战斗等状态用"基础图 → 图生图 → 状态衍生图"（如 `C_Alia → C_Alia_Injured`），衍生图保持基础资产的身份、体型、材质、颜色与关键辨识特征。
7. **视频提示词分开声明资产职责**，从总表提取本镜条目、不重命名，缺项标待补齐。规划格式示例：

```text
【场景】@S11_RiverBank
【角色】@C_Alia @C_Father
【生物】@B_Anaconda
【道具】@P_FamilyCloth
```

资产只负责身份、结构与视觉一致性；动作、状态写入视频提示词或图生图衍生。资产与视频共用同一份总表及场景布局；联合批次同批交付，单类型请求保持原范围。登记规范见 [总表规范](references/asset-registry.md)。

## 按场景分批，资产与视频配套

- 完整制作默认一个场景或连续剧情段落为一批；本批包含所需资产与对应视频提示词，分别放独立代码块。片段过多时按完整演出负荷再分小批，已交付的共享资产只引用。明确只要资产或视频时只交该类。
- **Clip 编号标准（批-序，强制）：**每个视频片段编号为 `批-序`，即“第几批-该批内第几个”，如 `1-1`（第1批第1个）、`4-6`（第4批第6个）、`11-3`（第11批第3个）。批次对应场景/连续剧情段，序号在该批内从 1 累加。Clip 标题写成 `# Clip 批-序｜<片段名>`；`project.md` 的 Clip 序列表用单列“编号(批-序)”。新增或插入片段时按所属批次与批内次序给号，同步更新 `视频.txt` 标题与 `project.md` 序列表。
- 本批固定顺序：范围与片段号 → 资产总表及场景布局 → 新增/需修改的资产提示词（S/C/B/P 分项）→ 对应视频提示词（七栏目，时间戳内写运镜）→ 待生成/待绑定与检查结果。生成片段以接近30秒为编排目标，片内镜头和细节照常展开，执行时核验实际模式时长范围。
- 给出本批次类型与范围、样本版本、可复制样本、预期效果与确认请求，然后停下。用户提修改先改样本再等确认；仅文字时不声称已生成或已验收。
- 联合批次先给一组配套样本，统一确认本批名称、造型、布局与视频演出；确认后完整交付本批，再等待用户继续下一批。仅确认某一资产时仍按该确认范围处理；已确认且未变的资产跨批次直接复用。
- 批量输出多镜时每镜保持与首镜同等分段密度（时间戳粒度与画面/运镜/声音细节一致），不因靠后而合成长段或压缩成概括；确属动作更简单才减段。
- 角色资产样本默认单角色完整六行组板（左侧正面面部、右侧无头正面/侧面/背面），用户明确要仅定脸或半身时才用局部样本；已指定或纠正的版式持续继承。

## 输出验证关卡

**CHECKPOINT：文本检查失败先修复再交付；「预期效果」不替代「验证结果」。此关卡由助手执行，不新增用户审批。**

1. 提取本轮交付约束：类型、范围、版式、已确认身份/服装、状态、时长、素材可用性；区分用户已确认项与助手候选设计。样本只截代表性内容，不把整段剧情压进样本时长。
2. 角色六行组板交付前按 [角色资产模板](references/template-character-asset-delivery.md#六行结构自动校验) 的校验函数核对六行结构与顺序，报告并修复失败项；用户指定的其他格式不套此检查。
3.0 **对白覆盖核对（合并/拆分/改编片段时强制）：**把确认稿（剧本）里的所有台词逐句列成清单，逐句勾到对应 Clip 的【分段演出】`对白：` 行；每句落在其发生的 beat、写成 `对白：<说话人：台词>`，不得只写进动作或声音描述。无台词片段显式标注“本段无对白（设计）”，不靠“没写”默认。合并批次、精简或改编后若某句找不到落点即视为遗漏，必须补回或说明删改理由。
3. 语义核对：基础角色按已确认基础造型呈现，剧情状态与道具按发生/取得/持有/丢失节点核对；遍历全部可复制字段，发现否定句点名范围外对象时删除该句或按「提示词内容边界」改成当前事实。右侧无头为取景裁切，保留颈根以下至鞋底。名称/文件/status 按总表逐项检查，缺项如实记为待补齐。
4. 场景资产和视频空间描述从同一份布局记录取值（见总表规范），使用已约定坐标或地标相对位置。文字布局标“待出图核对”；实际场景图出来后核对数量、位置和可通行区域，再修图或经确认同步视频。
5. **调用名一致性（含 `@` 的提示词交付前必做）**：读项目 `asset-registry.json`，对总表运行 `seedance_lint.py --asset-registry` 核对每个 `@handle` 是否登记且逐字一致；缺表或读不到时标「跨批次未核对」、不把逻辑调用名写进可提交提示词，只给中文名描述的条件性方案；资产批次交付时把总表作为交付物回传。
6. 附验证记录：`对象与版本｜自动检查结果｜语义核对与待确认设计｜生成/视觉验收状态｜lint 与总表状态`。引用实际运行或阅读证据；无子代理时报单代理核对或 dry_run，无生成结果时写「未生成，视觉未验收」，不虚报独立投票、full_test 或效果通过。

| 触发条件 | 修复 |
|---|---|
| 六行或视图检查失败 | 修正同一样本重跑检查，不以「符合规范」交付失败版本 |
| 字面通过但状态/道具与剧本冲突，或否定句泄漏范围外对象 | 删泄漏句及标签，片段内确需出现的改成正向登场/状态变化，再检查所有字段 |
| 批量后段镜头分段变长、节点骤减或细节明显少于前镜 | 视为密度退化，按首镜密度重写；确属动作更简单减段的在分配表注明依据 |
| 生成图右侧仍有头部或身份漂移 | 按模板局部修复并保留已确认面部，未修复前不标视觉通过 |
| 读不到总表或 `@` 名与总表对不上 | 取得或重建总表并逐字对齐 handle，改正后重跑 lint；始终不可得时只交条件性方案并标「跨批次未核对」 |

## 默认值与输出

- 缺省 Seedance 2.5、16:9、中文。时长继承用户预算；未指定时生成片段默认以模型单次上限（约 30 秒）为目标，单片段承载连续多阶段动态，相邻镜头优先合并进一次近 30 秒生成，靠真实连续动作填满而非放慢或留白注水；长动作超上限才分段接续。编辑继承母片时间线，延伸只估算新增内容。
- **对白单列在分段：**台词一律写在【分段演出】对应 beat 的 `对白：<说话人：台词>` 行，动作与声音描述不重复承载台词；跨批次合并、精简或改编时按上述“对白覆盖核对”逐句回对确认稿，防止台词被并进散文而丢失。无台词片段显式标注“本段无对白（设计）”。
- **【资产与参考锁定】栏只列名称：**该栏按 角色/生物/道具/场景 分组，只列出本片段出现的**资产中文名**（如“角色：艾莉娅、猿人”），不写序号、不展开采用属性/保留程度/服装状态等描述——身份与结构由对应资产图承担，状态与连续性写在分段演出与关键约束里，视觉/声音/时段写在全局视听栏。有真实参考素材需排除背景/多视图时，把排除项放在块外说明，不塞进该栏。
- 完整视频按七栏目交付：资产与参考锁定、一句话总合成、全局视听与空间、主体行为与节奏规则、分段演出、结尾状态与交接、关键约束与排除。全局规则写一次，分段写行动、响应及同时/先后/触发/持续等时序关系；身份、数量、归属、朝向、损伤、破坏累计等跨段状态继承融入分段演出的段间承接与关键约束的数量/身份锚点，不单列连续性栏。每个分镜只指定本镜实际需要的声源，跨镜声场一致性由后期处理；默认 NO BGM。**模型、画幅、时长、速度等平台设置写在提示词代码块之外，正文不另加【模型与规格】【规格】等栏目。**
- 样本确认后动作默认交付高强度、慢节奏、中间型三套方案；标准/极速为独立速度轴，用户只选一套则只交该套。完整参数见 [导演编排](references/directing-workflow.md)。
- 角色资产完整读取 [角色资产模板](references/template-character-asset-delivery.md)，保留六行提示词、左侧面部与右侧无头三视图、身份与材质锁定及无文字要求。
- 原生 HTML 分镜、代码动画、纯音频、图像及 [双语 JSON](references/seedance-bilingual-json.md) 按对应格式交付，默认无字幕、无水印、无未要求的旁白。
- 参数来自对应模型资料，快照过期或无法核验时标待核验；当前环境仅处理本地文本并提供执行交接，不把外部操作写成已完成的生成或验证。

## 按任务读取

| 任务 | 参考文件 |
|---|---|
| 跨会话继承剧本与资产、项目工作区 | [project-workspace](references/project-workspace.md) |
| 选择平台工作区或工具 | [higgsfield-workspaces](references/higgsfield-workspaces.md) |
| 提示词写作、改写、MCSLA | [higgsfield-prompt](references/higgsfield-prompt.md) |
| 图像景别、构图与角度 | [higgsfield-image-shots](references/higgsfield-image-shots.md) |
| GPT Image、UI、信息图与参考表 | [higgsfield-gpt-image-2](references/higgsfield-gpt-image-2.md) |
| 模型选择与比较 | [higgsfield-models](references/higgsfield-models.md) |
| 摄影机运动与控制 | [higgsfield-camera](references/higgsfield-camera.md) |
| 命名运动预设与 VFX | [higgsfield-motion](references/higgsfield-motion.md) |
| 视觉风格 | [higgsfield-style](references/higgsfield-style.md) |
| Soul ID、角色一致性 | [higgsfield-soul](references/higgsfield-soul.md) |
| 人物、世界、故事、视觉 DNA、试演 | [higgsfield-character-design](references/higgsfield-character-design.md) |
| 场景目标、障碍、策略、反转和价值变化 | [higgsfield-scene-engine](references/higgsfield-scene-engine.md) |
| 一键 App | [higgsfield-apps](references/higgsfield-apps.md) |
| 类型配方 | [higgsfield-recipes](references/higgsfield-recipes.md) |
| 失败生成诊断 | [higgsfield-troubleshoot](references/higgsfield-troubleshoot.md) |
| 情绪板、色彩与项目一致性 | [higgsfield-moodboard](references/higgsfield-moodboard.md) |
| 混合媒介、艺术变换、预设叠加 | [higgsfield-mixed-media](references/higgsfield-mixed-media.md) |
| Assist、预算、额度和套餐 | [higgsfield-assist](references/higgsfield-assist.md) |
| Cinema Studio、镜头物理、Hero Frame、Elements、Soul Cast | [higgsfield-cinema](references/higgsfield-cinema.md) |
| Higgsfield Canvas 节点画布及协作 | [higgsfield-canvas](references/higgsfield-canvas.md) |
| 多镜头、短片、工具串联与接续 | [higgsfield-pipeline](references/higgsfield-pipeline.md) |
| Vibe Motion / Remotion 可编辑代码动画 | [higgsfield-vibe-motion](references/higgsfield-vibe-motion.md) |
| 对白、音效、环境声、独立音频与 TTS | [higgsfield-audio](references/higgsfield-audio.md) |
| Seedance 2.0/Pro、延长、过滤检查、HELL-GRIND 制片流程 | [higgsfield-seedance](references/higgsfield-seedance.md) |
| Seedance 2.5、多参考、编辑、延伸、VFX 全流程 | [higgsfield-seedance-2-5](references/higgsfield-seedance-2-5.md) |
| 真实源视频的特效、背景、光色和定时运镜 | [higgsfield-seedance-vfx](references/higgsfield-seedance-vfx.md) |
| 人物行为、身体表演、眼神、潜台词与声音档案 | [higgsfield-acting](references/higgsfield-acting.md) |
| 剧本拆镜、全局风格、@ 素材表、可编辑 HTML | [higgsfield-shotlist-director](references/higgsfield-shotlist-director.md) |
| 面部 FACS、AU 与微表演 | [higgsfield-facs](references/higgsfield-facs.md) |
| CLI、MCP、费用预检与执行交接 | [higgsfield-stack](references/higgsfield-stack.md) |

## 参数、模板与检查

- 模型参数：[视频](references/MODEL-SPECS.md)、[图像](references/IMAGE-MODEL-SPECS.md)、[音频](references/AUDIO-MODEL-SPECS.md)。其他：[模型选择](references/model-guide.md)、[图像模型方法](references/image-models.md)、[摄影词汇](references/vocab.md)、[提示词示例](references/prompt-examples.md)、[Photodump 预设](references/photodump-presets.md)。
- 题材、站位、地图、文字叠加与各模式模板在 references/template-*.md，按 [平台制作指南](references/higgsfield-guide.md) 选用。
- [共享约束](references/negative-constraints.md) 作为内部诊断菜单，按「提示词内容边界」转成当前镜头必要的正向描述，不直接追加预防词句；[制作检查](references/production-checks.md) 用于交付与单变量迭代。
- 本地提示词检查（Python 标准库，从 skill 根目录运行）：

```bash
python3 scripts/seedance_lint.py --preflight --model seedance_2_5 --file /path/to/prompt.txt --asset-registry /path/to/project/asset-registry.json
```

覆盖过滤风险、结构及已知模型参数；传 `--asset-registry` 时另做跨批次名称核对。脚本不代替身份语义核对、真实绑定检查与视觉验收。

用户素材从其实际路径读取，生成文件写入用户项目目录；不移动原始素材，不向 skill 安装目录写项目文件。接收其他创作包的确认稿时保留 copyVersion、正文、人物世界设定、不可改项与待定制作规格。

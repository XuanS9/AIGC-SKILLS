---
name: video-script-studio
description: 将剧本、图片、首尾帧、分镜与参考视频编排成资产提示词、视频脚本、镜头清单及可复制提示词；资产与视频按用户请求分开写，每次先给对应类型的样本，用户确认后再输出本批次全部提示词。适用于打斗、追逐、人兽战、剧情、人物表演、角色资产、摄影、音频、Seedance、模型选择、VFX、Cinema、Canvas 与生成问题诊断；支持三强度两速度动作设计、多参考、视频编辑延伸及双语 JSON 交付。
---

# 视频脚本工作室

## 工作流程

1. 继承用户已确认的角色、剧情、结局、对白、模型、时长、画幅、语言、速度及素材。缺少非关键参数时采用默认值；只补问会影响执行的缺失信息。
   资产、视频、分镜及其改写任务均先完整读取 [项目资产总表](references/asset-registry.md)，读取用户项目内同一份 `asset-registry.json`；没有总表时从已确认交付及实际素材建立。样本和完整稿逐字复用已有调用名，交付前对表核对；分开生成不另起名称。
   提示词任务先完整读取 [样本确认流程](references/sample-approval.md)，识别本次类型：要求资产只写资产，要求视频只写视频；同时明确要求两类时分成独立批次，分别给样本、确认和交付。每次先交本次类型的代表性样本及预期效果，停止并等待用户明确确认，再输出对应批次全部提示词；新请求、改写、补镜、修词及单条交付均适用，历史确认不替代本次确认，不设跳过样本的例外。
2. 视频创作、改写、分镜、编辑或延伸：先区分剧情段落、镜头与模型生成片段，按观看任务、动作因果及表演负荷决定切点与时长，不向30秒或模型上限凑段；具体方法执行 [按内容拆镜与估时](references/narrative-planning.md#按内容拆镜与估时)。完整读取 [导演编排与交付](references/directing-workflow.md)、[叙事规划](references/narrative-planning.md)、[八栏目模板](references/template-general-director-2-5.md)；完整创作和改写还需完整读取 [演出范本](references/template-full-performance-example.md)。
3. 打斗、武打、追逐、对抗、演武、人兽战：完整读取 [动作导演](references/fight-director.md)，按需读取 [动作设计](references/fight-fight-design.md)、[动作摄影](references/fight-camera-guide.md)、[动作诊断](references/fight-diagnostics.md)。支持 Seedance、MiniMax-H3 及通用模型。
4. Higgsfield 任务：完整读取 [平台制作指南](references/higgsfield-guide.md) 和下表匹配的模块。提示词任务另须完整读取 [提示词构建](references/higgsfield-prompt.md)，按其 Load Map 加载模型与任务资料。联合动作任务先编排动作因果、空间和角色状态，再转换为平台格式。
5. 人物出现时加载表演与 FACS 身体微反应；剧情改写加载场景引擎；多场景或分镜加载拆镜模块；对白、具体声效或音乐同步加载音频模块。非动作任务沿用对应原生流程。
6. 交付前检查素材职责、人物身份、数量、时序绑定、动作因果、连续状态、实际模型限制及适用约束。失败迭代根据当前素材诊断，每轮只改一类变量。

## 电影视觉参考匹配标准

- 为剧情项目编写场景资产或视频提示词前，先按题材、世界环境、情绪和动作规模匹配一部具体电影作为主视觉参考；用户指定的参考优先，已有选择直接继承。用户未指定时给出一个推荐，并融入本批次样本，不新增独立审批步骤。
- 不能只写“大片感”“电影级”或只报片名。必须把参考转化为可执行的色彩、光源与反差、构图与尺度、空间纵深、材质与空气质感；按日景、夜景和室内条件适配，同一项目保持视觉一致。详细方法见 [视觉风格](references/higgsfield-style.md#电影视觉参考匹配)。
- 参考只负责视觉语言，不覆盖已确认的人物身份、服装、时代、剧情、空间和画幅，不自动搬用参考电影的角色、生物、军装、载具、地标或场面。场景资产仍为纯环境图；角色、B/P 孤立资产沿用各自背景规范，不为匹配电影而增加叙事背景。
- 示例：《绝境雨林》的雨林场景以《金刚：骷髅岛》（Kong: Skull Island，2017）为主视觉参考，提炼巨物尺度感、厚重热带植被、暖色日光与深绿阴影、潮湿材质及分层薄雾。皇室贵族度假身份与服装保持；不引入原片军事元素。此例仅适用于匹配的项目，不作为所有题材的固定画风。
- 片名是创作方向，不等于已上传视觉参考、平台预设或效果已验证。没有实际参考图时标为文字风格参考，不虚构素材槽位；仍按当前批次样本确认流程交付。

## 资产最小化、命名与衍生图规范

1. **只为多次出现或剧情重要的对象制作独立资产图。**反复出现、承担身份识别、动作连续性或关键剧情功能的角色、生物、植物、道具和场景，可以制作资产图；一次性、非关键、可由提示词直接描述的对象不单独制作资产图。普通守卫、医护、驾驶员、临时搬运人员、普通树枝、碎木和一次性文件等，默认不建立独立资产。
2. **资产按职责拆分，不混合制作。**使用四类短前缀：`S` = Scene 场景，`C` = Character 角色，`B` = Beast 生物/植物，`P` = Prop 道具。
3. **场景图必须是干净环境图。**场景图只包含地形、建筑或固定空间结构、植被、岩石、泥潭、固定环境、光线、天气、时间状态和可行动区域；不得包含角色、猿人、动物、异兽、捕食植物、专属道具、人物或动物影子、文字、数字、标牌或水印。直升机、运输笼、标枪、折刀等专属物件必须作为 `P` 资产独立调用；巨蚺、古鳄、翼兽、巨蛙和捕食植物必须作为 `B` 资产独立调用。
4. **`B` 与 `P` 默认制作孤立资产图，不携带叙事背景。**生物、植物和道具图只表现主体本身及其必要结构，不放雨林、泥潭、树枝、水面、笼舍、战斗现场等场景背景，不加入环境道具、人物或动物，不保留叙事性地面接触和环境影子。默认使用透明背景；若当前图像工具不能可靠输出透明通道，则使用无纹理纯浅灰背景作为临时承载底，并在交付中标记“待抠图”，不得把纯色底误当成场景背景。植物若必须展示根系、附着结构或底部形态，只保留主体自身结构，不带土壤、树干或雨林环境。
5. **角色图与生物/道具图的背景规则分开。**角色组板可按角色资产模板使用干净浅色背景；`B` 与 `P` 不使用角色组板式场景，不加入布景、道具陈列或环境氛围。它们在视频提示词中通过 `@` 名称叠加到 `S` 场景上。
6. **统一使用简短稳定的调用名。**逻辑调用名使用：`@S01_River`、`@C_Alia`、`@B_Anaconda`、`@P_Spear`。实际文件名使用：`S01_River_v01.png`、`C_Alia_v01.png`、`B_Anaconda_v01.png`、`P_Spear_v01.png`。视频提示词调用稳定的 `@` 名称，不直接依赖版本号；资产更新时只替换实际绑定文件版本，不修改全部视频提示词。
7. **本阶段只制作基础资产图。**伤势、湿污、破损、囚禁、开合和战斗状态等衍生图不在基础资产阶段展开，也不默认批量生成。后续需要时，必须采用“基础资产图 → 图生图 → 状态衍生图”，例如：`C_Alia → 图生图 → C_Alia_Injured`、`C_Ape → 图生图 → C_Ape_Caged`、`P_Cage → 图生图 → P_Cage_Open`。衍生图必须保持基础资产的身份、体型、材质、服装、颜色、结构和关键辨识特征。
8. **视频提示词分开声明资产职责。**从项目资产总表提取本镜条目，不重新命名。以下仅为规划格式示例，实际提示词须核对素材可用状态及真实平台绑定；缺项标记待补齐，不伪装成已绑定资产：

```text
【场景】
@S11_RiverBank
【角色】
@C_Alia
@C_Father
【生物】
@B_Crocodile
@B_Anaconda
【道具】
@P_FamilyCloth
```

资产只负责身份、结构和视觉一致性；动作、伤势、湿污、破损、开合和即时状态写入视频提示词，或在后续阶段通过图生图建立状态衍生资产。资产图与视频提示词仍按本 Skill 的样本确认流程分开交付，但必须共用同一份项目资产总表；资产确认不自动授权视频提示词交付。中文名称、稳定调用名、实际文件与可用状态按 [总表规范](references/asset-registry.md) 登记；项目调用名与平台槽位分别记录。

## 分类型写，先样本后完整提示词

- 资产请求只给角色、道具或场景资产样本；视频请求只给镜头或短片段样本。视频可说明已有资产与缺项，不附资产生成提示词；资产交付后不自动进入视频阶段。类型不明且上下文无法判断时先澄清。
- 给出本批次类型与范围、样本版本、可复制样本提示词、预期效果及确认请求，然后停止。用户提出修改时先改样本，再等待确认；仅有文字时不声称已经生成样图/样片或验证实际效果。
- 用户确认本批次当前样本后，直接输出该类型、该范围的全部提示词，不重复要求样本确认。新一轮提示词请求重新给样本；资产和视频各自确认，一类的确认不授权另一类。
- 完整输出的格式、三强度方案、角色六行与多视图等要求在本批次确认后执行；模块中直接交付、工具自动串联或无附言的建议不得绕过本流程。详情与原生 JSON 等格式适配见 [样本确认流程](references/sample-approval.md)。

## 默认值与输出

- 用户明确要求优先。模型、画幅和提示词语言缺省采用 Seedance 2.5、16:9、中文。时长继承用户已确认的全片及局部预算；未指定时按内容自然估算，不默认30秒，不把模型单次上限当目标。每镜可长可短，也可与其他镜头共用一次生成；不能均分、凑近30秒、机械翻倍或为填时长放慢动作。编辑继承母片时间线，延伸只估算新增内容，并遵守相应模式限制。
- 普通完整视频按八栏目交付：资产与参考锁定、一句话总合成、全局视听与空间、主体行为与节奏规则、分段演出、连续性、尾帧、关键约束与排除。全局规则写一次，保留分段行动、响应及同时/先后/触发/持续等时序关系。
- 样本确认后，动作默认交付高强度、慢节奏、中间型三套完整方案；标准/极速为独立速度轴。用户只选一套则只交该套。完整参数、角色资产格式及交付检查见 [导演编排与交付](references/directing-workflow.md)。
- 角色资产完整读取 [角色资产模板](references/template-character-asset-delivery.md)，保留六行提示词、左侧面部与右侧无头三视图、身份与材质锁定及无文字图像要求。
- 原生 HTML 分镜、代码动画、纯音频、图像及 [双语 JSON](references/seedance-bilingual-json.md) 按对应格式交付；同一内容不重复附加长稿。默认无字幕、无水印、不添加未要求的旁白。
- 参数和专有术语来自对应模型资料；快照过期或无法核验时明确待核验项。当前环境仅处理本地文本并提供执行交接；不把外部操作参考写成已经完成的生成或验证。

## 按任务读取

| 任务 | 参考文件 |
|---|---|
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

- 模型参数：[视频](references/MODEL-SPECS.md)、[图像](references/IMAGE-MODEL-SPECS.md)、[音频](references/AUDIO-MODEL-SPECS.md)；各自同名小写 JSON 保留完整机器参数和快照日期。
- [模型选择](references/model-guide.md)、[图像模型方法](references/image-models.md)、[摄影词汇](references/vocab.md)、[提示词示例](references/prompt-examples.md)、[Photodump 预设](references/photodump-presets.md)。
- 题材、角色设定、站位、地图、文字叠加和各模式模板在 references/template-*.md，按 [平台制作指南](references/higgsfield-guide.md) 和模块内链接选用。
- 使用 [共享约束](references/negative-constraints.md) 时只选择当前镜头适用的条目，避免重复锁定；[制作检查](references/production-checks.md) 用于交付和单变量迭代。
- 本地提示词检查使用 Python 标准库，从 skill 根目录运行：

```bash
python3 scripts/seedance_lint.py --help
python3 scripts/seedance_lint.py --preflight --model seedance_2_5 --file /path/to/prompt.txt --asset-registry /path/to/project/asset-registry.json
```

检查覆盖过滤风险、结构及已知模型参数组合；传入 `--asset-registry` 时另做跨批次资产名称核对，未传时明确提示未核对。脚本不能代替正文身份语义核对、真实素材绑定检查、视觉验收或实时平台验证。中文长度告警按对应提交格式解释，保留完整母稿。

用户素材从其实际路径读取，生成文件写入用户项目目录；不移动原始素材，不向 skill 安装目录写入项目文件。接收其他创作包的确认稿时保留 copyVersion、正文、人物世界设定、不可改项和待定制作规格。

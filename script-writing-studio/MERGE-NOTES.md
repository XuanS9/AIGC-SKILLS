# 剧本创作整合说明

来源：`剧本创作/script-writing-studio`。该目录本身已有单一入口，因此保留原结构及全部内容，没有重新压缩其创作规则。整合后的包仍名为 `script-writing-studio`。

## 文件与功能保留

全部 25 个源文件按原相对路径保留。除在 `SKILL.md` 末尾追加独立安装与交接兼容说明，其余 24 个源文件逐字不变。

| 资料 | 保留的功能 |
|---|---|
| `SKILL.md` | 3–30 分钟奇幻人兽斗定位、成年角色边界、变化密度、因果与悬念、故事梗概表确认、导演预演、默认格式与版本交付 |
| `references/00-preflight.md` | 写作前核对、继承已确认条件、缺项与范围管理 |
| `references/01-story-development.md` | 灵感、世界观、人物、大纲与故事开发 |
| `references/02-screenplay-writing.md` | 正文、续写、重写与完整动作细节 |
| `references/03-writing-intake.md` | 创作需求与材料接收 |
| `references/04-screenplay-format.md` | 剧本总表、场次表与正文格式 |
| `references/05-dramatic-pacing.md` | 节奏与有效变化 |
| `references/06-writing-delivery.md` | 交付契约、完整替换稿、版本及状态 |
| `references/07-writing-boundaries.md` | 创作边界与保留项 |
| `references/08-script-review.md` | 剧本会诊 |
| `references/09-review-intake.md` | 会诊需求与诊断范围 |
| `references/10-review-methods.md` | 审稿方法 |
| `references/11-review-panels.md` | 多维评审 |
| `references/12-review-handoff.md` | 会诊、回稿、文案确认与制作交接 |
| `references/13-dialogue-polish.md` | 对白、潜台词与人物语言精修 |
| `references/14-knowledge-storytelling.md` | 知识叙事与事实附注 |
| `references/15-dramatic-tension.md` | 戏剧张力、冲突与悬念 |
| `references/16-copy-confirmation.md` | 来稿再创作与重大方向确认 |
| `references/17-history-facts.md` | 历史、真实人物与事实改编 |
| `references/18-professional-facts.md` | 专业知识、安全与技术核验 |
| `references/19-runtime-structure.md` | 片长、段落时长与开场节奏 |
| `references/INDEX.md` | 任务路由、读取顺序与资料性质 |
| `agents/openai.yaml` | 原界面信息 |
| `tests/story-writing-cases.md` | 原创作验收案例 |
| `tests/validate_skill.py` | 单入口、相对链接与路由结构验证 |

## 外部交接

源文件提到的 `script-package-production`、`canvas-production` 没有随原文件提供，原本就是外部可选路由。本次保留名称并在入口注明能力缺失时的交接方式；另将本次 `video-script-studio` 纳入其能力范围内的可选制作交接。不将其等同于原外部工具的全部接口，也不让文案工作依赖另两个整合包。

## 校验

在本包目录运行 `python3 tests/validate_skill.py`。三套整合包外层另提供源文件清单及逐文件保留报告。校验确认结构与内容保留，不表示已经实际生成视频或验证模型服务。

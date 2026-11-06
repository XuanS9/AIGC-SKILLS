# 变更记录

规则正文只写当前规则；何时、为何改动记在这里。

## 2026-11-06

- 修复角色进出门编排缺少方向判据的问题：`spatial-layout.md`新增唯一负责的“门槛方向锁定”，按具名门两侧的起态→跨门→末态判断，不以进出画、朝向镜头或推拉门代替。
- 入口、加载路由、导演编译、交付模板及验收接入同一规则；替换空间转移中仅写出画/入画的旧例。定位秒保持起始侧，跨门只发生一次，切镜不重跨，独立Clip不在门槛中途断开。
- 新增两个6秒纯文字方向小样，加入真实契约/Seedance lint回归；人工语义回归覆盖进/出×门内/门外观察、拉门出门、室内房间门、跨完反打与场所不明。文档/文本检查不证明生成方向已通过，实际结果仍待视觉验收。
- 本轮验证：从Skill根目录运行 `python3 -m unittest discover -s scripts/tests -p 'test_*.py'`，137项通过，含两个方向小样的契约/Seedance检查及本地链接、锚点、围栏检查；`git diff --check`通过。最终改动仅为规则、示例与测试，未修改模型数据或用户项目；单代理人工回读两个小样的起始侧、跨门落脚与末态均与意图同向，八类语义情境按§3.2逐项核对，未执行视频生成。

- 对白照 Higgsfield 写在 `[声音]`：每句一行 `起s-止s｜说话人＋状态＋说：{English line}`；`[具体情节]` 段内不再写 `对白：` 行。lint 同步。
- 每条有人物的 Clip 第一秒加 hm：`[声音]` 写 `0s-1s｜<名字>轻声：{Hm.}` 锁定站位；`恰好 0 人` 不写。lint 缺失报 FAIL。
- 删除与剧本→Seedance 视频提示词无关的平台模块：Soul、Cinema、Canvas、Vibe Motion、Apps、Assist、Photodump、Mixed Media、Moodboard、Motion 预设、Workspaces、Stack、Pipeline、Recipes、prompt-examples、模型深度参考、VFX 首帧。
- 仙侠范本改写成当前块结构，拆成两条 Clip（`template-action-example-xianxia.md`）。
- 入口 SKILL.md 精简为契约与路由；细则下放到负责模块（文件命名 → asset-registry，纯环境场景图 → spatial-layout，角色组板 → template-character-asset-delivery）。
- 测试改为行为测试（范例跑两个 lint）和跨文件冲突扫描，删除只核对原话的测试。
- 动作导演的时长目标改为“接近所选模型的单次上限”。
- 调用的上游英文参考译成中文。

## 2026-11-05

- 完整视频改为 Higgsfield 块结构，块标签、字段与描述用中文，只有对白原句用英文；英文块标签与旧四段式停用。
- 取消字数上限；1800 字只属于双语 JSON 格式。
- 视频只用 Seedance 系列；其他视频生成模型与后期视频工具移除。

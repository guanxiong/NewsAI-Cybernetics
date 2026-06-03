# Agent Principles & Logic

## 1. 核心指挥原则 (Core Directives)
- **唯一真理**: `AGENTS.md` 是本目录及其子目录行为逻辑的唯一完整版。`CLAUDE.md` 和 `GEMINI.md` 仅作为重定向符号存在。
- **渐进披露**: 子目录的 `AGENTS.md` 仅实现该层级的差异化逻辑。
- **驾驭工程 (Harness Engineering)**: 所有的文件操作（导入、创建、更新、维护）必须遵循 `harness-engineering` 思想，确保工作流的可追踪性与可维护性。

## 2. 工程控制论核心逻辑 (Engineering Cybernetics)
依据钱学森《工程控制论》，本系统采用以下控制策略：
- **稳态控制**: 确保信息处理系统不因过载而崩溃，通过“筛选”环节维持系统的处理熵。
- **反馈闭环 (PDCA)**: 遵循 PDCA 原则，定时持续循环迭代。每次重大变更或任务阶段结束，必须更新 `VERSION.md`，记录计划、执行、检查与改进动作。
- **引导控制**: 优先通过自动化（API/Browser）获取高质量、可信源信息，而非被动接收。

## 3. News 价值过滤模型 (4-Layer Model)
所有处理的消息必须被贴上以下 YAML 标签之一：
1. `Tier: 1-Core-Decision` (生存/重大利益相关的即时行动)
2. `Tier: 2-Cognitive-Framework` (塑造长期世界观的深度阅读)
3. `Tier: 3-Social-Connection` (低频浅处理的社交货币)
4. `Tier: 4-Professional` (针对具体问题的知识学习)

## 4. 信息处理闭环 (5-Step Loop)
1. **获取 (Acquire)**: 权威源主动订阅。
2. **筛选 (Filter)**: 以“是否影响未来3个月决策”为初筛标准。
3. **处理 (Process)**: 根据分层层级，决定即时行动或深度思考。
4. **沉淀 (Precipitate)**: 转化为行动、知识或观点，存入个人库。
5. **淘汰 (Eliminate)**: 定期清理过时或无价值信息。

## 5. 执行记录规范 (Task Records)
- 每次启动前更新 `TASK.md` 建立 To-Do。
- 执行完每个 Todo 必须更新 `TASK.md` 勾选状态。
- Git 提交信息严格遵循：`brief: [Prompt], 交付物: [文件], 说明: [简述]`。

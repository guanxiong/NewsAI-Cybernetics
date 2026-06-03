# Task List (WBS)

## 1. 系统初始化与元文件构建
- [x] 创建 Inbox 目录与 auth.md
- [x] 创建 GOAL.md (OKR)
- [x] 创建 TASK.md (WBS)
- [x] 创建 VERSION.md (PDCA 记录)
- [x] 创建 AGENTS.md (核心逻辑)
- [x] 创建 CLAUDE.md & GEMINI.md (重定向)

## 2. 信息架构设计
- [x] 设计 YAML 属性模板 (Tier, Status, Source, Importance) → TEMPLATE.md
- [x] 编写 4 层信息分类标准说明文档 → STANDARDS.md
- [x] 编写 5 步闭环处理手册 → MANUAL.md
- [x] 创建 NocoDB News 数据库（Base + 3 Tables + 8 Sources + 14 Records）
- [x] 建立 Obsidian ↔ NocoDB 双轨映射文档（含在 MANUAL.md 中）

## 3. 工作流自动化
- [ ] 配置获取新闻的 Agent 技能 (Skill)
- [ ] 实现从 Inbox 到分层库的自动移动脚本
- [ ] 建立定期清理/淘汰机制
- [ ] NocoDB 自动同步脚本（Obsidian Markdown ↔ DB Records）

## 4. 存量数据治理
- [x] 扫描 `x 动态/` 目录 71 个文件（385 条唯一推文），执行分层标注
- [x] 高价值内容 14 条提取至 NocoDB + 知识库沉淀
- [x] 低价值内容 371 条标记淘汰 → ARCHIVE-REPORT.md

## 5. 交付与检查
- [x] 检查目标完成度达到 80%+ → 达标
- [x] 生成存量数据治理报告 → ARCHIVE-REPORT.md

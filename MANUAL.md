# 5-Step Loop 处理手册

> 本手册定义 News 系统从「获取」到「淘汰」的完整信息处理闭环。
> 关联文档：[[STANDARDS]]（分层标准）、[[TEMPLATE]]（笔记模板）、[[AGENTS]]（核心逻辑）

---

## 总览

```
获取(Acquire) → 筛选(Filter) → 处理(Process) → 沉淀(Precipitate) → 淘汰(Eliminate)
     ↑                                                              │
     └─────────────── PDCA 反馈闭环 ←──────────────────────────────┘
```

**时间约束**：Inbox 积压不超过 **24 小时**，超时未处理的信息自动标记为 `eliminated`。

---

## Step 1: 获取 (Acquire)

### 目标
从预设的权威信息源主动获取信息，存入 Inbox。

### 操作步骤
1. **Agent 自动采集**：通过浏览器自动化/API 定时抓取预设 Source（见 NocoDB Sources 表）
2. **手动采集**：用户遇到有价值信息时，复制 URL 或内容至 `Inbox/` 目录
3. **创建记录**：每条信息在 NocoDB `News Items` 表创建一条 `status: inbox` 记录
4. **写入 Processing Log**：记录 `Step: 1-Acquire`，`Executor: Agent/Manual`

### 筛选标准（初筛）
- ❌ 标题党/情绪化标题 → 直接淘汰
- ❌ 无来源/无法核实 → 直接淘汰
- ❌ 已有相同主题的重复信息 → 保留最新一条

### 数据流向
```
外部信息 → Inbox/ 目录 + NocoDB News Items (status: inbox)
```

---

## Step 2: 筛选 (Filter)

### 目标
用 **"是否影响未来 3 个月的决策"** 作为核心判据，为每条信息分配 Tier。

### 分层判定树
```
信息进入
  │
  ├─ 是否直接影响生存/安全/重大利益？ → Tier 1 (Core-Decision)
  │   例：极端天气、政策变动、行业巨变
  │
  ├─ 是否塑造长期认知/世界观？ → Tier 2 (Cognitive-Framework)
  │   例：国际局势、科技革命、宏观经济
  │
  ├─ 是否用于社交/情感调节？ → Tier 3 (Social-Connection)
  │   例：热点事件、娱乐八卦、体育赛事
  │
  └─ 是否解决具体专业问题？ → Tier 4 (Professional)
      例：技术文档、行业报告、工具教程
```

### 重要性评分
| Importance | 定义 | 处理优先级 |
|------------|------|-----------|
| 5 | 紧急且重要，需立即行动 | 立即处理 |
| 4 | 重要但不紧急，需深度思考 | 当天处理 |
| 3 | 一般价值，了解即可 | 批量处理 |
| 2 | 低价值，社交货币 | 每日 10 分钟扫盲 |
| 1 | 几乎无价值 | 直接淘汰 |

### 操作步骤
1. 读取 Inbox 中的待处理条目
2. 按判定树分配 `Tier` 和 `Importance`
3. 更新 NocoDB 记录的 `Tier`、`Importance`、`Tags` 字段
4. 更新 `Status` 为 `processing`
5. 写入 Processing Log：`Step: 2-Filter`

---

## Step 3: 处理 (Process)

### 目标
根据 Tier 层级执行对应的处理策略。

### 分层处理策略

#### Tier 1: Core-Decision（即时行动）
- **时效**：1 小时内必须转化为行动
- **动作**：
  - [ ] 明确需要采取的具体行动
  - [ ] 在 Obsidian 日记中创建 TODO
  - [ ] 行动完成后标记 `Action Taken: true`
- **原则**：行动完成即归档，不占用长期注意力

#### Tier 2: Cognitive-Framework（深度思考）
- **时效**：当天完成
- **动作**：
  - [ ] 找到至少 1 个与现有知识库的关联点
  - [ ] 记录不同立场的视角对比
  - [ ] 写出 1 段自己的独立判断
- **原则**：质量 > 数量，每条必须有独立的思考产出

#### Tier 3: Social-Connection（极简摘要）
- **时效**：每日 10 分钟批量处理
- **动作**：
  - [ ] 1 句话概括核心事实
  - [ ] 超过 7 天未产生价值的直接淘汰
- **原则**：知道即可，不深究

#### Tier 4: Professional（问题导向）
- **时效**：需要时才调取
- **动作**：
  - [ ] 关联到具体的专业问题或项目
  - [ ] 转化为永久笔记存入知识库
- **原则**：不囤积，只在需要时学习

### 操作步骤
1. 按 Tier 优先级（1 > 2 > 4 > 3）处理 `processing` 状态的条目
2. 执行对应的分层策略
3. 将处理笔记写入 `Notes` 字段
4. 写入 Processing Log：`Step: 3-Process`

---

## Step 4: 沉淀 (Precipitate)

### 目标
将有价值的信息转化为可复用的知识、行动或观点。

### 沉淀形式
| 类型 | 说明 | 存储位置 |
|------|------|---------|
| 行动 | 已转化为具体 TODO/行动项 | Obsidian 日记 |
| 知识 | 可复用的结构化知识 | Obsidian 知识库 |
| 观点 | 独立判断与思考 | News 笔记 `Notes` 字段 |
| 关联 | 与现有知识的连接 | `[[关联知识点]]` |

### 操作步骤
1. 确认处理已完成且有沉淀产出
2. 更新 `Status` 为 `precipitated`
3. 如有 Obsidian 笔记，填写 `Obsidian Path`
4. 标记 `Action Taken: true`（如已转化为行动）
5. 写入 Processing Log：`Step: 4-Precipitate`

---

## Step 5: 淘汰 (Eliminate)

### 目标
定期清理过时或无价值的信息，防止系统熵增。

### 淘汰触发条件（满足任一即淘汰）
1. ❌ Importance = 1 的信息
2. ❌ Tier 3 信息超过 7 天未产生价值
3. ❌ Inbox 中超过 24 小时未处理
4. ❌ 已被后续更完整的信息覆盖
5. ❌ 信息的事实已被证明不实

### 操作步骤
1. 执行淘汰检查（每日 / 每周）
2. 将淘汰条目的 `Status` 更新为 `eliminated`
3. 从 Obsidian Inbox 中移除对应文件（可选）
4. 写入 Processing Log：`Step: 5-Eliminate`

---

## Obsidian ↔ NocoDB 双轨映射

### 数据对照表
| Obsidian 文件 | NocoDB 记录 | 同步方向 |
|--------------|-------------|---------|
| `Inbox/*.md` (YAML frontmatter) | `News Items` (status: inbox) | Obsidian → NocoDB |
| `News Items` Notes 字段 | Obsidian 笔记正文 | NocoDB → Obsidian |
| `Sources` 表 | 无 Obsidian 对应 | NocoDB 单向管理 |
| `Processing Log` | 无 Obsidian 对应 | NocoDB 单向管理 |

### NocoDB 连接信息
- **地址**：`http://100.118.32.14:8080`（Tailscale 内网）
- **Base ID**：`p1ruzsg3vk7hnng`
- **Tables**：`News Items` / `Sources` / `Processing Log`

### Dataview 查询示例（Obsidian 内使用）
```dataview
TABLE tier, importance, status, date
FROM "pages/News"
WHERE tier
SORT importance DESC, date DESC
```

---

## 常见问题

### Q: NocoDB 视图创建失败？
A: 当前 NocoDB 版本（2026.05.1）视图 API 需企业版许可证。使用默认 Grid 视图 + 过滤器/排序功能替代。

### Q: 如何批量处理存量 Twitter 数据？
A: `x 动态/` 目录中的 73 个文件可按以下流程处理：
1. Agent 逐个扫描，提取核心内容
2. 按分层标准打标
3. 高价值内容写入 NocoDB + Obsidian 知识库
4. 低价值内容标记淘汰

### Q: 信息处理的时间分配？
| Tier | 建议时间占比 | 频率 |
|------|------------|------|
| Tier 1 | 30% | 即时 |
| Tier 2 | 40% | 每天/每周 |
| Tier 3 | 20% | 每日 10 分钟 |
| Tier 4 | 10% | 按需 |

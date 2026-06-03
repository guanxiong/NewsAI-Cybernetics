# 📣 Launch Materials

> Ready-to-post promotional content for community launch.

---

## Show HN

**Title:** NewsAI-Cybernetics: Engineering Cybernetics-driven news intelligence system

**Body:**

Hi HN! I built a personal news intelligence system that doesn't just aggregate news — it transforms information into decisions, knowledge, and action.

The core idea comes from Qian Xuesen's Engineering Cybernetics (工程控制论): treat personal information processing as a control system with:
- Stability control (anti-overload via 4-layer filtering)
- Feedback loops (PDCA — the system improves itself)
- Guided control (proactive acquisition, not passive scrolling)

What makes it different from RSS readers and AI summarizers:

1. **4-Layer Value Filter**: Every piece of information is classified by whether it affects your next 3 months:
   - Tier 1 (Core Decision): Immediate action items — security, policy, emergencies
   - Tier 2 (Cognitive Framework): Deep trends that shape your worldview
   - Tier 3 (Social Connection): Social currency, entertainment
   - Tier 4 (Professional): Problem-solving knowledge

2. **5-Step Processing Loop**: Information has a lifecycle — Acquire → Filter → Process → Precipitate → Eliminate. No information lives forever. Most systems stop at "read"; this one tracks through to "action taken" and "eliminated."

3. **Self-Improving via PDCA**: Every iteration is logged in VERSION.md. The system gets better over time. No other news tool does this.

4. **Dual-track architecture**: Obsidian (Markdown flexibility) + NocoDB (structured database). You get the best of both worlds.

5. **Agent-native**: Built for AI agents (Claude Code, Gemini CLI, Codex) as first-class users via AGENTS.md protocol. Your AI agent IS the processing engine.

**Demo in 30 seconds:**
```bash
git clone https://github.com/guanxiong/NewsAI-Cybernetics
cd NewsAI-Cybernetics && bash demo.sh
```

The acquisition script fetches from HN API + 5 RSS sources (dev.to, Ars Technica, Techmeme, 36Kr, The Verge), auto-classifies by tier using keyword-weight rules, and outputs structured data for Obsidian + NocoDB.

I'd love feedback on:
- Is the 4-layer model useful for your information diet?
- What sources would you want integrated?
- Would you prefer LLM-based classification over keyword rules?

Repo: https://github.com/guanxiong/NewsAI-Cybernetics

---

## Reddit (r/selfhosted, r/ObsidianMD, r/productivity)

**Title:** I built a news system that doesn't just collect — it transforms information into action

**Body:**

Tired of RSS readers that just pile up unread items? I built NewsAI-Cybernetics — a news intelligence system based on Engineering Cybernetics that actually processes information instead of just collecting it.

The key insight: **information is for becoming, not collecting.**

The system uses a 4-layer value filter to classify everything by impact on your next 3 months:
- 🔴 Core Decision (act now)
- 🟡 Cognitive Framework (deep think)
- 🟢 Social Connection (scan and forget)
- 🔵 Professional (learn on demand)

Then a 5-step loop ensures nothing just "sits there": Acquire → Filter → Process → Precipitate → Eliminate.

It's Obsidian + NocoDB dual-track, self-hosted, agent-native (works with Claude Code/Gemini CLI), has Docker one-click deploy, and auto-improves via PDCA cycles.

Demo runs in 30 seconds: `bash demo.sh`

Repo: https://github.com/guanxiong/NewsAI-Cybernetics

---

## V2EX

**标题**: 🧠 做了个基于工程控制论的新闻智能处理系统，不聚合，只转化

**正文**:

大家好，我做了一个不一样的新闻系统。不做聚合器，做价值转化引擎。

核心思路来自钱学森的工程控制论：把个人信息处理当作控制系统来设计。

**4 层价值过滤模型**（不是看什么，而是看了会怎样）：
- 🔴 核心决策层：影响未来3个月生存/安全的 → 1小时内行动
- 🟡 认知框架层：塑造世界观的 → 深度思考
- 🟢 社交连接层：社交货币 → 每日10分钟扫盲
- 🔵 专业知识层：解决具体问题 → 按需学习

**5 步闭环**：获取 → 筛选 → 处理 → 沉淀 → 淘汰。信息有生命周期，不该永远躺在收件箱里。

技术栈：Obsidian + NocoDB 双轨，Python 自动采集 + 分类，GitHub Actions 每日 CI，Docker 一键部署。

30 秒 Demo：`bash demo.sh`

仓库：https://github.com/guanxiong/NewsAI-Cybernetics

欢迎交流！

---

## Twitter/X

🧠 Built a news system based on Engineering Cybernetics.

Not another aggregator. A value transformation engine:
• 4-layer value filter (does it affect your next 3 months?)
• 5-step processing loop (acquire → filter → process → precipitate → eliminate)
• Self-improving via PDCA
• Obsidian + NocoDB dual-track
• Agent-native (Claude Code / Gemini CLI)

30s demo → bash demo.sh

⭐ https://github.com/guanxiong/NewsAI-Cybernetics

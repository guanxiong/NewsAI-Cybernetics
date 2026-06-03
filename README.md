# 🧠 NewsAI-Cybernetics

> **The world's first Engineering Cybernetics-driven personal news intelligence system.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](scripts/acquire.py)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-purple.svg)](https://obsidian.md)
[![NocoDB](https://img.shields.io/badge/NocoDB-Integrated-orange.svg)](https://nocodb.com)
[![Agent-Native](https://img.shields.io/badge/Agent-Claude%20%7C%20Gemini%20%7C%20Codex-green.svg)]()
[![CI](https://img.shields.io/badge/GitHub_Actions-Daily_Acquire-yellow.svg)](.github/workflows/daily-acquire.yml)

**Not another news aggregator.** A value transformation engine that turns information overload into personal decisions, cognitive growth, and actionable knowledge — powered by Qian Xuesen's Engineering Cybernetics.

---

## 🎯 Why This Is Different

Every existing news system helps you **collect more**. None help you **become more**.

| Problem | Others | NewsAI-Cybernetics |
|---------|--------|-------------------|
| Information overload | Collect everything | **4-Layer Value Filter** — only what matters |
| Read-and-forget | No lifecycle | **5-Step Processing Loop** — from inbox to action |
| Static system | No self-improvement | **PDCA feedback** — the system gets smarter |
| Single format | MD or DB, not both | **Obsidian + NocoDB** — flexibility meets structure |
| Human-only | Built for humans | **Agent-native** — AI agents are first-class users |
| Manual curation | All manual | **Auto-acquire + Classify** — scripts + CI/CD |

### Feature-by-Feature Comparison

| Feature | FreshRSS | newspaper3k | llm-wiki | AI每日新闻 | **NewsAI** |
|---------|----------|-------------|----------|-----------|-----------|
| Stars on GitHub | 9k+ | 4k+ | 1k+ | 500+ | 🆕 New |
| Auto-acquisition | ✅ RSS | ❌ | ❌ | ✅ 23源 | ✅ HN+RSS |
| AI classification | ❌ | ❌ | ✅ | ✅ LLM | ✅ Rule engine |
| Value-based filtering | ❌ | ❌ | ❌ | ❌ | ✅ **4-Layer** |
| Complete lifecycle | ❌ | ❌ | ❌ | ❌ | ✅ **5-Step** |
| Self-improvement (PDCA) | ❌ | ❌ | ❌ | ❌ | ✅ **Built-in** |
| Dual-track storage | ❌ | ❌ | Partial | ❌ | ✅ **MD+DB** |
| Agent-native design | ❌ | ❌ | Partial | ❌ | ✅ **Multi-agent** |
| CI/CD automated | ❌ | ❌ | ❌ | ✅ GHA | ✅ **GHA daily** |
| Knowledge precipitation | ❌ | ❌ | ✅ | ❌ | ✅ **Action→Knowledge** |
| Theoretical foundation | ❌ | ❌ | ❌ | ❌ | ✅ **Cybernetics** |

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│                  NEWS AI CYBERNETICS                │
│                                                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐  │
│  │ ACQUIRE  │───▶│  FILTER  │───▶│   PROCESS    │  │
│  │ RSS/API  │    │ 4-Layer  │    │ By Tier      │  │
│  │ Browser  │    │ Model    │    │ Strategy     │  │
│  └──────────┘    └──────────┘    └──────┬───────┘  │
│       ▲                                 │          │
│       │         ┌──────────┐    ┌──────▼───────┐  │
│       │         │ELIMINATE │◀───│ PRECIPITATE  │  │
│       │         │ Clean up │    │ Knowledge DB │  │
│       │         └──────────┘    └──────────────┘  │
│       │                                             │
│       └──────────── PDCA Feedback ◀────────────────│
│                                                     │
│  ┌─────────────────────┐  ┌─────────────────────┐  │
│  │    OBSIDIAN (MD)     │  │   NOCODB (SQL)      │  │
│  │  • Flexible notes    │  │  • Structured data  │  │
│  │  • Dataview queries  │  │  • API access       │  │
│  │  • Templates         │  │  • Sources mgmt     │  │
│  └─────────────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

## 📊 The 4-Layer Value Filter Model

Inspired by the question: *"Does this information affect my next 3 months?"*

| Layer | Name | What Goes Here | Time Budget | Action |
|-------|------|----------------|-------------|--------|
| **Tier 1** | 🔴 Core Decision | Survival, safety, major interests | 30% | Immediate action (< 1hr) |
| **Tier 2** | 🟡 Cognitive Framework | Worldview-shaping trends & analysis | 40% | Deep thinking + connection |
| **Tier 3** | 🟢 Social Connection | Social currency, emotional resonance | 20% | 10-min scan, forget after 7 days |
| **Tier 4** | 🔵 Professional | Problem-solving knowledge | 10% | Pull on demand |

**Key insight**: 90%+ of information is Tier 3. Most people spend 80% of their time on Tier 3 content. This system flips that ratio.

---

## 🔄 The 5-Step Processing Loop

```
Acquire → Filter → Process → Precipitate → Eliminate
   ↑                                        │
   └───────── PDCA Feedback Loop ◀──────────┘
```

1. **Acquire**: Proactive subscription from curated sources (no doom-scrolling)
2. **Filter**: "Does this affect my next 3 months?" → Assign Tier + Importance
3. **Process**: Execute tier-specific strategy (immediate action / deep think / scan / pull)
4. **Precipitate**: Transform into Action / Knowledge / Insight — store permanently
5. **Eliminate**: Remove outdated/low-value items — prevent system entropy

**No information lives forever in this system.** Everything has a lifecycle.

---

## 🚀 Quick Start

### 30-Second Demo (No Installation Required)

```bash
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git
cd NewsAI-Cybernetics
bash demo.sh
```

**What you'll see** — real-time HN acquisition + auto-classification in under 10 seconds:

```
📡 Step 1: Acquire — Fetching top Hacker News stories...
   ✅ Fetched 10 stories from Hacker News API

🔍 Step 2: Filter — Auto-Classification Results
  🔴 [Core-Decision] ★5 Hacking your PC using your speaker without ever touching it
  🟡 [Cognitive-Framework] ★4 Gemma 4 12B: A unified, encoder-free multimodal model
  🟡 [Cognitive-Framework] ★4 Uber's $1,500/month AI limit is a useful signal
  🔵 [Professional] ★3 Elixir v1.20: Now a gradually typed language
  🔵 [Professional] ★3 DaVinci Resolve 21
  ...
```

### Full Setup

**Prerequisites**: Python 3.10+, [Obsidian](https://obsidian.md), [NocoDB](https://nocodb.com), AI Agent (Claude Code / Gemini CLI / Codex)

```bash
# 1. Clone into your Obsidian vault
cd your-obsidian-vault/pages/
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git News

# 2. Fetch & classify news right now
python3 scripts/acquire.py --source all --limit 20 --classify

# 3. Set up NocoDB (optional — system works with just Obsidian)
#    Create base with schema matching TEMPLATE.md fields
#    Update AGENTS.md with your NocoDB URL

# 4. Let your AI agent run the system
#    "Read AGENTS.md and follow its instructions"
```

### GitHub Actions (Automated Daily Reports)

Fork this repo → GitHub Actions auto-runs every day at 01:17 UTC:
- Fetches from HN API + RSS feeds
- Auto-classifies by 4-Layer model
- Generates daily Markdown report in `Inbox/`
- Commits to your fork automatically

### First Steps
1. Read `STANDARDS.md` to understand the 4-layer model
2. Read `MANUAL.md` for the 5-step processing workflow
3. Use `TEMPLATE.md` to create your first news note
4. Let your AI agent handle the rest

---

## 📁 Directory Structure

```
pages/News/
├── README.md          # You are here
├── GOAL.md            # Project vision, OKR, roadmap
├── AGENTS.md          # ⭐ Single source of truth for AI agents
├── CLAUDE.md          # Redirect → AGENTS.md
├── GEMINI.md          # Redirect → AGENTS.md
├── TASK.md            # WBS task tracking
├── VERSION.md         # PDCA iteration history
├── STANDARDS.md       # 4-layer classification standards
├── MANUAL.md          # 5-step processing manual
├── TEMPLATE.md        # YAML frontmatter template
├── ARCHIVE-REPORT.md  # Data governance reports
├── auth.md            # Authorization records
├── Inbox/             # Entry point for new information
└── x 动态/            # Cold archive (processed items)
```

---

## 🤝 Contributing

This project thrives on diverse perspectives. Areas where we need help:

- **🌐 Internationalization**: Translation of standards and templates
- **🔌 Source Plugins**: Connectors for RSS, Reddit, HN, WeChat, etc.
- **📊 Visualization**: Dashboard designs for the processing pipeline
- **🧠 Theory**: Refine the cybernetics model — critique welcome
- **🔄 Automation**: Obsidian ↔ NocoDB sync scripts

See [GOAL.md](GOAL.md) for the full roadmap.

---

## 📜 License

MIT License — Use it, fork it, improve it. Just remember: **information is for becoming, not collecting.**

---

## 🙏 Acknowledgments

- **Qian Xuesen (钱学森)** — Engineering Cybernetics, the theoretical foundation
- **Andrej Karpathy** — LLM Wiki pattern, inspiration for agent-native knowledge systems
- **Obsidian** — The best Markdown knowledge base
- **NocoDB** — Open-source Airtable alternative
- **Harness Engineering** — Engineering discipline principles

---

> *"The goal is not to collect more information, but to become more through information."*

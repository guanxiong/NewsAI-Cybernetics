# 🧠 NewsAI-Cybernetics

> **The world's first Engineering Cybernetics-driven personal news intelligence system.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-purple.svg)](https://obsidian.md)
[![NocoDB](https://img.shields.io/badge/NocoDB-Integrated-orange.svg)](https://nocodb.com)
[![Agent-Native](https://img.shields.io/badge/Agent-Claude%20%7C%20Gemini%20%7C%20Codex-green.svg)]()

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

### Prerequisites
- [Obsidian](https://obsidian.md) (or any Markdown editor)
- [NocoDB](https://nocodb.com) (self-hosted or cloud)
- An AI agent: [Claude Code](https://claude.ai/code), [Gemini CLI](https://github.com/google-gemini/gemini-cli), or [Codex](https://github.com/openai/codex)

### Installation

```bash
# 1. Clone this repository into your Obsidian vault
cd your-obsidian-vault/pages/
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git News

# 2. Set up NocoDB
# Create a new base using the schema in nocoDB-schema.json
# Update AGENTS.md with your NocoDB connection details

# 3. Start processing
# Tell your AI agent: "Read pages/News/AGENTS.md and follow its instructions"
```

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

<div align="center">

# 🧠 NewsAI-Cybernetics

### Stop collecting news. Start becoming from it.

**The world's first Engineering Cybernetics-driven personal news intelligence system.**

Not another aggregator. Not another AI summarizer. A **value transformation engine** that turns information overload into decisions, knowledge, and action.

[![GitHub stars](https://img.shields.io/github/stars/guanxiong/NewsAI-Cybernetics?style=social)](https://github.com/guanxiong/NewsAI-Cybernetics)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](scripts/acquire.py)
[![Obsidian](https://img.shields.io/badge/Obsidian-Compatible-7C3AED?logo=obsidian&logoColor=white)](https://obsidian.md)
[![NocoDB](https://img.shields.io/badge/NocoDB-Integrated-FF6B35?logo=nocodb&logoColor=white)](https://nocodb.com)
[![CI](https://github.com/guanxiong/NewsAI-Cybernetics/actions/workflows/daily-acquire.yml/badge.svg)](https://github.com/guanxiong/NewsAI-Cybernetics/actions)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](docker-compose.yml)

**English** · [中文](#chinese-readme) · [日本語](#japanese-readme)

**⭐ Star** · **🍴 Fork** · **📢 Share**

</div>

---

## ⚡ 30 Seconds to Wow

```bash
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git
cd NewsAI-Cybernetics
bash demo.sh
```

**What you'll see** (real output, no mocks):

```
📡 Step 1/4: ACQUIRE — Fetching from 6 sources...
  ✅ HackerNews API:  10 stories
  ✅ RSS Feeds:      10 articles (dev.to, Ars, Techmeme, 36Kr, The Verge)
  ✅ Total fetched:  20 items

🏷️  Step 2/4: CLASSIFY — Auto-classification by 4-Layer Model
  🔴 Tier 1 Core Decision:      1 items  (act within 1 hour)
  🟡 Tier 2 Cognitive Framework: 8 items  (deep think today)
  🔵 Tier 4 Professional:       11 items  (learn on demand)

📰 Step 3/4: TOP ITEMS
  🔴 ★★★★★ Hacking your PC using your speaker...
  🟡 ★★★★  Gemma 4 12B: A unified multimodal model
  🟡 ★★★★  Uber's $1,500/month AI limit is a useful signal

⏱️  Pipeline time: < 10 seconds
```

**No API key needed. No Python packages to install. No config files.** Just bash.

---

## 🤔 Why This Exists

Every news system has the same flaw: **they help you *collect* more, but don't help you *become* more.**

RSS readers collect. AI summarizers condense. But none answer the real question:

> *"How should this information change my life?"*

This system answers that through **Qian Xuesen's Engineering Cybernetics** — treating personal information processing as a control system with stability control (anti-overload), feedback loops (PDCA self-improvement), and guided control (proactive acquisition).

---

## 🔥 What Makes This Different

| Problem | Others | NewsAI-Cybernetics |
|---------|--------|-------------------|
| Information overload | Collect everything | **4-Layer Value Filter** — only what matters |
| Read-and-forget | No lifecycle | **5-Step Loop** — from inbox to action to elimination |
| Static system | No self-improvement | **PDCA feedback** — the system evolves itself |
| Single format | MD or DB, not both | **Obsidian + NocoDB** — flexibility meets structure |
| Human-only | Built for humans | **Agent-native** — Claude Code / Gemini CLI / Codex |
| Manual curation | All manual | **Auto-acquire + Classify + CI/CD** |
| No theory | Just features | **Engineering Cybernetics foundation** |

---

## 🧠 The 4-Layer Value Filter Model

> Inspired by one question: *"Does this information affect my next 3 months?"*

| Tier | Name | What | Time | Action |
|------|------|------|------|--------|
| 🔴 | **Core Decision** | Survival, safety, major interests | 30% | Act within 1 hour |
| 🟡 | **Cognitive Framework** | Worldview-shaping trends | 40% | Deep think today |
| 🟢 | **Social Connection** | Social currency, entertainment | 20% | 10-min scan |
| 🔵 | **Professional** | Problem-solving knowledge | 10% | Learn on demand |

**90%+ of information is Tier 3.** Most people spend 80% of their time on Tier 3. This system flips that ratio.

---

## 🔄 The 5-Step Processing Loop

```
Acquire → Filter → Process → Precipitate → Eliminate
   ↑                                        │
   └──────────── PDCA Feedback Loop ◀─────────┘
```

No information lives forever in this system. Everything has a lifecycle.

---

## 🆚 vs The Known Alternatives

| Feature | FreshRSS<br>(9k★) | llm-wiki<br>(1k★) | AI每日新闻<br>(500★) | **NewsAI** |
|---------|----------|---------|----------|-----------|
| **Theoretical foundation** | ❌ | ❌ | ❌ | ✅ Cybernetics |
| **Value-based filtering** | ❌ | ❌ | ❌ | ✅ 4-Layer Model |
| **Complete lifecycle** | ❌ | ❌ | ❌ | ✅ 5-Step Loop |
| **Self-improvement (PDCA)** | ❌ | ❌ | ❌ | ✅ Built-in |
| **Auto-acquisition** | ✅ RSS | ❌ | ✅ 23源 | ✅ HN+RSS |
| **Auto-classification** | ❌ | ✅ LLM | ✅ LLM | ✅ Rule Engine |
| **Knowledge precipitation** | ❌ | ✅ | ❌ | ✅ Action→Knowledge |
| **Dual-track storage** | ❌ | Partial | ❌ | ✅ Obsidian+NocoDB |
| **Agent-native** | ❌ | Partial | ❌ | ✅ Multi-agent |
| **CI/CD automated** | ❌ | ❌ | ✅ | ✅ Daily |
| **Docker deploy** | ✅ | ❌ | ❌ | ✅ One-click |
| **No API key needed** | ✅ | ❌ | ❌ | ✅ Works immediately |

---

## 🚀 Quick Start

### Option 1: Just try it (30 seconds)

```bash
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git
cd NewsAI-Cybernetics
bash demo.sh
```

### Option 2: Full setup with Obsidian

```bash
# In your Obsidian vault
cd your-obsidian-vault/pages/
git clone https://github.com/guanxiong/NewsAI-Cybernetics.git News

# Fetch & classify news right now
python3 scripts/acquire.py --source all --limit 20 --classify

# Start using with your AI agent
# Tell Claude Code: "Read pages/News/AGENTS.md and follow its instructions"
```

### Option 3: Docker (full stack with NocoDB)

```bash
docker compose up -d
# NocoDB at http://localhost:8080
# Auto-acquisition every 4 hours
```

### Option 4: Fork for daily auto-acquisition

Fork → GitHub Actions auto-runs every day at 01:17 UTC:
- Fetches from HN + RSS
- Auto-classifies by 4-Layer model
- Generates daily report
- Commits to your fork

---

## 📁 What's Inside

```
├── README.md              # You are here
├── AGENTS.md              # ⭐ Single source of truth for AI agents
├── demo.sh                # 30-second interactive demo
├── scripts/
│   ├── acquire.py         # Multi-source fetcher + auto-classifier
│   └── sync.py            # Obsidian ↔ NocoDB bidirectional sync
├── skills/
│   └── news-acquire.md    # Agent skill definition
├── .github/workflows/
│   └── daily-acquire.yml  # CI: daily auto-acquisition
├── docker-compose.yml     # One-click full stack
├── STANDARDS.md           # 4-Layer classification standard
├── MANUAL.md              # 5-Step processing manual
├── CONTRIBUTING.md         # How to contribute
└── PROMOTION.md            # Launch materials (Show HN, Reddit, etc.)
```

---

## 🗺️ Roadmap

### v1.x — Current
- [x] 4-Layer Value Filter Model
- [x] 5-Step Processing Loop with PDCA
- [x] Multi-source auto-acquisition (HN API + 6 RSS)
- [x] Auto-classification engine (keyword-weight)
- [x] Obsidian + NocoDB dual-track
- [x] GitHub Actions CI/CD
- [x] Docker one-click deployment
- [x] 28 real news items processed and stored

### v2.0 — Intelligence
- [ ] LLM-powered classification (OpenAI/Claude API)
- [ ] Personal value model (adapts to your behavior)
- [ ] Cross-source correlation (connect related items)
- [ ] Proactive Tier-1 alerts

### v3.0 — Community
- [ ] Plugin system for custom sources/processors
- [ ] Shared filter templates ("startup founder", "researcher", "investor")
- [ ] Multi-user support
- [ ] Web dashboard

---

## 🤝 Contributing

We especially welcome: **new RSS connectors**, **classification improvements**, **translations** (中文/日本語/한국어), and **LLM integration**.

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License

MIT — Use it, fork it, improve it.

---

<div align="center">

**Remember: Information is for becoming, not collecting.** 🧠

[⭐ Star this repo](https://github.com/guanxiong/NewsAI-Cyberpoints) · [🍴 Fork](https://github.com/guanxiong/NewsAI-Cybernetics/fork) · [📢 Share on X](https://twitter.com/intent/tweet?text=NewsAI-Cybernetics%20%E2%80%94%20the%20first%20Engineering%20Cybernetics-driven%20news%20intelligence%20system&url=https://github.com/guanxiong/NewsAI-Cybernetics) · [💬 Discuss](https://github.com/guanxiong/NewsAI-Cybernetics/discussions)

</div>

---

<a id="chinese-readme"></a>
## 中文说明

🧠 NewsAI-Cybernetics — 全球首个基于**工程控制论**的个人新闻智能处理系统。

不做聚合器，做价值转化引擎。通过**4 层价值过滤模型**和**5 步闭环处理**，将信息过载转化为个人决策、认知与能力的增长动力。

**30 秒体验**：`git clone → cd → bash demo.sh`

无需 API Key，无需安装依赖，无需配置文件。

<a id="japanese-readme"></a>
## 日本語

🧠 NewsAI-Cybernetics — 世界初の**エンジニアリング・サイバネティクス**駆動の個人ニュースインテリジェンスシステム。

ニュース収集ではなく、**価値変換エンジン**。4層価値フィルターと5ステップ処理ループで、情報オーバーロードを個人の成長動力に変換します。

**30秒で体験**：`git clone → cd → bash demo.sh`

APIキー不要、依存パッケージ不要、設定ファイル不要。

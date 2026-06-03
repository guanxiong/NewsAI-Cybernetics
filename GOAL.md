# Project Goals (OKR)

## Vision

> **NewsAI-Cybernetics**: The world's first Engineering Cybernetics-driven personal news intelligence system.
> Not another news aggregator — a **value transformation engine** that turns information overload into personal growth fuel.

## Why This Project Exists

Every existing news system has the same flaw: **they help you *collect* more, but don't help you *become more*.**

RSS readers collect. AI summarizers condense. But none answer the fundamental question:

> *"How should this information change my life?"*

This system answers that question through the lens of **Qian Xuesen's Engineering Cybernetics** — treating personal information processing as a control system that maintains stability (anti-overload), uses feedback loops (PDCA), and applies guided control (proactive acquisition).

---

## Objective: Build the definitive open-source NewsAI processing system

### KR1: Theory-Driven Architecture 🧠
- **Content**: The 4-Layer Value Filter Model + 5-Step Processing Loop, derived from Engineering Cybernetics
- **Metric**: 100% of processed items have explicit Tier classification and lifecycle state
- **Uniqueness**: No other system combines cybernetics theory with news AI

### KR2: Complete Information Lifecycle 🔄
- **Content**: Acquire → Filter → Process → Precipitate → Eliminate — every piece of information follows this path
- **Metric**: Inbox backlog < 24 hours; 95% of Tier-1 items trigger actions within 1 hour
- **Uniqueness**: Most systems stop at "read"; we track through "action" and "elimination"

### KR3: Self-Improving System 📈
- **Content**: PDCA (Plan-Do-Check-Act) loops embedded at every level — the system gets better over time
- **Metric**: VERSION.md records every iteration; each cycle improves filter accuracy by measurable delta
- **Uniqueness**: The only news system that improves itself through structured feedback

### KR4: Dual-Track Data Architecture 🗄️
- **Content**: Obsidian (flexible Markdown) + NocoDB (structured database) working in concert
- **Metric**: All high-value items exist in both systems with bidirectional references
- **Uniqueness**: No other system combines note-taking flexibility with database queryability

### KR5: Agent-Native Design 🤖
- **Content**: Built from day one as an AI agent workspace — works with Claude Code, Gemini CLI, Codex
- **Metric**: AGENTS.md serves as the single source of truth for any AI agent
- **Uniqueness**: Not a tool for humans to use, but a system humans and AI agents co-operate

---

## Competitive Landscape

| Feature | FreshRSS | newspaper3k | tl-dw | llm-wiki | **NewsAI-Cybernetics** |
|---------|----------|-------------|-------|----------|----------------------|
| Theoretical foundation | ❌ | ❌ | ❌ | ❌ | ✅ Engineering Cybernetics |
| Value-based filtering | ❌ | ❌ | ❌ | ❌ | ✅ 4-Layer Model |
| Complete lifecycle | ❌ | ❌ | ❌ | Partial | ✅ 5-Step Loop |
| Self-improvement (PDCA) | ❌ | ❌ | ❌ | ❌ | ✅ Built-in |
| Dual-track (MD + DB) | ❌ | ❌ | ❌ | Partial | ✅ Obsidian + NocoDB |
| Agent-native | ❌ | ❌ | ❌ | Partial | ✅ Multi-agent |
| Knowledge precipitation | ❌ | ❌ | ❌ | ✅ | ✅ Decision → Knowledge → Action |

---

## Roadmap

### v0.x — Foundation (Current)
- [x] 4-Layer Value Filter Model
- [x] 5-Step Processing Loop
- [x] NocoDB database schema (3 tables)
- [x] Obsidian integration (templates, standards, manual)
- [x] PDCA versioning system
- [x] Stock data governance (385 tweets → 14 high-value)

### v1.0 — Agent Automation
- [ ] Auto-acquisition from configurable sources (RSS, X, Reddit, HN)
- [ ] LLM-powered auto-classification (Tier + Importance)
- [ ] Obsidian ↔ NocoDB bidirectional sync
- [ ] Processing dashboard (NocoDB views or custom)

### v2.0 — Intelligence
- [ ] Personal value model learning (adapts filters to user behavior)
- [ ] Cross-source correlation (connect related items across sources)
- [ ] Proactive alerts for Tier-1 items
- [ ] Weekly/monthly intelligence reports auto-generated

### v3.0 — Community
- [ ] Multi-user support
- [ ] Plugin system for custom sources and processors
- [ ] Shared filter templates (e.g., "startup founder", "researcher", "investor")
- [ ] Docker one-click deployment

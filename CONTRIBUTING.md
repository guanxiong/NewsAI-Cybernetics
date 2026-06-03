# Contributing to NewsAI-Cybernetics

Thank you for your interest! We welcome contributions that make this system better for everyone.

## 🎯 Priority Areas

| Area | Difficulty | Impact |
|------|-----------|--------|
| New RSS source connectors | 🟢 Easy | More coverage |
| Classification keyword improvements | 🟢 Easy | Better accuracy |
| New language translations | 🟢 Easy | Global reach |
| LLM API integration (OpenAI/Claude) | 🟡 Medium | Smarter classification |
| Obsidian plugin | 🟡 Medium | Native integration |
| Docker deployment | 🟡 Medium | Easy setup |
| Dashboard/visualization | 🔴 Hard | User experience |

## 🚀 Quick Start

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Test: `python3 scripts/acquire.py --source hn --limit 5 --classify`
5. Submit a Pull Request

## 📐 Architecture Principles

### The 4-Layer Model is Sacred
All contributions must respect the tier system:
- **Tier 1** (Core-Decision): Only security, policy, emergency content
- **Tier 2** (Cognitive-Framework): Macro trends, AI developments, science
- **Tier 3** (Social-Connection): Entertainment, sports, social topics
- **Tier 4** (Professional): Dev tools, product updates, technical content

### Agent-Native Design
All features should work with AI agents as first-class users:
- Read `AGENTS.md` for the single source of truth
- Maintain `CLAUDE.md` and `GEMINI.md` as redirects
- Keep the agent instruction layer clean

### PDCA Cycles
Every significant change should update `VERSION.md` with Plan/Do/Check/Act.

## 🧪 Testing

```bash
# Test acquisition pipeline
python3 scripts/acquire.py --source all --limit 5 --classify

# Test sync script
python3 scripts/sync.py status

# Test demo
bash demo.sh
```

## 📝 Commit Messages

Follow this format:
```
type: brief description

detail: what changed
files: list of changed files
note: why this change was made
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`

## 🌍 Translations

We especially welcome translations of:
- `STANDARDS.md` → `STANDARDS.{lang}.md`
- `MANUAL.md` → `MANUAL.{lang}.md`
- Classification keywords in `scripts/acquire.py`

## 💡 Ideas Welcome

Not sure what to build? Check [Issues](https://github.com/guanxiong/NewsAI-Cybernetics/issues) or start a [Discussion](https://github.com/guanxiong/NewsAI-Cybernetics/discussions).

## 📜 Code of Conduct

Be respectful. Be constructive. Remember: information is for becoming, not collecting.

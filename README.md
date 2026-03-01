# soul.py 🧠

**Your AI forgets everything when the conversation ends. soul.py fixes that in 10 lines.**

```python
from soul import Agent

agent = Agent()
agent.ask("My name is Prahlad and I'm building an AI research lab.")
# → "That's exciting — what are you working on first?"

# Later. New process. New session. Memory persists.
agent = Agent()
agent.ask("What do you know about me?")
# → "You're Prahlad, building an AI research lab."
```

No database. No server. No vector embeddings. Just markdown files.

---

## Install

```bash
pip install soul-agent          # zero required deps
pip install soul-agent[anthropic]   # + Anthropic SDK
pip install soul-agent[openai]      # + OpenAI SDK
```

## Quickstart

```bash
soul init   # interactive setup — creates SOUL.md and MEMORY.md
```

Or manually:

```python
from soul import Agent

# Anthropic (default)
agent = Agent(provider="anthropic")

# OpenAI
agent = Agent(provider="openai")

# Local Ollama — no API key needed
agent = Agent(provider="openai-compatible", base_url="http://localhost:11434/v1", model="llama3.2", api_key="ollama")
```

## How it works

soul.py uses two markdown files as the agent's persistent state:

| File | Purpose |
|------|---------|
| `SOUL.md` | Identity — who the agent is, how it behaves, what it cares about |
| `MEMORY.md` | Memory — timestamped log of past exchanges, manually added notes |

On every `agent.ask()` call:
1. `SOUL.md` + `MEMORY.md` are injected into the system prompt
2. The LLM responds in character, with full memory context
3. The exchange is appended to `MEMORY.md` with a timestamp

That's it. No embeddings. No vector store. No infrastructure.

## API

```python
agent.ask(question, remember=True)   # ask + persist to memory
agent.remember(note)                  # manually write a note to MEMORY.md
agent.reset_conversation()            # clear in-session history (not MEMORY.md)
```

## Example SOUL.md

```markdown
# SOUL.md
You are Pi, an AI research assistant for Dr. Prahlad Menon.
You are direct, curious, and think independently.
You remember everything and build on prior conversations.
You have opinions — you share them when relevant.
```

## Example MEMORY.md

```markdown
# MEMORY.md

## 2026-03-01 08:30
Q: My name is Prahlad and I'm working on a paper about agent memory.
A: Great — persistent memory is one of the most underserved problems in agent design...

## 2026-03-01 09:15
Q: What do you think the key insight should be?
A: The distinction between episodic and semantic memory matters more than most...
```

---

## Roadmap

soul.py is designed to grow with your needs without changing your code.

### v0.1 — Now
- Markdown-native memory, zero infrastructure
- Anthropic, OpenAI, Ollama support
- `soul init` wizard

### v1.0 — RAG backend
- Local vector store (ChromaDB / FAISS) for large memory files
- Same `agent.ask()` API — retrieval is invisible
- Handles memory files with thousands of entries

### v2.0 — RAG + RLM hybrid
- Query router: focused queries → RAG, exhaustive queries → RLM
- Based on: [RAG + RLM: The Complete Knowledge Base Architecture](https://blog.themenonlab.com/blog/rag-plus-rlm-complete-knowledge-base-architecture)
- External vector store support: Pinecone, Weaviate, Qdrant — no local compute required
- `agent = Agent("SOUL.md", memory_backend="pinecone")`

The key insight from the RAG + RLM architecture: ~90% of memory queries are focused lookups (RAG). The other 10% — *"what patterns appear across all my decisions?"* — require exhaustive reasoning (RLM). The router dispatches automatically.

---

## Why not LangChain / LlamaIndex / MemGPT?

Those are powerful frameworks. soul.py is a primitive.

- **LangChain** — orchestration framework, requires significant setup
- **LlamaIndex** — document indexing, needs infrastructure
- **MemGPT** — impressive but opinionated about the full agent stack

soul.py does one thing: give any LLM a persistent identity and memory via files you can read, edit, and version-control yourself. Drop it into whatever you're building.

---

## Contributing

PRs welcome. The goal is to stay small and composable.

## License

MIT

## Citation

If you use soul.py in research:

```bibtex
@software{menon2026soul,
  author = {Menon, Prahlad G.},
  title  = {soul.py: Persistent Identity and Memory for LLM Agents},
  year   = {2026},
  url    = {https://github.com/menonpg/soul.py}
}
```

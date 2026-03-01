# soul.py — Project Plan

## What this is
Persistent identity + memory for any LLM agent. Two markdown files replace
the need for a database. v0.1 is pure markdown; v2.0 will be a full
RAG + RLM hybrid. Goal: viral GitHub repo + academic credibility.

## Current status: v0.1 SHIPPED (2026-03-01)
- Repo: https://github.com/menonpg/soul.py
- Package: pip install soul-agent
- Tests: 8/8 passing, no SDK required
- CI: GitHub Actions on Python 3.10/3.11/3.12

## Roadmap

### v0.1 ✅ Done
- Agent class with SOUL.md + MEMORY.md
- Anthropic / OpenAI / Ollama support
- `soul init` wizard
- 8 unit tests passing
- GitHub Actions CI

### v1.0 — Local RAG backend
- ChromaDB or FAISS for memory files > ~6000 chars
- Same `agent.ask()` API — retrieval invisible to caller
- Test: pytest + Railway for load testing
- Target: when memory files grow to 1000+ entries

### v2.0 — RAG + RLM Hybrid (the research contribution)
Architecture based on: https://blog.themenonlab.com/blog/rag-plus-rlm-complete-knowledge-base-architecture

```
Query → Router (LLM classifier)
          ├── FOCUSED (~90%) → RAG → vector search → answer
          └── EXHAUSTIVE (~10%) → RLM → recursive decomposition → answer
```

- Query router: single LLM call classifies FOCUSED vs EXHAUSTIVE
- RAG path: embed → search → top-k → inject → generate
- RLM path: DSPy RLM or manual recursive sub-calls through memory
- External backends: Pinecone, Weaviate, Qdrant — zero local compute
  - `agent = Agent("SOUL.md", memory_backend="pinecone", api_key="...")`
- Publish as paper + repo combo for maximum academic/community traction

## Distribution strategy
1. Blog post: menonography — personal story + technical depth
2. HackerNews Show HN — weekday evening EST
3. Reddit: r/LocalLLaMA, r/MachineLearning self-promotion thread
4. Twitter/X: demo GIF thread
5. Cite Prahlad's RAG+RLM blog as architecture reference

## Testing infrastructure
- Phone/CI: unit tests (no API, mocked) — already passing
- GitHub Actions: runs on every push, free
- Railway: ~$5/mo for v1/v2 integration + load tests, shut down after use

## Immediate next steps
1. Add ANTHROPIC_API_KEY to GitHub secrets (repo Settings → Secrets → Actions)
2. Write blog post draft on menonography
3. Create demo GIF: two terminals, memory persists across Python processes
4. Post to HackerNews Show HN
5. u/the-ai-scientist posts to r/LocalLLaMA

## Key people / links
- Author: Prahlad G. Menon (menonpg) — menon.prahlad@gmail.com
- Blog: https://blog.themenonlab.com
- RAG+RLM architecture post: https://blog.themenonlab.com/blog/rag-plus-rlm-complete-knowledge-base-architecture
- Reddit: u/the-ai-scientist
- Local source: /storage/emulated/0/Download/soul-repo/

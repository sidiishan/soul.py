"""
SoulMate — Persistent AI Memory as a Service

Enterprise-grade hosted memory layer for AI agents.
BYOK (Bring Your Own Key) — you provide the LLM key, we handle memory.

Usage:
    from soulmate import SoulMateClient
    
    sm = SoulMateClient(
        api_key="sm_live_xxxxx",
        llm_provider="anthropic",
        llm_key="sk-ant-..."
    )
    
    response = sm.ask("customer_123", "What's my account status?")
    print(response)
"""

from .client import SoulMateClient

__all__ = ["SoulMateClient"]
__version__ = "0.1.5"

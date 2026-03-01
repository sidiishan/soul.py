from soul import Agent

# Works with any local model via Ollama — no API key needed
agent = Agent(
    provider="openai-compatible",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model="llama3.2",
)

response = agent.ask("Summarise what you remember about my projects.")
print(response)

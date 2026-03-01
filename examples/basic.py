from soul import Agent

agent = Agent(provider="anthropic")  # or "openai"

# First session
response = agent.ask("My name is Prahlad and I work on AI research.")
print(response)

# Later — new instance, same files, memory persists
agent2 = Agent(provider="anthropic")
response2 = agent2.ask("What do you know about me?")
print(response2)

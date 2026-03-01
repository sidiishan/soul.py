"""
Run this on a cron schedule — e.g. every morning at 8:30 AM.
The agent checks in, remembers the exchange, builds context over time.
"""
import datetime
from soul import Agent

agent = Agent(provider="anthropic")

today = datetime.date.today().strftime("%A, %B %d")
response = agent.ask(
    f"Good morning. Today is {today}. "
    "Based on everything you remember, what should I focus on today?"
)
print(response)

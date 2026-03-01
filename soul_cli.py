"""soul init — interactive setup wizard."""
import sys

def main():
    args = sys.argv[1:]
    if not args or args[0] == "init":
        _init()
    else:
        print(f"Unknown command: {args[0]}")
        print("Usage: soul init")

def _init():
    print("\n🧠 soul.py setup\n")
    name = input("Agent name [Assistant]: ").strip() or "Assistant"
    provider = input("LLM provider — anthropic / openai / openai-compatible [anthropic]: ").strip() or "anthropic"

    soul_content = f"# SOUL.md\nYou are {name}.\nYou have a persistent memory and strong opinions.\nYou are concise, direct, and genuinely helpful.\n"
    mem_content  = "# MEMORY.md\n(No memories yet.)\n"

    with open("SOUL.md", "w") as f: f.write(soul_content)
    with open("MEMORY.md", "w") as f: f.write(mem_content)

    print(f"\n✅ Created SOUL.md and MEMORY.md")
    print(f"   Provider: {provider}")
    print(f"\nNext steps:")
    if provider == "anthropic":
        print("   export ANTHROPIC_API_KEY=sk-ant-...")
        print("   pip install anthropic")
    else:
        print("   export OPENAI_API_KEY=sk-...")
        print("   pip install openai")
    print("\n   Then: python -c \"from soul import Agent; print(Agent().ask('Hello'))\"")

if __name__ == "__main__":
    main()

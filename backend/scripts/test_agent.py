import sys
import os

# Add the backend directory to sys.path to allow running from scripts/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agent.sales_agent import SalesAIAgent

def main():
    agent = SalesAIAgent()

    questions = [
        "Give me a pipeline summary",
        "What deals are at risk?",
        "How good are our leads?",
        "Tell me something random"
    ]

    for q in questions:
        print(f"\nQ: {q}")
        print(agent.answer(q))

if __name__ == "__main__":
    main()

import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

# Ensure environment variables are loaded
load_dotenv(find_dotenv())

# Retrieve API key safely
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    # Fallback or error logging if needed
    pass
else:
    genai.configure(api_key=api_key)

MODEL_NAME = "gemini-2.5-flash"

def get_model():
    """Lazily initialize the model."""
    return genai.GenerativeModel(MODEL_NAME)

ALLOWED_INTENTS = [
    "PIPELINE_SUMMARY",
    "RISK_ANALYSIS",
    "LEAD_QUALITY",
    "AVG_DEAL_SIZE",
    "TOP_CUSTOMERS",
    "RECENT_ACTIVITY",
    "UNKNOWN"
]

def classify_intent(user_question: str) -> str:
    try:
        model = get_model()
        prompt = f"""
You are an intent classifier for a sales analytics system.

Classify the user question into ONE of the following intents:
- PIPELINE_SUMMARY (Overview of pipeline, total deals, total value)
- RISK_ANALYSIS (Stalled deals, risks, high value deals at risk)
- LEAD_QUALITY (Lead scores, lead quality, effectiveness)
- AVG_DEAL_SIZE (Average deal size, average opportunity value)
- TOP_CUSTOMERS (Best customers, highest spending clients, who buys the most)
- RECENT_ACTIVITY (Latest updates, what happened recently, sales logs)
- UNKNOWN (Anything else or greeting)

Return ONLY the intent label.

Question:
{user_question}
"""
        response = model.generate_content(prompt)
        intent = response.text.strip().upper()

        if intent not in ALLOWED_INTENTS:
             # Heuristic fallback
             if "PIPELINE" in intent: return "PIPELINE_SUMMARY"
             if "RISK" in intent: return "RISK_ANALYSIS"
             if "LEAD" in intent: return "LEAD_QUALITY"
             if "AVG" in intent or "AVERAGE" in intent: return "AVG_DEAL_SIZE"
             if "TOP" in intent or "CUSTOMER" in intent: return "TOP_CUSTOMERS"
             if "ACTIVITY" in intent or "RECENT" in intent: return "RECENT_ACTIVITY"
             return "UNKNOWN"

        return intent
    except Exception as e:
        print(f"Intent classification failed: {e}")
        return "UNKNOWN"

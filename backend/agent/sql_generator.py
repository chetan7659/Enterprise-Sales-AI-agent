import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv
from agent.schema_context import SCHEMA_DESCRIPTION

load_dotenv(find_dotenv())

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Using verified working model
MODEL_NAME = "gemini-2.5-flash"

def get_model():
    return genai.GenerativeModel(MODEL_NAME)

def generate_sql(user_question: str) -> str:
    try:
        model = get_model()
        prompt = f"""
{SCHEMA_DESCRIPTION}

User question:
{user_question}

Return ONLY the SQL query. Do not use markdown formatting like ```sql. Just the query.
"""

        response = model.generate_content(prompt)
        # Clean up response to ensure just SQL
        sql = response.text.replace("```sql", "").replace("```", "").strip()
        return sql
    except Exception as e:
        print(f"SQL Generation failed: {e}")
        return ""

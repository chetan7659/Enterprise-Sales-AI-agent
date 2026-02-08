import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Using verified working model
MODEL_NAME = "gemini-2.5-flash"

def get_model():
    return genai.GenerativeModel(MODEL_NAME)

def explain_result(question, columns, rows) -> str:
    try:
        model = get_model()
        prompt = f"""
User question:
{question}

Query result columns:
{columns}

Query result rows:
{rows}

Explain the result in clear business language. Focus on the answer to the user's question.
If the result is empty, say so.
"""

        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error explaining results: {e}"

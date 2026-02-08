from agent.sql_generator import generate_sql
from agent.sql_validator import validate_sql
from agent.answer_explainer import explain_result
from db.query_executor import run_query

class NLSQLAgent:
    
    def answer(self, question: str) -> str:
        print(f"[DEBUG] Processing Question: {question}")
        
        # 1. Generate SQL
        sql = generate_sql(question)
        print(f"[DEBUG] Generated SQL: {sql}")

        if not sql:
             return "I tried to generate a query but failed. Please try rephrasing."

        # 2. Validate SQL
        if not validate_sql(sql):
            return "Sorry, I cannot generate a safe query for that request (or retrieval failed)."

        # 3. Execute SQL
        try:
            columns, rows = run_query(sql)
            print(f"[DEBUG] Rows returned: {len(rows) if rows else 0}")
        except Exception as e:
            return f"I generated a query but it failed to run: {e}"

        if not rows and not columns:
             return "No data found matching your request."
        
        # 4. Explain Results
        return explain_result(question, columns, rows)

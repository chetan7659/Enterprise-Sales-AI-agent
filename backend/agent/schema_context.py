SCHEMA_DESCRIPTION = """
You are working with a Snowflake database SALES_AI, schema CRM.

Available tables and columns:

1. customers
   - customer_id (INTEGER)
   - name (STRING)
   - industry (STRING)
   - region (STRING)

2. leads
   - lead_id (INTEGER)
   - customer_id (INTEGER)
   - status (STRING)
   - score (INTEGER)

3. opportunities
   - opp_id (INTEGER)
   - customer_id (INTEGER)
   - value (NUMBER)
   - stage (STRING)

4. sales_activity
   - activity_id (INTEGER)
   - opp_id (INTEGER)
   - notes (STRING)
   - activity_date (DATE)

Rules:
- Generate ONLY SELECT queries
- Do NOT use DELETE, UPDATE, INSERT, DROP
- Use correct table and column names
- Prefer simple queries
"""

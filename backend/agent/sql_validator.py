import re

FORBIDDEN_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE", "GRANT", "REVOKE"
]

def validate_sql(sql: str) -> bool:
    if not sql:
        return False
        
    sql_upper = sql.upper().strip()

    # Must start with SELECT (or WITH ... SELECT, but limiting to SELECT for safety/simplicity as per prompt)
    if not sql_upper.startswith("SELECT") and not sql_upper.startswith("WITH"):
        return False

    # Check for forbidden keywords as whole words
    for word in FORBIDDEN_KEYWORDS:
        # \b matches word boundary
        if re.search(rf"\b{word}\b", sql_upper):
            # Allow "UPDATE" provided it's not the command (e.g. in a string?), but simplistic check is safer
            return False

    return True

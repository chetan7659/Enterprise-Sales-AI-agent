from db.connection import get_connection

def run_query(sql: str):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        columns = [desc[0] for desc in cur.description]
        rows = cur.fetchall()
        return columns, rows
    finally:
        cur.close()
        conn.close()

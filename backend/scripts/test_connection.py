import sys
import os

# Add the backend directory to sys.path to allow running from scripts/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.connection import get_connection

def main():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        print("Snowflake connection OK. Result:", result)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()

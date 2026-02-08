import sys
import os

# Add the backend directory to sys.path to allow running from scripts/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from db.query_executor import run_query

def print_result(title, sql):
    print(f"\n--- {title} ---")
    columns, rows = run_query(sql)
    print(columns)
    for row in rows:
        print(row)

def main():
    print_result(
        "Pipeline by Stage",
        """
        SELECT stage, COUNT(*) AS deals, SUM(value) AS total_value
        FROM opportunities
        GROUP BY stage
        """
    )

    print_result(
        "High Value Stalled Deals",
        """
        SELECT opp_id, customer_id, value
        FROM opportunities
        WHERE stage = 'stalled' AND value > 100000
        """
    )

    print_result(
        "Lead Quality Overview",
        """
        SELECT status, AVG(score) AS avg_score
        FROM leads
        GROUP BY status
        """
    )

if __name__ == "__main__":
    main()

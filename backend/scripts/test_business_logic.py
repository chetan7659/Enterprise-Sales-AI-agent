import sys
import os

# Add the backend directory to sys.path to allow running from scripts/ folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic.sales_insights import (
    get_pipeline_summary,
    get_high_risk_deals,
    get_lead_quality
)

def main():
    print("\n--- Pipeline Summary ---")
    for item in get_pipeline_summary():
        print(item)

    print("\n--- High Risk Deals ---")
    for deal in get_high_risk_deals():
        print(deal)

    print("\n--- Lead Quality ---")
    print(get_lead_quality())


if __name__ == "__main__":
    main()

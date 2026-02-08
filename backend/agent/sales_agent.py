from logic.sales_insights import (
    get_pipeline_summary,
    get_high_risk_deals,
    get_lead_quality,
    get_avg_deal_size,
    get_top_customers,
    get_recent_activity
)
from agent.intent_router import classify_intent


class SalesAIAgent:

    def answer(self, question: str) -> str:
        intent = classify_intent(question)
        
        print(f"[DEBUG] Intent detected: {intent}")

        if intent == "PIPELINE_SUMMARY":
            return self._pipeline_response()

        if intent == "RISK_ANALYSIS":
            return self._risk_response()

        if intent == "LEAD_QUALITY":
            return self._lead_quality_response()
            
        if intent == "AVG_DEAL_SIZE":
            return self._avg_deal_size_response()

        if intent == "TOP_CUSTOMERS":
            return self._top_customers_response()

        if intent == "RECENT_ACTIVITY":
            return self._recent_activity_response()

        return (
            "I can help with pipeline summary, risk analysis, lead quality, "
            "average deal size, top customers, or recent activity. "
            "Please ask a sales-related question."
        )

    def _pipeline_response(self):
        summary = get_pipeline_summary()
        if not summary:
             return "The sales pipeline is currently empty."
             
        lines = ["Here is the current sales pipeline summary:"]

        for item in summary:
            lines.append(
                f"- {item['stage'].title()}: "
                f"{item['deals']} deals worth {item['total_value']:.0f}"
            )

        return "\n".join(lines)

    def _risk_response(self):
        risks = get_high_risk_deals()

        if not risks:
            return "There are no high-risk stalled deals at the moment."

        lines = ["These high-value deals are currently at risk:"]

        for deal in risks:
            lines.append(
                f"- Opportunity {deal['opportunity_id']} "
                f"(Customer {deal['customer_id']}): "
                f"value {deal['value']:.0f}"
            )

        return "\n".join(lines)

    def _lead_quality_response(self):
        quality = get_lead_quality()
        if not quality:
             return "No lead quality data available."
             
        lines = ["Lead quality by status:"]

        for status, score in quality.items():
            lines.append(f"- {status.title()}: average score {score}")

        return "\n".join(lines)

    def _avg_deal_size_response(self):
        avg_size = get_avg_deal_size()
        return f"The average deal size across all opportunities is {avg_size:,.2f}"

    def _top_customers_response(self):
        customers = get_top_customers()
        if not customers:
            return "No customer data available."
            
        lines = ["Here are our top customers by total opportunity value:"]
        for i, cust in enumerate(customers, 1):
            lines.append(f"{i}. {cust['name']}: {cust['total_value']:,.2f}")
            
        return "\n".join(lines)

    def _recent_activity_response(self):
        activities = get_recent_activity()
        if not activities:
            return "No recent sales activity found."
            
        lines = ["Here are the most recent sales activities:"]
        for act in activities:
             lines.append(f"- {act['date']} ({act['type']}): {act['notes']} (Opp {act['opportunity_id']})")
             
        return "\n".join(lines)

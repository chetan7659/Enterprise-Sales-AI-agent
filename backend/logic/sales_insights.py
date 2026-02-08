from db.query_executor import run_query

def get_pipeline_summary():
    sql = """
    SELECT stage, COUNT(*) AS deals, SUM(value) AS total_value
    FROM opportunities
    GROUP BY stage
    """
    columns, rows = run_query(sql)

    summary = []
    for stage, deals, value in rows:
        summary.append({
            "stage": stage,
            "deals": int(deals),
            "total_value": float(value) if value is not None else 0.0
        })

    return summary


def get_high_risk_deals(min_value=100000):
    sql = f"""
    SELECT opp_id, customer_id, value
    FROM opportunities
    WHERE stage = 'stalled' AND value > {min_value}
    """
    columns, rows = run_query(sql)

    risks = []
    for opp_id, customer_id, value in rows:
        risks.append({
            "opportunity_id": opp_id,
            "customer_id": customer_id,
            "value": float(value) if value is not None else 0.0,
            "risk_reason": "High-value deal stalled"
        })

    return risks


def get_lead_quality():
    sql = """
    SELECT status, AVG(score) AS avg_score
    FROM leads
    GROUP BY status
    """
    columns, rows = run_query(sql)

    quality = {}
    for status, avg_score in rows:
        quality[status] = round(float(avg_score), 2) if avg_score is not None else 0.0

    return quality

def get_avg_deal_size():
    sql = """
    SELECT AVG(value) as avg_value
    FROM opportunities
    """
    columns, rows = run_query(sql)
    
    if rows and rows[0][0] is not None:
        return float(rows[0][0])
    return 0.0

def get_top_customers(limit=3):
    sql = f"""
    SELECT c.name, SUM(o.value) as total_value
    FROM customers c
    JOIN opportunities o ON c.customer_id = o.customer_id
    GROUP BY c.name
    ORDER BY total_value DESC
    LIMIT {limit}
    """
    columns, rows = run_query(sql)
    
    top_customers = []
    for name, value in rows:
        top_customers.append({
            "name": name,
            "total_value": float(value) if value is not None else 0.0
        })
    return top_customers

def get_recent_activity(limit=5):
    sql = f"""
    SELECT a.activity_date, a.activity_type, a.notes, o.opp_id
    FROM sales_activity a
    JOIN opportunities o ON a.opp_id = o.opp_id
    ORDER BY a.activity_date DESC
    LIMIT {limit}
    """
    columns, rows = run_query(sql)
    
    activities = []
    for date, type_, notes, opp_id in rows:
        activities.append({
            "date": str(date),
            "type": type_,
            "notes": notes,
            "opportunity_id": opp_id
        })
    return activities

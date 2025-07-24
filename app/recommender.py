# app/recommender.py
from app.database import conn

def recommend_schemes(user_id: int):
    result = conn.execute(f"SELECT * FROM users WHERE user_id = {user_id}")
    row = result.fetchone()
    if not row:
        return [], []

    user_cols = [desc[0] for desc in result.description]
    user = dict(zip(user_cols, row))

    query = f"""
    SELECT scheme_id, name, category, description FROM schemes
    WHERE
        {user['age']} BETWEEN min_age AND max_age AND
        (caste = '{user['caste']}' OR caste = 'ALL') AND
        {user['income']} BETWEEN min_income AND max_income AND
        (employment_type = '{user['employment_type']}' OR employment_type = 'ALL') AND
        ('{user['health_status']}' = health_condition OR health_condition = 'ALL')
    """

    scheme_result = conn.execute(query)
    return scheme_result.fetchall(), [desc[0] for desc in scheme_result.description]



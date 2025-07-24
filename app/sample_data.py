# app/sample_data.py
from app.database import conn

def load_sample_data():
    conn.execute("DELETE FROM users")
    conn.execute("DELETE FROM schemes")

    conn.execute("""
    INSERT INTO users VALUES
    (1, 'Amit', 35, 'Male', 'OBC', 'Mumbai', 'Normal', 550000, 'Private'),
    (2, 'Neha', 28, 'Female', 'SC', 'Delhi', 'Disabled', 250000, 'Unemployed')
    """)

    conn.execute("""
    INSERT INTO schemes VALUES
    (101, 'PMAY', 'Govt', 'Housing subsidy for low income group', 18, 60, 'ALL', 0, 600000, 'ALL', 'ALL'),
    (102, 'NPS', 'Govt', 'Pension scheme for private employees', 18, 60, 'ALL', 200000, 1500000, 'Private', 'ALL'),
    (103, 'Disability Pension', 'Govt', 'Scheme for persons with disabilities', 18, 60, 'ALL', 0, 500000, 'ALL', 'Disabled')
    """)

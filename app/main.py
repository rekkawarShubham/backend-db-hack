# app/main.py
from fastapi import FastAPI
from app.models import User, Recommendation
from app.database import init_db, conn
from app.sample_data import load_sample_data
from app.recommender import recommend_schemes
from fastapi import HTTPException


app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()
    load_sample_data()

@app.post("/register/")
def register_user(user: User):
    conn.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                 (user.user_id, user.name, user.age, user.gender, user.caste,
                  user.city, user.health_status, user.income, user.employment_type))
    return {"status": "User registered"}

@app.get("/recommend/{user_id}", response_model=list[Recommendation])
def get_recommendations(user_id: int):
    results, columns = recommend_schemes(user_id)

    if not results:
        raise HTTPException(status_code=404, detail="User not found or no schemes")

    return [Recommendation(**dict(zip(columns, row))) for row in results]
import app
from fastapi import FastAPI, Request, HTTPException
from app.models import User
from app.database import upsert_user, get_user_by_id
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:9002"],  # Your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/user")
async def create_or_update_user(user: User, request: Request):
    upsert_user(user)
    return {"message": "User created or updated"}


@app.get("/user/{user_id}")
async def get_user(user_id: int):
    user_data = get_user_by_id(user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_data
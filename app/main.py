from fastapi import FastAPI, Request, HTTPException
from app.models import User, AdvisorRequest
from app.database import upsert_user, get_user_by_id
from pydantic.json import pydantic_encoder
from dotenv import load_dotenv
import json
from openai import OpenAI
import os
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()  # Load the .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # use ["http://localhost:3000"] for restricted access
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

@app.post("/advisor")
async def financial_advisor(request: AdvisorRequest):

    user_data = get_user_by_id(request.user_id)
    if user_data is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert datetime.date to string
    profile_json = json.dumps(user_data, indent=2, default=pydantic_encoder)

    # Build the prompt
    prompt = f"""
You are a highly experienced financial advisor helping individuals make sound financial decisions.

The following is the user's financial profile:
{profile_json}

The user is asking the following question:
"{request.question}"

Provide detailed, empathetic, and actionable financial advice considering their current profile. Use practical Indian investment instruments like SIPs, mutual funds, FD, PPF, NPS, etc. Keep the tone friendly and realistic.
"""

    try:
        client = OpenAI(api_key=OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial advisor."},
                {"role": "user", "content": prompt}
            ]
        )

        answer = response.choices[0].message.content

        return {
            "user_id": request.user_id,
            "question": request.question,
            "response": answer
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI error: {str(e)}")
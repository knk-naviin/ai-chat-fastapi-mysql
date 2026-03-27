from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv
import mysql.connector

# Load env
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

db_config = {
    "host": os.getenv("MYSQL_HOST"),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DB")
}

app = FastAPI()

# Request model
class ChatRequest(BaseModel):
    message: str

# DB connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# ✅ Create table automatically
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()

@app.on_event("startup")
def startup():
    create_table()

# Home route
@app.get("/")
def home():
    return {"message": "🚀 Simple AI Chat Running"}

# Chat endpoint
@app.post("/chat")
def chat(req: ChatRequest):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Call OpenRouter
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini",
                "messages": [
                    {"role": "user", "content": req.message}
                ]
            }
        )

        result = response.json()

        if "choices" not in result:
            raise HTTPException(status_code=500, detail=result)

        ai_reply = result["choices"][0]["message"]["content"]

        # ✅ Store only message (you can store both if needed)
        cursor.execute(
            "INSERT INTO messages (message) VALUES (%s)",
            (ai_reply,)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return {"reply": ai_reply}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# View all messages
@app.get("/messages")
def get_messages():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM messages ORDER BY id DESC")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"data": data}
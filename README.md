# 🚀 AI Chat Backend (FastAPI + OpenRouter + MySQL)

A simple and scalable AI-powered chat backend built using **FastAPI**, integrated with **OpenRouter API** for generating AI responses, and **MySQL** for storing chat messages.

---

## 📌 Features

* 🤖 AI response generation using OpenRouter
* ⚡ FastAPI-based REST API
* 🗄️ MySQL integration for persistent storage
* 🔐 Secure API key management using `.env`
* 🏗️ Automatic table creation on startup
* 📡 Simple `/chat` endpoint for interaction
* 📄 Retrieve stored messages from database

---

## 🛠️ Tech Stack

* **Backend:** FastAPI (Python)
* **AI API:** OpenRouter
* **Database:** MySQL
* **Environment Management:** python-dotenv

---

## 📁 Project Structure

```
project/
│── main.py
│── .env
│── requirements.txt
│── README.md
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
OPENROUTER_API_KEY=your_api_key_here

MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_password
MYSQL_DB=chatdb
```

---

## 📦 Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/ai-chat-fastapi-mysql.git
cd ai-chat-fastapi-mysql
```

### 2️⃣ Create virtual environment

```
python3 -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
uvicorn main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🌐 API Documentation

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### 🔹 POST `/chat`

Send a message to AI and store response in database.

**Request Body:**

```json
{
  "message": "Hello AI"
}
```

**Response:**

```json
{
  "reply": "Hello! How can I help you?"
}
```

---

### 🔹 GET `/messages`

Retrieve all stored messages.

---

## 🗄️ Database Schema

Table: `messages`

| Column     | Type      | Description                |
| ---------- | --------- | -------------------------- |
| id         | INT       | Auto-increment primary key |
| message    | TEXT      | AI response message        |
| created_at | TIMESTAMP | Auto-generated timestamp   |

---

## ⚙️ How It Works

1. User sends a message to `/chat`
2. FastAPI sends request to OpenRouter API
3. AI generates a response
4. Response is stored in MySQL
5. API returns the response to user

---

## 🚨 Common Issues

* ❌ `.env` not loading → ensure correct file location
* ❌ MySQL connection error → check credentials
* ❌ Table error → restart server to auto-create

---

## 🔥 Future Improvements

* Add user authentication (JWT)
* Store full conversation history
* Real-time streaming responses
* React frontend integration
* Deployment (Render / AWS)

---

## 👨‍💻 Author

**Naveen K**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

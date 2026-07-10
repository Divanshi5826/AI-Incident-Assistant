# 🤖 IncidentIQ
AI Incident Assistant is an AI-powered incident analysis system that helps troubleshoot common software incidents using **Retrieval-Augmented Generation (RAG)**.

The application retrieves relevant troubleshooting documents from a vector database and generates context-aware responses using **Google Gemini**.

---

## 🚀 Features

- AI-powered incident analysis
- Retrieval-Augmented Generation (RAG)
- Semantic Search using Vector Embeddings
- LangGraph workflow orchestration
- ChromaDB Vector Database
- Google Gemini integration
- FastAPI backend
- React + TailwindCSS frontend
- Source-aware responses
- Simple and modular architecture

---

## 🛠 Tech Stack

**Frontend**
- React
- Tailwind CSS
- Vite

**Backend**
- FastAPI
- Python

**AI / LLM**
- Google Gemini API
- LangChain
- LangGraph

**Vector Database**
- ChromaDB

**Embeddings**
- sentence-transformers (all-MiniLM-L6-v2)

---

## 🏗 Project Architecture

```
User
   │
   ▼
React Frontend
   │
   ▼
FastAPI
   │
   ▼
LangGraph
   │
   ├── Retrieve Node
   └── Generate Node
   │
   ▼
ChromaDB (Vector Search)
   │
   ▼
Google Gemini
   │
   ▼
AI Response
```

---

## 📂 Knowledge Base

The project uses markdown documents as its knowledge base.

- authentication.md
- database.md
- deployment.md
- redis.md
- server.md

These documents are chunked, embedded, indexed in ChromaDB, and retrieved using semantic similarity.

---

## ⚙️ Setup

### Clone Repository

```bash
git clone <repository-url>
cd AI-Incident-Assistant
```

### Backend

```bash
cd backend

python -m venv .venv

# Windows
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

Create a `.env` file inside the backend folder.

```env
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

Run the backend

```bash
uvicorn app:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## 📌 API Endpoint

### POST `/ask`

Example Request

```json
{
  "query": "Login API returning 401 Unauthorized"
}
```

Example Response

```json
{
  "question": "Login API returning 401 Unauthorized",
  "answer": "...",
  "sources": [
    "authentication.md"
  ]
}
```

---


## 🔮 Future Improvements

- Conversation memory
- PDF knowledge base support
- Multiple LLM providers
- User authentication
- Admin dashboard
- Cloud deployment

---

## 👨‍💻 Author

Divanshi

Built as a portfolio project to demonstrate practical implementation of RAG, LangGraph, FastAPI, React, and Generative AI.

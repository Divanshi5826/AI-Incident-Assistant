# AI Incident Assistant

AI Incident Assistant is a simple, interview-friendly project for analyzing software incidents. This repository is intentionally initialized with only the backend foundation so it stays easy to explain and extend in one week.

## What is included now

- `backend/` FastAPI application
- CORS enabled for future local frontend development
- Minimal configuration with `python-dotenv`
- Empty `frontend/` folder reserved for later work

## Backend structure

- `backend/app.py` - FastAPI entrypoint
- `backend/config.py` - Environment-based settings
- `backend/requirements.txt` - Python dependencies
- `backend/.env.example` - Sample environment variables
- `backend/.gitignore` - Python and local environment ignores

## Run the backend

1. Create a virtual environment.
2. Install dependencies from `backend/requirements.txt`.
3. Copy `backend/.env.example` to `backend/.env`.
4. Start the API with Uvicorn.

Example:

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

## Health check

Open `GET /` and the API returns:

```json
{
  "status": "running",
  "project": "AI Incident Assistant"
}
```

## Notes

- The frontend is intentionally not implemented yet.
- RAG, LangGraph, Gemini, and vector search are not added in this initialization step.

## Running the Project

1. Create a virtual environment.
2. Install requirements.
3. Add GOOGLE_API_KEY in backend/.env.
4. Run the API server.

Example:

```bash
cd backend
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload
```

API Endpoint:

POST /ask

Example request:

```json
{
  "query":"Login API returning 401"
}
```

Example response:

```json
{
  "question":"Login API returning 401",
  "answer":"...",
  "sources":[
    "authentication.md"
  ]
}
```

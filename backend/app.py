from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from config import settings
from graph.graph import run_graph

app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
)

# Allow the React frontend to call this API during local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "status": "running",
        "project": settings.project_name,
    }


class AskRequest(BaseModel):
    query: str


@app.post("/ask")
def ask(request: AskRequest) -> dict[str, object]:
    # Validate input early so users get a clear error message.
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    try:
        return run_graph(query)
    except ValueError as exc:
        # Surface configuration/input issues cleanly (for example missing API key).
        raise HTTPException(status_code=400, detail=str(exc)) from exc

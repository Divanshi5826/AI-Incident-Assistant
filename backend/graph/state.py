from typing import TypedDict


class IncidentState(TypedDict):
    """Shared state passed between LangGraph nodes."""

    query: str
    context: str
    answer: str
    sources: list[str]

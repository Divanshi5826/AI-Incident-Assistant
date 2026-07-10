from pathlib import Path

from langgraph.graph import END, START, StateGraph

from graph.state import IncidentState
from rag.llm import get_llm
from rag.rag_pipeline import PROMPT_TEMPLATE
from rag.retriever import retrieve


NO_INFO_MESSAGE = "I could not find enough information in the knowledge base."


def retrieve_node(state: IncidentState) -> IncidentState:
    """Retrieve the top 3 relevant chunks and build context for generation."""
    query = state["query"].strip()
    docs = retrieve(query)

    # If no relevant documents are found, keep the context empty.
    if not docs:
        return {
            **state,
            "context": "",
            "sources": [],
            "answer": "",
        }

    # Merge retrieved chunks into one context string.
    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    # Collect unique source filenames so the UI can show where the answer came from.
    sources: list[str] = []
    for doc in docs:
        source = doc.metadata.get("source")
        if isinstance(source, str):
            filename = Path(source).name
            if filename not in sources:
                sources.append(filename)

    return {
        **state,
        "context": context,
        "sources": sources,
        "answer": "",
    }


def generate_node(state: IncidentState) -> IncidentState:
    """Generate the final answer from retrieved context using Gemini."""
    query = state["query"].strip()
    context = state["context"].strip()

    # If nothing was retrieved, keep the response simple and deterministic.
    if not context:
        return {
            **state,
            "answer": NO_INFO_MESSAGE,
        }

    prompt = PROMPT_TEMPLATE.format(context=context, query=query)
    llm = get_llm()
    response = llm.invoke(prompt)
    answer = response.content if isinstance(response.content, str) else str(response.content)

    return {
        **state,
        "answer": answer.strip(),
    }


builder = StateGraph(IncidentState)
builder.add_node("retrieve_node", retrieve_node)
builder.add_node("generate_node", generate_node)
builder.add_edge(START, "retrieve_node")
builder.add_edge("retrieve_node", "generate_node")
builder.add_edge("generate_node", END)
compiled_graph = builder.compile()


def run_graph(query: str) -> dict[str, object]:
    """Run the LangGraph workflow for one incident query."""
    clean_query = query.strip()
    if not clean_query:
        raise ValueError("Query cannot be empty.")

    result = compiled_graph.invoke(
        {
            "query": clean_query,
            "context": "",
            "answer": "",
            "sources": [],
        }
    )

    return {
        "question": clean_query,
        "answer": result["answer"],
        "sources": result["sources"],
    }

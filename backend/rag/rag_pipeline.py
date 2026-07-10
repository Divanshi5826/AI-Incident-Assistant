from pathlib import Path

from rag.llm import get_llm
from rag.retriever import retrieve


PROMPT_TEMPLATE = """
You are an AI Incident Assistant.

Your job is to help users troubleshoot software incidents.

Instructions:
- Use ONLY the information provided in the Context.
- Summarize the information in clear and simple English.
- Do NOT make up facts.
- Do NOT use outside knowledge.
- If the context does not contain enough information, reply exactly:

"I could not find enough information in the knowledge base."

Context:
-----------------------
{context}
-----------------------

Question:
{query}

Answer:
"""


def answer_query(query: str) -> dict[str, object]:
    """Run the complete Retrieval-Augmented Generation (RAG) pipeline."""

    clean_query = query.strip()

    if not clean_query:
        raise ValueError("Query cannot be empty.")

    # Step 1: Retrieve the most relevant document chunks
    docs = retrieve(clean_query)

    # If nothing relevant is retrieved, return immediately
    if not docs:
        return {
            "question": clean_query,
            "answer": "I could not find enough information in the knowledge base.",
            "sources": [],
        }

    # Step 2: Merge retrieved chunks into one context
    context = "\n\n---\n\n".join(doc.page_content for doc in docs)

    # Step 3: Collect unique source filenames
    sources = []

    for doc in docs:
        source = doc.metadata.get("source")

        if isinstance(source, str):
            filename = Path(source).name

            if filename not in sources:
                sources.append(filename)

    # Step 4: Create the prompt for Gemini
    prompt = PROMPT_TEMPLATE.format(
        context=context,
        query=clean_query,
    )

    # Step 5: Generate the answer
    llm = get_llm()
    response = llm.invoke(prompt)

    answer = (
        response.content
        if isinstance(response.content, str)
        else str(response.content)
    )

    # Step 6: Return the response
    return {
        "question": clean_query,
        "answer": answer.strip(),
        "sources": sources,
    }
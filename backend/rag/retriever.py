from langchain_core.documents import Document

from rag.vector_store import get_vector_store


def retrieve(query: str) -> list[Document]:
	"""Return the top 3 most relevant document chunks for a user query."""
	clean_query = query.strip()
	if not clean_query:
		return []

	vector_store = get_vector_store()

	# Similarity search returns the most relevant chunks from the vector DB.
	return vector_store.similarity_search(clean_query, k=3)

from functools import lru_cache

from langchain_huggingface import HuggingFaceEmbeddings


@lru_cache(maxsize=1)
def get_embedding_model() -> HuggingFaceEmbeddings:
	"""Create and reuse the embedding model across the app."""
	return HuggingFaceEmbeddings(
		model_name="sentence-transformers/all-MiniLM-L6-v2"
	)

import shutil
from pathlib import Path

from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter

from rag.embedder import get_embedding_model
from rag.loader import load_markdown_documents


# Persist vectors inside backend/vector_db/ as requested.
VECTOR_DB_DIR = Path(__file__).resolve().parent.parent / "vector_db"
COLLECTION_NAME = "incident_docs"


def build_vector_store() -> Chroma:
	"""Create a fresh Chroma database from markdown docs."""
	documents = load_markdown_documents()
	if not documents:
		raise ValueError("No markdown files found in backend/data/docs.")

	# Split long files into smaller, searchable chunks.
	splitter = RecursiveCharacterTextSplitter(
    separators=["\n## ", "\n# ", "\n\n", "\n", " "],
    chunk_size=800,
    chunk_overlap=150,
)
	chunks = splitter.split_documents(documents)

	# Rebuild the local vector DB to avoid duplicate chunks across reruns.
	if VECTOR_DB_DIR.exists():
		shutil.rmtree(VECTOR_DB_DIR)
	VECTOR_DB_DIR.mkdir(parents=True, exist_ok=True)

	embeddings = get_embedding_model()

	# Build and persist the Chroma collection locally.
	return Chroma.from_documents(
		documents=chunks,
		embedding=embeddings,
		persist_directory=str(VECTOR_DB_DIR),
		collection_name=COLLECTION_NAME,
	)


def load_vector_store() -> Chroma:
	"""Load an existing Chroma database from disk."""
	return Chroma(
		persist_directory=str(VECTOR_DB_DIR),
		embedding_function=get_embedding_model(),
		collection_name=COLLECTION_NAME,
	)


def get_vector_store() -> Chroma:
	"""Load vectors if available, otherwise build them from docs."""
	has_existing_index = VECTOR_DB_DIR.exists() and any(VECTOR_DB_DIR.iterdir())
	if has_existing_index:
		return load_vector_store()
	return build_vector_store()

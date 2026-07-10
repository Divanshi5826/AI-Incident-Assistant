from pathlib import Path

from langchain_core.documents import Document


# Resolve the docs directory relative to backend/rag/loader.py.
DOCS_DIR = Path(__file__).resolve().parent.parent / "data" / "docs"


def load_markdown_documents() -> list[Document]:
	"""Load every markdown file from backend/data/docs as LangChain Documents."""
	documents: list[Document] = []

	# Read files in a stable order for predictable behavior.
	for file_path in sorted(DOCS_DIR.glob("*.md")):
		content = file_path.read_text(encoding="utf-8")

		# Store source metadata so retrieved chunks can be traced back to files.
		documents.append(
			Document(
				page_content=content,
				metadata={"source": str(file_path)},
			)
		)

	return documents

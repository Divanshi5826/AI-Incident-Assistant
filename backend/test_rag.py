from rag.rag_pipeline import answer_query


SAMPLE_QUERIES = [
    "Login API returning 401 Unauthorized",
    "Application works locally but fails after deployment",
    "Redis cache is not responding",
]


def main() -> None:
    """Run a few sample RAG queries and print question, answer, and sources."""
    for query in SAMPLE_QUERIES:
        print("=" * 80)
        print(f"Question: {query}")

        try:
            result = answer_query(query)
            print(f"Answer: {result['answer']}")
            print("Sources:")

            sources = result.get("sources", [])
            if sources:
                for source in sources:
                    print(f"- {source}")
            else:
                print("- No sources returned")

        except Exception as exc:  # Keep this simple for beginner-friendly debugging output.
            print(f"Error: {exc}")


if __name__ == "__main__":
    main()

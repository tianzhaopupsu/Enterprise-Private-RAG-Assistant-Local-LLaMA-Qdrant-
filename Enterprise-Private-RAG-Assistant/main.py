from app.rag_pipeline import RAGPipeline


def print_sources(sources, max_chars=200):

    print("\n📚 Sources:")

    for i, s in enumerate(sources):

        # 🔧 handle BOTH formats: flat dict OR qdrant payload dict
        payload = s.get("payload", s)

        text = payload.get("text", "")
        page = payload.get("page", "N/A")
        source = payload.get("source", "unknown")

        print(f"\n[{i+1}] Page {page} | Source: {source}")
        print(text[:max_chars].strip(), "...")


def main():

    rag = RAGPipeline()

    print("\n🤖 Scientific RAG Chatbot Ready")
    print("Type 'exit' or 'quit' to stop\n")

    while True:

        try:
            query = input("You: ").strip()

            if not query:
                continue

            if query.lower() in ["exit", "quit"]:
                print("\n👋 Goodbye!")
                break

            result = rag.ask(query)

            answer = result.get("answer", "No answer returned.")

            print("\n🤖 Bot:\n")
            print(answer)

            print_sources(result.get("sources", []))

            print("\n" + "-" * 60 + "\n")
        except KeyboardInterrupt:
            print("\n\n👋 Interrupted. Exiting...")
            break

        except Exception as e:
            print("\n⚠️ Error:", str(e))
            print("Continuing...\n")


if __name__ == "__main__":
    main()

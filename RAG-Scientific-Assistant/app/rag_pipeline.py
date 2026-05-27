from app.retriever import Retriever
from app.llm import LocalLlama
from app.prompt import build_prompt


class RAGPipeline:
    def __init__(self):
        self.retriever = Retriever()
        self.llm = LocalLlama()

    def ask(self, query: str):
        contexts = self.retriever.retrieve(query)

        prompt = build_prompt(query, contexts)

        response = self.llm.generate(prompt)

        return {
            "query": query,
            "answer": response,
            "sources": contexts
        }

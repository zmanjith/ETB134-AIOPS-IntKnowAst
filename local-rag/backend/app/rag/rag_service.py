from retrieval.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from LLM.ollama_service import OllamaService


class RagService:

    def __init__(self):

        self.retriever = Retriever()
        self.prompt_builder = PromptBuilder()
        self.llm = OllamaService()

    def ask(self, question):

        retrieved_chunks = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question,
            retrieved_chunks
        )

        answer = self.llm.generate(
            prompt["final_prompt"]
        )

        return {
            "question": question,
            "answer": answer,
            "sources": [
                result.payload["source"]
                for result in retrieved_chunks
            ]
        }
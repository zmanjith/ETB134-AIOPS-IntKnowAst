from retrieval.retriever import Retriever
from rag.prompt_builder import PromptBuilder

question = "Why did the payment service fail?"

retriever = Retriever()
builder = PromptBuilder()

results = retriever.retrieve(question)

prompt = builder.build(question, results)

print(prompt["final_prompt"])
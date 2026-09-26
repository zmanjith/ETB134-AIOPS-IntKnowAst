from retrieval.retriever import Retriever
from rag.prompt_builder import PromptBuilder


question = "Why is my pod in CrashLoopBackOff?"

retriever = Retriever()

results = retriever.retrieve(question)

builder = PromptBuilder()

prompt = builder.build(question, results)

print(prompt["final_prompt"])
from pathlib import Path

from loaders.knowledge_loader import KnowledgeLoader

knowledge = Path("../../knowledge")

loader = KnowledgeLoader()

documents = loader.load(knowledge)

print(len(documents))

print(documents[0])
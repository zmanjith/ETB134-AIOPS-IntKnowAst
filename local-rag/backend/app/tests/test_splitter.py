from pathlib import Path

from loaders.knowledge_loader import KnowledgeLoader

from chunking.splitter import DocumentSplitter


loader = KnowledgeLoader()

documents = loader.load(Path("../../knowledge"))

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

print(len(chunks))

print(chunks[3])
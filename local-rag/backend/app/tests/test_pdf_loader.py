from pathlib import Path
from loaders.pdf_loader import PDFLoader

loader = PDFLoader()

knowledge_dir = Path("../../knowledge/kubernetes")

pdf_file = next(knowledge_dir.glob("*.pdf"))

documents = loader.load(pdf_file)

print(f"Pages loaded: {len(documents)}")

print(documents[0])
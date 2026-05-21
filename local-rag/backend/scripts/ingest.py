from pypdf import PdfReader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# PDF path

BASE_DIR = Path(__file__).resolve().parent.parent
pdf_path = BASE_DIR / "data" / "AIAA-presentation_Nandan_Last.pdf"

# Read PDF
reader = PdfReader(pdf_path)

# Extract text
text = ""

for page in reader.pages:
    text += page.extract_text()

# Create splitter
splitter = RecursiveCharacterTextSplitter(
    #chunk_size=500,
    #chunk_overlap=50
    #chunk_size=200,
    chunk_size=1000,
    #chunk_overlap=20
    chunk_overlap=200
)

# Split text into chunks
chunks = splitter.split_text(text)

# Print info
print(f"Total chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")
print(chunks[0])

print("\nSECOND CHUNK:\n")
print(chunks[1])
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
# each chunk will have 500 characters and an overlap of 50 characters between chunks
# meaning that the last 50 characters of one chunk will be the first 50 characters of the next chunk
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

#print("\nFIRST CHUNK:\n")
#print(chunks[0])

#print("\nSECOND CHUNK:\n")
#print(chunks[1])

with open("chunks.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"\n--- CHUNK {i+1} ---\n")
        f.write(chunk)
        f.write("\n")
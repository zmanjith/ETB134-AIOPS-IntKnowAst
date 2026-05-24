from pypdf import PdfReader
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance
from qdrant_client.models import PointStruct


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
    chunk_size=1000,
    chunk_overlap=200
)

# Split text into chunks
chunks = splitter.split_text(text)

# Print info
print(f"Total chunks: {len(chunks)}")

#** For debugging purposes, we can write the chunks to a file to see how they look. */
#with open("chunks.txt", "w", encoding="utf-8") as f:
#    for i, chunk in enumerate(chunks):
#        f.write(f"\n--- CHUNK {i+1} ---\n")
#        f.write(chunk)
#        f.write("\n")

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(chunks)

# Connect Qdrant
client = QdrantClient(
    host="localhost",
    port=6333
)

# Create points
points = []

for i, vector in enumerate(embeddings):
    points.append(
        PointStruct(
            id=i,
            vector=vector.tolist(),
            payload={"text": chunks[i]}
        )
    )

# Upload
client.upsert(
    collection_name="documents",
    points=points
)

print("Vectors uploaded successfully")       
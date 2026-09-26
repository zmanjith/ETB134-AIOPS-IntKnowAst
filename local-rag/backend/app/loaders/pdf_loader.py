from pathlib import Path
from pypdf import PdfReader


class PDFLoader:

    def load(self, pdf_path: Path):

        reader = PdfReader(pdf_path)

        documents = []

        for page_num, page in enumerate(reader.pages):

            text = page.extract_text()

            if not text:
                continue

            documents.append(
                {
                    "text": text,
                    "source": pdf_path.name,
                    "category": pdf_path.parent.name,
                    "document_type": "pdf",
                    "filepath": str(pdf_path),
                    "page": page_num + 1
                }
            )

        return documents
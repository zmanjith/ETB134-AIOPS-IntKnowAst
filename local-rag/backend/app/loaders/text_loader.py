from pathlib import Path


class TextLoader:

    def load(self, file_path: Path):

        text = file_path.read_text(encoding="utf-8")

        return [

            {

                "text": text,

                "source": file_path.name,

                "category": file_path.parent.name,

                "document_type": "text",
                
                "filepath": str(file_path),

                "page": 1

            }

        ]
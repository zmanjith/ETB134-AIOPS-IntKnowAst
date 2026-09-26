from pathlib import Path


class MarkdownLoader:

    def load(self, file_path: Path):

        text = file_path.read_text(encoding="utf-8")

        return [

            {

                "text": text,

                "source": file_path.name,

                "category": file_path.parent.name,

                "document_type": "markdown",
                
                "filepath": str(file_path),

                "page": 1

            }

        ]
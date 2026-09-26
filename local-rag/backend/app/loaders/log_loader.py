from pathlib import Path


class LogLoader:

    def load(self, file_path: Path):

        text = file_path.read_text(encoding="utf-8")

        return [

            {

                "text": text,

                "source": file_path.name,

                "category": file_path.parent.name,

                "document_type": "log",
                
                "filepath": str(file_path),
                
                "technology": "application",

                "page": 1

            }

        ]
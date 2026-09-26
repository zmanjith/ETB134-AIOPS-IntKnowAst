from pathlib import Path


class DocumentDiscovery:

    SUPPORTED_EXTENSIONS = {
        ".pdf",
        ".md",
        ".txt",
        ".log"
    }

    def discover(self, knowledge_path: Path):

        documents = []

        for file in knowledge_path.rglob("*"):

            if not file.is_file():
                continue

            if file.suffix.lower() in self.SUPPORTED_EXTENSIONS:

                documents.append(file)

        return documents
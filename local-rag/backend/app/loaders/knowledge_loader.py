from loaders.loader_factory import LoaderFactory

from discovery.document_discovery import DocumentDiscovery


class KnowledgeLoader:

    def __init__(self):

        self.discovery = DocumentDiscovery()

    def load(self, knowledge_path):

        all_documents = []

        files = self.discovery.discover(knowledge_path)   ## calling the Discovery class to discover the files in the knowledge_path

        for file in files:

            loader = LoaderFactory.get_loader(file.suffix)

            if loader:

                documents = loader.load(file) 

                all_documents.extend(documents)

        return all_documents
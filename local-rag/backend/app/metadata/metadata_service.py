from pathlib import Path


class MetadataService:

    def enrich(self, document):

        source = Path(document["source"])

        document["metadata"] = {

            "source": source.name,

            "filename": source.stem,

            "extension": source.suffix,

            "category": document["category"],

            "technology": self._get_technology(document),

            "document_type": document["document_type"],
            
            "filepath": document["filepath"]

        }

        return document
    
# documents is a list returned by: loader.load(...). passing a list instead of a single document.

    def enrich_documents(self, documents):

        enriched = []

        for document in documents:
            enriched.append(self.enrich(document))

        return enriched
    
    
    # later we need to implement a more sophisticated way to determine the technology based on the document content or metadata
    def _get_technology(self, document):

        return document.get("technology", "general")
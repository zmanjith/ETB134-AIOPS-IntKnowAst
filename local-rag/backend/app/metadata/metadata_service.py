from pathlib import Path
from models.knowledge_unit import KnowledgeUnit

class MetadataService:
## this is called in Ingest.py now. Need to update it to respective Loader class.
    def enrich(self, document):
        document = self._normalize(document)
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
        return [self.enrich(document) for document in documents]
     
    
    def _get_technology(self, document):
        return document.get("technology", "general")
    
    
    def _normalize(self, document):
        """
        Temporary shim — removed in Step 1.9 once every source speaks
        KnowledgeUnit directly. Accepts the legacy dict shape from
        existing loaders unchanged, or converts a KnowledgeUnit into
        that same dict shape.
        """
        if isinstance(document, KnowledgeUnit):
            data = document.model_dump(mode="json")
            object_name = (data.get("labels") or {}).get("object", "unknown")

            return {
                "text": data["text"],
                "source": data["source"],
                "category": data["category"],
                "document_type": data["document_type"],
                "technology": data["technology"],
                "filepath": f"{data['source']}://{data.get('namespace')}/{object_name}",
                "page": 1,
            }

        return document
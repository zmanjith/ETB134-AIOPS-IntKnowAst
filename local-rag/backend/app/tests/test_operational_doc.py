from app.models.knowledge_unit import KnowledgeUnit
from app.enums.category import Category
from app.enums.document_type import DocumentType
from app.enums.severity import Severity
from app.enums.technology import Technology

doc = KnowledgeUnit(
    ingestion_channel=IngestionChannel.MANUAL,
  
    text="Database authentication failed.",

    source="payment.log",

    category=Category.LOGS,

    document_type=DocumentType.LOG,

    technology=Technology.POSTGRESQL
)

print(doc)
from metadata.metadata_service import MetadataService
from models.knowledge_unit import KnowledgeUnit
from enums.category import Category
from enums.document_type import DocumentType
from enums.technology import Technology
from enums.severity import Severity
from enums.ingestion_channel import IngestionChannel

unit = KnowledgeUnit(
    text='test', source='kubernetes', category=Category.KUBERNETES,
    document_type=DocumentType.K8S_EVENT, technology=Technology.KUBERNETES,
    severity=Severity.WARNING, ingestion_channel=IngestionChannel.LIVE_SIGNAL,
    namespace='default', labels={'object': 'bad-pod'}
)
result = MetadataService().enrich(unit)
print(result)
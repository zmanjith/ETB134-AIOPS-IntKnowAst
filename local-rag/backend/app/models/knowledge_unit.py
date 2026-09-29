from typing import Dict, Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone

from pydantic import BaseModel, Field, ConfigDict

from enums.category import Category
from enums.document_type import DocumentType
from enums.severity import Severity
from enums.technology import Technology
from enums.ingestion_channel import IngestionChannel


class KnowledgeUnit(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: UUID = Field(default_factory=uuid4)

    text: str
    source: str
    category: Category
    document_type: DocumentType
    technology: Technology
    severity: Severity

    ingestion_channel: IngestionChannel

    timestamp: Optional[str] = None
    ingested_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    ttl_expires_at: Optional[datetime] = None

    namespace: Optional[str] = None
    cluster: Optional[str] = None
    labels: Optional[Dict[str, str]] = None
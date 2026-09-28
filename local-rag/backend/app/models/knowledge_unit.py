from datetime import datetime
from typing import Dict, Optional
from pydantic import BaseModel, Field
from enums.category import Category
from enums.document_type import DocumentType
from enums.severity import Severity
from enums.technology import Technology
from enums.ingestion_channel import IngestionChannel


class KnowledgeUnit(BaseModel):
    """
    Canonical representation of operational knowledge
    inside the AIOps platform.
    """
    ingestion_channel: IngestionChannel
    ingested_at: datetime = Field(default_factory=datetime.utcnow)
    ttl_expires_at: Optional[datetime] = None

    # ---------- Required ----------#
    text: str = Field(
        description="Primary textual content to be embedded."
    )

    source: str = Field(
        description="Original source file or system."
    )

    category: Category = Field(
        description="High-level source category."
    )

    document_type: DocumentType = Field(
        description="Type of operational document."
    )

    technology: Technology = Field(
        description="Associated technology."
    )
    
    severity: Severity = Field(
        description="Severity level of the operational document."
    )
    
    # ---------- Optional ----------
    timestamp: Optional[str] = None

    namespace: Optional[str] = None

    cluster: Optional[str] = None

    labels: Optional[Dict[str, str]] = None
    
  
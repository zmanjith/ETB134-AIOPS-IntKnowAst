from typing import Dict, Optional

from pydantic import BaseModel, Field
from app.enums.category import Category
from app.enums.document_type import DocumentType
from app.enums.severity import Severity
from app.enums.technology import Technology

class OperationalDocument(BaseModel):
    """
    Canonical representation of operational knowledge
    inside the AIOps platform.
    """

    # ---------- Required ----------
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

    # ---------- Optional ----------
    timestamp: Optional[str] = None

    severity: Severity = Field(
        description="Severity level of the operational document."
    )

    namespace: Optional[str] = None

    cluster: Optional[str] = None

    labels: Optional[Dict[str, str]] = None
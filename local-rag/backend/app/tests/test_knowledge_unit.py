import pytest
from pydantic import ValidationError

from models.knowledge_unit import KnowledgeUnit
from enums.category import Category
from enums.document_type import DocumentType
from enums.technology import Technology
from enums.severity import Severity
from enums.ingestion_channel import IngestionChannel


def make_valid_unit(**overrides):
    data = dict(
        text="Sample text",
        source="test-source",
        category=Category.LOGS,
        document_type=DocumentType.LOG,
        technology=Technology.KUBERNETES,
        severity=Severity.WARNING,
        ingestion_channel=IngestionChannel.LIVE_SIGNAL,
        timestamp="2026-09-28T00:00:00",
    )
    data.update(overrides)
    return KnowledgeUnit(**data)


def test_valid_unit_constructs():
    unit = make_valid_unit()
    assert unit.text == "Sample text"
    assert unit.ingestion_channel == IngestionChannel.LIVE_SIGNAL


def test_id_and_ingested_at_auto_populate():
    unit = make_valid_unit()
    assert unit.id is not None
    assert unit.ingested_at is not None


def test_missing_required_field_raises():
    with pytest.raises(ValidationError):
        KnowledgeUnit(
            text="Sample text",
            source="test-source",
            category=Category.LOGS,
            document_type=DocumentType.LOG,
            technology=Technology.KUBERNETES,
            severity=Severity.WARNING,
            timestamp="2026-09-28T00:00:00",
        )


def test_invalid_enum_value_raises():
    with pytest.raises(ValidationError):
        make_valid_unit(category="not-a-real-category")


def test_ttl_defaults_to_none():
    unit = make_valid_unit()
    assert unit.ttl_expires_at is None
from src.api.models import *
import pytest
from pydantic import ValidationError

def test_message_defaults():
    m1 = ChatMessage(role="user", content="hi")
    m2 = ChatMessage(role="user", content="hi")
    assert m1.message_id != m2.message_id
    assert isinstance(m1.created_at, datetime)
    assert m1.metadata is None

def test_invalid_role_rejected():
    with pytest.raises(ValidationError):
        ChatMessage(role="hacker", content="hi")

def test_session_id_validation():
    with pytest.raises(ValidationError):
        ChatRequest(user_id=1, session_id="not-a-uuid", messages=[])

def test_platform_optional_but_validated():
    req_ok = ChatRequest(user_id=1, session_id=uuid4(), messages=[], platform=None)
    assert req_ok.platform is None
    with pytest.raises(ValidationError):
        ChatRequest(user_id=1, session_id=uuid4(), messages=[], platform="twitter")

def test_roundtrip():
    original = ChatMessage(role="assistant", content="ok", metadata={"action": "click"})
    data = original.model_dump(mode="json")
    restored = ChatMessage.model_validate(data)
    assert restored.message_id == original.message_id
    assert restored.created_at == original.created_at
    assert restored.metadata == original.metadata

def test_metadata_arbitrary():
    m = ChatMessage(role="assistant", content="x", metadata={"nested": {"a": [1, 2]}})
    assert m.metadata["nested"]["a"] == [1, 2]

def test_created_at_is_timezone_aware():
    m = ChatMessage(role="user", content="hi")
    assert m.created_at.tzinfo is not None
    assert m.created_at.utcoffset().total_seconds() == 0
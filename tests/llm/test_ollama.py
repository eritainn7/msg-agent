from langchain_ollama import ChatOllama
from src.llm.ollama import get_ollama_llm
import pytest

def test_get_ollama_llm():
    llm = get_ollama_llm()
    assert isinstance(llm, ChatOllama)

@pytest.mark.integration
@pytest.mark.timeout(15)
def test_ollama_real_connection():
    llm = get_ollama_llm()
    response = llm.invoke("Say 'OK'")
    assert response.content
    assert len(response.content) > 0
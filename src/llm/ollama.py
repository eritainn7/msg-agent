from langchain_ollama import ChatOllama
from src.llm.config import MODEL, BASE_URL

def get_ollama_llm()->ChatOllama:
    llm = ChatOllama(
        model=MODEL,
        base_url=BASE_URL,
    )

    return llm
from langchain.agents import create_agent
from src.llm.ollama import get_ollama_llm
from pathlib import Path

def load_prompt(name: str) -> str:
    prompt_path = Path(__file__).parent / "prompts" / f"{name}.md"

    if not prompt_path.exists():
        raise FileNotFoundError(f"Промпт {name} не найден по пути {prompt_path}")

    return prompt_path.read_text(encoding="utf-8")


def build_agent():
    llm = get_ollama_llm()
    system_prompt = load_prompt("system")

    return create_agent(
        model=llm,
        tools=[],
        system_prompt=system_prompt
    )
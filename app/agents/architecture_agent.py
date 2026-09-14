from pathlib import Path

from app.services.llm_service import LLMService

llm = LLMService()


def review(query: str):

    prompt_path = Path("app/prompts/architecture_prompt.txt")

    prompt_template = prompt_path.read_text(
        encoding="utf-8"
    )

    prompt = prompt_template.replace(
        "{query}",
        query
    )

    result = llm.generate(prompt)

    return {
        "reviewType": "Architecture Review",
        "agent": "Architecture Agent",
        "response": result
    }
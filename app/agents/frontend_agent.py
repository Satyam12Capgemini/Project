from pathlib import Path

from app.services.llm_service import LLMService

llm = LLMService()


def review(query: str):

    prompt_template = Path(
        "app/prompts/frontend_prompt.txt"
    ).read_text(
        encoding="utf-8"
    )

    prompt = prompt_template.replace(
        "{query}",
        query
    )

    response = llm.generate(prompt)

    return {
        "reviewType": "Frontend Review",
        "agent": "Frontend Agent",
        "response": response
    }
from pathlib import Path
from app.services.llm_service import LLMService

llm = LLMService()

def review(query: str):

    prompt = Path(
        "app/prompts/backend_prompt.txt"
    ).read_text(
        encoding="utf-8"
    )

    prompt = prompt.replace(
        "{query}",
        query
    )

    result = llm.generate(prompt)

    return {
        "reviewType": "Backend Review",
        "agent": "Backend Agent",
        "response": result
    }

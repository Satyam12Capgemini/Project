from app.services.llm_service import LLMService

llm = LLMService()


def review(query: str):

    prompt = f"""
    You are a Senior Code Review Agent.

    Review the following code or request:

    {query}

    Check:

    1. Security Issues
    2. Complexity
    3. Code Smells
    4. Hardcoded Secrets
    5. Refactoring Opportunities
    6. Best Practices

    Provide a structured review.
    """

    response = llm.generate(prompt)

    return {
        "reviewType": "Code Review",
        "agent": "Code Review Agent",
        "response": response
    }
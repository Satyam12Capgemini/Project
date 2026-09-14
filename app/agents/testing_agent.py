from app.services.llm_service import LLMService

llm = LLMService()

def review(query: str):

    prompt = f"""
    You are a Test Architect.

    Generate:

    - Unit Tests
    - Edge Cases
    - Boundary Conditions
    - Coverage Recommendations

    Input:

    {query}
    """

    response = llm.generate(prompt)

    return {
        "reviewType": "Testing Review",
        "agent": "Testing Agent",
        "response": response
    }

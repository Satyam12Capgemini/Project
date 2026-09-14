from app.services.llm_service import LLMService

llm = LLMService()

response = llm.generate(
    "Say Hello and confirm connection."
)

print(response)
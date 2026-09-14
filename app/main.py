from typing import List

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from app.router.intent_router import detect_agent
from app.services.file_service import FileService

from app.agents.architecture_agent import review as architecture_review
from app.agents.backend_agent import review as backend_review
from app.agents.frontend_agent import review as frontend_review
from app.agents.code_review_agent import review as code_review
from app.agents.testing_agent import review as testing_review


# =====================================================
# FASTAPI APP
# =====================================================

app = FastAPI(
    title="AI SDLC Review Assistant",
    version="2.0.0"
)


# =====================================================
# REQUEST MODELS
# =====================================================

class ReviewRequest(BaseModel):
    query: str


# =====================================================
# HEALTH CHECK
# =====================================================

@app.get("/")
def health():

    return {
        "status": "running",
        "application": "AI SDLC Review Assistant",
        "version": "2.0.0"
    }


# =====================================================
# REVIEW EXECUTOR
# =====================================================

def execute_review(agent: str, content: str):

    if agent == "architecture":
        return architecture_review(content)

    elif agent == "backend":
        return backend_review(content)

    elif agent == "frontend":
        return frontend_review(content)

    elif agent == "code_review":
        return code_review(content)

    elif agent == "testing":
        return testing_review(content)

    return {
        "reviewType": "Unknown",
        "agent": "Unknown",
        "message": "Unable to determine appropriate agent."
    }


# =====================================================
# QUERY REVIEW
# =====================================================

@app.post("/review")
def review_request(
    request: ReviewRequest
):

    agent = detect_agent(
        request.query
    )

    return execute_review(
        agent,
        request.query
    )


# =====================================================
# SINGLE FILE REVIEW
# =====================================================

@app.post("/review-file")
async def review_file(
    file: UploadFile = File(...)
):

    file_location = f"uploads/{file.filename}"

    with open(file_location, "wb") as f:

        content = await file.read()

        f.write(content)

    extracted_text = FileService.extract_text(
        file_location
    )

    agent = detect_agent(
        extracted_text
    )

    return execute_review(
        agent,
        extracted_text
    )


# =====================================================
# MULTIPLE FILE REVIEW
# =====================================================

from typing import List

@app.post("/review-multiple-files")
async def review_multiple_files(
    files: List[UploadFile] = File(...)
):

    reviews = []

    architecture_count = 0
    backend_count = 0
    frontend_count = 0
    code_count = 0
    testing_count = 0

    for file in files:

        file_location = f"uploads/{file.filename}"

        with open(file_location, "wb") as f:

            content = await file.read()

            f.write(content)

        extracted_text = FileService.extract_text(
            file_location
        )

        agent = detect_agent(
            extracted_text
        )

        result = execute_review(
            agent,
            extracted_text
        )

        if agent == "architecture":
            architecture_count += 1

        elif agent == "backend":
            backend_count += 1

        elif agent == "frontend":
            frontend_count += 1

        elif agent == "code_review":
            code_count += 1

        elif agent == "testing":
            testing_count += 1

        reviews.append(
            {
                "fileName": file.filename,
                "agentDetected": agent,
                "review": result
            }
        )

    return {

        "executiveSummary": {

            "totalFiles": len(files),

            "architectureReviews": architecture_count,

            "backendReviews": backend_count,

            "frontendReviews": frontend_count,

            "codeReviews": code_count,

            "testingReviews": testing_count

        },

        "reviews": reviews

    }
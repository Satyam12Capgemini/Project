# =====================================================
# AI SDLC REVIEW ASSISTANT
# INTENT ROUTER
# =====================================================

def detect_agent(content: str) -> str:

    q = content.lower()

    scores = {
        "architecture": 0,
        "backend": 0,
        "frontend": 0,
        "code_review": 0,
        "testing": 0
    }

    # =================================================
    # ARCHITECTURE KEYWORDS
    # =================================================

    architecture_keywords = {
        "microservice": 10,
        "microservices": 10,
        "architecture": 12,
        "system design": 12,
        "high level design": 12,
        "database design": 10,
        "adr": 12,
        "scalability": 10,
        "availability": 10,
        "capacity planning": 8,
        "distributed system": 10,
        "event driven": 10,
        "kafka": 10,
        "cqrs": 10,
        "saga": 10,
        "service boundary": 8
    }

    # =================================================
    # BACKEND KEYWORDS
    # =================================================

    backend_keywords = {
        "openapi": 15,
        "swagger": 15,
        "endpoint": 10,
        "rest api": 12,
        "/api": 8,
        "/products": 8,
        "/orders": 8,
        "requestbody": 10,
        "response": 4,
        "response schema": 10,
        "api versioning": 12,
        "backend": 10,
        "http": 6,
        "jwt": 12,
        "oauth": 12,
        "authorization": 8,
        "authentication": 8,
        "controller": 8
    }

    # =================================================
    # FRONTEND KEYWORDS
    # =================================================

    frontend_keywords = {
        "react": 20,
        "angular": 20,
        "vue": 20,
        "frontend": 15,
        "component": 12,
        "ui": 12,
        "ux": 12,
        "wcag": 20,
        "accessibility": 20,
        "state management": 15,
        "redux": 15,
        "zustand": 15,
        "jsx": 15,
        "tsx": 15,
        "html": 8,
        "css": 8,
        "tailwind": 12,
        "bootstrap": 8,
        "material ui": 12,
        "responsive": 10,
        "screen reader": 12,
        "aria": 12,
        "loading state": 10,
        "error state": 10,
        "ui risk": 10
    }

    # =================================================
    # CODE REVIEW KEYWORDS
    # =================================================

    code_keywords = {
        "public class": 20,
        "private": 10,
        "@service": 20,
        "@repository": 20,
        "@component": 20,
        "cyclomatic": 20,
        "code smell": 15,
        "refactor": 12,
        "refactoring": 12,
        "clean code": 12,
        "sonarqube": 12,
        "security vulnerability": 12,
        "java class": 12,
        "hardcoded": 12,
        "sql injection": 15,
        "java": 6,
        ".java": 20
    }

    # =================================================
    # TESTING KEYWORDS
    # =================================================

    testing_keywords = {
        "junit": 20,
        "@test": 20,
        "test case": 20,
        "test cases": 20,
        "coverage": 15,
        "mockito": 20,
        "unit test": 20,
        "unit tests": 20,
        "integration test": 20,
        "integration tests": 20,
        "test strategy": 15,
        "test plan": 15,
        "regression testing": 20,
        "regression checklist": 20,
        "qa": 10,
        "testing": 10
    }

    # =================================================
    # SCORE CALCULATION
    # =================================================

    for keyword, weight in architecture_keywords.items():

        if keyword in q:
            scores["architecture"] += weight

    for keyword, weight in backend_keywords.items():

        if keyword in q:
            scores["backend"] += weight

    for keyword, weight in frontend_keywords.items():

        if keyword in q:
            scores["frontend"] += weight

    for keyword, weight in code_keywords.items():

        if keyword in q:
            scores["code_review"] += weight

    for keyword, weight in testing_keywords.items():

        if keyword in q:
            scores["testing"] += weight

    # =================================================
    # FILE EXTENSION BOOSTERS
    # =================================================

    if ".jsx" in q:
        scores["frontend"] += 25

    if ".tsx" in q:
        scores["frontend"] += 25

    if ".java" in q:
        scores["code_review"] += 20

    if ".yaml" in q:
        scores["backend"] += 15

    if ".yml" in q:
        scores["backend"] += 15

    if ".feature" in q:
        scores["testing"] += 15

    # =================================================
    # SPECIAL CASES
    # =================================================

    if (
        "react" in q
        or "angular" in q
        or "wcag" in q
        or "accessibility" in q
    ):
        scores["frontend"] += 30

    if (
        "junit" in q
        or "mockito" in q
        or "@test" in q
    ):
        scores["testing"] += 30

    if (
        "swagger" in q
        or "openapi" in q
    ):
        scores["backend"] += 30

    # =================================================
    # DEBUG (OPTIONAL)
    # =================================================

    print(
        "Agent Routing Scores:",
        scores
    )

    # =================================================
    # WINNER
    # =================================================

    best_agent = max(
        scores,
        key=scores.get
    )

    return best_agent
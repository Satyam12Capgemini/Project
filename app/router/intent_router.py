def detect_agent(content: str) -> str:

    q = content.lower()

    if any(word in q for word in [
        "microservice",
        "architecture",
        "requirement",
        "adr",
        "database design"
    ]):
        return "architecture"

    if any(word in q for word in [
        "openapi",
        "swagger",
        "endpoint",
        "rest api",
        "/products"
    ]):
        return "backend"

    if any(word in q for word in [
        "react",
        "angular",
        "wcag",
        "component",
        "frontend"
    ]):
        return "frontend"

    if any(word in q for word in [
        "public class",
        "private",
        "security",
        "cyclomatic",
        "@service",
        "@repository"
    ]):
        return "code_review"

    if any(word in q for word in [
        "junit",
        "test case",
        "@test",
        "coverage"
    ]):
        return "testing"

    return "architecture"
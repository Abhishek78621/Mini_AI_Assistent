# response_generator.py
from config import USE_LLM, LLM_PROVIDER

def generate_response(intent: str, message: str) -> str:
    """
    Generates response based on detected intent.
    Uses logic by default, AI optionally.
    """

    # SENSITIVE CASE 
    if intent == "sensitive / human_required":
        return (
            "This message contains sensitive content. "
            "Please seek help from a trusted person or a qualified professional."
        )

    # OPTIONAL AI MODE
    if USE_LLM:
        return generate_with_llm(intent, message)

    # LOGIC-BASED RESPONSES 
    if intent == "content_generation":
        return (
            "Artificial Intelligence (AI) is a branch of computer science "
            "that focuses on creating machines capable of performing tasks "
            "that normally require human intelligence."
        )

    if intent == "summarization":
        return (
            "The text explains how artificial intelligence improves efficiency "
            "through automation and better decision-making."
        )

    if intent == "classification":
        return "This request is classified as an informational query."

    return "Unable to process the request."


def generate_with_llm(intent: str, message: str) -> str:
    """
    Placeholder for OpenAI / Gemini content generation.
    """

    if LLM_PROVIDER == "openai":
        return "[OpenAI-generated response would appear here]"

    if LLM_PROVIDER == "gemini":
        return "[Gemini-generated response would appear here]"

    return "LLM provider not supported."
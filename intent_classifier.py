# intent_classifier.py
import re
from config import USE_LLM


def classify_intent(message: str) -> str:
    """
    Classifies user intent BEFORE response generation.
    Hybrid approach:
    - Logic-based rules (default)
    - Optional LLM-based classification (future)
    """

    text = message.lower()

    # Sensitive check
    if re.search(r"(suicide|self harm|kill myself|depressed)", text):
        return "sensitive / human_required"
    
    if any(phrase in text for phrase in [
        "not feeling well",
        "feeling low",
        "feeling sad",
        "mentally tired",
        "i am sad",
        "emotionally drained"
    ]):
        return "sensitive / human_required"

    # Logical intent detection
    if "summarize" in text or "summary" in text:
        return "summarization"

    if "classify" in text or "sentiment" in text or "tone" in text:
        return "classification"

    # Optional AI fallback
    if USE_LLM:
        return classify_with_llm(message)

    # Default
    return "content_generation"


def classify_with_llm(message: str) -> str:
    """
    Placeholder for OpenAI / Gemini intent classification.
    Replace this function later with real API calls.
    """
    # Example (future):
    # return openai_classify(message)
    return "content_generation"

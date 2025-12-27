****Mini AI Assistant with Decision Logic****

**Overview**

This project implements a small AI-inspired assistant that decides how a user request should be handled before generating a response.
The main objective is to demonstrate decision-making logic, system design, and safe handling of user requests, rather than advanced machine learning models or UI development.

The assistant classifies user input into predefined intent categories and then routes the request to the appropriate response handler.

**Features**

- Accepts free-text user input via the command line

- Classifies intent before generating a response

- Supports four intent categories:

    - content_generation

    - summarization

    - classification

    - sensitive / human_required

- Safely declines sensitive requests

- Modular, readable, and easy to extend

- Designed to optionally integrate OpenAI or Gemini in the future

**Approach**

The system follows a two-layer pipeline.

1.**Decision Layer (Intent Classification)**

Before generating any response, the system determines what the user wants.

A logic-first hybrid approach is used:

-  Sensitive content is detected first (highest priority)

-  Logical rules identify summarization and classification requests

-  Remaining requests default to content generation

-  The design is LLM-agnostic and can be extended to OpenAI or Gemini later

2.**Response Handling**

After intent is identified, the request is routed to the correct response handler:

- Generates content for content requests

- Summarizes text for summarization requests

- Returns a label for classification requests

- Declines and explains responses for sensitive requests

**Intent Categories**

        Intent	                                        Description

    content_generation	                    Generate new content

    summarization	                        Produce a concise summary

    classification	                        Classify tone or intent

    sensitive / human_required	            Decline and recommend human intervention



**Project Structure**

Mini_AI_Assistent

        app.py                  # Main CLI application

        config.py               # Configuration (LLM toggle)

        intent_classifier.py    # Decision layer

        response_generator.py   # Response handling

        README.md

**Sample Inputs and Outputs**

**Example 1**

Input

Summarize artificial intelligence in healthcare


Output

Detected Intent: summarization
Response:
The text explains how artificial intelligence improves efficiency through automation and better decision-making.

**Example 2**

Input

    Classify the sentiment of this message


Output

    Detected Intent: classification
    Response:
    This request is classified as an informational query.

**Example 3**

Input

    I feel depressed and want to hurt myself


Output

    Detected Intent: sensitive / human_required
    Response:
    This message contains sensitive content. Please seek help from a trusted person or a qualified professional.

**Design Decisions**

- Logic-first intent classification ensures clarity and stability

- Sensitive requests are handled before any response is generated

- Modular structure improves maintainability and testing

- External AI models are optional and not required to run the system

**Limitations**

- Responses are rule-based for demonstration purposes

- Live LLM API calls are disabled by default

- Semantic understanding is limited compared to full LLM integration

**Future Improvements**

- Integrate OpenAI or Gemini for advanced reasoning and generation

- Improve semantic intent detection

- Add confidence scoring for intent classification

- Provide a REST API interface

**How to Run**

    python app.py


Type exit to quit the program.
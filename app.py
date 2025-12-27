# app.py
from intent_classifier import classify_intent
from response_generator import generate_response

def main():
    print("Mini AI Assistant")
    print("-" * 30)

    while True:
        user_input = input("\nEnter your message (type 'exit' to quit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        intent = classify_intent(user_input)
        print(f"\nDetected Intent: {intent}")

        response = generate_response(intent, user_input)
        print("Response:")
        print(response)

if __name__ == "__main__":
    main()

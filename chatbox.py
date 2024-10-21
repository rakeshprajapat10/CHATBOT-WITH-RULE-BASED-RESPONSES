responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you?": "I'm just a computer program, but thanks for asking!",
    "what is your name?": "I'm a simple rule-based chatbot.",
    "bye": "Goodbye! Have a great day!",
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, "I'm sorry, I don't understand that.")

def main():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    
    while True:
        user_input = input("chatbot: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
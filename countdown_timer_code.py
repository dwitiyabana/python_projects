"""
Simple Rule-Based Chatbot
-------------------------
A basic chatbot using pattern matching (regex) to respond to user input.
Extend it later with an LLM API call for a more powerful version (see bottom).
"""
import random
import re
 
# ----------------------------
# Pattern -> Response mapping
# ----------------------------
patterns = [
    (r'hi|hello|hey', [
        "Hello! How can I help you today?",
        "Hey there! What's on your mind?"
    ]),
    (r'how are you', [
        "I'm just a program, but I'm doing great! How about you?",
        "Running smoothly, thanks for asking!"
    ]),
    (r'what is your name', [
        "I'm a simple chatbot built in Python.",
        "You can call me PyBot."
    ]),
    (r'(.*) your name', [
        "I'm PyBot, nice to meet you!"
    ]),
    (r'bye|exit|quit', [
        "Goodbye! Have a great day!",
        "See you later!"
    ]),
    (r'thank you|thanks', [
        "You're welcome!",
        "No problem at all!"
    ]),
    (r'(.*)', [   # fallback for anything unmatched
        "I'm not sure I understand. Could you rephrase that?",
        "Interesting — tell me more.",
        "Hmm, I don't have a good answer for that yet."
    ])
]

def get_response(user_input: str) -> str:
    user_input = user_input.lower().strip()
    for pattern, responses in patterns:
        if re.search(pattern, user_input):
            return random.choice(responses)
    return "Sorry, I didn't understand that."
 
def chat():
    print("PyBot: Hi! I'm PyBot. Type 'bye' to exit.\n")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"PyBot: {response}")
        if re.search(r'bye|exit|quit', user_input.lower()):
            break

if __name__ == "__main__":
    chat()





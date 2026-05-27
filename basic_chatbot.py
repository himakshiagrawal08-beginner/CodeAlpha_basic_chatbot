#   TASK 3: Rule-Based Chatbot in Python

def get_bot_reply(message):
    """Return a predefined reply based on user input."""
    msg = message.lower().strip()

    # --- Greetings ---
    if msg in ["hello", "hi", "hey", "howdy"]:
        return "Hi there! Great to meet you! 😊"

    # --- Wellbeing ---
    elif "how are you" in msg or "how r u" in msg:
        return "I'm doing great, thanks for asking! How about you?"

    # --- Identity ---
    elif "your name" in msg or "who are you" in msg:
        return "I'm RuleBot — a simple if-elif powered chatbot!"

    # --- Help / Commands ---
    elif "help" in msg or "what can you do" in msg:
        return "I understand: hello, how are you, what's your name, joke, thanks, and bye!"

    # --- Jokes ---
    elif "joke" in msg or "funny" in msg:
        return "Why do programmers prefer dark mode? Because light attracts bugs! 🐛"

    # --- Gratitude ---
    elif "thank" in msg or msg == "thanks":
        return "You're welcome! Happy to help! 🙌"

    # --- Farewell ---
    elif msg in ["bye", "goodbye", "see you", "cya"]:
        return "Goodbye! See you next time! 👋"

    # --- Default / Fallback ---
    else:
        return "Hmm, I didn't understand that. Try: hello, how are you, or bye!"


def run_chatbot():
    """Main loop — keeps chatting until the user says bye."""
    print("RuleBot: Hi! I'm RuleBot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")            # Get input

        if not user_input.strip():             # Ignore empty input
            continue

        reply = get_bot_reply(user_input)      # Get reply using if-elif
        print(f"RuleBot: {reply}\n")

        # End the loop on farewell
        if user_input.lower().strip() in ["bye", "goodbye", "see you", "cya"]:
            break


# Entry point
if __name__ == "__main__":
    run_chatbot()
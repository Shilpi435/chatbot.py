import random

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.memory = []

        # Knowledge base
        self.responses = {
            "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
            "how are you": ["I'm just a bot, but I'm doing great!", 
                            "All systems running perfectly!"],
            "ai": ["AI stands for Artificial Intelligence.",
                   "AI enables machines to think and learn."],
            "bye": ["Goodbye!", "See you soon!", "Have a nice day!"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        self.memory.append(user_input)

        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])

        return "I'm not sure about that. Can you ask something else?"

    def show_memory(self):
        print("Conversation History:")
        for msg in self.memory:
            print("-", msg)


# Create chatbot
bot = Chatbot("MyBot")

print("Chatbot started! Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    response = bot.get_response(user_input)
    print("Bot:", response)

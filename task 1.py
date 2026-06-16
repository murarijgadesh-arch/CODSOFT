def chatbot():
    print("=" * 50)
    print("🤖 Welcome to the Rule-Based Chatbot!")
    print("Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user = input("\nYou: ").lower().strip()

        # Greetings
        if user in ["hi", "hello", "hey", "good morning", "good evening"]:
            print("Bot: Hello! Nice to meet you. 😊")

        # Asking chatbot name
        elif "your name" in user or "who are you" in user:
            print("Bot: My name is ChatBot. I'm a simple AI chatbot built using Python.")

        # Asking chatbot age
        elif "your age" in user or "how old are you" in user:
            print("Bot: I don't have an age, but I was created recently!")

        # Asking how chatbot is
        elif "how are you" in user:
            print("Bot: I'm doing great! Thanks for asking. How about you?")

        # User feeling good
        elif user in ["i am fine", "fine", "good", "great", "awesome"]:
            print("Bot: That's wonderful to hear! 😊")

        # User feeling bad
        elif "sad" in user or "not good" in user or "bad" in user:
            print("Bot: I'm sorry to hear that. I hope things get better soon.")

        # Help
        elif "help" in user:
            print("Bot: I can answer questions about:")
            print("- Greetings")
            print("- My name")
            print("- Time")
            print("- Date")
            print("- Weather")
            print("- Programming")
            print("- Jokes")
            print("- Motivation")
            print("- Calculator")
            print("- Bye")

        # Time
        elif "time" in user:
            from datetime import datetime
            current_time = datetime.now().strftime("%I:%M %p")
            print(f"Bot: Current time is {current_time}")

        # Date
        elif "date" in user:
            from datetime import datetime
            today = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {today}")

        # Weather
        elif "weather" in user:
            print("Bot: I can't check live weather, but I hope it's a pleasant day where you are!")

        # Programming
        elif "python" in user:
            print("Bot: Python is an easy-to-learn, powerful programming language used in AI, Web Development, Data Science, and more.")

        elif "java" in user:
            print("Bot: Java is an object-oriented programming language widely used for enterprise and Android development.")

        elif "c++" in user or "cpp" in user:
            print("Bot: C++ is a fast programming language commonly used for system software, game development, and competitive programming.")

        # AI
        elif "artificial intelligence" in user or user == "ai":
            print("Bot: Artificial Intelligence enables machines to perform tasks that usually require human intelligence.")

        # Joke
        elif "joke" in user:
            print("Bot: Why do programmers prefer dark mode?")
            print("Bot: Because light attracts bugs! 😂")

        # Motivation
        elif "motivate" in user or "motivation" in user:
            print("Bot: Believe in yourself. Every expert was once a beginner!")

        # Favorite color
        elif "favorite color" in user:
            print("Bot: I like blue because it reminds me of technology!")

        # Calculator
        elif user.startswith("calculate"):
            try:
                expression = user.replace("calculate", "").strip()
                result = eval(expression)
                print(f"Bot: The answer is {result}")
            except:
                print("Bot: Please enter a valid mathematical expression.")
                print("Example: calculate 15 + 25")

        # Thanks
        elif "thank" in user:
            print("Bot: You're welcome! Happy to help. 😊")

        # Goodbye
        elif user in ["bye", "exit", "quit"]:
            print("Bot: Goodbye! Have a wonderful day! 👋")
            break

        # Unknown input
        else:
            print("Bot: Sorry, I didn't understand that.")
            print("Bot: Type 'help' to see what I can do.")


# Start the chatbot
chatbot()
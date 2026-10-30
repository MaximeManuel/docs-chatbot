print("Type 'Quit' whenever you are ready to exit the program")

def get_reply(message):
    return f"You said: {message}"

while True:

    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("stopped")
        break

    if user_input == "": 
        continue

    answer = get_reply(user_input)
    print(answer)



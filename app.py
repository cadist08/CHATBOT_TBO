from engine import ChatbotEngine


def main():
    bot = ChatbotEngine()

    print("=" * 50)
    print("CHATBOT LAYANAN PUBLIK")
    print("=" * 50)

    print(bot.process("mulai"))

    while True:
        user_input = input("\nAnda : ")

        response = bot.process(user_input)
        print("\nBot :", response)

        if bot.state == "EXIT":
            break


if __name__ == "__main__":
    main()
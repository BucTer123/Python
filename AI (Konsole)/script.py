from dotenv import load_dotenv
import os
from art import text2art
from openai import OpenAI

dotenv_path = "/home/shlawa/PyCharmMiscProject/AI (Konsole)/main.env"
load_dotenv(dotenv_path)

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

print(text2art("C H A T G P T !"))

messages = [{"role": "system", "content": "You are smart assistance"}]

while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create (
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    print(bot_reply)

    messages.append({"role": "assistant", "content": bot_reply})

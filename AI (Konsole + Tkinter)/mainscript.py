from dotenv import load_dotenv
import tkinter as tk
import os
from openai import OpenAI

win = tk.Tk()

win.title("App")

win.geometry("800x600")


def start_chat_callback():
    dotenv_path = "/AI (Konsole + Tkinter)/main.env"

    load_dotenv(dotenv_path)

    api_key = os.getenv("OPENAI_API_KEY")

    client = OpenAI(api_key=api_key)

    messages = [{"role": "system", "content": "You are smart assistant"}]

    if entry.get() == "exit":
        win.quit()
        return

    messages.append({"role": "user", "content": entry.get()})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    bot_reply = response.choices[0].message.content
    tk.Label(win, text=bot_reply)

    messages.append({"role": "assistant", "content": bot_reply.pack()})

    entry.delete(0, tk.END)

def ai():
    global entry

    text_input = tk.Label(win, text="> ")
    entry = tk.Entry(win)

    entry.get()
    text_input.pack()

    tk.Button(win, text="Go", command=start_chat_callback)
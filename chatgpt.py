import openai
import os

openai.api_key = ""
openai.Model.list()

# init chat 
chat_messages = [{"role": "system", "content": "You are a helpful voice assistant, speak only in English, with sentences less than 10 words."}]

# user messages
user_messages = ["what can you say about football?", "Who won the world series in 2020?", "Where was it played?"]

for message in user_messages:

    print("user:", message)

    chat_messages.append({"role": "user", "content": message})

    completions = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=chat_messages
    )

    assistant_answer = completions.choices[0].message.content
    print("assistant:", assistant_answer)

    chat_messages.append({"role": "assistant", "content": assistant_answer})
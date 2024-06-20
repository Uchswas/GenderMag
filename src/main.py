from openai import OpenAI
from promptlayer import PromptLayer
from dotenv import load_dotenv
import os

load_dotenv()
PROPLAYER_API_KEY = os.getenv('PROPLAYER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

promptlayer_client = PromptLayer(api_key=PROPLAYER_API_KEY)
OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()

def create_chat_completion(messages, tags):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        pl_tags=tags
    )
    return response

messages = [
    {"role": "system", "content": "You are an AI assistant."}
]

def handle_user_input(user_input):
    messages.append({"role": "user", "content": user_input})
    completion = create_chat_completion(messages, ["continuous-chat"])
    assistant_reply = completion.choices[0].message['content']
    messages.append({"role": "assistant", "content": assistant_reply})
    print(assistant_reply)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    handle_user_input(user_input)

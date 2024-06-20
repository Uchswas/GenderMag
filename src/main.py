from openai import OpenAI
from promptlayer import PromptLayer
from dotenv import load_dotenv
import os
from subgoals_actions import strings_to_iterate_over
from examples import starting_prompt

import sys
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)
from utils import extract_answer_and_facets

load_dotenv()
PROPLAYER_API_KEY = os.getenv('PROPLAYER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

promptlayer_client = PromptLayer(api_key=PROPLAYER_API_KEY)
OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()

def create_chat_completion(messages, tags):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        pl_tags=tags,
        temperature = 0
    )
    return response

messages = [
    {"role": "system", "content": starting_prompt}
]

def handle_user_input(user_input):
    messages.append({"role": "user", "content": user_input})
    completion = create_chat_completion(messages, ["gendermag", "gmmomment2", "tempdefault"])
    assistant_reply = completion.choices[0].message.content
    print(user_input)
    print("\n\n")
    print(assistant_reply)
    print("\n\n")
    print("\n\n")
    print("\n\n")
    messages.append({"role": "assistant", "content": assistant_reply})



for user_input in strings_to_iterate_over:
    handle_user_input(user_input)

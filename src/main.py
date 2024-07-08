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

def extract_before_explanation(text):
    # Define the delimiter
    delimiter = "Explanation of the Image:"
    
    # Find the index of the delimiter
    delimiter_index = text.find(delimiter)
    
    # Extract the portion before the delimiter
    if delimiter_index != -1:
        result = text[:delimiter_index].strip()
    else:
        result = text.strip()
    
    return result


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
    completion = create_chat_completion(messages, ["gendermag", "GMMOMENTFINAL1", "tempdefault"])
    assistant_reply = completion.choices[0].message.content
    print(user_input)
    print("\n\n")
    print(assistant_reply)
    print("\n\n")
    print("\n\n")
    print("\n\n")
    assistant_reply = extract_before_explanation(assistant_reply)
    messages.append({"role": "assistant", "content": assistant_reply})



for user_input in strings_to_iterate_over:
    handle_user_input(user_input)

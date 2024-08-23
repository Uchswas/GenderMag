from openai import OpenAI
from promptlayer import PromptLayer
from dotenv import load_dotenv
import os
from subgoals_actions import strings_to_iterate_over, TAG, TYPE
from examples import starting_prompt
import re
import sys
global count 

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)
from utils import extract_answer_and_facets

load_dotenv()
PROPLAYER_API_KEY = os.getenv('PROPLAYER_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

promptlayer_client = PromptLayer(api_key=PROPLAYER_API_KEY)
OpenAI = promptlayer_client.openai.OpenAI
client = OpenAI()

def find_links(text):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(
        r'(https?://[^\s]+)')
    # Find all URLs using the pattern
    urls = url_pattern.findall(text)
    return urls[0]


def extract_before_explanation(text):
    # Define the delimiter
    delimiter = "Details of the image"
    
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
    image_link = find_links(user_input)
    print(image_link)
    messages.append({"role": "user", "content":[ {
        "type": "text",
        "text" : user_input
         },
         {
             "type" : "image_url",
             "image_url" : {
                 "url": image_link
             }
         }

        ]
        })
    completion = create_chat_completion(messages, ["YesNoOnly", TAG, TYPE])
    assistant_reply = completion.choices[0].message.content
    print(user_input)
    print("\n\n")
    print(assistant_reply)
    print("\n\n")
    print("\n\n")
    print("\n\n")
    messages.append({"role": "assistant", "content": assistant_reply})
    


user_answer = input("Do you change the Tag in requesta and change the before question AND CHANGE THE HMTL TO PNG? If so, Press Y to proceed ")
if user_answer == 'y' or user_answer == 'Y':
    count = 1
    for user_input in strings_to_iterate_over:
        print(count)
        handle_user_input(user_input)
        count = count + 1
else:
    print("Do it")


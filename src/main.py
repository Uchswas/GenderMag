from openai import OpenAI
from promptlayer import PromptLayer
from dotenv import load_dotenv
import os
from openpyxl import Workbook, load_workbook

from subgoals_actions import strings_to_iterate_over, TAG, TYPE
from examples import starting_prompt
import re
import sys
import time
responses = []

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
        temperature = 0,
    )
    return response

messages = [
    {"role": "system", "content": starting_prompt}
]

def handle_user_input(user_input,i):
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
    completion = create_chat_completion(messages, ["YesNoOnly", TAG, TYPE,f"Iteration{i}"])
    assistant_reply = completion.choices[0].message.content
    responses.append(assistant_reply)
    messages.append({"role": "assistant", "content": assistant_reply})
    


for i in range(2,6):
    responses = []
    messages = [
    {"role": "system", "content": starting_prompt}
    ]

    for user_input in strings_to_iterate_over:
        handle_user_input(user_input,i)
    wb = Workbook()
    ws = wb.active

    for index, value in enumerate(responses, start=1):
        ws.cell(row=index, column=1, value=value)
    wb.save("../outputs/"+TAG+str(i)+'.xlsx')

    time.sleep(6)

  
else:
    print("Do it")


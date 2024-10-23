import google.generativeai as genai  # Correct import for Gemini API
from dotenv import load_dotenv
import os
from openpyxl import Workbook
import re
import sys
import time

from subgoals_actions import strings_to_iterate_over, TAG, TYPE
from examples import starting_prompt

# Ensure the correct path configuration
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_directory)
from utils import extract_answer_and_facets

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Configure the Gemini API client
genai.configure(api_key=GEMINI_API_KEY)

responses = []

def find_links(text):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    urls = url_pattern.findall(text)
    return urls[0] if urls else ""

def extract_before_explanation(text):
    delimiter = "Details of the image"
    delimiter_index = text.find(delimiter)
    return text[:delimiter_index].strip() if delimiter_index != -1 else text.strip()

def create_chat_completion(messages, tags):
    # Flatten the messages into a single string
    def extract_content(msg):
        if isinstance(msg["content"], list):
            # If content is a list, join the individual items into a string
            return "\n".join([str(item) for sublist in msg["content"] for item in sublist.values()])
        return msg["content"]

    # Create the full prompt by extracting and joining all message contents
    full_prompt = "\n".join([extract_content(msg) for msg in messages])

    # Generate content using the Gemini API
    model = genai.GenerativeModel('gemini-1.0-pro')
    response = model.generate_content(full_prompt)
    return response


messages = [{"role": "system", "content": starting_prompt}]

def handle_user_input(user_input, i):
    image_link = find_links(user_input)
    print(image_link)
    messages.append({
        "role": "user",
        "content": [
            {"type": "text", "text": user_input},
            {"type": "image_url", "image_url": {"url": image_link}},
        ]
    })
    completion = create_chat_completion(messages, ["YesNoOnly", TAG, TYPE, f"Iteration{i}"])
    assistant_reply = completion.text
    responses.append(assistant_reply)
    messages.append({"role": "assistant", "content": assistant_reply})

for i in range(1, 2):
    responses = []
    messages = [{"role": "system", "content": starting_prompt}]

    for user_input in strings_to_iterate_over:
        handle_user_input(user_input, i)
        time.sleep(6)
    wb = Workbook()
    ws = wb.active

    for index, value in enumerate(responses, start=1):
        ws.cell(row=index, column=1, value=value)

    output_path = f"../outputs/{TAG}{i}.xlsx"
    wb.save(output_path)
    print(f"Saved to {output_path}")

    time.sleep(6)

else:
    print("Do it")

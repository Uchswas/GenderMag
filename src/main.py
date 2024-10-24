import anthropic
import base64
import os
import re
import time
from openpyxl import Workbook
from examples import starting_prompt
from subgoals_actions import strings_to_iterate_over, TAG, TYPE
from dotenv import load_dotenv
import os

load_dotenv()



client = anthropic.Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))

def load_image_as_base64(image_url):
    # Download and convert the image to base64
    import requests
    response = requests.get(image_url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8'), response.headers['Content-Type']
    else:
        raise ValueError(f"Failed to load image from {image_url}")

def find_links(text):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    urls = url_pattern.findall(text)
    return urls[0] if urls else None

def create_chat_completion(image_media_type, image_data, user_text, tags):
    # Prepare the message structure for the API call
    message = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": image_media_type,
                            "data": image_data,
                        },
                    },
                    {
                        "type": "text",
                        "text": user_text,
                    },
                ],
            }
        ],
    )
    return message

def handle_user_input(user_input, i):
    # Extract image URL from the user input
    image_link = find_links(user_input)
    print(f"Image link: {image_link}")

    # Load the image as base64
    image_data, image_media_type = load_image_as_base64(image_link)

    # Create the user message and call the API
    completion = create_chat_completion(
        image_media_type, image_data, user_input, [TAG, TYPE, f"Iteration{i}"]
    )

    # Extract and store the assistant's reply
    print(completion.content[0].text)
    assistant_reply = completion.content[0].text
    responses.append(assistant_reply)
    print(f"Assistant reply: {assistant_reply}")

def save_responses_to_excel(responses, iteration):
    # Save the responses to an Excel file
    wb = Workbook()
    ws = wb.active

    for index, value in enumerate(responses, start=1):
        ws.cell(row=index, column=1, value=value)

    output_path = f"../outputs/{TAG}{iteration}.xlsx"
    wb.save(output_path)
    print(f"Responses saved to {output_path}")

responses = []

for i in range(1, 2):
    responses = []  # Reset responses for each iteration

    for user_input in strings_to_iterate_over:
        try:
            handle_user_input(user_input, i)
        except Exception as e:
            print(f"Error processing input: {e}")

    save_responses_to_excel(responses, i)

    # Pause to avoid rate limits
    time.sleep(6)

print("Completed.")

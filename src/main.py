import openai
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up your API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PROPLAYER_API_KEY = os.getenv('PROPLAYER_API_KEY')
CONTEXT_ID = os.getenv('CONTEXT_ID')

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Function to call OpenAI API
def chat_with_gpt(prompt, conversation_history):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation_history + [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# Function to get or update context using PropLayer (pseudo code, adjust as per actual API)
def update_proplayer_context(context_id, new_prompt):
    headers = {
        'Authorization': f'Bearer {PROPLAYER_API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'context_id': context_id,
        'new_prompt': new_prompt
    }
    response = requests.post('https://api.proplayer.com/update_context', headers=headers, json=data)
    return response.json()

# Initialize conversation
conversation_history = []

while True:
    user_input = input("You: ")
    
    # Update context with new user input
    update_response = update_proplayer_context(CONTEXT_ID, user_input)
    
    # Get updated conversation history
    conversation_history = update_response['conversation_history']
    
    # Get response from GPT-3.5
    gpt_response = chat_with_gpt(user_input, conversation_history)
    
    # Update conversation history with GPT response
    conversation_history.append({"role": "assistant", "content": gpt_response})
    
    # Print GPT response
    print(f"GPT: {gpt_response}")

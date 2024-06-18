import openai
from proptlayr import PromptLayer

# Set up the OpenAI API key
openai.api_key = 'your-openai-api-key'

# Set up ProptLayr
pl = PromptLayer(api_key='your-proptlayr-api-key')

# Define the few-shot examples
examples = [
    {
        "role": "system",
        "content": "You are a helpful assistant with the persona of ABI. Answer questions as ABI would."
    },
    {
        "role": "user",
        "content": "Would ABI know what to do next on this webpage?"
    },
    {
        "role": "assistant",
        "content": "ABI would probably look for a clear and prominent button or link that indicates the next step."
    },
    {
        "role": "user",
        "content": "How would ABI react to a complex form?"
    },
    {
        "role": "assistant",
        "content": "ABI might feel overwhelmed by a complex form and prefer more straightforward, step-by-step guidance."
    },
    {
        "role": "user",
        "content": "Would ABI find this feature easy to use?"
    },
    {
        "role": "assistant",
        "content": "ABI might find this feature confusing without clear instructions or a tutorial."
    }
]

# Initialize PromptLayer with the initial examples
pl.add_messages(examples)

# Define the function to get the LLM's response with context
def get_response_from_llm():
    response = openai.ChatCompletion.create(
        model="gpt-4",  # Use "gpt-3.5-turbo" or another chat model if "gpt-4" is not available
        messages=pl.get_messages()
    )

    return response.choices[0].message['content'].strip()

# Continuous chat loop with context
def continuous_chat():
    print("Starting the GenderMag continuous chat. Type 'exit' to end the chat.")
    
    while True:
        question = input("Enter the action or sub-goal to evaluate: ")
        if question.lower() == 'exit':
            print("Exiting the chat.")
            break
        
        pl.add_message({"role": "user", "content": question})
        response = get_response_from_llm()
        pl.add_message({"role": "assistant", "content": response})
        print(f"Response: {response}")

# Run the continuous chat loop
continuous_chat()

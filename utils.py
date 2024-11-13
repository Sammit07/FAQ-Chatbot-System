import os
from openai import OpenAI

def generate_response(user_input):
    # Initialize the OpenAI client with your API key
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    if not client.api_key:
        raise ValueError("OpenAI API key is not set in environment variables.")

    try:
        # Use the new API interface to create a chat completion
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": user_input}],
            model="ft:gpt-3.5-turbo-0125:student:intelligent-faq:9O3zLbYZ"
        )
        # Extract and return the response text
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"An error occurred while generating a response: {e}")
        raise







import os

import openai
import requests
from bs4 import BeautifulSoup

# Set OpenAI API key
openai_api_key = os.environ.get('OPENAI_API_KEY')

# Initialize messages as an empty list
messages = [{"role": "system", "content": "You are a knowledgeable person. Nice to chat with you."}]

def message_history_str(messages):
    """
    Convert message history to a string.

    Args:
        messages (list): List of dictionaries representing messages.

    Returns:
        str: String representation of message history.
    """
    output = "\n".join([line.get("role") + ": " + line.get("content") for line in messages])
    return output

def generate_response(prompt, messages):
    """
    Generate a response using OpenAI's Chat Completion API.

    Args:
        prompt (str): The prompt or user input.
        messages (list): List of dictionaries representing messages.

    Returns:
        str: Generated response from the Chat Completion API.
    """
    # Check if API key is available
    if not openai_api_key:
        raise ValueError("OpenAI API key not found in environment variables.")

    # Generate response using OpenAI API
    response = openai.ChatCompletion.create(
        model="ft:gpt-3.5-turbo-0125:student:intelligent-faq:9O3zLbYZ",
        messages=messages,
        max_tokens=150,
        api_key=openai_api_key  # Pass the API key to the API request
    )

    # Extract the message from the response
    message = response.choices[0].message
    messages.append({"role": message.role, "content": message.content.strip()})

    return message.content.strip()



def scrape_webpage(url):
    """
    Scrape a webpage and return its content.

    Args:
        url (str): URL of the webpage to scrape.

    Returns:
        str: Content of the webpage.
    """
    url=""
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.content, 'html.parser')
    return soup

# Example usage
if __name__ == "__main__":
    # Example usage of functions
    print("Message History:")
    print(message_history_str(messages))

    # Example usage of generate_response function
    print("\nGenerated Response:")
    user_input = "Hello, how are you?"
    print(generate_response(user_input, messages))

    # Example usage of scrape_webpage function
    print("\nWebpage Content:")
    url = ""
    webpage_content = scrape_webpage(url)
    print(webpage_content)


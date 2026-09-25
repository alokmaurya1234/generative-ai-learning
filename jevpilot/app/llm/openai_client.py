import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from jevpilot/.env
load_dotenv()

# Initialize the client automatically picking up OPENAI_API_KEY from the environment
client = OpenAI()

def generate_response(prompt: str, system_message: str = "You are a helpful assistant.") -> str:
    """
    A reusable wrapper for OpenAI text generation.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-6-luna", # You were right! Using the newly released Luna model.
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7 
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error connecting to OpenAI: {str(e)}"
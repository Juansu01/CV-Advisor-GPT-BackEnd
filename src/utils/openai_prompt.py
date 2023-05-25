import os
from dotenv import load_dotenv, find_dotenv
import openai

_ = load_dotenv(find_dotenv())
MY_OPENAI_KEY = os.getenv('MY_OPENAI_KEY')
openai.api_key = MY_OPENAI_KEY

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

# Configure the GEMINI LLM
genai.configure(api_key=getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

openai_client = OpenAI(
    # This is the default and can be omitted
    api_key=getenv("OPENAI_API_KEY"),
)


# basic generation
def gemini_generate(prompt):
    response = model.generate_content(prompt)
    return response.text


def openai_generate(prompt, model="gpt-3.5-turbo"):

    chat_completion = openai_client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
     response_format={ "type": "json_object" }
     )

    return json.loads(chat_completion.json())["choices"][0]["message"]["content"]
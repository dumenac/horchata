import google.generativeai as genai
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Configure the GEMINI LLM
genai.configure(api_key=getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


# basic generation
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

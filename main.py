from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import generate
from os import getenv
from dotenv import load_dotenv

load_dotenv()

description = """
The Horchata API helps you do awesome stuff. 🚀

It enables you to ask to the Gemini Pro by Google or GPT-3-Turbo by OpenAI and get a JSON response matching the schema you specify in the request body.
"""

app = FastAPI(
    title="🥤 Horchata API",
    description=description,
    summary="Ask LLMs, get JSON in return!",
    version="1.0",
    contact={
        "name": "Domenec Mele",
        "url": "https://mele.dev",
        "email": "domenec@mele.dev",
    },
    license_info={
        "name": "MIT License",
        "identifier": "MIT",
    }
)

app.include_router(generate.router)


@app.get("/", include_in_schema=False)
async def redirect():
    response = RedirectResponse(url=getenv("ROOT_REDIRECT_URL"))
    return response
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import generate
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(generate.router)

@app.get("/")
async def redirect():
    response = RedirectResponse(url=getenv("ROOT_REDIRECT_URL"))
    return response
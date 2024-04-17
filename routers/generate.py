from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional, Any, Dict

from dependencies.json_tools import (
    extract_json,
    validate_json_with_model,
    model_to_json,
    json_to_pydantic,
    json_schema_to_model,
)
from dependencies.gemini_generate import generate_text

router = APIRouter()


class Prompt(BaseModel):
    topic: str
    model: Dict[str, Any]

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "topic": "Magnus Carlsen",
                    "model": {
                        "title": "Player information",
                        "properties": {
                            "first_name": {
                                "type": "string",
                                "description": "First name of the player",
                            },
                            "last_name": {
                                "type": "string",
                                "description": "Last name of the player",
                            },
                            "birthplace_city": {
                                "type": "string",
                                "description": "City where the player was born",
                            },
                            "birthplace_country": {
                                "type": "string",
                                "description": "City where the player was born",
                            },
                            "birthday": {
                                "type": "string",
                                "format": "date",
                                "description": "When the player was born",
                            },
                            "favourite_opening_strategies": {
                                "type": "array",
                                "description": "List of the names of the favourite opening strategies by this player",
                            },
                        },
                    },
                }
            ]
        }
    }


@router.post("/generate", tags=["Generation"])
async def generate(prompt: Prompt) -> dict:
    if prompt.model is None:
        return {"error": "Model definition is required."}

    try:
        pydantic_model_cls = json_schema_to_model(prompt.model)
    except ValueError as e:
        return {"error": "Invalid model definition."}

    json_model_schema = model_to_json(pydantic_model_cls())
    modified_prompt = f"Give me information about {prompt.topic}. Please provide a response in a structured JSON format that matches the following model: {json_model_schema}"

    try:
        gemini_response = generate_text(modified_prompt)
    except Exception as e:
        return {"error": f"Gemini error. {e.message}"}

    json_responses = extract_json(gemini_response)

    if not json_responses:
        return {"error": "No valid JSON found in response."}

    validation_success, validation_errors = validate_json_with_model(
        pydantic_model_cls, json_responses
    )

    if not validation_success:
        return {"Validation errors": validation_errors}

    model_object = json_to_pydantic(pydantic_model_cls, json_responses[0])
    return dict(model_object)

def model_to_json(model_instance):
    """
    Converts a Pydantic model instance to a JSON string.
    Args:
        model_instance (YourModel): An instance of your Pydantic model.
    Returns:
        str: A JSON string representation of the model.
    """
    return model_instance.model_dump_json()
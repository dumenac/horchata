
# 🥤 Horchata API

Welcome to the Horchata API, where you can ask LLMs and get JSON in return! Our API enables you to interact with the Gemini Pro LLM—developed and trained by Google—to receive structured JSON responses that match your specified schema.

## Features

- **LLM to JSON Conversion:** Send queries to Gemini Pro LLM and receive structured JSON.
- **Custom JSON Schemas:** Tailor the JSON response format to meet your specific data needs.
- **Built with FastAPI:** Take advantage of a fast, scalable, and developer-friendly framework.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip

### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/dumenac/horchata.git
cd horchata
```

Install the required packages:
```bash
pip install -r requirements.txt
```
### Running the API

Launch the API server using the following command:

### Running the API

Launch the API server using the following command:

bash

`uvicorn main:app --reload` 

This starts the server on `http://127.0.0.1:8000`, with `--reload` enabling auto-reload for development ease.

## API Endpoints

### `/generate`

-   **Method:** POST
    
-   **Description:** Submit a query and specify your JSON schema to receive structured responses.
    
-   **Request Body:**
    
    json
    

-   `{
      "topic": "Your query topic",
      "model": {
        "Your JSON schema details"
      }
    }` 
    
-   **Success Response:**
    
    json
    
-   `{
      "Your structured JSON response based on the specified schema"
    }` 
    
-   **Error Response:**
    
    json
    

-   `{
      "detail": [
        {
          "loc": ["location of the error"],
          "msg": "error message",
          "type": "error type"
        }
      ]
    }` 
    

## Usage Example

Use `curl` to interact with the API:

bash

`curl -X 'POST' \
  'http://127.0.0.1:8000/generate' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "topic": "Magnus Carlsen",
  "model": {
    "Player information"
  }
}'` 

## Documentation

Visit `http://127.0.0.1:8000/docs` for interactive API documentation using Swagger UI.

## Contributing

Contributions are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](https://api.horchata.io/static/license.md) link for details.

## Contact

Domenec Mele - [Website](https://mele.dev/) - domenec@mele.dev

Project Link: [https://github.com/dumenac/horchata](https://github.com/dumenac/horchata)

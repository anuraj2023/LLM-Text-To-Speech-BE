# FastAPI Text-to-Speech Project

This project is a FastAPI-based service that converts text to speech using a local Language Model (LLM) running in a separate Docker container.

## Features

- FastAPI backend with CORS support
- Integration with a local LLM for text-to-speech conversion

## Prerequisites

- Python 3.9+

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/fastapi-tts-project.git
   cd fastapi-tts-project
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add the following:
   ```
   LLM_SERVICE_URL=http://localhost:8001
   ```
   Adjust the URL if your local LLM service is running on a different port.

## Running the Project Locally

1. Start the FastAPI application:
   ```
   python main.py
   ```
   Or use Uvicorn directly:
   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

2. The API will be available at `http://localhost:8000`

3. Access the API documentation at `http://localhost:8000/docs`

## API Endpoints

- `GET /api/health`: Health check endpoint
- `POST /api/text-to-speech`: Convert text to speech

## Development

- The main application code is in `main.py`
- Update the `requirements.txt` file if you add new dependencies

## Testing

To test the API endpoints:

1. Health Check:
   ```
   curl http://localhost:8000/api/health
   ```

2. Text-to-Speech Conversion:
   ```
   curl -X POST "http://localhost:8000/api/text-to-speech" \
        -H "Content-Type: application/json" \
        -d '{"text":"Hello, this is a test."}'
   ```

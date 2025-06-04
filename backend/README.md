# DontSurf Backend

FastAPI backend for the DontSurf Chrome extension.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

```bash
uvicorn app.main:app --reload
```

The server will start at http://localhost:8000

## API Endpoints

- `GET /ping`: Health check endpoint
- `POST /classify`: Classify page content (coming soon)
- `GET /recommend`: Get book recommendations (coming soon)

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 
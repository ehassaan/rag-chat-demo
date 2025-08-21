# FastAPI Chat Storage Microservice

This project is a FastAPI-based microservice for managing chat sessions and messages, using PostgreSQL, SQLModel, and pgvector. It features API key authentication, user-specific rate limiting (via SlowAPI), centralized logging, Docker support, and production-ready error handling.

## Features

- **Chat Sessions Management**: Create, retrieve, update, and delete chat sessions.
- **Chat Messages Management**: Add and retrieve messages for sessions.
- **API Key Authentication**: Secure endpoints with API key authentication (header: `X-API-Key`).
- **User-Specific Rate Limiting**: Prevent abuse with per-user limits using SlowAPI.
- **Centralized Logging**: Log application events and errors for monitoring.
- **Global Error Handling**: Consistent error responses across the API.
- **Docker Support**: Easily deploy the application using Docker.
- **Vector Storage**: Store and query vector embeddings with pgvector.

## Directory Structure

```
fastapi-chat-storage
├── src
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   └── v1
│   │       ├── chat_sessions.py
│   │       └── chat_messages.py
│   ├── models
│   │   ├── __init__.py
│   │   └── chat.py
│   ├── db
│   │   ├── __init__.py
│   │   ├── session.py
│   │   └── vector.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── logging.py
│   │   ├── errors.py
│   │   ├── auth.py
│   │   └── rate_limit.py
│   ├── middlewares
│   │   ├── __init__.py
│   │   ├── index.py
│   │   └── rate_limit.py
│   ├── schemas
│   │   └── chat.py
│   ├── utils
│   │   └── __init__.py
│   └── types
│       └── index.py
├── tests
│   ├── __init__.py
│   ├── test_chat_sessions.py
│   ├── test_chat_messages.py
│   └── test_auth.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── alembic.ini
├── alembic
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── .env.example
├── .gitignore
├── README.md
└── pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.11 or higher
- PostgreSQL with pgvector extension enabled
- Docker (optional)

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd fastapi-chat-storage
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env
   # Edit .env with your database and API key values
   ```

5. Initialize the database tables:
   ```
   python src/db/init_db.py
   ```

### Running the Application

To run the application locally:
```
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

### Docker

To build and run the entire application using single command:
```
docker-compose up --build
```

## API Authentication

All endpoints require an API key in the header:
```
X-API-Key: your_api_key
```

## Rate Limiting

User-specific rate limits are enforced using SlowAPI. Limits are configured via environment variables or .env file.

## API Documentation

Interactive API docs are available at [http://localhost:8000/docs](http://localhost:8000/docs) after starting the application.

## Testing

To run the tests:
```
pytest
```

# FastAPI Chat Storage Microservice

This project is a FastAPI-based microservice for managing chat sessions and messages, using PostgreSQL, SQLModel, and pgvector. It features API key authentication, user-specific rate limiting (via SlowAPI), centralized logging, Docker support, and production-ready error handling.

## Features

- **Chat Sessions Management**: Create, retrieve, update, and delete chat sessions.
- **Chat Messages Management**: Add and retrieve messages for sessions.
- **API Key Authentication**: Secure endpoints with API key authentication (header: `X-API-Key`).
- **Rate Limiting**: Prevent abuse with global and IP address specific rate limits using SlowAPI.
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
│   ├── dependencies
│   │   ├── auth.py
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

### Create initial database structure

To create initial database structure in an empty database, please run the database migrations,

Linux,
```sh
export PYTHONPATH=.
export DATABASE_URL=<your_db_conn_str>
alembic upgrade head
```
Windows,
```cmd
set PYTHONPATH=.
set DATABASE_URL=<your_db_conn_str>
alembic upgrade head
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

### API Endpoints

Below are the main API endpoints provided by the FastAPI Chat Storage Microservice. Detailed API docs can be found in /docs endpoint.

#### Session Endpoints

- `GET /api/v1/sessions/`
  - List all chat sessions.
- `POST /api/v1/sessions/`
  - Create a new chat session.
- `GET /api/v1/sessions/{session_id}`
  - Retrieve details of a specific chat session.
- `PATCH /api/v1/sessions/{session_id}`
  - Update a chat session (e.g., rename, mark as favorite).
- `DELETE /api/v1/sessions/{session_id}`
  - Delete a chat session.

#### Message Endpoints

- `GET /api/v1/sessions/{session_id}/messages`
  - List messages for a specific chat session (supports pagination).
- `POST /api/v1/sessions/{session_id}/messages`
  - Add a new message to a chat session.
- `DELETE /api/v1/messages/{message_id}`
  - Delete a given message.


#### Other Endpoints

- `GET /healthz`
  - Returns a simple status message to verify the service is running.
- `GET /docs`
  - Endpoint for OpenAPI/Swagger docs.
- `GET /openapi.json`
  - OpenAPI json file for endpoint and schema discovery in API client tools (Postman/Insomnia)

## Testing

To run the tests:
```
pytest
```

## Tech Stack

- **FastAPI**: High-performance Python web framework for building APIs.
- **SQLModel**: ORM and data validation library built on SQLAlchemy and Pydantic.
- **PostgreSQL**: Relational database for persistent storage.
- **SlowAPI**: Rate limiting middleware for FastAPI.
- **Uvicorn**: ASGI server for running FastAPI applications.
- **Alembic**: Library for database migrations and versioning.
- **Docker & Docker Compose**: Containerization and orchestration for development and deployment.

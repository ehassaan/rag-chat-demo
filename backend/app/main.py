from fastapi import FastAPI
from app.api.v1 import chat_sessions, chat_messages
from app.core.logging import setup_logging
from app.core.config import settings
from app.middlewares.index import configure_middlewares
from app.dependencies.auth import ValidateApiKey


app = FastAPI(title="Chat Storage Microservice")

# Logging setup
setup_logging()

# Middleware setup
app = configure_middlewares(app)

# Include API routes
app.include_router(
    chat_sessions.router,
    prefix="/api/v1/sessions",
    tags=["chat_sessions"],
    dependencies=[ValidateApiKey],
)
app.include_router(
    chat_messages.router,
    prefix="/api/v1",
    tags=["chat_messages"],
    dependencies=[ValidateApiKey],
)


@app.get("/healthz")
async def root():
    return {"message": "Working"}

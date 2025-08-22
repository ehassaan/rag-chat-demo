from fastapi import FastAPI
from app.api.v1 import message_controller, rag_controller, session_controller
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
    session_controller.router,
    prefix="/api/v1/sessions",
    tags=["chat_sessions"],
    dependencies=[ValidateApiKey],
)
app.include_router(
    message_controller.router,
    prefix="/api/v1",
    tags=["chat_messages"],
    dependencies=[ValidateApiKey],
)

app.include_router(
    rag_controller.router,
    prefix="/api/v1/rag",
    tags=["rag"],
    dependencies=[ValidateApiKey],
)


@app.get("/healthz")
async def root():
    return {"message": "Working"}

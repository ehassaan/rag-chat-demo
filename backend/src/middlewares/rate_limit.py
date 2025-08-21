import logging
from core.config import settings
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI
from fastapi.responses import JSONResponse


logger = logging.getLogger(__name__)

def rate_limit_exceeded_handler(request, exc: RateLimitExceeded):
    address = get_remote_address(request)
    logger.warning(f"Rate limit exceeded for address: {address} - {exc}")
    response = JSONResponse(
        {"error": f"Rate limit exceeded: {exc.detail}"}, status_code=429
    )
    return response


def configure_rate_limit(app: FastAPI):
    limiter = Limiter(key_func=get_remote_address, default_limits=[settings.rate_limit])
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
    return app

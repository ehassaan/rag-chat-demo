from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from time import time
from collections import defaultdict

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, rate_limit: int = 100, time_window: int = 60):
        super().__init__(app)
        self.rate_limit = rate_limit
        self.time_window = time_window
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time()

        # Clean up old requests
        self.requests[client_ip] = [
            timestamp for timestamp in self.requests[client_ip]
            if current_time - timestamp < self.time_window
        ]

        if len(self.requests[client_ip]) >= self.rate_limit:
            return JSONResponse(
                status_code=HTTPException.status_code,
                content={"detail": "Rate limit exceeded. Try again later."}
            )

        self.requests[client_ip].append(current_time)
        response = await call_next(request)
        return response
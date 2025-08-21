from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from middlewares.rate_limit import configure_rate_limit


def configure_middlewares(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # for production set it to deployed frontend origin        
        allow_credentials=False,
        allow_methods=["GET", "POST", "PUT", "PATCH", "DELETE"],
        allow_headers=["X-API-Key", "Content-Type"],
    )
    app.add_middleware(GZipMiddleware)
    app = configure_rate_limit(app)
    return app

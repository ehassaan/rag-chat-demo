from fastapi import FastAPI
import logging
from logging.config import dictConfig
import os

def setup_logging():
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    dictConfig({
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "()": "logging.Formatter",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "formatter": "default",
                "level": log_level,
            },
        },
        "loggers": {
            "uvicorn": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": True,
            },
            "fastapi": {
                "handlers": ["console"],
                "level": log_level,
                "propagate": True,
            },
            "": {  # root logger
                "handlers": ["console"],
                "level": log_level,
                "propagate": False,
            },
        },
    })

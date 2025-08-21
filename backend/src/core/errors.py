from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

class NotFoundError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_404_NOT_FOUND, detail=detail)

class BadRequestError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, detail=detail)
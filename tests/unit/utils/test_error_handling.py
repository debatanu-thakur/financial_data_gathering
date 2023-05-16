import pytest

from app.utils import AppException, ErrorHandlerFactory


def test_get_error_handler_with_app_exception():
    error = AppException(400, "Bad Request")
    error_handler = ErrorHandlerFactory.get_error_handler(error)
    assert type(error_handler).__name__ == "BadRequestHandler"

def test_get_error_handler_with_error_code():
    error = AppException(404, "Not Found")
    error_handler = ErrorHandlerFactory.get_error_handler(error)
    assert type(error_handler).__name__ == "NotFoundHandler"

def test_get_error_handler_with_internal_server_error_code():
    error = AppException(500, "Internal Error")
    error_handler = ErrorHandlerFactory.get_error_handler(error)
    assert type(error_handler).__name__ == "InternalServerErrorHandler"

def test_get_error_handler_with_unknown_error_code():
    error = AppException(403, "Forbidden")
    error_handler = ErrorHandlerFactory.get_error_handler(error)
    assert type(error_handler).__name__ == "DefaultErrorHandler"

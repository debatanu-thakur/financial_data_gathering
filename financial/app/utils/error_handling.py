from flask.json import jsonify

class ErrorHandlerFactory:
    @staticmethod
    def get_error_handler(error):
        if isinstance(error, AppException):
            error_code = error.error_code
            error_message = error.error_message
        else:
            error_code = 500
            error_message = str(error)
        if error_code == 400:
            return BadRequestHandler(error_code, error_message)
        if error_code == 401:
            return UnauthorizedHandler(error_code, error_message)
        if error_code == 404:
            return NotFoundHandler(error_code, error_message)
        if error_code == 500:
            return InternalServerErrorHandler(error_code, error_message)
        return DefaultErrorHandler(error_code, error_message)

class AppException(Exception):
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message
        super().__init__(f"{error_code}: {error_message}")

class ErrorHandler:
    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message

    def handle_error(self):
        pass

class BadRequestHandler(ErrorHandler):
    def handle_error(self):
        return jsonify({"error": self.error_message}), 400

class UnauthorizedHandler(ErrorHandler):
    def handle_error(self):
        return jsonify({"error": self.error_message}), 401

class NotFoundHandler(ErrorHandler):
    def handle_error(self):
        return jsonify({"error": self.error_message}), 404

class InternalServerErrorHandler(ErrorHandler):
    def handle_error(self):
        return jsonify({"error": self.error_message}), 500

class DefaultErrorHandler(ErrorHandler):
    def handle_error(self):
        return jsonify({"error": self.error_message}), self.error_code

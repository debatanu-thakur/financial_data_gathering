from tenacity import retry, wait_random_exponential, stop_after_attempt, RetryError
import requests
from requests.exceptions import HTTPError

from .constants import (
    WAIT_MULTIPLIER,
    MIN_WAIT_TIME,
    MAX_WAIT_TIME,
    MAX_RETRY_ATTEMPTS,
    API_KEY
)

from .utils import AppException

class RetryableRequests:
    def __init__(self):
        self._api_key = API_KEY

    @retry(
        wait=wait_random_exponential(multiplier=WAIT_MULTIPLIER, min=MIN_WAIT_TIME, max=MAX_WAIT_TIME),
        stop=stop_after_attempt(MAX_RETRY_ATTEMPTS)
    )
    def _get_request(self, url, params):
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response

    def get_request(self, url, params=None):
        """
        GET request with retryable option and error handling
        """
        try:
            if params is None:
                params = {}
            params["apikey"] = self._api_key
            return self._get_request(url, params=params)
        except RetryError as error:
            original_exception = error.last_attempt.exception()
            if isinstance(original_exception, HTTPError):
                http_code, message = self._extract_http_code(str(original_exception))
                raise AppException(http_code, message)
            raise AppException(500, str(original_exception))

    @retry(
        wait=wait_random_exponential(multiplier=WAIT_MULTIPLIER, min=MIN_WAIT_TIME, max=MAX_WAIT_TIME),
        stop=stop_after_attempt(MAX_RETRY_ATTEMPTS)
    )
    def _post_request(self, url, data=None, headers=None, params=None):
        response = requests.post(url, data=data, headers=headers, params=params)
        response.raise_for_status()
        return response

    def post_request(self, url, data=None, headers=None, params=None):
        """
        POST request with retryable option and error handling
        """
        try:
            if params is None:
                params = {}
            if data is None:
                data = {}
            if headers is None:
                headers = {}
            params["apikey"] = self._api_key
            return self._post_request(url, data=data, headers=headers, params=params)
        except RetryError as error:
            original_exception = error.last_attempt.exception()
            if isinstance(original_exception, HTTPError):
                http_code, message = self._extract_http_code(str(original_exception))
                raise AppException(http_code, message)
            raise AppException(500, str(original_exception))

    def _extract_http_code(self, error_message):
        http_code = 500
        message = error_message
        try:
            http_code = int(error_message[0:3]) # Gets the first three entries, which is usually the error code
        except Exception:
            pass
        return http_code, message
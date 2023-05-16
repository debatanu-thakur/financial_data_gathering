import pytest
import requests
from unittest import mock
from requests.exceptions import HTTPError

from app.requests import RetryableRequests
from app.utils import AppException


@pytest.fixture()
def retryable_requests():
    return RetryableRequests()


def test_retryable_requests_get_request_success(retryable_requests):
    with mock.patch.object(requests, 'get') as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        response = retryable_requests.get_request("http://localhost:8000")
        
        assert response == mock_response


def test_retryable_requests_post_request_success(retryable_requests):
    with mock.patch.object(requests, 'post') as mock_post:
        mock_response = mock.MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        response = retryable_requests.post_request("http://localhost:800")
        
        assert response == mock_response


def test_retryable_requests_get_request_retry(retryable_requests):
    with mock.patch.object(requests, 'get') as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = HTTPError
        mock_get.return_value = mock_response
        with pytest.raises(AppException):
            retryable_requests.get_request("http://localhost:8000")
        
        

def test_retryable_requests_post_request_retry(retryable_requests):
    with mock.patch.object(requests, 'post') as mock_post:
        mock_response = mock.MagicMock()
        mock_response.status_code = 500
        mock_response.raise_for_status.side_effect = HTTPError
        mock_post.return_value = mock_response

        with pytest.raises(AppException):
            retryable_requests.post_request("http://localhost:800")

def test_retryable_requests_get_request_http_error(retryable_requests):
    with mock.patch.object(requests, 'get') as mock_get:
        mock_response = mock.MagicMock()
        mock_response.status_code = 400
        mock_response.raise_for_status.side_effect = HTTPError
        mock_get.return_value = mock_response

        with pytest.raises(AppException):
            retryable_requests.get_request("http://localhost:8000")

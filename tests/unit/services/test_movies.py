import pytest

from app.services import MoviesService

from tests.unit import (
    MOVIE_DETAILS,
    MOVIE_RESULTS,
    mock_get_movie_details, 
    mock_get_search_results
)

movieService = MoviesService()

# test successful movies responses

def test_get_details_success(mock_get_movie_details):
    """
    Successful get details call
    """
    query_parameters = {}
    result = movieService.get_details(218, query_parameters)
    assert result == MOVIE_DETAILS

def test_get_search_results_success(mock_get_search_results):
    """
    Successful get search results call
    """
    query_parameters = {"query": "scarface"}
    result = movieService.get_search_results(query_parameters)
    assert result == MOVIE_RESULTS

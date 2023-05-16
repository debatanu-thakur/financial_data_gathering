import pytest

from app.services import Genres

from tests.unit import (
    MOVIE_SAMPLE,
    MOVIE_RESULTS,
    mock_get_genre_details, 
)

genreService = Genres.get_instance()

def test_single_ton_class():
     # should throw error while creating new object since singleton
     with pytest.raises(Exception):
         Genres()

# test successful genre list responses

def test_update_genre_details(mock_get_genre_details):
    """
    Successful update genre list call
    """
    result = genreService.update_genre_details(MOVIE_SAMPLE["results"])
    assert result == MOVIE_RESULTS["results"]


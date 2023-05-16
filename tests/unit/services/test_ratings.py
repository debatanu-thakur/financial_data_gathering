import pytest

from app.services import Ratings

from tests.unit import (
    GUEST_SESSION,
    RATING_RESULT,
    mock_add_rating, 
)

ratingService = Ratings()

# test successful addition of rating

def test_add_rating(mock_add_rating):
    """
    Successful addition of ratings
    """
    rating = {"value": 10}
    result = ratingService.add_rating(218, GUEST_SESSION, rating)
    assert result == RATING_RESULT


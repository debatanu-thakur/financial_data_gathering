import pytest

from app.services import Images

from tests.unit import (
    MOVIE_DETAILS_ABSOLUTE,
    MOVIE_DETAILS,
    mock_get_image_details, 
)

imageService = Images.get_instance()

def test_single_ton_class():
     # should throw error while creating new object since singleton
     with pytest.raises(Exception):
         Images()

# test successful image responses

def test_add_image_absolute_path(mock_get_image_details):
    """
    Successful absolute image path addition
    """
    result = imageService.add_image_absolute_path([MOVIE_DETAILS])
    assert result == [MOVIE_DETAILS_ABSOLUTE]


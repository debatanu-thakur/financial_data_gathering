import pytest

from app.services import GuestSession

from tests.unit import (
    GUEST_SESSION,
    mock_get_new_session, 
)

guestSessionService = GuestSession.get_instance()

def test_singleton_class():
     # should throw error while creating new object since singleton
     with pytest.raises(Exception):
         GuestSession()

# test successful creation of session

def test_get_session(mock_get_new_session):
    """
    Successful update genre list call
    """
    result = guestSessionService.get_session()
    assert result == GUEST_SESSION


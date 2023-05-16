from unittest.mock import patch

import pytest

from app import create_app

app = create_app() # pylint: disable=invalid-name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()

def test_movie_details(client):  # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN the '/v1/movies/<movie_id>/details' endpoint is requested (GET)
    THEN check that the response is valid
    """
    resp = client.get('/v1/movies/218/details')
    assert resp.status_code == 200
    assert resp.json['title'] == 'The Terminator'

def test_search_list(client): # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN the '/v1/movies/search?qeuery=<query>' endpoint is requested (GET)
    THEN check that the response is valid
    """
    resp = client.get("/v1/movies/search?query=scarface")
    assert resp.status_code == 200
    # the total result could change, hence not hardcoding the value and asserting for equal
    assert resp.json["total_results"] > 0
    assert resp.json["total_pages"] > 0

def test_search_list_with_genres(client): # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN the '/v1/movies/search?qeuery=<query>' endpoint is requested (GET)
    THEN check that the response is valid and has genres with names in them
    """
    resp = client.get("/v1/movies/search?query=scarface")
    assert resp.status_code == 200
    # the total result could change, hence not hardcoding the value and asserting for equal
    assert resp.json["total_results"] > 0
    assert resp.json["total_pages"] > 0
    assert all('genres' in result for result in resp.json["results"])
    # check whether genres have name
    results = resp.json['results']
    genres = results[0]['genres']
    assert all('name' in genre for genre in genres)

def test_movie_details(client):  # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN the '/v1/movies/<movie_id>/details' endpoint is requested (GET)
    THEN check that the response is valid and has absolute poster path for image with width 500px
    """
    resp = client.get('/v1/movies/218/details')
    assert resp.status_code == 200
    assert resp.json['title'] == 'The Terminator'
    assert 'poster_image_w500' in resp.json \
            and "http://" in resp.json["poster_image_w500"] \
            and "w500" in resp.json["poster_image_w500"]
    assert "poster_image_w500_secure" in resp.json \
            and "https://" in resp.json["poster_image_w500_secure"] \
            and "w500" in resp.json["poster_image_w500_secure"]

def test_search_list_with_correct_image_path(client): # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN the '/v1/movies/search?qeuery=<query>' endpoint is requested (GET)
    THEN check that the response is valid and has absolute poster path for image with width 500px
    """
    resp = client.get("/v1/movies/search?query=scarface")
    assert resp.status_code == 200
    assert resp.json["total_results"] > 0
    assert resp.json["total_pages"] > 0
    assert all('poster_image_w500' in result for result in resp.json["results"])
    assert all('poster_image_w500_secure' in result for result in resp.json["results"])

# Add integ testing for ratings
def test_add_ratings(client): # pylint: disable=redefined-outer-name
    """
    GIVEN a movie application configured for testing
    WHEN we add rating using '/v1/movies/<movie_id>/rating' endpoint (POST)
    THEN check that the response is valid
    """
    ratings = {"value": "8"}
    resp = client.post("/v1/movies/218/rating", json=ratings)
    assert resp.status_code == 200
    assert resp.json["guest_session_id"] != ""

# Some failure test cases
def test_movie_details_with_negative_movie_id(client):  # pylint: disable=redefined-outer-name
    """
    GIVEN a Flask application configured for testing
    WHEN the '/v1/movies/<movie_id>/details' endpoint is requested (GET), with -ve movie_id schema
    THEN check that the response is invalid
    """

    resp = client.get('/v1/movies/-218/details')
    assert resp.status_code == 404

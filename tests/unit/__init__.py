import pytest
import re
from app.constants import (
    TMDB_V3_SEARCH_MOVIE,
    TMDB_V3_GET_DETAILS,
    TMDB_V3_MOVIE_GENRE_DETAILS,
    TMDB_V3_IMAGE_CONFIG,
    TMDB_V3_CREATE_GUEST_SESSION,
    TMDB_V3
)


MOVIE_DETAILS = {"title": "The Terminator", "poster_path": "/test.jpg"}
MOVIE_DETAILS_ABSOLUTE = {"title": "The Terminator", "poster_path": "/test.jpg", "poster_image_w500": "http://image.tmdb.org/t/p/w500/test.jpg", "poster_image_w500_secure": "https://image.tmdb.org/t/p/w500/test.jpg"}

MOVIE_RESULTS = {
  "page": 1, 
  "results": [
    {
      "adult": False, 
      "backdrop_path": "/s5lFQN26viKOjj0OCSqZioeB0Ln.jpg", 
      "genre_ids": [
        80, 
        27, 
        53
      ], 
      "genres": [
        {
          "id": 80, 
          "name": "Crime"
        }, 
        {
          "id": 27, 
          "name": "Horror"
        }, 
        {
          "id": 53, 
          "name": "Thriller"
        }
      ], 
      "id": 24499, 
      "original_language": "en", 
      "original_title": "Scar", 
      "overview": "Joan Burrows returns to her hometown for her niece's graduation, only to be confronted by the serial killer she thought she offed years ago -- after he kidnapped and tormented her and her best friend.", 
      "popularity": 5.473, 
      "poster_image_w500": "http://image.tmdb.org/t/p/w500/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "poster_image_w500_secure": "https://image.tmdb.org/t/p/w500/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "poster_path": "/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "release_date": "2007-05-19", 
      "title": "Scar", 
      "video": False, 
      "vote_average": 4.657, 
      "vote_count": 54
    }, 
    {
      "adult": False, 
      "backdrop_path": "/g03h9TULzJZOoXA34Abp5LE7lvt.jpg", 
      "genre_ids": [
        16, 
        14, 
        12
      ], 
      "genres": [
        {
          "id": 16, 
          "name": "Animation"
        }, 
        {
          "id": 14, 
          "name": "Fantasy"
        }, 
        {
          "id": 12, 
          "name": "Adventure"
        }
      ], 
      "id": 876792, 
      "original_language": "ja", 
      "original_title": "\u5287\u5834\u7248 \u8ee2\u751f\u3057\u305f\u3089\u30b9\u30e9\u30a4\u30e0\u3060\u3063\u305f\u4ef6 \u7d05\u84ee\u306e\u7d46\u7de8", 
      "overview": "A long-running conspiracy is swirling over a mysterious power wielded by the Queen in Raja, a small country west of Tempest. When a slime who evolved into a Demon Lord named Rimuru Tempest crosses paths with Hiiro, a survivor of the Ogre race, an incredible adventure packed with new characters begins. The power of bonds will be put to the test!", 
      "popularity": 469.563, 
      "poster_image_w500": "http://image.tmdb.org/t/p/w500/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "poster_image_w500_secure": "https://image.tmdb.org/t/p/w500/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "poster_path": "/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "release_date": "2022-11-25", 
      "title": "That Time I Got Reincarnated as a Slime the Movie: Scarlet Bond", 
      "video": False, 
      "vote_average": 7.633, 
      "vote_count": 177
    }
  ]
}
MOVIE_SAMPLE = {
  "page": 1, 
  "results": [
    {
      "adult": False, 
      "backdrop_path": "/s5lFQN26viKOjj0OCSqZioeB0Ln.jpg", 
      "genre_ids": [
        80, 
        27, 
        53
      ], 
      "id": 24499, 
      "original_language": "en", 
      "original_title": "Scar", 
      "overview": "Joan Burrows returns to her hometown for her niece's graduation, only to be confronted by the serial killer she thought she offed years ago -- after he kidnapped and tormented her and her best friend.", 
      "popularity": 5.473, 
      "poster_image_w500": "http://image.tmdb.org/t/p/w500/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "poster_image_w500_secure": "https://image.tmdb.org/t/p/w500/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "poster_path": "/rGriXcu1LouvATDIE5AqUvEcs1W.jpg", 
      "release_date": "2007-05-19", 
      "title": "Scar", 
      "video": False, 
      "vote_average": 4.657, 
      "vote_count": 54
    }, 
    {
      "adult": False, 
      "backdrop_path": "/g03h9TULzJZOoXA34Abp5LE7lvt.jpg", 
      "genre_ids": [
        16, 
        14, 
        12
      ], 
      "id": 876792, 
      "original_language": "ja", 
      "original_title": "\u5287\u5834\u7248 \u8ee2\u751f\u3057\u305f\u3089\u30b9\u30e9\u30a4\u30e0\u3060\u3063\u305f\u4ef6 \u7d05\u84ee\u306e\u7d46\u7de8", 
      "overview": "A long-running conspiracy is swirling over a mysterious power wielded by the Queen in Raja, a small country west of Tempest. When a slime who evolved into a Demon Lord named Rimuru Tempest crosses paths with Hiiro, a survivor of the Ogre race, an incredible adventure packed with new characters begins. The power of bonds will be put to the test!", 
      "popularity": 469.563, 
      "poster_image_w500": "http://image.tmdb.org/t/p/w500/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "poster_image_w500_secure": "https://image.tmdb.org/t/p/w500/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "poster_path": "/xITip9n9uMAUA0TU6niMXU2tbh0.jpg", 
      "release_date": "2022-11-25", 
      "title": "That Time I Got Reincarnated as a Slime the Movie: Scarlet Bond", 
      "video": False, 
      "vote_average": 7.633, 
      "vote_count": 177
    }
  ]
}
TEST_IMAGE_CONFIG = {
  "images": {
    "base_url": "http://image.tmdb.org/t/p/",
    "secure_base_url": "https://image.tmdb.org/t/p/",
    "poster_sizes": [
      "w92",
      "w154",
      "w185",
      "w342",
      "w500",
      "w780",
      "original"
    ]}
}

GENRE_LIST = {
  "genres": [
    {
      "id": 28,
      "name": "Action"
    },
    {
      "id": 12,
      "name": "Adventure"
    },
    {
      "id": 16,
      "name": "Animation"
    },
    {
      "id": 35,
      "name": "Comedy"
    },
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 99,
      "name": "Documentary"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 10751,
      "name": "Family"
    },
    {
      "id": 14,
      "name": "Fantasy"
    },
    {
      "id": 36,
      "name": "History"
    },
    {
      "id": 27,
      "name": "Horror"
    },
    {
      "id": 10402,
      "name": "Music"
    },
    {
      "id": 9648,
      "name": "Mystery"
    },
    {
      "id": 10749,
      "name": "Romance"
    },
    {
      "id": 878,
      "name": "Science Fiction"
    },
    {
      "id": 10770,
      "name": "TV Movie"
    },
    {
      "id": 53,
      "name": "Thriller"
    },
    {
      "id": 10752,
      "name": "War"
    },
    {
      "id": 37,
      "name": "Western"
    }
  ]
}
GUEST_SESSION = {
    'guest_session_id': '12334',
    'expires_at': '2021-01-01 01:01:11 UTC'
}

RATING_RESULT = {
  "expires_at": '2021-01-01 01:01:11 UTC',
  "guest_session_id": '12334',
  "status_code": 1,
  "status_message": "Success.",
  "success": True
}

@pytest.fixture(scope='function')
def mock_get_movie_details(requests_mock):
    pattern = re.compile(r'https://api.themoviedb.org/3/movie/\d+')
    requests_mock.get(pattern, json=MOVIE_DETAILS)
    yield


@pytest.fixture(scope='function')
def mock_get_search_results(requests_mock):
    requests_mock.get(f"{TMDB_V3_SEARCH_MOVIE}", json=MOVIE_RESULTS)
    yield

@pytest.fixture(scope='function')
def mock_get_genre_details(requests_mock):
    requests_mock.get(f"{TMDB_V3_MOVIE_GENRE_DETAILS}", json=GENRE_LIST)
    yield

@pytest.fixture(scope='function')
def mock_get_image_details(requests_mock):
    requests_mock.get(f"{TMDB_V3_IMAGE_CONFIG}", json=TEST_IMAGE_CONFIG)
    yield

@pytest.fixture(scope='function')
def mock_get_new_session(requests_mock):
    requests_mock.get(f"{TMDB_V3_CREATE_GUEST_SESSION}", json=GUEST_SESSION)
    yield

@pytest.fixture(scope='function')
def mock_add_rating(requests_mock):
    pattern = re.compile(r'https://api.themoviedb.org/3/movie/\d+/rating')
    requests_mock.post(pattern, json=RATING_RESULT)
    yield
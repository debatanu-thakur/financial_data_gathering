import pytest
from app.utils import AppException
from app.utils import ValidationMixin

class TestValidationMixin:
    @pytest.fixture()
    def validation_mixin(self):
        return ValidationMixin()
    
    def test_validate_movie_id_valid_id(self, validation_mixin):
        validation_mixin.validate_movie_id(12345)
    
    def test_validate_movie_id_invalid_id(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_movie_id("not an int")
        assert str(exc.value) == "400: Movie Id is a required field and should be an integer"
    
    def test_validate_movie_id_none_id(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_movie_id(None)
        assert str(exc.value) == "400: Movie Id is a required field and should be an integer"
    
    def test_validate_search_query_valid_query(self, validation_mixin):
        validation_mixin.validate_search_query({'query': 'Star Wars'})
    
    def test_validate_search_query_empty_query(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_search_query({'query': ''})
        assert str(exc.value) == "400: Please submit a search query. Search query cannot be empty."
    
    def test_validate_search_query_no_query(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_search_query({'key': 'value'})
        assert str(exc.value) == "400: Please submit a search query. Search query cannot be empty."
    
    def test_validate_ratings_valid_rating(self, validation_mixin):
        validation_mixin.validate_ratings({'value': '7.5'})
    
    def test_validate_ratings_empty_rating(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_ratings({'value': ''})
        assert str(exc.value) == "400: Please submit a rating for the movie."
    
    def test_validate_ratings_no_value(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_ratings({'key': 'value'})
        assert str(exc.value) == "400: Please submit a rating for the movie."
    
    def test_validate_ratings_invalid_rating(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_ratings({'value': 'not a number'})
        assert str(exc.value) == "400: Rating should be between 0.5-10. Please submit a valid rating value."
    
    def test_validate_ratings_out_of_range_rating(self, validation_mixin):
        with pytest.raises(AppException) as exc:
            validation_mixin.validate_ratings({'value': '15.0'})
        assert str(exc.value) == "400: Rating should be between 0.5-10. Please submit a valid rating value."

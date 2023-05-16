import pytest
from app.utils import AppException
from app.utils import ValidationMixin

class TestValidationMixin:
    def test_validate_symbol(self):
        validation_mixin = ValidationMixin()

        # Test valid symbol
        symbol = "AAPL"
        validation_mixin.validate_symbol(symbol)

        # Test invalid symbol
        symbol = None
        with pytest.raises(AppException) as exc_info:
            validation_mixin.validate_symbol(symbol)
        assert exc_info.value.error_code == 400
        assert str(exc_info.value.error_message) == "Symbol is a required field and should be a string"

        symbol = 123
        with pytest.raises(AppException) as exc_info:
            validation_mixin.validate_symbol(symbol)
        assert exc_info.value.error_code == 400
        assert str(exc_info.value.error_message) == "Symbol is a required field and should be a string"

    def test_validate_dates(self):
        validation_mixin = ValidationMixin()

        # Test valid dates
        start_date = "2022-01-01"
        end_date = "2022-01-03"
        validation_mixin.validate_dates(start_date, end_date)

        # Test invalid dates
        start_date = None
        end_date = "2022-01-03"
        with pytest.raises(AppException) as exc_info:
            validation_mixin.validate_dates(start_date, end_date)
        assert exc_info.value.error_code == 400
        assert str(exc_info.value.error_message) == "start_date and end_date is a required field and should be a date string"

        start_date = "2022-01-01"
        end_date = 123
        with pytest.raises(AppException) as exc_info:
            validation_mixin.validate_dates(start_date, end_date)
        assert exc_info.value.error_code == 400
        assert str(exc_info.value.error_message) == "start_date and end_date is a required field and should be a date string"

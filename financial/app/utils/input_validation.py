from .error_handling import AppException

class ValidationMixin:
    def validate_symbol(self, symbol):
        """
        Validate Symbol required field and field type
        """
        if symbol is None or not isinstance(symbol, str):
            raise AppException(400, "Symbol is a required field and should be a string")
    
    def validate_dates(self, start_date, end_date):
        """
        Validate start_date and end_date required field and field type
        """
        if start_date is None or not isinstance(start_date, str):
            raise AppException(400, "start_date and end_date is a required field and should be a date string")
        if end_date is None or not isinstance(end_date, str):
            raise AppException(400, "start_date and end_date is a required field and should be a date string")
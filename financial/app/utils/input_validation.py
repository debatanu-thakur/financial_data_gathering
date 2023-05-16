from .error_handling import AppException

class ValidationMixin:
    def validate_movie_id(self, movie_id):
        """
        Validate movie_id required field and field type
        """
        if movie_id is None or not isinstance(movie_id, int):
            raise AppException(400, "Movie Id is a required field and should be an integer")

    def validate_search_query(self, query_parameters):
        """
        Validate search query for movie search
        """
        if 'query' not in query_parameters or not query_parameters['query']:
            raise AppException(400, "Please submit a search query. Search query cannot be empty.")

    def validate_ratings(self, ratings):
        """
        Validate rating value
        """
        if ratings is None or 'value' not in ratings or not ratings['value']:
            raise AppException(400, "Please submit a rating for the movie.")
        try:
            val = float(ratings['value'])
            if val < 0.5 or val > 10:
                raise AppException(400, "Rating should be between 0.5-10. Please submit a valid rating value.")
        except Exception:
            raise AppException(400, "Rating should be between 0.5-10. Please submit a valid rating value.")

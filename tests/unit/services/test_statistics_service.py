import pytest
from datetime import datetime
from app.models import Financial
from app.services import StatisticService
from unittest.mock import patch

class TestStatisticService:
    @pytest.fixture
    def statistic_service(self):
        return StatisticService()
    

    def test_get_daily_average_results(self, statistic_service):
        start_date = "2022-01-01"
        end_date = "2022-01-03"
        symbol = "ABC"
        # Mock query parameters
        query_parameters = {
            "symbol": symbol,
            "start_date": start_date,
            "end_date": end_date
        }

        # Mock Financial.query.all() response
        with patch("app.services.statistics.Financial") as mock_query:
            mock_query.query = mock_query
            mock_query.filter.return_value = mock_query
            mock_query.filter.return_value.all.return_value = [
                Financial(open_price=10, close_price=15, volume=100, date="2022-01-01", symbol=symbol),
            Financial(open_price=12, close_price=18, volume=150, date="2022-01-02", symbol=symbol),
            Financial(open_price=9, close_price=13, volume=120, date="2022-01-03", symbol=symbol)
            ]
            # Call the method under test
            result = statistic_service.get_daily_average_results(query_parameters)

            # Assertions
            assert "start_date" in result["data"]
            assert "end_date" in result["data"]
            assert "symbol" in result["data"]
            assert "average_daily_open_price" in result["data"]
            assert "average_daily_close_price" in result["data"]
            assert "average_daily_volume" in result["data"]
            assert "info" in result

from unittest.mock import patch

import pytest

from financial.run import create_app

app = create_app() # pylint: disable=invalid-name

@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()

def test_financial_details(client):  # pylint: disable=redefined-outer-name
    """
    GIVEN a financial application configured for testing
    WHEN the '/v1/financials/search' endpoint is requested (GET)
    THEN check that the response is valid
    """
    resp = client.get('/v1/financials/search')
    assert resp.status_code == 200
    assert len(resp.json['data']) > 0
    assert "pagination" in resp.json
    assert "info" in resp.json
    assert resp.json["info"]["error"] == ""


def test_statistic_detail(client): # pylint: disable=redefined-outer-name
    """
    GIVEN a statistic application configured for testing
    WHEN the '/v1/statistics/get' endpoint is requested (GET)
    THEN check that the response is valid
    """
    resp = client.get("/v1/statistics/get?start_date=2023-05-02&end_date=2023-05-15&symbol=AAPL")
    assert resp.status_code == 200
    # the total result could change, hence not hardcoding the value and asserting for equal
    assert float(resp.json["data"]["average_daily_close_price"]) > 0
    assert resp.json["info"]["error"] == ""

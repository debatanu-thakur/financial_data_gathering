import pytest
from datetime import datetime
from app.services import FinancialService
from app.models import Financial
from unittest.mock import patch

INTERMEDIATE_RESULT = [
    Financial("AAPL", "2023-05-02", "170.09", "168.54", 48425696),
    Financial("AAPL", "2023-05-03", "169.09", "167.54", 65136018),
]

@pytest.fixture
def mock_db_query():
    with patch('app.services.financial.Financial') as mock_query:
        yield mock_query

def test_get_search_results_with_symbol(mock_db_query):
    mock_db_query.all.return_value = INTERMEDIATE_RESULT
    # Create an instance of the FinancialService
    financial_service = FinancialService()

    # Define the query parameters for testing
    query_parameters = {
        'symbol': 'AAPL',
        'start_date': datetime(2022, 1, 1),
        'end_date': datetime(2022, 1, 31),
        'limit': 2,
        'page': 1
    }

    
    # Call the get_search_results method
    result = financial_service.get_search_results(query_parameters)

    # Perform assertions on the result
    assert 'data' in result
    assert 'pagination' in result
    assert 'info' in result

    data = result['data']
    pagination = result['pagination']
    info = result['info']

    assert isinstance(data, list)
    assert isinstance(pagination, dict)
    assert isinstance(info, dict)

    assert len(data) <= pagination['limit']
    assert pagination['page'] == query_parameters['page']
    assert pagination['limit'] == query_parameters['limit']


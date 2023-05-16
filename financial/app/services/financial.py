from app.utils import ValidationMixin
from app.models import Financial
from datetime import datetime

class FinancialService(ValidationMixin):

    def _get_result(self, all_data, limit, page):
        res = []
        response = {
            "data": res
        }
        len_data = len(all_data)
        offset = (page - 1) * limit
        for i in range(offset, offset + limit):
            data = all_data[i]
            det = {
                "symbol": data.symbol,
                "date": data.date.strftime("%Y-%m-%d"),
                "open_price": data.open_price,
                "close_price": data.close_price,
                "volume": data.volume
            }
            res.append(det)
        response["pagination"] = {
            "count": len_data,
            "page": page,
            "limit": limit,
            "pages": int(len_data/limit)
        }
        response["info"] = {'error': ''}

        return response

    def get_search_results(self, query_parameters):
        """
        Gets the paginated search results based on input
        """

        symbol, start_date, end_date, limit, page = ("", "", "", 5, 1)
        query = Financial.query
        if 'symbol' in query_parameters:
            symbol = query_parameters["symbol"]
            query = query.filter(Financial.symbol==symbol)
        if 'start_date' in query_parameters:
            start_date = query_parameters["start_date"]
        if 'end_date' in query_parameters:
            end_date = query_parameters["end_date"]
        if 'limit' in query_parameters:
            limit = int(query_parameters['limit'])
        if 'page' in query_parameters:
            page = int(query_parameters['page'])

        if start_date and end_date:
            query = query.filter(Financial.date.between(start_date, end_date))

        response = query.all()
        return self._get_result(response, limit, page)

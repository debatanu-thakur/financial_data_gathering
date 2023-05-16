from app.utils import ValidationMixin
from app.models import Financial
from datetime import datetime
import math

class StatisticService(ValidationMixin):

    def _get_calculated_result(self, all_data, start_date, end_date, symbol):
        res = {
            "start_date": start_date,
            "end_date": end_date,
            "symbol": symbol,
        }
        response = {
            "data": res
        }
        len_data = len(all_data)
        avg_daily_open = 0
        avg_daily_close = 0
        avg_daily_volume = 0
        for data in all_data:
            avg_daily_open += data.open_price
            avg_daily_close += data.close_price
            avg_daily_volume += data.volume
        
        avg_daily_open = avg_daily_open/len_data
        avg_daily_close = avg_daily_close/len_data
        avg_daily_volume = avg_daily_volume/len_data

        res["average_daily_open_price"] = round(avg_daily_open, 2)
        res["average_daily_close_price"] = round(avg_daily_close, 2)
        res["average_daily_volume"] = math.ceil(avg_daily_volume)

        response["info"] = {'error': ''}

        return response

    def get_daily_average_results(self, query_parameters):
        """
        Gets the search results based on input
        """
        symbol, start_date, end_date = ("",datetime.now(),datetime.now())
        query = Financial.query
        if 'symbol' in query_parameters:
            symbol = query_parameters["symbol"]
            query = query.filter(Financial.symbol == symbol)
        if 'start_date' in query_parameters:
            start_date = query_parameters["start_date"]
        if 'end_date' in query_parameters:
            end_date = query_parameters["end_date"]

        self.validate_symbol(symbol)
        self.validate_dates(start_date, end_date)

        if start_date and end_date:
            query = query.filter(Financial.date.between(start_date, end_date))

        response = query.all()
        return self._get_calculated_result(response, start_date, end_date, symbol)

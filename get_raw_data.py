from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from financial.app.requests import RetryableRequests
from model import Financial
from financial.app.constants import (
    ALPHAVANTAGE,
    DATABASE_URI,
    DAILY_DETAILS_KEY,
    METADATA_KEY,
    SYMBOL_KEY,
    OPEN_KEY,
    CLOSE_KEY,
    VOLUME_KEY
)
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

class GatherFinancialData(RetryableRequests):
    def __init__(self):
        super().__init__()
    
    def _get_financials(self, symbol):
        query_params = {
            "symbol": symbol,
            "function": "TIME_SERIES_DAILY_ADJUSTED"
        }
        response = self.get_request(ALPHAVANTAGE, params=query_params)
        json_data = response.json()
        print(f"response is {len(json_data)}")
        return json_data
    
    def _parse_data(self, data, all_dates):
        content = data[DAILY_DETAILS_KEY]
        meta = data[METADATA_KEY]
        symbol = meta[SYMBOL_KEY]
        list_financials = []
        for date in all_dates:
            if date in content:
                res = content[date]
                open_price = res[OPEN_KEY]
                close_price = res[CLOSE_KEY]
                volume = res[VOLUME_KEY]
                list_financials.append({"symbol": symbol, "date": date, "open_price": open_price, "close_price": close_price, "volume": volume})
        return list_financials

    def _get_start_and_end_dates(self):
        all_dates = []
        current_date = datetime.now()
        current_date_formatted = current_date.strftime("%Y-%m-%d")
        all_dates.append(current_date_formatted)
        for i in range(1, 15):
            day = current_date - timedelta(days=i)
            all_dates.append(day.strftime("%Y-%m-%d"))
        return all_dates

    def _insert_data(self, data_set):
        print(f"starting committing of data - {len(data_set)}")
        for data in data_set:
            check_data = session.query(Financial).filter_by(symbol=data["symbol"], date=data["date"]).first()
            if not check_data:
                result = Financial(
                    data["symbol"],
                    data["date"],
                    data["open_price"],
                    data["close_price"],
                    data["volume"]
                )
                session.add(result)
                print(f"added successfully - {result}")
            else:
                print("Data already present, skipping")
        session.commit()
    def get_data_from_financials_api(self, symbols = []):
        res = []
        parsed_data = []
        all_dates = self._get_start_and_end_dates()
        if symbols:
            res = [self._get_financials(symbol) for symbol in symbols]
        if res:
            for data in res:
                parsed_data.extend(self._parse_data(data, all_dates))
        print(f"parsed data - {len(parsed_data)}")
        for i in range(0, len(parsed_data), 2):
            self._insert_data(parsed_data[i:i+2])
        session.close()

res = GatherFinancialData()
run = res.get_data_from_financials_api(["IBM", "AAPL"])

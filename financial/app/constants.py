import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.cfg')
WAIT_MULTIPLIER = config.getfloat("retry_settings", "WAIT_MULTIPLIER")
MIN_WAIT_TIME = config.getfloat("retry_settings", "MIN_WAIT_TIME")
MAX_WAIT_TIME = config.getfloat("retry_settings", "MAX_WAIT_TIME")
MAX_RETRY_ATTEMPTS = config.getint("retry_settings", "MAX_RETRY_ATTEMPTS")
DATABASE_URI = config.get("DATABASE", "DATABASE_URL")

API_KEY = os.getenv('API_KEY', '')
ALPHAVANTAGE = "https://www.alphavantage.co/query"
DAILY_DETAILS_KEY = "Time Series (Daily)"
OPEN_KEY = "1. open"
CLOSE_KEY = "4. close"
VOLUME_KEY = "6. volume"
SYMBOL_KEY = "2. Symbol"
METADATA_KEY = "Meta Data"
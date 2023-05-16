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
LATEST_DATA = {
    "Meta Data": {
        "1. Information": "Daily Time Series with Splits and Dividend Events",
        "2. Symbol": "IBM",
        "3. Last Refreshed": "2023-05-15",
        "4. Output Size": "Compact",
        "5. Time Zone": "US/Eastern"
    },
    "Time Series (Daily)": {
        "2023-05-15": {
            "1. open": "123.0",
            "2. high": "123.6881",
            "3. low": "122.34",
            "4. close": "123.36",
            "5. adjusted close": "123.36",
            "6. volume": "2909922",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-12": {
            "1. open": "121.41",
            "2. high": "122.86",
            "3. low": "121.11",
            "4. close": "122.84",
            "5. adjusted close": "122.84",
            "6. volume": "4564825",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-11": {
            "1. open": "122.02",
            "2. high": "122.24",
            "3. low": "120.55",
            "4. close": "120.9",
            "5. adjusted close": "120.9",
            "6. volume": "3446452",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-10": {
            "1. open": "121.99",
            "2. high": "122.49",
            "3. low": "121.1",
            "4. close": "122.02",
            "5. adjusted close": "122.02",
            "6. volume": "4189222",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-09": {
            "1. open": "121.9",
            "2. high": "121.97",
            "3. low": "120.66",
            "4. close": "121.17",
            "5. adjusted close": "121.17",
            "6. volume": "4540047",
            "7. dividend amount": "1.6600",
            "8. split coefficient": "1.0"
        },
        "2023-05-08": {
            "1. open": "123.76",
            "2. high": "123.92",
            "3. low": "122.55",
            "4. close": "123.4",
            "5. adjusted close": "121.732296670195",
            "6. volume": "3663818",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-05": {
            "1. open": "123.11",
            "2. high": "124.1",
            "3. low": "122.805",
            "4. close": "123.65",
            "5. adjusted close": "121.978918016771",
            "6. volume": "4971936",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-04": {
            "1. open": "123.03",
            "2. high": "123.52",
            "3. low": "121.7563",
            "4. close": "122.57",
            "5. adjusted close": "120.91351379956",
            "6. volume": "4468237",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-03": {
            "1. open": "125.46",
            "2. high": "125.57",
            "3. low": "123.26",
            "4. close": "123.45",
            "5. adjusted close": "121.78162093951",
            "6. volume": "4554212",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-02": {
            "1. open": "126.3",
            "2. high": "126.45",
            "3. low": "123.27",
            "4. close": "125.16",
            "5. adjusted close": "123.468510950094",
            "6. volume": "4445283",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-05-01": {
            "1. open": "126.35",
            "2. high": "126.75",
            "3. low": "126.06",
            "4. close": "126.09",
            "5. adjusted close": "124.385942359358",
            "6. volume": "2724992",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-28": {
            "1. open": "126.58",
            "2. high": "127.25",
            "3. low": "125.64",
            "4. close": "126.41",
            "5. adjusted close": "124.701617682976",
            "6. volume": "5061247",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-27": {
            "1. open": "126.37",
            "2. high": "127.02",
            "3. low": "125.455",
            "4. close": "126.97",
            "5. adjusted close": "125.254049499308",
            "6. volume": "3204889",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-26": {
            "1. open": "125.81",
            "2. high": "126.545",
            "3. low": "125.12",
            "4. close": "125.85",
            "5. adjusted close": "124.149185866645",
            "6. volume": "4058800",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-25": {
            "1. open": "124.9",
            "2. high": "126.19",
            "3. low": "124.76",
            "4. close": "125.89",
            "5. adjusted close": "124.188645282097",
            "6. volume": "4275396",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-24": {
            "1. open": "125.55",
            "2. high": "126.05",
            "3. low": "124.56",
            "4. close": "125.4",
            "5. adjusted close": "123.705267442807",
            "6. volume": "4043892",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-21": {
            "1. open": "126.0",
            "2. high": "126.7",
            "3. low": "125.27",
            "4. close": "125.73",
            "5. adjusted close": "124.030807620288",
            "6. volume": "6725426",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-20": {
            "1. open": "130.15",
            "2. high": "130.98",
            "3. low": "125.84",
            "4. close": "126.36",
            "5. adjusted close": "124.652293413661",
            "6. volume": "9749618",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-19": {
            "1. open": "126.5",
            "2. high": "126.98",
            "3. low": "125.3",
            "4. close": "126.32",
            "5. adjusted close": "124.612833998209",
            "6. volume": "7014368",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-18": {
            "1. open": "128.14",
            "2. high": "128.68",
            "3. low": "127.35",
            "4. close": "127.78",
            "5. adjusted close": "126.053102662216",
            "6. volume": "3193787",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-17": {
            "1. open": "128.3",
            "2. high": "128.72",
            "3. low": "126.8",
            "4. close": "127.82",
            "5. adjusted close": "126.092562077668",
            "6. volume": "3657929",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-14": {
            "1. open": "128.46",
            "2. high": "129.84",
            "3. low": "127.31",
            "4. close": "128.14",
            "5. adjusted close": "126.408237401286",
            "6. volume": "4180614",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-13": {
            "1. open": "128.01",
            "2. high": "128.39",
            "3. low": "126.0",
            "4. close": "127.9",
            "5. adjusted close": "126.171480908573",
            "6. volume": "5621512",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-12": {
            "1. open": "130.4",
            "2. high": "130.8857",
            "3. low": "128.17",
            "4. close": "128.54",
            "5. adjusted close": "126.802831555809",
            "6. volume": "3957542",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-11": {
            "1. open": "130.58",
            "2. high": "131.105",
            "3. low": "130.18",
            "4. close": "130.42",
            "5. adjusted close": "128.657424082065",
            "6. volume": "3132430",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-10": {
            "1. open": "129.83",
            "2. high": "131.08",
            "3. low": "129.24",
            "4. close": "131.03",
            "5. adjusted close": "129.259180167711",
            "6. volume": "2614402",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-06": {
            "1. open": "132.16",
            "2. high": "132.6",
            "3. low": "130.315",
            "4. close": "130.5",
            "5. adjusted close": "128.736342912969",
            "6. volume": "3050581",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-05": {
            "1. open": "131.37",
            "2. high": "132.61",
            "3. low": "131.37",
            "4. close": "132.14",
            "5. adjusted close": "130.354178946511",
            "6. volume": "2898759",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-04": {
            "1. open": "131.99",
            "2. high": "132.1499",
            "3. low": "130.89",
            "4. close": "131.6",
            "5. adjusted close": "129.821476837906",
            "6. volume": "3382783",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-04-03": {
            "1. open": "130.97",
            "2. high": "132.61",
            "3. low": "130.77",
            "4. close": "132.06",
            "5. adjusted close": "130.275260115607",
            "6. volume": "3840139",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-31": {
            "1. open": "129.47",
            "2. high": "131.23",
            "3. low": "129.42",
            "4. close": "131.09",
            "5. adjusted close": "129.31836929089",
            "6. volume": "4524686",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-30": {
            "1. open": "130.16",
            "2. high": "131.48",
            "3. low": "129.1",
            "4. close": "129.22",
            "5. adjusted close": "127.473641618497",
            "6. volume": "3561762",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-29": {
            "1. open": "130.12",
            "2. high": "130.35",
            "3. low": "129.18",
            "4. close": "129.71",
            "5. adjusted close": "127.957019457787",
            "6. volume": "3279846",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-28": {
            "1. open": "129.18",
            "2. high": "129.66",
            "3. low": "128.8",
            "4. close": "129.34",
            "5. adjusted close": "127.592019864854",
            "6. volume": "2889115",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-27": {
            "1. open": "126.47",
            "2. high": "130.255",
            "3. low": "126.47",
            "4. close": "129.31",
            "5. adjusted close": "127.562425303265",
            "6. volume": "6524113",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-24": {
            "1. open": "123.36",
            "2. high": "125.4",
            "3. low": "122.88",
            "4. close": "125.29",
            "5. adjusted close": "123.596754050313",
            "6. volume": "3812644",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-23": {
            "1. open": "123.81",
            "2. high": "124.93",
            "3. low": "122.6",
            "4. close": "123.37",
            "5. adjusted close": "121.702702108605",
            "6. volume": "4651936",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-22": {
            "1. open": "127.0",
            "2. high": "127.215",
            "3. low": "124.01",
            "4. close": "124.05",
            "5. adjusted close": "122.373512171294",
            "6. volume": "3549024",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-21": {
            "1. open": "126.9",
            "2. high": "127.15",
            "3. low": "125.66",
            "4. close": "126.57",
            "5. adjusted close": "124.859455344785",
            "6. volume": "3856345",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-20": {
            "1. open": "124.31",
            "2. high": "126.16",
            "3. low": "124.19",
            "4. close": "125.94",
            "5. adjusted close": "124.237969551413",
            "6. volume": "4588304",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-17": {
            "1. open": "124.08",
            "2. high": "124.52",
            "3. low": "122.93",
            "4. close": "123.69",
            "5. adjusted close": "122.018377432223",
            "6. volume": "37400167",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-16": {
            "1. open": "122.96",
            "2. high": "124.82",
            "3. low": "121.92",
            "4. close": "124.7",
            "5. adjusted close": "123.014727672393",
            "6. volume": "6440023",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-15": {
            "1. open": "122.99",
            "2. high": "123.35",
            "3. low": "121.71",
            "4. close": "123.28",
            "5. adjusted close": "121.613918423838",
            "6. volume": "5989339",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-14": {
            "1. open": "126.49",
            "2. high": "126.64",
            "3. low": "123.2",
            "4. close": "124.65",
            "5. adjusted close": "122.965403403077",
            "6. volume": "8114792",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-13": {
            "1. open": "125.15",
            "2. high": "128.19",
            "3. low": "124.85",
            "4. close": "125.58",
            "5. adjusted close": "123.882834812342",
            "6. volume": "8188369",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-10": {
            "1. open": "126.12",
            "2. high": "127.29",
            "3. low": "125.13",
            "4. close": "125.45",
            "5. adjusted close": "123.754591712122",
            "6. volume": "5990867",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-09": {
            "1. open": "128.3",
            "2. high": "128.53",
            "3. low": "125.98",
            "4. close": "126.16",
            "5. adjusted close": "124.4549963364",
            "6. volume": "5478317",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-08": {
            "1. open": "128.48",
            "2. high": "128.74",
            "3. low": "127.545",
            "4. close": "128.05",
            "5. adjusted close": "126.319453716519",
            "6. volume": "2778798",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-07": {
            "1. open": "130.28",
            "2. high": "130.42",
            "3. low": "128.19",
            "4. close": "128.25",
            "5. adjusted close": "126.51675079378",
            "6. volume": "3530439",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-06": {
            "1. open": "129.64",
            "2. high": "130.86",
            "3. low": "129.59",
            "4. close": "130.19",
            "5. adjusted close": "128.430532443214",
            "6. volume": "2982980",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-03": {
            "1. open": "129.35",
            "2. high": "129.905",
            "3. low": "128.77",
            "4. close": "129.64",
            "5. adjusted close": "127.887965480746",
            "6. volume": "2860286",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-02": {
            "1. open": "128.39",
            "2. high": "129.22",
            "3. low": "127.71",
            "4. close": "128.93",
            "5. adjusted close": "127.187560856468",
            "6. volume": "3340254",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-03-01": {
            "1. open": "128.9",
            "2. high": "129.4726",
            "3. low": "127.74",
            "4. close": "128.19",
            "5. adjusted close": "126.457561670602",
            "6. volume": "3760678",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-28": {
            "1. open": "130.55",
            "2. high": "130.61",
            "3. low": "129.14",
            "4. close": "129.3",
            "5. adjusted close": "127.552560449402",
            "6. volume": "5143133",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-27": {
            "1. open": "131.42",
            "2. high": "131.87",
            "3. low": "130.13",
            "4. close": "130.49",
            "5. adjusted close": "128.726478059106",
            "6. volume": "2761326",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-24": {
            "1. open": "129.62",
            "2. high": "130.67",
            "3. low": "129.22",
            "4. close": "130.57",
            "5. adjusted close": "128.805396890011",
            "6. volume": "3015907",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-23": {
            "1. open": "131.5",
            "2. high": "131.7",
            "3. low": "128.86",
            "4. close": "130.79",
            "5. adjusted close": "129.022423674998",
            "6. volume": "3725648",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-22": {
            "1. open": "131.9",
            "2. high": "131.99",
            "3. low": "130.29",
            "4. close": "130.97",
            "5. adjusted close": "129.199991044533",
            "6. volume": "3200185",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-21": {
            "1. open": "134.0",
            "2. high": "134.385",
            "3. low": "131.66",
            "4. close": "131.71",
            "5. adjusted close": "129.9299902304",
            "6. volume": "4257210",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-17": {
            "1. open": "134.5",
            "2. high": "135.58",
            "3. low": "133.89",
            "4. close": "135.02",
            "5. adjusted close": "133.195256859074",
            "6. volume": "3466184",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-16": {
            "1. open": "135.57",
            "2. high": "135.9672",
            "3. low": "134.59",
            "4. close": "135.0",
            "5. adjusted close": "133.175527151347",
            "6. volume": "2965495",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-15": {
            "1. open": "135.2",
            "2. high": "136.445",
            "3. low": "135.07",
            "4. close": "136.4",
            "5. adjusted close": "134.556606692176",
            "6. volume": "2507004",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-14": {
            "1. open": "137.05",
            "2. high": "137.24",
            "3. low": "135.05",
            "4. close": "136.01",
            "5. adjusted close": "134.171877391517",
            "6. volume": "3202172",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-13": {
            "1. open": "136.0",
            "2. high": "137.39",
            "3. low": "135.85",
            "4. close": "137.35",
            "5. adjusted close": "135.493767809167",
            "6. volume": "4403015",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-10": {
            "1. open": "133.78",
            "2. high": "135.77",
            "3. low": "133.5",
            "4. close": "135.6",
            "5. adjusted close": "133.767418383131",
            "6. volume": "5049571",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-09": {
            "1. open": "134.99",
            "2. high": "135.73",
            "3. low": "133.34",
            "4. close": "133.75",
            "5. adjusted close": "131.942420418465",
            "6. volume": "3918817",
            "7. dividend amount": "1.6500",
            "8. split coefficient": "1.0"
        },
        "2023-02-08": {
            "1. open": "135.71",
            "2. high": "136.74",
            "3. low": "135.16",
            "4. close": "135.98",
            "5. adjusted close": "132.507609516269",
            "6. volume": "4593748",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-07": {
            "1. open": "135.67",
            "2. high": "136.4",
            "3. low": "134.45",
            "4. close": "135.84",
            "5. adjusted close": "132.371184561626",
            "6. volume": "3737553",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-06": {
            "1. open": "135.83",
            "2. high": "136.32",
            "3. low": "134.95",
            "4. close": "136.18",
            "5. adjusted close": "132.702502308615",
            "6. volume": "4841300",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-03": {
            "1. open": "136.35",
            "2. high": "136.95",
            "3. low": "135.53",
            "4. close": "136.94",
            "5. adjusted close": "133.443094919531",
            "6. volume": "3755720",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-02": {
            "1. open": "135.96",
            "2. high": "136.72",
            "3. low": "134.85",
            "4. close": "136.39",
            "5. adjusted close": "132.907139740579",
            "6. volume": "6107793",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-02-01": {
            "1. open": "134.49",
            "2. high": "135.79",
            "3. low": "132.8",
            "4. close": "135.09",
            "5. adjusted close": "131.640336590328",
            "6. volume": "5428898",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-31": {
            "1. open": "135.5",
            "2. high": "135.65",
            "3. low": "133.76",
            "4. close": "134.73",
            "5. adjusted close": "131.289529564104",
            "6. volume": "7206448",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-30": {
            "1. open": "134.32",
            "2. high": "136.11",
            "3. low": "133.98",
            "4. close": "135.3",
            "5. adjusted close": "131.844974022291",
            "6. volume": "5375712",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-27": {
            "1. open": "134.44",
            "2. high": "135.488",
            "3. low": "133.7701",
            "4. close": "134.39",
            "5. adjusted close": "130.958211817116",
            "6. volume": "8143146",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-26": {
            "1. open": "137.53",
            "2. high": "138.27",
            "3. low": "132.98",
            "4. close": "134.45",
            "5. adjusted close": "131.016679654819",
            "6. volume": "17548483",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-25": {
            "1. open": "140.47",
            "2. high": "141.03",
            "3. low": "139.36",
            "4. close": "140.76",
            "5. adjusted close": "137.165547253346",
            "6. volume": "7347453",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-24": {
            "1. open": "141.25",
            "2. high": "142.75",
            "3. low": "140.0",
            "4. close": "141.49",
            "5. adjusted close": "137.87690594541",
            "6. volume": "4407622",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-23": {
            "1. open": "141.4",
            "2. high": "142.985",
            "3. low": "141.06",
            "4. close": "141.86",
            "5. adjusted close": "138.237457611251",
            "6. volume": "5898436",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-20": {
            "1. open": "141.67",
            "2. high": "141.86",
            "3. low": "140.51",
            "4. close": "141.2",
            "5. adjusted close": "137.594311396508",
            "6. volume": "7153341",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-19": {
            "1. open": "140.0",
            "2. high": "142.23",
            "3. low": "139.75",
            "4. close": "140.62",
            "5. adjusted close": "137.029122298704",
            "6. volume": "4833924",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-18": {
            "1. open": "144.4",
            "2. high": "144.678",
            "3. low": "140.225",
            "4. close": "140.41",
            "5. adjusted close": "136.82448486674",
            "6. volume": "6445642",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-17": {
            "1. open": "146.42",
            "2. high": "147.18",
            "3. low": "145.01",
            "4. close": "145.19",
            "5. adjusted close": "141.482422603817",
            "6. volume": "2986461",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-13": {
            "1. open": "144.06",
            "2. high": "146.1",
            "3. low": "144.01",
            "4. close": "145.89",
            "5. adjusted close": "142.164547377029",
            "6. volume": "2455786",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-12": {
            "1. open": "144.88",
            "2. high": "146.66",
            "3. low": "144.52",
            "4. close": "145.55",
            "5. adjusted close": "141.833229630041",
            "6. volume": "2716118",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-11": {
            "1. open": "145.0",
            "2. high": "145.53",
            "3. low": "143.45",
            "4. close": "145.26",
            "5. adjusted close": "141.550635081139",
            "6. volume": "3268738",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-10": {
            "1. open": "143.61",
            "2. high": "144.85",
            "3. low": "142.9",
            "4. close": "144.8",
            "5. adjusted close": "141.102381658742",
            "6. volume": "2152172",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-09": {
            "1. open": "144.08",
            "2. high": "145.47",
            "3. low": "143.4",
            "4. close": "143.55",
            "5. adjusted close": "139.884301706577",
            "6. volume": "3987782",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-06": {
            "1. open": "142.38",
            "2. high": "144.25",
            "3. low": "141.58",
            "4. close": "143.7",
            "5. adjusted close": "140.030471300837",
            "6. volume": "3574042",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-05": {
            "1. open": "142.44",
            "2. high": "142.498",
            "3. low": "140.01",
            "4. close": "141.11",
            "5. adjusted close": "137.506609639952",
            "6. volume": "2866648",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-04": {
            "1. open": "142.07",
            "2. high": "143.615",
            "3. low": "141.3675",
            "4. close": "142.6",
            "5. adjusted close": "138.958560942932",
            "6. volume": "3869236",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2023-01-03": {
            "1. open": "141.1",
            "2. high": "141.9",
            "3. low": "140.48",
            "4. close": "141.55",
            "5. adjusted close": "137.935373783114",
            "6. volume": "3338829",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-30": {
            "1. open": "140.54",
            "2. high": "140.9",
            "3. low": "139.45",
            "4. close": "140.89",
            "5. adjusted close": "137.292227568371",
            "6. volume": "2858110",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-29": {
            "1. open": "140.58",
            "2. high": "142.26",
            "3. low": "140.45",
            "4. close": "141.06",
            "5. adjusted close": "137.457886441866",
            "6. volume": "2337207",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-28": {
            "1. open": "142.4",
            "2. high": "142.81",
            "3. low": "139.95",
            "4. close": "140.02",
            "5. adjusted close": "136.444443921665",
            "6. volume": "2539577",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-27": {
            "1. open": "141.73",
            "2. high": "142.72",
            "3. low": "141.23",
            "4. close": "142.42",
            "5. adjusted close": "138.783157429821",
            "6. volume": "2742525",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-23": {
            "1. open": "140.59",
            "2. high": "141.8565",
            "3. low": "139.6",
            "4. close": "141.65",
            "5. adjusted close": "138.032820179287",
            "6. volume": "2092715",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-22": {
            "1. open": "140.95",
            "2. high": "141.44",
            "3. low": "138.62",
            "4. close": "140.88",
            "5. adjusted close": "137.282482928754",
            "6. volume": "3337851",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-21": {
            "1. open": "141.84",
            "2. high": "143.09",
            "3. low": "140.975",
            "4. close": "142.14",
            "5. adjusted close": "138.510307520536",
            "6. volume": "3793700",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        },
        "2022-12-20": {
            "1. open": "138.84",
            "2. high": "141.425",
            "3. low": "138.34",
            "4. close": "141.28",
            "5. adjusted close": "137.672268513447",
            "6. volume": "5156450",
            "7. dividend amount": "0.0000",
            "8. split coefficient": "1.0"
        }
    }
}

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
        # json_data = LATEST_DATA
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

        session.commit()
        print(f"committed successfully")
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

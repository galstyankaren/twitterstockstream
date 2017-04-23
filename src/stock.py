from rtstock.stock import Stock
from rtstock.utils import request_historical
import json
import datetime

def getStockInfoVerbose(ticker):
    """Return verbose result of the ticker"""
    stock = Stock(ticker)
    # datadump=json.dumps(stock.get_info())
    return stock.get_info()

""" Verbose content
[
  {
    "Ask": "143.64",
    "AverageDailyVolume": "27163800",
    "Bid": "143.60",
    "BookValue": "25.19",
    "Change": "-0.27",
    "ChangeFromFiftydayMovingAverage": "6.49",
    "ChangeFromTwoHundreddayMovingAverage": "23.46",
    "ChangeFromYearHigh": "-0.61",
    "ChangeFromYearLow": "54.19",
    "Change_PercentChange": "-0.27 - -0.19%",
    "ChangeinPercent": "-0.19%",
    "Currency": "USD",
    "DaysHigh": "144.27",
    "DaysLow": "143.01",
    "DaysRange": "143.01 - 144.27",
    "DividendPayDate": "2/16/2017",
    "DividendShare": "2.28",
    "DividendYield": "1.58",
    "EBITDA": "69.75B",
    "EPSEstimateCurrentYear": "8.94",
    "EPSEstimateNextQuarter": "1.62",
    "EPSEstimateNextYear": "10.19",
    "EarningsShare": "8.33",
    "ExDividendDate": "2/9/2017",
    "FiftydayMovingAverage": "137.18",
    "LastTradeDate": "3/31/2017",
    "LastTradePriceOnly": "143.66",
    "LastTradeTime": "4:00pm",
    "LastTradeWithTime": "4:00pm - <b>143.66</b>",
    "MarketCapitalization": "753.72B",
    "Name": "Apple Inc.",
    "OneyrTargetPrice": "146.76",
    "Open": "143.72",
    "PEGRatio": "1.74",
    "PERatio": "17.25",
    "PercebtChangeFromYearHigh": "-0.42%",
    "PercentChange": "-0.19%",
    "PercentChangeFromFiftydayMovingAverage": "+4.73%",
    "PercentChangeFromTwoHundreddayMovingAverage": "+19.52%",
    "PercentChangeFromYearLow": "+60.57%",
    "PreviousClose": "143.93",
    "PriceBook": "5.71",
    "PriceEPSEstimateCurrentYear": "16.05",
    "PriceEPSEstimateNextYear": "14.07",
    "PriceSales": "3.46",
    "ShortRatio": "2.33",
    "StockExchange": "NMS",
    "Symbol": "AAPL",
    "TwoHundreddayMovingAverage": "120.20",
    "Volume": "19661651",
    "YearHigh": "144.27",
    "YearLow": "89.47",
    "YearRange": "89.47 - 144.27"
  }
]
"""

def getLatestPrice(ticker):
    """Return latest price result of the ticker"""
    stock = Stock(ticker)
    # datadump=json.dumps(stock.get_info())
    return stock.get_latest_price()


def getHistoricalPrices(ticker, startDate, endDate):
    """Return Historical Prices for the specified ticker"""
    try:
        print(ticker)
        return request_historical(ticker, startDate, endDate)
    except:
        return 0


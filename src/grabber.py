import tweepy
import json
import time

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from rtstock.stock import Stock
from rtstock.utils import request_historical


CONSUMER_KEY = "YqAo5ZRvG1QpPkcGG6rJ0JqwU"
CONSUMER_SECRET = "AiM11Y5qhg6zsnbrMepUqxe7ejWuwm6NYdck2nOLlzXYcR6yJC"
ACCESS_TOKEN = "781620753456308224-3pGPA8366kQLCwsnpm46clwaebrszWV"
ACCESS_SECRET = "fBNJ3ayrwgq3xkPJuvOKrEL1gLwg71jF1bD8H7beXuwnN"


COMPANY = ""
TICKER = ""
"""Stock Grabber"""


class Data(object):
    def __init__(_self, _tweet, _ticker, _date, _open, _close, _high, _low):
        self.ticker = _ticker
        self.tweet = _tweet
        self.date = _date
        self.open = _open
        self.close = _close
        self.high = _high
        self.low = _low


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
    return request_historical(ticker, startDate, endDate)

"""Twitter Grabber"""

""" Status content

['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__',
  '__hash__', '__init__', '__le__', '__lt__', '__module__', '__ne__',
  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api',
   '_json', 'author', 'contributors', 'coordinates', 'created_at', 'destroy',
   'entities', 'favorite', 'favorite_count', 'favorited', 'filter_level',
    'geo', 'id', 'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id',
    'in_reply_to_status_id_str', 'in_reply_to_user_id', 'in_reply_to_user_id_str',
     'is_quote_status', 'lang', 'parse', 'parse_list', 'place', 'possibly_sensitive',
      'retweet', 'retweet_count', 'retweeted', 'retweets', 'source', 'source_url',
      'text', 'timestamp_ms', 'truncated', 'user']

"""
""" Date format (created_at)
2017-04-02 15:10:36
"""


def jdefault(o):
    return o.__dict__


class GrabberStreamListener(tweepy.StreamListener):
    """overrides tweepy.StreamListener to add logic to on_status and on_error"""

    def on_status(self, status):
        stockdata = getStockInfoVerbose(TICKER)
        with open('data.json', 'w') as outfile:
            jsonData = Data(status.text,TICKER,status.created_at,stockdata.Open,stockdata.Close,stockdata.High,stockdata.Low)
            temp=json.dumps(jsonData, outfile, default=jdefault, ensure_ascii=False)
            print(temp)

    def on_error(self, status_code):
        if status_code == 420:
            # returning False in on_data disconnects the stream
            return False


def limit_handler(cursor):
    """Handling Twitter API request Limits"""
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def Authenticate():
    """OAuth for Twitter API"""
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # TODO fix JSON parser error
    api = tweepy.API(auth)  # ,parser=tweepy.parsers.JSONParser())
    return api


def QueryProfile(api, QUERY_PROFILE, limit):
    """Query a profile with provided profile id, returning tweets to a limit of pages"""
    user = api.user_timeline(QUERY_PROFILE)
    tweets = []
    for tweet in limit_handler(tweepy.Cursor(api.user_timeline, id=QUERY_PROFILE).pages(limit)):
        tweets.append(tweet)
        print(type(tweet))
    return tweets


def StartStream(api,company,ticker):
	"""Query Twitter with a specific filter"""
	COMPANY=company
	TICKER=ticker
	StreamListener = GrabberStreamListener()
	stream = tweepy.Stream(auth=api.auth, listener=GrabberStreamListener())
	#TODO make async
	stream.filter(track=[COMPANY,TICKER])
	return stream

import sys, os, json, datetime
import tweepy
import stock
import utils
import praw
import time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

CONSUMER_KEY = "YqAo5ZRvG1QpPkcGG6rJ0JqwU"
CONSUMER_SECRET = "AiM11Y5qhg6zsnbrMepUqxe7ejWuwm6NYdck2nOLlzXYcR6yJC"
ACCESS_TOKEN = "781620753456308224-3pGPA8366kQLCwsnpm46clwaebrszWV"
ACCESS_SECRET = "fBNJ3ayrwgq3xkPJuvOKrEL1gLwg71jF1bD8H7beXuwnN"


"""Stock Grabber"""
#Full Ticker list
companies_ticker = {"JPMorgan":"JPM", "AIG":"AIG", "HSBC":"HBC", "INTEL":"INTC", "Agilent": "A", "Alcoa ": "AA", "Apple": "AAPL", "AmerisourceBergen ": "ABC", "Abbott Laboratories": "ABT", "ACE Limited": "ACE", "Accenture": "ACN", "Adobe Systems ": "ADBE", "Adobe": "ADBE", "Analog Devices ": "ADI", "Archer-Daniels-Midland": "ADM", "Automatic Data Processing": "ADP", "ADP": "ADP", "Autodesk ": "ADSK", "ADT ": "ADT", "Ameren ": "AEE", "American Electric Power": "AEP", "AES ": "AES", "Aetna ": "AET", "AFLAC ": "AFL", "Allergan ": "AGN", "American Intl Group ": "AIG", "Apartment Investment & Mgmt": "AIV", "Apartment Investment": "AIV", "Assurant ": "AIZ", "Akamai Technologies ": "AKAM", "Akamai": "AKAM", "Allstate ": "ALL", "Altera ": "ALTR", "Alexion Pharmaceuticals": "ALXN", "Alexion": "ALXN", "Applied Materials ": "AMAT", "Advanced Micro Devices": "AMD", "AMD": "AMD", "Amgen ": "AMGN", "Ameriprise Financial": "AMP", "American Tower": "AMT", "Amazoncom ": "AMZN", "Amazon": "AMZN", "AutoNation ": "AN", "Abercrombie & Fitch Company": "ANF", "Abercrombie": "ANF", "Aon plc": "AON", "Apache": "APA", "Anadarko Petroleum ": "APC", "Air Products & Chemicals ": "APD", "Amphenol": "APH", "Apollo Group ": "APOL", "Airgas ": "ARG", "Allegheny Technologies ": "ATI", "AvalonBay Communities, ": "AVB", "Avon Products": "AVP", "Avon": "AVP", "Avery Dennison ": "AVY", "American Express Co": "AXP", "American Express": "AXP", "Amex": "AXP", "AutoZone ": "AZO", "Boeing Company": "BA", "Bank of America ": "BAC", "BofA": "BAC", "Baxter International ": "BAX", "Bed Bath & Beyond": "BBBY", "BB&T ": "BBT", "Best Buy": "BBY", "Bard": "BCR", "Becton Dickinson": "BDX", "Beam ": "BEAM", "Franklin Resources": "BEN", "Brown-Forman ": "BF.B", "Baker Hughes ": "BHI", "Big Lots ": "BIG", "BIOGEN IDEC ": "BIIB", "The Bank of New York Mellon ": "BK", "BlackRock": "BLK", "Ball ": "BLL", "BMC Software": "BMC", "Bemis Company": "BMS", "Bristol-Myers Squibb": "BMY", "Broadcom ": "BRCM", "Berkshire Hathaway": "BRK.B", "Berkshire": "BRK.B", "Boston Scientific": "BSX", "Peabody Energy": "BTU", "BorgWarner": "BWA", "Boston Properties": "BXP", "Citigroup ": "C", " CA ": "CA", "ConAgra Foods ": "CAG", "ConAgra": "CAG", "Cardinal Health ": "CAH", "Cameron International ": "CAM", "Caterpillar ": "CAT", "Chubb ": "CB", "CBRE Group": "CBG", "CBS ": "CBS", "Coca-Cola": "CCE", "Coke": "CCE", "Crown Castle": "CCI", "Carnival ": "CCL", "Celgene ": "CELG", "Cerner": "CERN", "CF Industries Holdings ": "CF", "Carefusion": "CFN", "Chesapeake Energy": "CHK", "C H Robinson Worldwide": "CHRW", "CIGNA ": "CI", "Cinnati Financial": "CINF", "Colgate-Palmolive": "CL", "Cliffs Natural Resources": "CLF", "The Clorox Company": "CLX", "Comerica ": "CMA", "Comcast ": "CMCSA", "CME Group ": "CME", "Chipotle": "CMG", "Cummins ": "CMI", "CMS Energy": "CMS", "CenterPoint Energy": "CNP", "CONSOL Energy ": "CNX", "Capital One Financial": "COF", "CapitalOne": "COF", "Capital One": "COF", "Cabot Oil & Gas": "COG", "Coach ": "COH", "Rockwell Collins": "COL", "ConocoPhillips": "COP", "Costco": "COST", "Covidien": "COV", "Campbell Soup": "CPB", "Campbell's": "CPB", "Salesforce.com": "CRM", "Salesforce": "CRM", "Computer Sciences ": "CSC", "Cisco": "CSCO", "Cisco Systems": "CSCO", "CSX ": "CSX", "Cintas ": "CTAS", "CenturyLink ": "CTL", "Cognizant Technology Solutions": "CTSH", "Citrix Systems": "CTXS", "Cablevision Systems ": "CVC", "Coventry Health Care ": "CVH", "CVS Caremark ": "CVS", "Chevron ": "CVX", "Dominion Resources": "D", "Du Pont": "DD", "Deere & Co": "DE", "Dell ": "DELL", "Dean Foods": "DF", "Discover Financial Services": "DFS", "Dollar General": "DG", "Quest Diagnostics": "DGX", "D R Horton": "DHI", "Danaher ": "DHR", "Walt Disney": "DIS", "Disney": "DIS", "Discovery Communications": "DISCA", "Dollar Tree": "DLTR", "Dun & Bradstreet": "DNB", "Denbury Resources ": "DNR", "Diamond Offshore Drilling": "DO", "Dover ": "DOV", "Dow Chemical": "DOW", "Dow ": "DOW", "Dr Pepper Snapple Group": "DPS", "Darden Restaurants": "DRI", "DTE Energy Co": "DTE", "DirecTV": "DTV", "Duke Energy": "DUK", "DaVita ": "DVA", "Devon Energy ": "DVN", "Electronic Arts": "EA", " EA ": "EA", "eBay ": "EBAY", "Ecolab ": "ECL", "Consolidated Edison": "ED", "Equifax ": "EFX", "Edison Int'l": "EIX", "Estee Lauder": "EL", "EMC ": "EMC", "Eastman Chemical": "EMN", "Emerson Electric": "EMR", "EOG Resources": "EOG", "Equity Residential": "EQR", "EQT ": "EQT", "Express Scripts": "ESRX", "Ensco plc": "ESV", "E-Trade": "ETFC", "Eaton ": "ETN", "Entergy ": "ETR", "Edwards Lifesciences": "EW", "Exelon ": "EXC", "Expeditors": "EXPD", "Expedia ": "EXPE", "Ford Motor": "F", "Fastenal": "FAST", "Freeport-McMoran Cp & Gld": "FCX", "Family Dollar Stores": "FDO", "FedEx ": "FDX", "FirstEnergy ": "FE", "F5 Networks": "FFIV", "First Horizon National": "FHN", "Federated Investors ": "FII", "Fidelity National Information Services": "FIS", "Fiserv ": "FISV", "Fifth Third Ban": "FITB", "FLIR Systems": "FLIR", "Fluor ": "FLR", "Flowserve ": "FLS", "FMC ": "FMC", "Fossil": "FOSL", "Forest Laboratories": "FRX", "First Solar ": "FSLR", "FMC Technologies ": "FTI", "Frontier Communications": "FTR", "Frontier": "FTR", "AGL Resources ": "GAS", "Gannett": "GCI", "General Dynamics": "GD", "General Electric": "GE", "Gilead Sciences": "GILD", "General Mills": "GIS", "Corning ": "GLW", "GameStop ": "GME", "Genworth Financial ": "GNW", "Google ": "GOOG", "Genuine Parts": "GPC", "Gap (The)": "GPS", "The Gap": "GPS", "Goldman Sachs Group": "GS", "Goldman Sachs": "GS", "Goodyear Tire & Rubber": "GT", "Goodyear": "GT", "Grainger (WW) ": "GWW", "Halliburton": "HAL", "Harman Int'l Industries": "HAR", "Hasbro ": "HAS", "Huntington Bancshares": "HBAN", "Hudson City Ban": "HCBK", "Health Care REIT": "HCN", "HCP ": "HCP", "Home Depot": "HD", "Hess ": "HES", "Hartford Financial SvcGp": "HIG", "Heinz": "HNZ", "Harley-Davidson": "HOG", "Honeywell": "HON", "Starwood Hotels & Resorts": "HOT", "Starwood": "HOT", "Helmerich & Payne": "HP", "Hewlett-Packard": "HPQ", "Block H&R": "HRB", "Hormel Foods ": "HRL", "Harris ": "HRS", "Hospira ": "HSP", "Host Hotels & Resorts": "HST", "The Hershey Company": "HSY", "Hershey": "HSY", "Humana ": "HUM", "International Bus Machines": "IBM", "IntercontinentalExchange ": "ICE", "International Flav/Frag": "IFF", "International Game Technology": "IGT", "Intel ": "INTC", "Intuit ": "INTU", "International Paper": "IP", "Interpublic Group": "IPG", "Ingersoll-Rand PLC": "IR", "Iron Mountain orporated": "IRM", "Intuitive Surgical ": "ISRG", "Illinois Tool Works": "ITW", "Invesco Ltd": "IVZ", "Jabil Circuit": "JBL", "Johnson Controls": "JCI", "Penney (JC)": "JCP", "JC Penney": "JCP", "JDS Uniphase ": "JDSU", "Jacobs Engineering Group": "JEC", "Johnson & Johnson": "JNJ", "J&J": "JNJ", "Juniper Networks": "JNPR", "Joy Global ": "JOY", "JPMorgan Chase & Co": "JPM", "JPMorgan Chase": "JPM", "JPMorgan": "JPM", "Nordstrom": "JWN", "Kellogg Co": "K", "Kimco Realty": "KIM", "KLA-Tencor ": "KLAC", "Kimberly-Clark": "KMB", "Kinder Morgan": "KMI", "Carmax ": "KMX", "Coca Cola": "KO", "Kroger Co": "KR", "Kraft Foods Group": "KRFT", "Kraft": "KRFT", "Kohl's ": "KSS", "Loews ": "L", "Leggett & Platt": "LEG", "Lennar ": "LEN", "Laboratory  of America Holding": "LH", "Life Technologies": "LIFE", "L-3 Communications": "LLL", "Linear Technology ": "LLTC", "Lilly (Eli) & Co": "LLY", "Eli Lilly": "LLY", "Legg Mason": "LM", "Lockheed Martin ": "LMT", "Loln National": "LNC", "Lorillard ": "LO", "Lowe's": "LOW", "Lam Research": "LRCX", "LSI ": "LSI", "Limited Brands ": "LTD", "Leucadia National ": "LUK", "Southwest Airlines": "LUV", "LyondellBasell": "LYB", "Macy's ": "M", "Mastercard ": "MA", "Marriott": "MAR", "Masco ": "MAS", "Mattel ": "MAT", "McDonald's ": "MCD", "Microchip Technology": "MCHP", "McKesson ": "MCK", "Moody's ": "MCO", "Mondelez International": "MDLZ", "Medtronic ": "MDT", "MetLife ": "MET", "McGraw-Hill": "MHP", "Mead Johnson": "MJN", "McCormick & Co": "MKC", "Marsh & McLennan": "MMC", "3M": "MMM", "Monster Beverage": "MNST", "Altria Group ": "MO", "Molex ": "MOLX", "Monsanto": "MON", "The Mosaic Company": "MOS", "Marathon Petroleum": "MPC", "Merck & Co": "MRK", "Marathon Oil ": "MRO", "Morgan Stanley": "MS", "Microsoft ": "MSFT", "Motorola Solutions ": "MSI", "M&T Bank ": "MTB", "Micron Technology": "MU", "Murphy Oil": "MUR", "MeadWestvaco ": "MWV", "Mylan ": "MYL", "Noble Energy ": "NBL", "Nabors Industries Ltd": "NBR", "NASDAQ OMX Group": "NDAQ", "Noble ": "NE", "NextEra Energy Resources": "NEE", "Newmont Mining  (Hldg Co)": "NEM", "NetFlix ": "NFLX", "Newfield": "NFX", "NiSource ": "NI", "NIKE ": "NKE", "Northrop Grumman ": "NOC", "National Oilwell Varco ": "NOV", "NRG Energy": "NRG", "Norfolk Southern ": "NSC", "NetApp": "NTAP", "Northern Trust ": "NTRS", "Northeast Utilities": "NU", "Nucor ": "NUE", "Nvidia ": "NVDA", "Newell Rubbermaid": "NWL", "NYSE Euronext": "NYX", "Owens-Illinois ": "OI", "ONEOK": "OKE", "Omnicom Group": "OMC", "Oracle ": "ORCL", "O'Reilly Automotive": "ORLY", "Occidental Petroleum": "OXY", "Paychex ": "PAYX", "People's United Bank": "PBCT", "Pitney-Bowes": "PBI", "PACCAR ": "PCAR", "PG&E ": "PCG", "Plum Creek Timber": "PCL", "Priceline.com ": "PCLN", "Precision Castparts": "PCP", "MetroPCS Communications ": "PCS", "Patterson Companies": "PDCO", "Public Serv Enterprise ": "PEG", "PepsiCo ": "PEP", "Pet Smart": "PETM", "Pfizer ": "PFE", "Pripal Financial Group": "PFG", "Procter & Gamble": "PG", "Progressive ": "PGR", "Parker-Hannifin": "PH", "Pulte Homes ": "PHM", "PerkinElmer": "PKI", "ProLogis": "PLD", "Pall ": "PLL", "Philip Morris": "PM", "PNC Financial Services": "PNC", "Pentair": "PNR", "Pinnacle West Capital": "PNW", "Pepco ": "POM", "PPG ": "PPG", "PPL ": "PPL", "Perrigo": "PRGO", "Prudential Financial": "PRU", "Public Storage": "PSA", "Phillips 66": "PSX", "Quanta Services ": "PWR", "Praxair ": "PX", "Pioneer Natural Resources": "PXD", "QUALCOMM ": "QCOM", "QEP Resources": "QEP", "Ryder System": "R", "Reynolds American ": "RAI", "Rowan": "RDC", "Regions": "RF", "Robert Half": "RHI", "Red Hat ": "RHT", "Polo Ralph Lauren ": "RL", "Rockwell Automation ": "ROK", "Roper Industries": "ROP", "Ross Stores ": "ROST", "Range Resources ": "RRC", "RR Donnelley & Sons": "RRD", "Republic Services ": "RSG", "Raytheon": "RTN", "Sprint Nextel ": "S", "SAIC": "SAI", "Starbucks ": "SBUX", "SCANA ": "SCG", "Charles Schwab": "SCHW", "Spectra Energy ": "SE", "New Sealed Air": "SEE", "Sherwin-Williams": "SHW", "Sigma-Aldrich": "SIAL", "Smucker (JM)": "SJM", "Schlumberger": "SLB", "SLM ": "SLM", "Snap-On ": "SNA", "SanDisk ": "SNDK", "Scripps Networks Interactive ": "SNI", "Simon Property Group ": "SPG", "Staples ": "SPLS", "Stericycle ": "SRCL", "Sempra Energy": "SRE", "SunTrust Banks": "STI", "St Jude Medical": "STJ", "State Street ": "STT", "Seagate Technology": "STX", "Constellation Brands": "STZ", "Stanley Black & Decker": "SWK", "Southwestern Energy": "SWN", "Safeway ": "SWY", "Stryker ": "SYK", "Symantec ": "SYMC", "Sysco ": "SYY", "AT&T ": "T", "Molson Coors Brewing Company": "TAP", "Teradata ": "TDC", "TECO Energy": "TE", "Integrys Energy Group ": "TEG", "TE Connectivity Ltd": "TEL", "Teradyne ": "TER", "Target ": "TGT", "Tenet Healthcare ": "THC", "Titanium Metals ": "TIE", "Tiffany": "TIF", "TJX Companies ": "TJX", "Torchmark ": "TMK", "Thermo Fisher Scientific": "TMO", "TripAdvisor": "TRIP", "T Rowe Price Group": "TROW", "The Travelers Companies ": "TRV", "Tyson Foods": "TSN", "Tesoro Petroleum Co": "TSO", "Total System Services": "TSS", "Time Warner Cable ": "TWC", "Time Warner ": "TWX", "Texas Instruments": "TXN", "Textron ": "TXT", "Tyco International": "TYC", "United Health Group ": "UNH", "Unum Group": "UNM", "Union Pacific": "UNP", "United Parcel Service": "UPS", "Urban Outfitters": "URBN", "US Ban": "USB", "United Technologies": "UTX", "Visa ": "V", "Varian Medical Systems": "VAR", "VF ": "VFC", "Viacom ": "VIAB", "Valero Energy": "VLO", "Vulcan Materials": "VMC", "Vornado Realty Trust": "VNO", "Verisign ": "VRSN", "Ventas ": "VTR", "Verizon Communications": "VZ", "Walgreen Co": "WAG", "Waters ": "WAT", "Western Digital": "WDC", "Wisconsin Energy ": "WEC", "Whole Foods": "WFM", "Whirlpool ": "WHR", "Windstream ": "WIN", "WellPoint ": "WLP", "Waste Management ": "WM", "Williams Cos": "WMB", "Wal-Mart": "WMT", "Watson Pharmaceuticals": "WPI", "Washington Post": "WPO", "WPX Energy": "WPX", "Western Union": "WU", "Weyerhaeuser ": "WY", "Wyndham Worldwide": "WYN", "Wynn Resorts": "WYNN", "United States Steel ": "X", "Xcel Energy ": "XEL", "XL Capital": "XL", "Xilinx ": "XLNX", "Exxon Mobil ": "XOM", "Dentsply International": "XRAY", "Xerox ": "XRX", "Xylem ": "XYL", "Yahoo ": "YHOO", "Yum! Brands ": "YUM", "Zions Ban": "ZION", "Zimmer Holdings": "ZMH"}
#Twitter accounts to grab data from
#TODO filter with trusted accounts
twitter_accounts={"Reuters":1652541}

#FOR TESTING ONLY
#TICKER="AAPL"

class DataReddit(object):
    def __init__(self,_user,_ups,_downs,_title, _ticker, _date, _open, _previousClose, _daysHigh, _daysLow):
        self.ticker = _ticker
        self.user = _user
        self.ups = _ups
        self.downs = _downs
        self.title = _title
        self.date = _date
        self.open = _open
        self.PreviousClose = _previousClose
        self.DaysHigh = _daysHigh
        self.DaysLow = _daysLow

class DataTwitter(object):
    def __init__(self,_user,_favorite_count,_retweet_count,_tweet, _ticker, _date, _open, _previousClose, _daysHigh, _daysLow):
        self.ticker = _ticker
        self.user = _user
        self.favorite_count = _favorite_count
        self.retweet_count = _retweet_count
        self.tweet = _tweet
        self.date = _date
        self.open = _open
        self.PreviousClose = _previousClose
        self.DaysHigh = _daysHigh
        self.DaysLow = _daysLow

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




class GrabberStreamListener(tweepy.StreamListener):
    """overrides tweepy.StreamListener to add logic to on_status and on_error"""

    def on_status(self, status):
        for company, ticker in companies_ticker.items():
            if utils.findWholeWord(company)(status.text):
                temp = stock.getStockInfoVerbose(ticker)
                stockdata=temp[0]
                with open('data.json', 'a') as outfile:

                    jsonData = DataTwitter(status.id_str,status.favorite_count,tweet[0].retweet_count,status.text,ticker, status.created_at,
                                    stockdata["Open"], stockdata["PreviousClose"], stockdata["DaysHigh"], stockdata["DaysLow"])
                    json.dump(jsonData, outfile,
                                      default=utils.jdefualt,sort_keys = True, indent = 4, ensure_ascii=False)
                    print(json.dumps(jsonData,
                                      default=utils.jdefualt,sort_keys = True, indent = 4, ensure_ascii=False))

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True 
    def on_timeout(self):
        print >> sys.stderr, 'Timeout with Twitter'
        return True # 

def limit_handler(cursor):
    """Handling Twitter API request Limits"""
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


def AuthenticateTwitter():
    """OAuth for Twitter API"""
    auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)  # ,parser=tweepy.parsers.JSONParser())
    return api


def QueryProfile(api, QUERY_PROFILE, limit):
    """Query a profile with provided profile id, returning tweets to a limit of pages"""
    try:
        user = api.user_timeline(QUERY_PROFILE)
        for tweet in limit_handler(tweepy.Cursor(api.user_timeline, id=QUERY_PROFILE).pages(limit)):
            for company, ticker in companies_ticker.items():
                if utils.findWholeWord(company)(tweet[0].text):
                    queryDate=str(tweet[0].created_at)
                    DateFormated=utils.formatDate(queryDate)
                    temp = stock.getHistoricalPrices(ticker,DateFormated,DateFormated)
                    if temp!=0:
                      stockdata=temp[0]
                      with open('temptweet.json', 'a') as outfile:
                          jsonData = DataTwitter(tweet[0].id_str,tweet[0].favorite_count,tweet[0].retweet_count,tweet[0].text,ticker, queryDate,
                                          stockdata["Open"], stockdata["Close"], stockdata["High"], stockdata["Low"])
                          json.dump(jsonData, outfile,
                                            default=utils.jdefault,sort_keys = True, indent = 4, ensure_ascii=False)
                          print(json.dumps(jsonData,
                                            default=utils.jdefault,sort_keys = True, indent = 4, ensure_ascii=False))
        utils.JSONify('temptweet.json','tweets.json')
    except KeyboardInterrupt:
        print('\nProfile Query Interupted')
        utils.JSONify('temptweet.json','tweets.json')


def StartStream(api,company):
    """Query Twitter with a specific filter"""
    try:
        StreamListener = GrabberStreamListener()
        stream = tweepy.Stream(auth=api.auth, listener=GrabberStreamListener())
        stream.filter(track=[company], languages=["en"])
        stream.userstream( track=all_users(), async=True )
    except KeyboardInterrupt:
        print('\nGrabber stream Interupted')
        try: 
            stream.disconnect()
            del stream
            utils.JSONify('temptweet.json','tweets.json')
            sys.exit(0)
        except SystemExit:
            os._exit(0)

#Reddit Block
def AuthorizeReddit():
  """Authorize reddit from reddit.txt"""
  with open("reddit.txt", 'r') as temp:
    credentials = [x.strip().split(':') for x in temp.readlines()]
    for cred in credentials:
      redditApi = praw.Reddit(client_id=cred[0],
                                 client_secret=cred[1],
                                 user_agent=cred[2]
                                 )
    return redditApi
def RedditLimitHandler(redditApi,subReddit,start_date,end_date):
  params = {'sort':'new', 'limit':None, 'syntax':'cloudsearch'}
  return redditApi.subreddit(subReddit).submissions(end_date,start_date)
  #.search('timestamp:{0}..{1}'.format(end_date,start_date), **params)

def RedditAppendData(subResults,start_date):
  lastdate=start_date
  for post in subResults:
      for company, ticker in companies_ticker.items():
        if utils.findWholeWord(company)(post.title):
          queryDate=utils.formatDateUtf(post.created_utc)
          DateFormated=utils.formatDate(queryDate)
          if int(post.created_utc)<lastdate:
            lastdate=post.created_utc
          temp = stock.getHistoricalPrices(ticker,DateFormated,DateFormated)
          if temp!=0:
            stockdata=temp[0]
            with open('tempreddit.json', 'a') as outfile:
              jsonData = DataReddit(post.id,post.ups,post.downs,post.title,ticker, queryDate,
                                            stockdata["Open"], stockdata["Close"], stockdata["High"], stockdata["Low"])
              json.dump(jsonData, outfile,
                                              default=utils.jdefault,sort_keys = True, indent = 4, ensure_ascii=False)
              print(json.dumps(jsonData,
                                              default=utils.jdefault,sort_keys = True, indent = 4, ensure_ascii=False)) 
  return lastdate

def CycleReddit(redditApi,subReddit,start_date,end_date):
  while(start_date>=end_date):
    limit=RedditLimitHandler(redditApi,subReddit,start_date,end_date)
    lastdate=RedditAppendData(limit,start_date)
    print("Start Date "+str(utils.formatDateUtf(lastdate)))
    print("End Date "+str(utils.formatDateUtf(end_date)))
    CycleReddit(redditApi,subReddit,lastdate,end_date)

def QuerySubreddit(redditApi,subReddit):
  """Query a specific subreddit with a limit l"""
  try:
    start_date =1433184973#int((datetime.datetime.now() - datetime.timedelta(days=365)).timestamp())#int(datetime.datetime.now().timestamp())
    end_date= int((datetime.datetime.now() - datetime.timedelta(days=730)).timestamp())#int((datetime.datetime.now() - datetime.timedelta(days=365)).timestamp())
    CycleReddit(redditApi,subReddit,start_date,end_date)

    utils.JSONify('tempreddit.json','reddit.json')
  except KeyboardInterrupt:
    print('\nProfile Query Interupted')
    utils.JSONify('tempreddit.json','reddit.json')   

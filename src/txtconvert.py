import json
import random
import string
import utils
import stock
import nltk
from nltk.stem import *
from nltk import pos_tag
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

say
import codecs
import re
import os
from datetime import timedelta, date
#import csv


companies_ticker = {"jpmorgan":"jpm", "aig":"aig", "hsbc":"hbc", "intel":"intc", "agilent": "a", "alcoa ": "aa", "apple": "aapl", "amerisourcebergen ": "abc", "abbott laboratories": "abt", "ace limited": "ace", "accenture": "acn", "adobe systems ": "adbe", "adobe": "adbe", "analog devices ": "adi", "archer-daniels-midland": "adm", "automatic data processing": "adp", "adp": "adp", "autodesk ": "adsk", "adt ": "adt", "ameren ": "aee", "american electric power": "aep", "aes ": "aes", "aetna ": "aet", "aflac ": "afl", "allergan ": "agn", "american intl group ": "aig", "apartment investment & mgmt": "aiv", "apartment investment": "aiv", "assurant ": "aiz", "akamai technologies ": "akam", "akamai": "akam", "allstate ": "all", "altera ": "altr", "alexion pharmaceuticals": "alxn", "alexion": "alxn", "applied materials ": "amat", "advanced micro devices": "amd", "amd": "amd", "amgen ": "amgn", "ameriprise financial": "amp", "american tower": "amt", "amazoncom ": "amzn", "amazon": "amzn", "autonation ": "an", "abercrombie & fitch company": "anf", "abercrombie": "anf", "aon plc": "aon", "apache": "apa", "anadarko petroleum ": "apc", "air products & chemicals ": "apd", "amphenol": "aph", "apollo group ": "apol", "airgas ": "arg", "allegheny technologies ": "ati", "avalonbay communities, ": "avb", "avon products": "avp", "avon": "avp", "avery dennison ": "avy", "american express co": "axp", "american express": "axp", "amex": "axp", "autozone ": "azo", "boeing company": "ba", "bank of america ": "bac", "bofa": "bac", "baxter international ": "bax", "bed bath & beyond": "bbby", "bb&t ": "bbt", "best buy": "bby", "bard": "bcr", "becton dickinson": "bdx", "beam ": "beam", "franklin resources": "ben", "brown-forman ": "bf.b", "baker hughes ": "bhi", "big lots ": "big", "biogen idec ": "biib", "the bank of new york mellon ": "bk", "blackrock": "blk", "ball ": "bll", "bmc software": "bmc", "bemis company": "bms", "bristol-myers squibb": "bmy", "broadcom ": "brcm", "berkshire hathaway": "brk.b", "berkshire": "brk.b", "boston scientific": "bsx", "peabody energy": "btu", "borgwarner": "bwa", "boston properties": "bxp", "citigroup ": "c", " ca ": "ca", "conagra foods ": "cag", "conagra": "cag", "cardinal health ": "cah", "cameron international ": "cam", "caterpillar ": "cat", "chubb ": "cb", "cbre group": "cbg", "cbs ": "cbs", "coca-cola": "cce", "coke": "cce", "crown castle": "cci", "carnival ": "ccl", "celgene ": "celg", "cerner": "cern", "cf industries holdings ": "cf", "carefusion": "cfn", "chesapeake energy": "chk", "c h robinson worldwide": "chrw", "cigna ": "ci", "cinnati financial": "cinf", "colgate-palmolive": "cl", "cliffs natural resources": "clf", "the clorox company": "clx", "comerica ": "cma", "comcast ": "cmcsa", "cme group ": "cme", "chipotle": "cmg", "cummins ": "cmi", "cms energy": "cms", "centerpoint energy": "cnp", "consol energy ": "cnx", "capital one financial": "cof", "capitalone": "cof", "capital one": "cof", "cabot oil & gas": "cog", "coach ": "coh", "rockwell collins": "col", "conocophillips": "cop", "costco": "cost", "covidien": "cov", "campbell soup": "cpb", "campbell's": "cpb", "salesforce.com": "crm", "salesforce": "crm", "computer sciences ": "csc", "cisco": "csco", "cisco systems": "csco", "csx ": "csx", "cintas ": "ctas", "centurylink ": "ctl", "cognizant technology solutions": "ctsh", "citrix systems": "ctxs", "cablevision systems ": "cvc", "coventry health care ": "cvh", "cvs caremark ": "cvs", "chevron ": "cvx", "dominion resources": "d", "du pont": "dd", "deere & co": "de", "dell ": "dell", "dean foods": "df", "discover financial services": "dfs", "dollar general": "dg", "quest diagnostics": "dgx", "d r horton": "dhi", "danaher ": "dhr", "walt disney": "dis", "disney": "dis", "discovery communications": "disca", "dollar tree": "dltr", "dun & bradstreet": "dnb", "denbury resources ": "dnr", "diamond offshore drilling": "do", "dover ": "dov", "dow chemical": "dow", "dow ": "dow", "dr pepper snapple group": "dps", "darden restaurants": "dri", "dte energy co": "dte", "directv": "dtv", "duke energy": "duk", "davita ": "dva", "devon energy ": "dvn", "electronic arts": "ea", " ea ": "ea", "ebay ": "ebay", "ecolab ": "ecl", "consolidated edison": "ed", "equifax ": "efx", "edison int'l": "eix", "estee lauder": "el", "emc ": "emc", "eastman chemical": "emn", "emerson electric": "emr", "eog resources": "eog", "equity residential": "eqr", "eqt ": "eqt", "express scripts": "esrx", "ensco plc": "esv", "e-trade": "etfc", "eaton ": "etn", "entergy ": "etr", "edwards lifesciences": "ew", "exelon ": "exc", "expeditors": "expd", "expedia ": "expe", "ford motor": "f", "fastenal": "fast", "freeport-mcmoran cp & gld": "fcx", "family dollar stores": "fdo", "fedex ": "fdx", "firstenergy ": "fe", "f5 networks": "ffiv", "first horizon national": "fhn", "federated investors ": "fii", "fidelity national information services": "fis", "fiserv ": "fisv", "fifth third ban": "fitb", "flir systems": "flir", "fluor ": "flr", "flowserve ": "fls", "fmc ": "fmc", "fossil": "fosl", "forest laboratories": "frx", "first solar ": "fslr", "fmc technologies ": "fti", "frontier communications": "ftr", "frontier": "ftr", "agl resources ": "gas", "gannett": "gci", "general dynamics": "gd", "general electric": "ge", "gilead sciences": "gild", "general mills": "gis", "corning ": "glw", "gamestop ": "gme", "genworth financial ": "gnw", "google ": "goog", "genuine parts": "gpc", "gap (the)": "gps", "the gap": "gps", "goldman sachs group": "gs", "goldman sachs": "gs", "goodyear tire & rubber": "gt", "goodyear": "gt", "grainger (ww) ": "gww", "halliburton": "hal", "harman int'l industries": "har", "hasbro ": "has", "huntington bancshares": "hban", "hudson city ban": "hcbk", "health care reit": "hcn", "hcp ": "hcp", "home depot": "hd", "hess ": "hes", "hartford financial svcgp": "hig", "heinz": "hnz", "harley-davidson": "hog", "honeywell": "hon", "starwood hotels & resorts": "hot", "starwood": "hot", "helmerich & payne": "hp", "hewlett-packard": "hpq", "block h&r": "hrb", "hormel foods ": "hrl", "harris ": "hrs", "hospira ": "hsp", "host hotels & resorts": "hst", "the hershey company": "hsy", "hershey": "hsy", "humana ": "hum", "international bus machines": "ibm", "intercontinentalexchange ": "ice", "international flav/frag": "iff", "international game technology": "igt", "intel ": "intc", "intuit ": "intu", "international paper": "ip", "interpublic group": "ipg", "ingersoll-rand plc": "ir", "iron mountain orporated": "irm", "intuitive surgical ": "isrg", "illinois tool works": "itw", "invesco ltd": "ivz", "jabil circuit": "jbl", "johnson controls": "jci", "penney (jc)": "jcp", "jc penney": "jcp", "jds uniphase ": "jdsu", "jacobs engineering group": "jec", "johnson & johnson": "jnj", "j&j": "jnj", "juniper networks": "jnpr", "joy global ": "joy", "jpmorgan chase & co": "jpm", "jpmorgan chase": "jpm", "jpmorgan": "jpm", "nordstrom": "jwn", "kellogg co": "k", "kimco realty": "kim", "kla-tencor ": "klac", "kimberly-clark": "kmb", "kinder morgan": "kmi", "carmax ": "kmx", "coca cola": "ko", "kroger co": "kr", "kraft foods group": "krft", "kraft": "krft", "kohl's ": "kss", "loews ": "l", "leggett & platt": "leg", "lennar ": "len", "laboratory  of america holding": "lh", "life technologies": "life", "l-3 communications": "lll", "linear technology ": "lltc", "lilly (eli) & co": "lly", "eli lilly": "lly", "legg mason": "lm", "lockheed martin ": "lmt", "loln national": "lnc", "lorillard ": "lo", "lowe's": "low", "lam research": "lrcx", "lsi ": "lsi", "limited brands ": "ltd", "leucadia national ": "luk", "southwest airlines": "luv", "lyondellbasell": "lyb", "macy's ": "m", "mastercard ": "ma", "marriott": "mar", "masco ": "mas", "mattel ": "mat", "mcdonald's ": "mcd", "microchip technology": "mchp", "mckesson ": "mck", "moody's ": "mco", "mondelez international": "mdlz", "medtronic ": "mdt", "metlife ": "met", "mcgraw-hill": "mhp", "mead johnson": "mjn", "mccormick & co": "mkc", "marsh & mclennan": "mmc", "3m": "mmm", "monster beverage": "mnst", "altria group ": "mo", "molex ": "molx", "monsanto": "mon", "the mosaic company": "mos", "marathon petroleum": "mpc", "merck & co": "mrk", "marathon oil ": "mro", "morgan stanley": "ms", "microsoft ": "msft", "motorola solutions ": "msi", "m&t bank ": "mtb", "micron technology": "mu", "murphy oil": "mur", "meadwestvaco ": "mwv", "mylan ": "myl", "noble energy ": "nbl", "nabors industries ltd": "nbr", "nasdaq omx group": "ndaq", "noble ": "ne", "nextera energy resources": "nee", "newmont mining  (hldg co)": "nem", "netflix ": "nflx", "newfield": "nfx", "nisource ": "ni", "nike ": "nke", "northrop grumman ": "noc", "national oilwell varco ": "nov", "nrg energy": "nrg", "norfolk southern ": "nsc", "netapp": "ntap", "northern trust ": "ntrs", "northeast utilities": "nu", "nucor ": "nue", "nvidia ": "nvda", "newell rubbermaid": "nwl", "nyse euronext": "nyx", "owens-illinois ": "oi", "oneok": "oke", "omnicom group": "omc", "oracle ": "orcl", "o'reilly automotive": "orly", "occidental petroleum": "oxy", "paychex ": "payx", "people's united bank": "pbct", "pitney-bowes": "pbi", "paccar ": "pcar", "pg&e ": "pcg", "plum creek timber": "pcl", "priceline.com ": "pcln", "precision castparts": "pcp", "metropcs communications ": "pcs", "patterson companies": "pdco", "public serv enterprise ": "peg", "pepsico ": "pep", "pet smart": "petm", "pfizer ": "pfe", "pripal financial group": "pfg", "procter & gamble": "pg", "progressive ": "pgr", "parker-hannifin": "ph", "pulte homes ": "phm", "perkinelmer": "pki", "prologis": "pld", "pall ": "pll", "philip morris": "pm", "pnc financial services": "pnc", "pentair": "pnr", "pinnacle west capital": "pnw", "pepco ": "pom", "ppg ": "ppg", "ppl ": "ppl", "perrigo": "prgo", "prudential financial": "pru", "public storage": "psa", "phillips 66": "psx", "quanta services ": "pwr", "praxair ": "px", "pioneer natural resources": "pxd", "qualcomm ": "qcom", "qep resources": "qep", "ryder system": "r", "reynolds american ": "rai", "rowan": "rdc", "regions": "rf", "robert half": "rhi", "red hat ": "rht", "polo ralph lauren ": "rl", "rockwell automation ": "rok", "roper industries": "rop", "ross stores ": "rost", "range resources ": "rrc", "rr donnelley & sons": "rrd", "republic services ": "rsg", "raytheon": "rtn", "sprint nextel ": "s", "saic": "sai", "starbucks ": "sbux", "scana ": "scg", "charles schwab": "schw", "spectra energy ": "se", "new sealed air": "see", "sherwin-williams": "shw", "sigma-aldrich": "sial", "smucker (jm)": "sjm", "schlumberger": "slb", "slm ": "slm", "snap-on ": "sna", "sandisk ": "sndk", "scripps networks interactive ": "sni", "simon property group ": "spg", "staples ": "spls", "stericycle ": "srcl", "sempra energy": "sre", "suntrust banks": "sti", "st jude medical": "stj", "state street ": "stt", "seagate technology": "stx", "constellation brands": "stz", "stanley black & decker": "swk", "southwestern energy": "swn", "safeway ": "swy", "stryker ": "syk", "symantec ": "symc", "sysco ": "syy", "at&t ": "t", "molson coors brewing company": "tap", "teradata ": "tdc", "teco energy": "te", "integrys energy group ": "teg", "te connectivity ltd": "tel", "teradyne ": "ter", "target ": "tgt", "tenet healthcare ": "thc", "titanium metals ": "tie", "tiffany": "tif", "tjx companies ": "tjx", "torchmark ": "tmk", "thermo fisher scientific": "tmo", "tripadvisor": "trip", "t rowe price group": "trow", "the travelers companies ": "trv", "tyson foods": "tsn", "tesoro petroleum co": "tso", "total system services": "tss", "time warner cable ": "twc", "time warner ": "twx", "texas instruments": "txn", "textron ": "txt", "tyco international": "tyc", "united health group ": "unh", "unum group": "unm", "union pacific": "unp", "united parcel service": "ups", "urban outfitters": "urbn", "us ban": "usb", "united technologies": "utx", "visa ": "v", "varian medical systems": "var", "vf ": "vfc", "viacom ": "viab", "valero energy": "vlo", "vulcan materials": "vmc", "vornado realty trust": "vno", "verisign ": "vrsn", "ventas ": "vtr", "verizon communications": "vz", "walgreen co": "wag", "waters ": "wat", "western digital": "wdc", "wisconsin energy ": "wec", "whole foods": "wfm", "whirlpool ": "whr", "windstream ": "win", "wellpoint ": "wlp", "waste management ": "wm", "williams cos": "wmb", "wal-mart": "wmt", "watson pharmaceuticals": "wpi", "washington post": "wpo", "wpx energy": "wpx", "western union": "wu", "weyerhaeuser ": "wy", "wyndham worldwide": "wyn", "wynn resorts": "wynn", "united states steel ": "x", "xcel energy ": "xel", "xl capital": "xl", "xilinx ": "xlnx", "exxon mobil ": "xom", "dentsply international": "xray", "xerox ": "xrx", "xylem ": "xyl", "yahoo ": "yhoo", "yum! brands ": "yum", "zions ban": "zion", "zimmer holdings": "zmh"}


def DataConvert():
    with codecs.open("data.txt", "w", "utf-8-sig") as txt:
        with open('fixedReddit.json') as data_file:
            data = json.load(data_file)
            for entry in data:
                stockdate = entry["date"]
                ticker = entry["ticker"]
                nextdate = utils.giveNextDate(stockdate)
                NextDayStock = stock.getHistoricalPrices(ticker, nextdate, nextdate)
                print(NextDayStock)
                if NextDayStock != 0:
                    pd = float(NextDayStock[0]["Close"])
                    pd1 = float(entry["PreviousClose"])
                    if (pd-pd1)/pd1>0:
                        txt.write("__label__positive " + entry["title"] + "\n")
                    else:
                        txt.write("__label__negative " + entry["title"] + "\n")
    lines = open('data.txt').readlines()
    random.shuffle(lines)
    codecs.open('shuffled.txt', 'w',"utf-8-sig").writelines(lines)

def ProcessSentance(raw_sentence):
    steemer = SnowballStemmer("english")
    stops = set(stopwords.words("english"))
    letters_only = re.sub("[^a-zA-Z]", " ", raw_sentence)
    
    words = letters_only.lower().split()
    for company, ticker in companies_ticker.items():
        if utils.findWholeWord(company)(raw_sentence):
            raw_sentence.replace(company,'')
        if utils.findWholeWord(ticker)(raw_sentence):
            raw_sentence.replace(ticker,'')
    
    meaningful_words = [w for w in words if not w in stops]
    steemed_words = [steemer.stem(plural) for plural in meaningful_words]
    return(" ".join(steemed_words))

def CleanData():
    with open("fullreddit.json", "r") as jsonFile:
        data = json.load(jsonFile)
        for entry in data:
            temp = entry["title"]
            entry["title"] = ProcessSentance(temp)
        with open("fixedReddit.json", "w") as jsonFile:
            json.dump(data, jsonFile, default=utils.jdefault,
                      sort_keys=True, indent=4, ensure_ascii=True)
def RemoveTemp():
    os.remove("data.txt")
    os.remove("fixedReddit.json")

def PreProcess():
    #try:
        CleanData()
        DataConvert()
        RemoveTemp()
    #except:
     #   RemoveTemp()
      #  print("Failed to preprocess")

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def CollectStockData():
    datafile_path = "stockdata.txt"
    datafile_id = open(datafile_path, 'w+')
    #here you open the ascii file

    xarray = np.array([0,1,2,3,4,5])
    yarray = np.array([0,10,20,30,40,50])
    #here is your data, in two numpy arrays

    data = np.array([xarray, yarray])
    data = data.T
    #here you transpose your data, so to have it in two columns

    np.savetxt(datafile_id, data, fmt=['%.5f','%5f'])
    #here the ascii file is populated. 

    datafile_id.close()
    """
    with open("stockdata.csv", "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        start_date = date(2015, 5, 1)
        end_date = date(2017, 5,3)

        initrow=['Date']
        #initrow.extend(['Date','Open','Close','High','Low'])
        for key in companies_ticker:
            initrow.append(key)
        writer.writerow(initrow)
        for single_date in daterange(start_date, end_date):
            row=[]
            row.append(str(single_date))
            for key in companies_ticker:
                temp=stock.getHistoricalPrices(key,start_date,end_date)
                if temp!=0:
                    print(temp)
                else:
                    row.append(0)
                    """
#PreProcess()
CollectStockData()




# The stemmer vs lemmatizer debates goes on. It's a matter of
# preferring precision over efficiency. You should lemmatize to achieve
# linguistically meaningful units and stem to use minimal computing juice and still index a word
# and its variations under the same key.

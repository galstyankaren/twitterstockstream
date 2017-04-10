import os
import datetime
import re

def JSONify(jsonIn,jsonOut):
    with open(jsonIn,mode='rt') as fin:
        with open(jsonOut,mode='w') as fout:
            fout.write('[')
            for line in fin:
                fout.write(line.replace('}{', '},{'))
            fout.write(']')
    os.remove(jsonIn)
    print("\nData JSONified")

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

def formatDate(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%Y-%m-%d')

def jdefault(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    else:
        return o.__dict__
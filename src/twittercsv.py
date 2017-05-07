import csv
import stock
import datetime




companies_ticker = {"apple":"AAPL","google": "GOOG", "microsoft": "MSFT", "twitter": "TWTR"}



def DateParser(date):
	return datetime.datetime.strptime(date, '%a %b %d %H:%M:%S %z %Y').strftime('%Y-%m-%d')

def main():
	with open('test.csv', 'rt') as read:
		new=[]
		with open('newtest.csv', 'wt') as write:
			reader = csv.reader(read, delimiter=',')
			writer = csv.writer(write, delimiter=',')
			firstline = True
			for row in reader:
				if firstline:
					firstline = False
					continue
				date=DateParser(row[3])
				data=stock.getHistoricalPrices(companies_ticker[row[0]],date,date)
				if data!=0:
					stockdata=data[0]
					temp=row
					temp.extend([stockdata["Open"], stockdata["Close"], stockdata["High"], stockdata["Low"]])
					writer.writerow(temp)
main()
					  


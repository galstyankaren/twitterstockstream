import grabber
import sys
import getopt


def main():
	api = grabber.Authenticate()
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hs:q::", ["--stream,--query"])
	except getopt.GetoptError:
		print('Invalid option or input')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('\nExamples of usage \npython3 main.py -q Reuters:20\npython3 main.py -s AAPL')
		elif opt =='-q':
			QUERY_PROFILE=arg.split(':')
			print("Querying "+QUERY_PROFILE[0]+" up to "+QUERY_PROFILE[1]+" pages")
			grabber.QueryProfile(api,QUERY_PROFILE[0],int(QUERY_PROFILE[1]))
		elif opt =='-s':
			QUERY_FILTER=str(arg)
			print("Streaming with filter "+QUERY_FILTER)
			grabber.StartStream(api,QUERY_FILTER)
   	# QUERY_PROFILE = str(sys.argv[1])
    # QUERY_PROFILE = "Reuters"
    # print("Querying " + QUERY_PROFILE)
    # grabber.StartStream(api, QUERY_PROFILE)
    # grabber.QueryProfile(api,QUERY_PROFILE,50)
"""
	for key, value in companies_ticker.items():
		print("Querying "+key)
		grabber.StartStream(api,key)
"""
main()

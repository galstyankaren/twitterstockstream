import grabber
import sys
import getopt


def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], "hs:t::r::", ["--stream,--query"])
	except getopt.GetoptError:
		print('Invalid option or input')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('\nExamples of usage \npython3 main.py -qt Reuters:20\npython3 main.py -s AAPL\npython3 main.py -qr News')
		
		elif opt =='-t':
			QUERY_PROFILE=arg.split(':')
			api = grabber.AuthenticateTwitter()
			print("Querying "+QUERY_PROFILE[0]+" up to "+QUERY_PROFILE[1]+" pages")
			grabber.QueryProfile(api,QUERY_PROFILE[0],int(QUERY_PROFILE[1]))
		
		elif opt =='-r':
			api = grabber.AuthorizeReddit()
			QUERY_PROFILE=arg.split(':')
			print("Querying "+QUERY_PROFILE[0]+" up to "+QUERY_PROFILE[1]+" pages")
			grabber.QuerySubreddit(api,QUERY_PROFILE[0],int(QUERY_PROFILE[1]))
		
		elif opt =='-s':
			api = grabber.AuthenticateTwitter()
			QUERY_FILTER=str(arg)
			print("Streaming with filter "+QUERY_FILTER)
			grabber.StartStream(api,QUERY_FILTER)
main()

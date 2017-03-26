import twittergrabber as grabber
import sys

def main():
	QUERY_PROFILE=str(sys.argv[1])
	print("Querying "+QUERY_PROFILE)
	api=grabber.Authenticate()
	tweets=grabber.QueryProfile(api,QUERY_PROFILE,2)
main()

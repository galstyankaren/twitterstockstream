import grabber
import sys


def main():
    api = grabber.Authenticate()
   #QUERY_PROFILE = str(sys.argv[1])
    QUERY_PROFILE = "Reuters"
    print("Querying " + QUERY_PROFILE)
    #grabber.StartStream(api, QUERY_PROFILE)
    grabber.QueryProfile(api,QUERY_PROFILE,50)
"""
	for key, value in companies_ticker.items():
		print("Querying "+key)
		grabber.StartStream(api,key)
"""
main()

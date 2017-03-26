import sys
import tweepy
import json
import time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

CONSUMER_KEY = "YqAo5ZRvG1QpPkcGG6rJ0JqwU"
CONSUMER_SECRET = "AiM11Y5qhg6zsnbrMepUqxe7ejWuwm6NYdck2nOLlzXYcR6yJC"
ACCESS_TOKEN="781620753456308224-3pGPA8366kQLCwsnpm46clwaebrszWV"
ACCESS_SECRET="fBNJ3ayrwgq3xkPJuvOKrEL1gLwg71jF1bD8H7beXuwnN"

class GrabberStreamListener(tweepy.StreamListener):
	def on_status(self, status):
	    print(status.text)
	def on_error(self, status_code):
		if status_code == 420:
	        #returning False in on_data disconnects the stream
			return False
"""Handling Twitter API request Limits"""
def limit_handler(cursor):
	while True:
		try:
			yield cursor.next()
		except tweepy.RateLimitError:
			time.sleep(15 * 60)

def Authenticate():
	auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
	#TODO fix JSON parser error 
	api = tweepy.API(auth)#,parser=tweepy.parsers.JSONParser())
	return api

def QueryProfile(api,QUERY_PROFILE,limit):
	user = api.user_timeline(QUERY_PROFILE)
	tweets=[]
	for tweet in limit_handler(tweepy.Cursor(api.user_timeline,id=QUERY_PROFILE).pages(limit)):
		tweets.append(tweet)
		print(type(tweet))
	return tweets

def StartStream(api,filter):
	#override tweepy.StreamListener to add logic to on_status
	

	StreamListener =GrabberStreamListener()
	stream=tweepy.Stream(auth = api.auth, listener=GrabberStreamListener())
	stream.filter(track=[filter])
	return stream
import sys
import tweepy
import csv
import json
import time
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener


CONSUMER_KEY = "YqAo5ZRvG1QpPkcGG6rJ0JqwU"
CONSUMER_SECRET = "AiM11Y5qhg6zsnbrMepUqxe7ejWuwm6NYdck2nOLlzXYcR6yJC"
ACCESS_TOKEN="781620753456308224-3pGPA8366kQLCwsnpm46clwaebrszWV"
ACCESS_SECRET="fBNJ3ayrwgq3xkPJuvOKrEL1gLwg71jF1bD8H7beXuwnN"
START_TIME=time.time()

auth = OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth,parser=tweepy.parsers.JSONParser())

user = api.user_timeline('Reuters')
#print(user)

results = api.search(q="Reuters", count=100)
print (results)


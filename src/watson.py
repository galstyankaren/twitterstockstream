from watson_developer_cloud import ToneAnalyzerV3
from watson_developer_cloud import AuthorizationV1
from watson_developer_cloud import
import json

def Authorize():
	with open('watson.txt') as f:
        credentials = [x.strip().split(':') for x in f.readlines()]
        for username,password in credentials:
            authorization = AuthorizationV1(
            username=username,
            password=password)
		return credentials    
import praw


def Authorize():
    with open("reddit.txt", 'r') as temp:
        credentials = [x.strip().split(':') for x in temp.readlines()]
        for cred in credentials:
            redditApi = praw.Reddit(client_id=cred[0],
                                 client_secret=cred[1],
                                 user_agent=cred[2]
                                 )
    return redditApi
def QuerySubreddit(redditApi,subReddit,l):
	
	for post in redditApi.subreddit(subReddit).hot(limit=l):
		print(post.title)
		print(post.ups)
		print(post.downs)
		print(post.num_comments)
api=Authorize()
QuerySubreddit(api,"news",20)

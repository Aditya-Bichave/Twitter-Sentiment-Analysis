import tweepy
from textblob import TextBlob

consumer_key = "PFSGrmCX41xCW3ffp8ZWCx3Kk"
consumer_secret = "E6NVllPxwjYBTQnTa8x6N1YiEv0c1wJh4BGCFVy12EyQmxKc0L"

acess_token = "3680391439-BNPlqRhjK9umgA99iwQYYblpWCDkEtXJHIHhgmM"
acess_token_secret = "IjVhD9yMBkQoI5qWHeg19tiSPd9ddTo7XXDmh2ejl5Fq5"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_token_secret)

api = tweepy.API(auth)

public_tweets = api.search("Trump")

for tweet in public_tweets:
     print(tweet.text)
     analysis = TextBlob(tweet.text)
     print(analysis.sentiment)

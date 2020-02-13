import tweepy
import json
from tweepy import OAuthHandler
 
consumer_key = 'xP4bGwl51GD5lcfjszSYGVFGu'
consumer_secret = 'EEfuHS5gTZ73rqHn2aXgKbAckvMNZnjPT2ARPfxTOEX0YJd0bC'
access_token = '1124486895386238976-EMhJfl1eg38DfkWPcOT77a8jNkWIZE'
access_secret = 'uaYkAce5mvyp8w6i9EHUoSvI2DIQVJ0C9NNL9w6jWPRuL'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

f = open("data.txt","w+") 

def process_or_store(tweet):
    f.write(json.dumps(tweet))

user = api.me()

search = tweepy.Cursor(api.search, q="*", lang="bn").items(200)

i = 0
for item in search:
    i += 1
    f.write(str(i)+") "+item.text+'\n')

f.close()
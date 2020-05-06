# thetweetbot

import tweepy as tp
import random
import requests
import json
import time


def post():

    api_req = requests.get("https://thesimpsonsquoteapi.glitch.me/quotes")
    api = json.loads(api_req.content)
    caption = api[0]['quote']
    charac = api[0]['character']
    caption+="\n--"
    caption+=charac
    caption+="\n#TWITTERBOT #TWEEPY"

    # credentials to login to twitter api
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_secret = ''

    # login to twitter account api
    auth = tp.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tp.API(auth)
    
    for follower in tp.Cursor(api.followers).items():
        follower.follow()

    api.update_status(caption)

    tweets = api.home_timeline()
    for tweet in tweets:
        tweet.favorite()
    

if __name__ == '__main__':
    post()

import tweepy
import time
import random
import requests

# personal information
consumer_key = "Enter your consumer key"
consumer_secret = "Enter your consumer secret"
access_token = "Enter your access token"
access_token_secret = "Enter your access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

while True:

    with open("vocab.txt", "r") as grilled_cheese:

        lines = grilled_cheese.readlines()
        list_of_tweet = lines

        final = random.sample(lines, 9)

        x = ' '.join(final[0:9])
        x = x.strip()
        godspeak = "GodSpeak: \n" + x
        params = {
            'amount': '1',
        }

        response = requests.get('https://temple.xslendi.xyz/api/v1/quote',
                                params=params)
        tweet = response.json()
        final_tweet = tweet['quote']
        #print(final_tweet)
        final_tweet = "'" + final_tweet + "'-Terry A Davis"
        #print(final_tweet)
        api.update_status(status=godspeak)
        api.update_status(status=final_tweet)
        print("Tweet Sent")
        time.sleep(18000)

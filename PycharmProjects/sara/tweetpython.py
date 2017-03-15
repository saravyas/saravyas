from tweepy.streaming import StreamListener

from tweepy import OAuthHandler

from tweepy import Stream

import json

access_token = "2795912616-4ei6Q5E0rVWjizpvQgkJh2iDtv408oi4QdlKvUt"

access_token_secret = "pDFdfdeYttdWlBdfpXi966lCLaQgmg3ENib85rbRqLPw6"

consumer_key = "6GfJLdaDj9dXZfq2sCz1Maltl"

consumer_secret = "op2Pz6aO4d5A9gMjmVoUWyqwPqcnkL8WKSA6BjkWlvLPQok8ax"


# Defining listener class for getting the streamingclass StdOutListener(StreamListener):

def on_data(self, testdata2):
    # Retrieving the details like Id, tweeted text and created at.

    tweet = json.loads(testdata2)

    created_at = tweet["created_at"]

    id_str = tweet["id_str"]

    text = tweet["text"]

    obj = {"created_at": created_at, "id_str": id_str, "text": text, }

    tweetind = collection.insert_one(obj).inserted_id

    print obj

    return True


def on_error(self, status):
    print status


if __name__ == '__main__':
    # This handles Twitter authetification and the connection to Twitter Streaming AP

    class StdOutListener(StreamListener):
        def on_data(self, data):
            print data
            return True

        def on_error(self, status):
            print status


    l = StdOutListener()

    auth = OAuthHandler(consumer_key, consumer_secret)

    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    # Below code  is for making connection with mongoDB

    from pymongo import MongoClient

    client = MongoClient()

    client = MongoClient('localhost', 27017)

    db = client.gmx

    collection = db.tweet

    # This line filter Twitter Streams to capture data by the keywords: 'India'

    stream.filter(track=['India'])
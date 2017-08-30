import re
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob

#consumer key, consumer secret, access token, access secret.
ckey="****************"
csecret="****************"
atoken="*****************"
asecret="****************"


class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data["text"]
        username = all_data["user"]["screen_name"]
        result = re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", tweet)
        analysis = TextBlob(result)
        if analysis.sentiment.polarity > 0:
             print "username: ",username,"\npost: ",result
        else:
            print "normal post"
        return(True)

    def on_error(self, status):
        print status



auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["kill","death","murder","bomb","blast"])

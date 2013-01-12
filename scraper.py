import tweepy
import turtle
import secrets

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

def init_scraper():    
    conkey,consecret,acctok,acctoksecret = secrets.get_secrets()

    auth1 = tweepy.auth.OAuthHandler(conkey, consecret)
    auth1.set_access_token(acctok, acctoksecret)
    api = tweepy.API(auth1)
    l = StreamListener()
    streamer = tweepy.Stream(auth=auth1, listener=l, timeout=1000)
    searchTerms = dir(turtle)
    streamer.filter(None, searchTerms)

init_scraper()

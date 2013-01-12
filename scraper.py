import tweepy
import turtle
import secrets
import validation

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        validation.supply_words(status.text.split())

def init_scraper():
    # get all of our validation tokens. You don't get to see them
    conkey,consecret,acctok,acctoksecret = secrets.get_secrets()

    auth1 = tweepy.auth.OAuthHandler(conkey, consecret)
    auth1.set_access_token(acctok, acctoksecret)
    api = tweepy.API(auth1)

    l = StreamListener()
    streamer = tweepy.Stream(auth=auth1, listener=l, timeout=1000)
    searchTerms = ['forward', 'fd', 'back', 'bk', 'backward']#dir(turtle)
    streamer.filter(None, searchTerms)

init_scraper()

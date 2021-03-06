import tweepy
import turtle
import secrets
import validation
import colors

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        validation.supply_words(status)

def init_scraper():
    # get all of our validation tokens. You don't get to see them
    conkey,consecret,acctok,acctoksecret = secrets.get_secrets()

    auth1 = tweepy.auth.OAuthHandler(conkey, consecret)
    auth1.set_access_token(acctok, acctoksecret)
    api = tweepy.API(auth1)

    l = StreamListener()
    streamer = tweepy.Stream(auth=auth1, listener=l, timeout=None)
    searchTerms = [key for key in validation.command_templates]
    searchTerms.extend(colors.colors)
    streamer.filter(None, searchTerms)

init_scraper()

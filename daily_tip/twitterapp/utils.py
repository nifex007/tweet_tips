import tweepy
import os
import json 
import pprint
from tips.models import Tips

consumer_key = os.environ.get('TWITTER_API_KEY')
consumer_secret = os.environ.get('TWITTER_API_SECRET')
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


def tweepy_api_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    print(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api


def format_response(response):
    #convert to string
    json_str = json.dumps(response)
    #deserialise string into python object
    parsed = json.loads(json_str)
    print(json.dumps(parsed, indent=4, sort_keys=True))
    return parsed


def get_tweet(id):
   api = tweepy_api_auth()
   tweet = api.get_status(id)
#    print("tweet", tweet)
   tweet = tweet._json
   return format_response(tweet)


def get_timeline_tweets(screen_name, since):
    api = tweepy_api_auth()
    if since is None:
        tweets = api.user_timeline(screen_name=screen_name,
                                    include_rts=True,
                                    tweet_mode='extended',
                                    exclude_replies=True,
                                    count=2
                                    )
    else:
        tweets = api.user_timeline(screen_name=screen_name,
                                        include_rts=True,
                                        tweet_mode='extended',
                                        since_id=since,
                                        count=2,
                                        exclude_replies=True,
                                        )
    
    
    tweets_list = [tweet._json for tweet in tweets] # extract json part of tweepy response
   
    return format_response(tweets_list)


def extract_media_links(tweet):
    """
    :tweet single tweet object/dict
    :return turple (boolean, obj)
    """
    link_dict = {}
    has_link = False
    links = []
    try:
        media = tweet['entities']['media']
        for item in media:
            links.append(item['media_url_https'])
        has_link = True 
        link_dict['id'] = tweet['id']
        link_dict['links'] = links
    except KeyError:
        return has_link, link_dict
    
    return has_link, link_dict




from django.shortcuts import redirect
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


def get_timeline_tweets(screen_name, since_id, max_id):
    api = tweepy_api_auth()
    temp_tweets = []
    tweets_ = []

    if max_id is None and since_id is None:
        tweets = api.user_timeline(screen_name=screen_name,
                                    include_rts=True,
                                    tweet_mode='extended',
                                    exclude_replies=True,
                                    count=200
                                    )
            
        tweets_list = [tweet._json for tweet in tweets] # extract json part of tweepy response
        tweets_.append(tweets_list)
        return format_response(tweets_)
    
    elif since_id and max_id is None:
        tweets = api.user_timeline(screen_name=screen_name,
                                        include_rts=True,
                                        tweet_mode='extended',
                                        since_id = since_id,
                                        count=200,
                                        exclude_replies=True,
                                        )
        tweets_list = [tweet._json for tweet in tweets]
        if len(tweets_list) > 0:
            tweets_.append(tweets_list)
            max_id = tweets_list[-1]['id']
            get_timeline_tweets(screen_name, since_id, max_id)
        else:
            return format_response(tweets_)
    else:
        tweets = api.user_timeline(screen_name=screen_name,
                                    include_rts=True,
                                    tweet_mode='extended',
                                    exclude_replies=True,
                                    count=200,
                                    since_id = since_id,
                                    max_id = max_id
                                    )
        
        tweets_list = [tweet._json for tweet in tweets]
        tweets_.append(tweets_list)
        if len(tweets_list) > 0:
            max_id = tweets_list[-1]['id']
            get_timeline_tweets(screen_name, since_id, max_id)
        return format_response(tweets_)

   
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

def twitter_oauth(callback):
    return tweepy.OAuthHandler(consumer_key, consumer_secret, callback)


def get_twitter_login_url():
    callback = 'http://127.0.0.1:8000/social/' 
    oauth_handler = twitter_oauth(callback)
    login_url = oauth_handler.get_authorization_url()

    print("login url", login_url)

    return login_url


def tweepy_api(access_token, access_token_secret):
    # Authenticated api for users
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
    except tweepy.TweepError as e:
        print('Exception: {}'.format(e))

    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    return api


def redirect_to_login(request, signed_in):

    if signed_in:
        return redirect('http://{}/'.format(request.get_host()))

from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from django.views import View
from twitterapp.utils import tweepy_api_auth, format_response, get_tweet, get_timeline_tweets, extract_media_links
from tips.models import Tips, Links
from tips.utils import save_tip

# Create your views here.
class TwitterView(View):

    api = tweepy_api_auth()
    user_id = 'python_tip'

    def get(self, request):
        api = self.api
        user = self.user_id
        # get the last 200 tweets 
        tweets = get_timeline_tweets('python_tip', since=None)

        for tweet in tweets:
            print("tweet ", tweet)
            print("*************")
            save_tip(tweet)
        
        # t = get_tweet('1356230120604803075') 
        # print(t)     
        # save_tip(t)



        return HttpResponse("<h2> Twitter </h2>")


class TwitterAuth(View):
    pass
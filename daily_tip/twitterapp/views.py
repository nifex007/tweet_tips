from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
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
        # tweets = get_timeline_tweets('python_tip', since=None)

        # for tweet in tweets:
        #     print("tweet ", tweet)
        #     print("*************")
        #     save_tip(tweet)
    
        # t = get_tweet('1116283605368606721') 
        # save_tip(t)

        # for status in tweepy.Cursor(api.user_timeline, screen_name='python_tip', since_id=1116283605368606721).items():
        #     save_tip(status._json)
        #     print(status._json)
       



        return HttpResponse("<h2> Twitter </h2>")


class TwitterAuth(View):
    pass


class Home(TemplateView):
    template_name="twitterapp/home.html"
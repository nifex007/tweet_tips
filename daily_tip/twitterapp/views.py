from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from django.views import View
from twitterapp.utils import tweepy_api_auth, format_response, get_tweet, extract_media_links


# Create your views here.
class TwitterView(View):

    api = tweepy_api_auth()
    user_id = 'python_tip'

    def get(self, request):
        api = self.api
        user = self.user_id
        # get the last 200 tweets 
        # format_response(tweets)
        
        # print(get_tweet('1362776037428502534'))


        extract_media_links(get_tweet("1356937628566880260"))

        return HttpResponse("<h2> Twitter </h2>")


class TwitterAuth(View):
    pass
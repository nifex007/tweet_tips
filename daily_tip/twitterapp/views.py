from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from django.views import View
from twitterapp.utils import tweepy_api_auth
import pprint

# Create your views here.
class TwitterView(View):

    api = tweepy_api_auth()
    user_id = 'python_tip'

    def get(self, request):
        # get the last 200 tweets 
        return HttpResponse("<h2> Twitter </h2>")


class TwitterAuth(View):
    pass
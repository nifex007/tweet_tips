from django.shortcuts import render
from django.http import HttpResponse
import tweepy
from django.views import View

# Create your views here.
class TwitterView(View):
    def get(self, request):
        
        return HttpResponse("<h2> Twitter </h2>")


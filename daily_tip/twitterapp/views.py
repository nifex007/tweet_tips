from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
import tweepy
from django.views import View
from twitterapp.utils import tweepy_api_auth, format_response, get_twitter_login_url, \
                    get_tweet, get_timeline_tweets, extract_media_links, twitter_oauth, tweepy_api, \
                    redirect_to_login

from tips.models import Tips, Links
from twitterapp.models import TwitterAuthModel
from tips.utils import save_tip
import traceback

# Create your views here.
class TwitterView(View):

    api = tweepy_api_auth()
    user_id = 'python_tip'

    def get(self, request):
        api = self.api
        user = self.user_id
        twitter_login_url = 'http://{}/social/'.format(request.get_host())

        context = {'twitter_login_url': twitter_login_url}
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

        # get_twitter_login_url()


       



        return render(request, 'twitterapp/home.html', context)


class TwitterAuth(View):

    def get(self, request):
        # print("outh 1 ", request.GET.get('oauth_token', None))
        callback = 'http://127.0.0.1:8000/social/'

        oauth_token = request.GET.get('oauth_token', None)
        oauth_verifier = request.GET.get('oauth_verifier', None)

        if oauth_token and oauth_verifier:
            oauth = twitter_oauth(callback)
            # exchange token & verifier for user's access token
            oauth.request_token = {
                'oauth_token': oauth_token,
                'oauth_token_secret': oauth_verifier
            }

            oauth.get_access_token(oauth_verifier)
            
            # user's access token
            access_token = oauth.access_token

            # user's token secret
            access_token_secret = oauth.access_token_secret

            # get profile from twitter 
            api = tweepy_api(access_token, access_token_secret)
            profile = format_response(api.me())

            # check if handle exists (yes: redirect, no: create new)
            screen_name_exists = TwitterAuthModel.objects.filter(screen_name=profile['screen_name']).exists()
            if screen_name_exists: 
                user = TwitterAuthModel.objects.get(screen_name=profile['screen_name'])
                if user.is_authenticated:
                    request.session['screen_name'] = user.screen_name
                    request.session['signed_in']= True
                    return redirect('http://{}/tips/'.format(request.get_host()))
            else:
                # save in db
                t = TwitterAuthModel(screen_name=profile['screen_name'], access_token=access_token, access_token_secret=access_token_secret, is_authenticated=True)
                t.save()
                request.session['screen_name'] = t.screen_name
                request.session['signed_in'] = True
                return redirect('http://{}/tips/'.format(request.get_host()))
        
        else:
            signed_in = request.session.get('signed_in', False)
            if signed_in:
                return redirect('http://{}/tips/'.format(request.get_host()))
            else:
                login_url = get_twitter_login_url()
                return redirect(login_url)

            

        # login_url = get_twitter_login_url()
        # return redirect(login_url)

        return HttpResponse("<h2> Social Auth </h2>")
    


class Home(TemplateView):
    template_name="twitterapp/home.html"


class LogOut(View):

    def get(self, request):
        signed_in = request.session.get('signed_in', False) 
        screen_name = request.session.get('screen_name', None)

        if screen_name:
            t = TwitterAuthModel.objects.get(screen_name=screen_name)
            t.delete()
            del request.session['screen_name']

        if signed_in:
            del request.session['signed_in']

            return redirect('http://{}/'.format(request.get_host()))





    # delete credentials
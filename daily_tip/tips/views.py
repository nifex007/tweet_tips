from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView, View
from tips.models import Tips
from twitterapp.models import TwitterAuthModel
from twitterapp.utils import redirect_to_login, tweepy_api

# Create your views here.
class TipsView(ListView):
    

    
    def get(self, request):
        signed_in = request.session.get('signed_in', False)
        if not signed_in:
            return redirect('http://{}/'.format(request.get_host()))
        tips = Tips.objects.all().order_by('-likes', '-retweets')
        redirect_to_login(request,signed_in)
        context ={}

        p = Paginator(tips, 15)
        tips_count = len(tips)
        page_number = request.GET.get('page')
        host = request.get_host()
        context['page_obj'] = p.get_page(page_number)
        context['tips_count'] = tips_count
        context['tips'] = tips
        context['home_url'] = 'http://{}/logout'.format(host)
        context['retweet_url'] = 'http://{}/tips/retweet/'.format(host)


        return render(request, 'tips/tips_home.html', context)

    def post(self, request):
        signed_in = request.session.get('signed_in', False)
        if not signed_in:
            return redirect('http://{}/'.format(request.get_host()))

        search_word = request.POST.get('search')
        return redirect('http://{}/tips/{}'.format(request.get_host(),search_word))
       
class SearchView(ListView):

    def get(self, request, **kwargs):
        signed_in = request.session.get('signed_in', False)
        if not signed_in:
            return redirect('http://{}/'.format(request.get_host()))
        context = {}
        search_results = Tips.objects.filter(tip__search=kwargs['q'])
        p = Paginator(search_results, 15)
        page_number = request.GET.get('page')
        context['page_obj'] = p.get_page(page_number)
        search_count = len(search_results)
        context['search_count'] = search_count
        context['search_results'] = search_results

        return render(request, 'tips/tips_search.html', context)


class Retweet(View):
    
    def get(self, request, **kwargs):
        signed_in = request.session.get('signed_in', False)
        
        if not signed_in:
            return redirect('http://{}/'.format(request.get_host()))

        tweet_id = kwargs.get('tweet_id', None)
        screen_name = request.session.get('screen_name', None)
        if tweet_id and screen_name:
            tip = Tips.objects.get(id=tweet_id) 
            try:
                t = TwitterAuthModel.objects.get(screen_name=screen_name)
                api = tweepy_api(t.access_token, t.access_token_secret)
                tip = Tips.objects.get(id=tweet_id)
                if tip.retweeted:
                    api.unretweet(tweet_id) # undo retweet
                    tip.retweeted = False
                    tip.save()
                else:
                    api.retweet(tweet_id) # retweet
                    tip.retweeted = True
                    tip.save()
                    
            except BaseException as e:
                print("Exception: {}".format(e))

            
            return redirect('http://{}/tips'.format(request.get_host()))
        else:
            return redirect('http://{}/tips'.format(request.get_host()))






            



        



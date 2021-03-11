from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import ListView
from tips.models import Tips
from twitterapp.utils import redirect_to_login

# Create your views here.
class TipsView(ListView):
    all_tips =  Tips.objects.all().order_by('-likes', '-retweets')

    
    def get(self, request):
        signed_in = request.session.get('signed_in', False)
        if not signed_in:
            return redirect('http://{}/'.format(request.get_host()))
        
        redirect_to_login(request,signed_in)
        context ={}
        tips = self.all_tips

        p = Paginator(tips, 15)
        tips_count = len(tips)
        page_number = request.GET.get('page')
        context['page_obj'] = p.get_page(page_number)
        context['tips_count'] = tips_count
        context['tips'] = tips
        context['home_url'] = 'http://{}/logout'.format(request.get_host())

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

            




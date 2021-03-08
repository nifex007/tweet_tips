from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from tips.models import Tips

# Create your views here.
class TipsView(ListView):
    all_tips =  Tips.objects.all().order_by('-likes', '-retweets')

    
    def get(self, request):
        context ={}
        tips = self.all_tips

        p = Paginator(tips, 15)
        tips_count = len(tips)
        page_number = request.GET.get('page')
        context['page_obj'] = p.get_page(page_number)
        context['tips_count'] = tips_count
        context['tips'] = tips

        return render(request, 'tips/tips_home.html', context)
        
        
class SearchView(ListView):

    def get(self, request, **kwargs):
        context = {}
        search_results = Tips.objects.filter(tip__search=kwargs['q'])
        p = Paginator(search_results, 15)
        page_number = request.GET.get('page')
        context['page_obj'] = p.get_page(page_number)
        search_count = len(search_results)
        context['search_count'] = search_count
        context['search_results'] = search_results

        return render(request, 'tips/tips_search.html', context)

            




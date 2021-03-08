from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView
from tips.models import Tips

# Create your views here.
class TipsView(ListView):
    all_tips =  Tips.objects.all().order_by('-likes', '-retweets')

    # paginate_by = 10
    # model = Tips
    
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
        
        
        
            




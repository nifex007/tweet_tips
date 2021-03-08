from django.urls import path
from tips.views import TipsView, SearchView


urlpatterns = [
    path('',TipsView.as_view()),
    path('<q>', SearchView.as_view()),
]
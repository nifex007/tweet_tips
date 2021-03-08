from django.urls import path
from tips.views import TipsView


urlpatterns = [
    path('',TipsView.as_view()),
]
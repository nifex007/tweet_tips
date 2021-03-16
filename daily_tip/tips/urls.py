from django.urls import path
from tips.views import TipsView, SearchView, Retweet


urlpatterns = [
    path('',TipsView.as_view()),
    path("retweet/<tweet_id>", Retweet.as_view(), name="retweet"),
    path('<q>', SearchView.as_view()),
]
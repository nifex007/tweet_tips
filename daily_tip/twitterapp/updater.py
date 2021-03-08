from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from twitterapp.utils import get_timeline_tweets


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_timeline_tweets, 'interval', seconds=30)
    scheduler.start()

from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from twitterapp.utils import get_timeline_tweets
from tips.utils import process


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(process, 'interval', seconds=40)
    scheduler.start()

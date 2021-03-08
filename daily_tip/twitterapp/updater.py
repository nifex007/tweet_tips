from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from twitterapp.utils import get_timeline_tweets


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get_timeline_tweets, 'interval', seconds=1)
    scheduler.start()


# import logging

# from apscheduler.schedulers.sync import SyncScheduler
# from apscheduler.triggers.interval import IntervalTrigger
# from apscheduler.workers.sync import SyncWorker


# def say_hello():
#     print('Hello!')


# def start():
#     logging.basicConfig(level=logging.DEBUG)
#     try:
#         with SyncScheduler() as scheduler, SyncWorker(scheduler.data_store, portal=scheduler.portal):
#             scheduler.add_schedule(say_hello, IntervalTrigger(seconds=1))
#             scheduler.wait_until_stopped()
#     except (KeyboardInterrupt, SystemExit):
#         pass
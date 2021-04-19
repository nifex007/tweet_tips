from django.db.models import Max
from tips.models import Tips, Links
from dateutil.parser import parse
import datetime 
from tips.models import Tips
from twitterapp.utils import extract_media_links, get_timeline_tweets
import traceback



def convert_time(date_string):
    date_ = parse(date_string)
    return date_


def save_tip(tweet):
    """
    Write tip to database
    """
    try:
        text = tweet['full_text']
    except BaseException as e:
        print("Exception {}".format(e))
        traceback.print_exc()
        text = tweet['text']

    try:
        t = Tips(id=tweet['id'],
            tip=text,
            author=tweet['user']['screen_name'],
            timestamp=convert_time(tweet['created_at']),
            likes=tweet['favorite_count'],
            retweets=tweet['retweet_count']
            )

        t.save()

        has_links, links_dict = extract_media_links(tweet)
        if has_links:
            save_links(links_dict, t)
        
        return 'Tip Saved'
    except BaseException as e:
        print("Exception {}".format(e))
        traceback.print_exc()
        return 'Tip not saved'


def save_links(links_dict, tip):

    # {'id': 1356937628566880260,
    # 'links': ['https://pbs.twimg.com/media/EtTO-UfWgAM3SNZ.png']
    # }
    try:
        id = links_dict['id']
        links = links_dict['links']

        for link in links:
            l = Links(tip=tip, link=link)
            l.save()
        return "Links saved"
    except BaseException as e:
        print('Exception occured: {}'.format(e))
        traceback.print_exc()
        return "Link not saved :("


def process():
    screen_name = 'python_tip'
    last_tip = Tips.objects.last()
    last_tip_id = None
    since_id = None
    max_id = None
    try:
        last_tip_id = last_tip.id
        t = Tips.objects.aggregate(Max('id'))
        since_id = t['id__max']
    except BaseException as e:
        print("Exception {}".format(e))
        traceback.print_exc()
    # get tweets since the last in the db
    timeline_tweets = get_timeline_tweets(screen_name, since_id, max_id) 
    
    if len(timeline_tweets) > 0:
        print("process ", timeline_tweets)
    # save tweets in database
        for tip in timeline_tweets:
            save_tip(tip)
    else: # No recent tweets
        print("process: No tips to save to DB !" )


















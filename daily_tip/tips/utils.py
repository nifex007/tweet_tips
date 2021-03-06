from tips.models import Tips, Links
from dateutil.parser import parse
import datetime 
from twitterapp.utils import extract_media_links
import traceback

def convert_time(date_string):
    date_ = parse(date_string)
    return date_


def save_tip(tweet):
    """
    Write tip to datbase
    """
    try:
        t = Tips(id=tweet['id'],
            tip=tweet['text'],
            author=tweet['user']['screen_name'],
            timestamp=convert_time(tweet['created_at'])
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
















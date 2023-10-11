import random
import time
from datetime import datetime


FILE_NAME_NEW_LINK = './data/possible_new_video_link.txt'
FILE_NAME_LINK_TO_COMMENT = './data/video_link_to_comment.txt'
FILE_NAME_COMMENTED_LINK = './data/commented_video_link.txt'
FILE_NAME_COMMENT_TEXT = './data/comment_description.txt'
FILE_NAME_CANAL_LINK_TO_EXPLORE = './data/canal_link_to_explore.txt'

URL_SING_IN = 'https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com'

EMAIL_MICANAL = 'micanal1119'
EMAIL_DAYANA1989 = 'dayana.sanz1989'
PASSWORD_MICANAL = ''

URL_SEARCH_QUERY = 'https://www.youtube.com/results?search_query='

CANAL_NAME = ('ZMusical', 'Z Musical')
CANAL_LINK = 'https://www.youtube.com/channel/UCSOXYurvA9cUM3wf1LkAJag'

URL_YOUTUBE = 'https://www.youtube.com/'


def sleep_random(first=300, last=600):
    sleep_on_canal = random.randint(first, last)
    time.sleep(sleep_on_canal)


def print_time(message):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(message, current_time)
    return now

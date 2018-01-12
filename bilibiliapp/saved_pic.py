import os
import sys
import django

pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bilibili_app_server.settings")

django.setup()

import requests
from _datetime import datetime
from bilibiliapp.models import BilibiliApp

url = 'http://app.bilibili.com/x/splash?plat=0&width=1080&height=1920'

r = requests.get(url)


def unix_time_to_normal(time):
    return datetime.fromtimestamp(int(time)).strftime('%Y-%m-%d %H:%M:%S')


if r.status_code == 200:
    data_json = r.json()
    print(data_json)

    code = data_json['code']
    if code == 0:
        data_list = data_json['data']

        for i in data_list:
            start_time = unix_time_to_normal(i['start_time'])
            end_time = unix_time_to_normal(i['end_time'])

            pic_obj = BilibiliApp.objects.update_or_create(pic_id=i['id'], img_url=i['image'],
                                                           start_time=start_time, end_time=end_time)

            print(BilibiliApp.objects.get(pic_id=i['id']).to_json())

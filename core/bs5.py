import base64
import os
import django
import requests

from bs4 import BeautifulSoup
from django.db import models
from .models import News

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")

django.setup()

url = requests.get('https://turkmenportal.com/tm/rss/')
soup = BeautifulSoup(url.content, 'xml')
entries = soup.findAll('item')
source = 'https://turkmenportal.com/'
rss = 'https://turkmenportal.com/tm/rss/'

for entry in entries:
    # for media_content in entry.find_all_next('media:content'):
    title = entry.title
    pub_date = entry.pub_date
    link = entry.link
    description = entry.description
    content = entry.content
    enclosure = entry.enclosure['url']
    if enclosure:
        img = requests.get(enclosure)
        encoded_string = base64.b64encode(img.content)
        thumbnail = encoded_string

        news_create = News.objects.create(source=source, rss_feed=rss, title_en=title, title_ru=title, title_tm=title,
                                                      pub_date=pub_date, link=link, description=description,
                                                      content=content, image=encoded_string, thumbnail=encoded_string)
        news_create.save()

        # f.write(encoded_string.decode('utf-8') + "\n")
        # f.write("----------------------------------------------\n\n")

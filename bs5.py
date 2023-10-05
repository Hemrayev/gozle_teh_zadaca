import base64
import os
import django
from dateutil.parser import parse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")
django.setup()

import requests
from core.models import News
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = requests.get('https://turkmenportal.com/tm/rss/')
    soup = BeautifulSoup(url.content, 'xml')
    entries = soup.findAll('item')
    source = 'https://turkmenportal.com/'
    rss = 'https://turkmenportal.com/tm/rss/'

    for entry in entries:
        for media_content in entry.find_all_next('content:encoded'):
            content = media_content.text

        title = entry.title.text
        pub_date = entry.pubDate
        parsed_date = parse(pub_date.text.strip())
        link = entry.link.text
        description = entry.description.text

        enclosure = entry.enclosure['url']
        if enclosure:
            img = requests.get(enclosure)
            encoded_string = base64.b64encode(img.content)
            thumbnail = encoded_string

            try:
                news_create = News.objects.create(source=source, rss_feed=rss, title=title, description=description,
                                                  content=content, image=encoded_string, thumbnail=encoded_string,
                                                  pub_date=parsed_date, link=link)
            except Exception as e:
                print(e)
                print(source, rss, title, description, content, parsed_date, link)

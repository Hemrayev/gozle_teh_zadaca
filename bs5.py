import base64
import os
import django
import requests
import feedparser
import pandas as pd
from bs4 import BeautifulSoup
from dateutil.parser import parse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")
django.setup()

from core.models import News, Rss


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


if __name__ == '__main__':
    for item in Rss.objects.all():
        dp = feedparser.parse(item.name_tk)
        dp1 = feedparser.parse(item.name_en)
        dp2 = feedparser.parse(item.name_ru)

        for i,i1,i2, e, e1, e2 in enumerate(dp.entries), enumerate(dp1.entries), enumerate(dp2.entries):

            d = find_between(e.summary, 'src="', '"')

            one_feed = {'etitle': e.title if 'title' in e else f'title {i}',
                        'summary': e.summary if 'summary' in e else f'no summary {i}',
                        'elink': e.link if 'link' in e else f'link {i}',
                        'published': e.published if 'published' in e else f'no published {i}',
                        'category': [t.get('term') for t in e.tags] if 'category' in e else f'no categories {i}',
                        'elink_img': e.links[1].href or image if 'links' in e and len(
                            e.links) > 1 else f'no link_img {i}'}

            if one_feed['elink_img'] == f'no link_img {i}' and d != "":
                one_feed['elink_img'] = d

        # for i, e in enumerate(dp1.entries):
        #     one_feed += {
        #         'etitle_en': e.title if 'title' in e else f'title {i}',
        #         'category_en': [t.get('term') for t in e.tags] if 'category' in e else f'no categories {i}',
        #         'summary_en': e.summary if 'summary' in e else f'no summary {i}',
        #     }
        #
        # for i, e in enumerate(dp2.entries):
        #     one_feed += {
        #         'etitle_ru': e.title if 'title' in e else f'title {i}',
        #         'category_ru': [t.get('term') for t in e.tags] if 'category' in e else f'no categories {i}',
        #         'summary_ru': e.summary if 'summary' in e else f'no summary {i}',
        #     }
        #
        # for feeds in one_feed:
        #     print(f'{feeds}\n')

    # for item in Rss.objects.all():
    # url = requests.get('https://turkmenportal.com/tm/rss/')
    # soup = BeautifulSoup(url.content, 'xml')
    # entries = soup.findAll('item')
    # source = 'https://turkmenportal.com/'
    # rss = 'https://turkmenportal.com/tm/rss/'
    #
    # for entry in entries:
    #     for media_content in entry.find_all_next('content:encoded'):
    #         content = media_content.text
    #
    #     title = entry.title.text
    #     pub_date = entry.pubDate
    #     print(type(pub_date))
    #     parsed_date = parse(pub_date.text.strip())
    # #     link = entry.link.text
    #     description = entry.description.text
    #
    #     enclosure = entry.enclosure['url']
    #     if enclosure:
    #         img = requests.get(enclosure)
    #         encoded_string = base64.b64encode(img.content)
    #         thumbnail = encoded_string
    #
    #         try:
    #             news_create = News.objects.create(source=source, rss_feed=rss, title=title, description=description,
    #                                               content=content, image=encoded_string, thumbnail=encoded_string,
    #                                               pub_date=parsed_date, link=link)
    #         except Exception as e:
    #             print(e)
    #             print(source, rss, title, description, content, parsed_date, link)

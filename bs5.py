import base64
import os
import django
import requests
import feedparser
from dateutil.parser import parse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")
django.setup()

from core.models import News, Rss, NewsEnglish, NewsRussian


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def get_values(i, e):
        massiw = []
        d = find_between(e.summary, 'src="', '"')
        one_feed = {'etitle': e.title if 'title' in e else f'title {i}',
                    'summary': e.summary if 'summary' in e else f'no summary {i}',
                    'elink': e.link if 'link' in e else f'link {i}',
                    'published': e.published if 'published' in e else f'no published {i}',
                    # 'category': [t.get('term') for t in e.tags] if 'category' in e else f'no categories {i}',
                    'elink_img': e.links[1].href or image if 'links' in e and len(
                        e.links) > 1 else f'no link_img {i}'}

        if one_feed['elink_img'] == f'no link_img {i}' and d != "":
            one_feed['elink_img'] = d

        if one_feed['elink_img'] != f'no link_img {i}':
            img = requests.get(one_feed['elink_img'])
            encoded_string = base64.b64encode(img.content)
            encoded_string = encoded_string.decode('utf-8')
            one_feed['published'] = parse(one_feed['published'])

            massiw.append(one_feed['etitle'])
            massiw.append(one_feed['summary'])
            massiw.append(one_feed['elink'])
            massiw.append(one_feed['published'])
            massiw.append(encoded_string)

            return massiw


if __name__ == '__main__':

    for item in Rss.objects.all():
        dp = feedparser.parse(item.name_tk)
        dp1 = feedparser.parse(item.name_en)
        dp2 = feedparser.parse(item.name_ru)

        for i, e in enumerate(dp.entries):
            value = get_values(i, e)
            News.objects.create(title=value[0], content=value[1], link=value[2],rss_feed_id=item.id, pub_date=value[3],
                                image=value[4])

        for i, e in enumerate(dp1.entries):
            value = get_values(i, e)
            NewsEnglish.objects.create(title=value[0], content=value[1], link=value[2], rss_feed_id=item.id, pub_date=value[3],
                                image=value[4])

        for i, e in enumerate(dp2.entries):
            value = get_values(i, e)
            NewsRussian.objects.create(title=value[0], content=value[1], link=value[2], rss_feed_id=item.id,
                                       pub_date=value[3],
                                       image=value[4])

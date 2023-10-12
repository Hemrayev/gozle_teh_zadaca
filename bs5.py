import base64
import os
import django
import requests
import feedparser
from dateutil.parser import parse

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "parser.settings")
django.setup()

from core.models import *


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


def get_values(index, entries):

    d = find_between(entries.summary, 'src="', '"')

    one_feed = {'etitle': entries.title if 'title' in entries else f'title {index}',
                'summary': entries.summary if 'summary' in entries else f'no summary {index}',
                'elink': entries.link if 'link' in entries else f'link {index}',
                'published': entries.published if 'published' in entries else "",
                'category': [t.get('term') for t in
                             entries.tags] if 'category' in entries else f'no categories {index}',
                'elink_img': entries.links[1].href or image if 'links' in entries and len(
                    entries.links) > 1 else f'no link_img {index}'}

    if one_feed['elink_img'] == f'no link_img {index}' and d != "":
        one_feed['elink_img'] = d

    if one_feed['elink_img'] != f'no link_img {index}':
        img = requests.get(one_feed['elink_img'])
        encoded_string = base64.b64encode(img.content)
        encoded_string = encoded_string.decode('utf-8')
        one_feed['elink_img'] = encoded_string
        one_feed['published'] = parse(one_feed['published'])

        return one_feed


if __name__ == '__main__':

    for item in Rss.objects.all():
        dp = 0
        dp1 = 0
        dp2 = 0
        if item.name_tk:
            dp = feedparser.parse(item.name_tk)
        if item.name_en:
            dp1 = feedparser.parse(item.name_en)
        if item.name_ru:
            dp2 = feedparser.parse(item.name_ru)

        for i, entry in enumerate(dp.entries):
            value = get_values(i, entry)
            try:
                dj = News.objects.create(title=value['etitle'], content=value['summary'], link=value['elink'],
                                         rss_feed_id=item.id, pub_date=value['published'], image=value['elink_img'],
                                         source=item.source,
                                         )
                if value['category'] != "":
                    for term in value['category']:
                        obj, category = CategoryTk.objects.get_or_create(name=term)
                        dj.category_tk.add(obj.id)
                        dj.save()
                dj.save()
            except:
                pass

        for i, entry in enumerate(dp1.entries):
            value = get_values(i, entry)
            try:
                dj = NewsEnglish.objects.create(title=value['etitle'], content=value['summary'], link=value['elink'],
                                         rss_feed_id=item.id, pub_date=value['published'], image=value['elink_img'],
                                         source=item.source,
                                         )
                if value['category'] != "":
                    for term in value['category']:
                        obj, category = CategoryEn.objects.get_or_create(name=term)
                        dj.category_en.add(obj.id)
                        dj.save()
                dj.save()
            except:
                pass

        for i, entry in enumerate(dp2.entries):
            value = get_values(i, entry)
            try:
                dj = NewsRussian.objects.create(title=value['etitle'], content=value['summary'], link=value['elink'],
                                                rss_feed_id=item.id, pub_date=value['published'],
                                                image=value['elink_img'],
                                                source=item.source,
                                                )
                if value['category'] != "":
                    for term in value['category']:
                        obj, category = CategoryRu.objects.get_or_create(name=term)
                        dj.category_ru.add(obj.id)
                        dj.save()
                dj.save()
            except:
                pass

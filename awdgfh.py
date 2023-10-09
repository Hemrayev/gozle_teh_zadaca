import feedparser
import pandas as pd


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


rawrss = [
    'https://ahal.info/tm/rss',
    'https://orient.tm/tm/rss',
    'https://ashgabat.in/feed/',
    'https://turkmenportal.com/rss/',
]

df = pd.DataFrame([])

for url in rawrss:
    dp = feedparser.parse(url)

    for i, e in enumerate(dp.entries):
        # print(urllib.parse.quote_plus(find_between(e.description, 'src="', '"')))
        # print(find_between(e.summary, 'src="', '"'))
        d = find_between(e.summary, 'src="', '"')
        print(e)
        one_feed = {'etitle': e.title if 'title' in e else f'title {i}',
                    'summary': e.summary if 'summary' in e else f'no summary {i}',
                    'elink': e.link if 'link' in e else f'link {i}',
                    'published': e.published if 'published' in e else f'no published {i}',
                    'category': [t.get('term') for t in e.tags] if 'category' in e else f'no categories {i}',
                    'elink_img': e.links[1].href or image if 'links' in e and len(e.links) > 1  else f'no link_img {i}'}

        # df = df.append(pd.DataFrame([one_feed]), ignore_index=True)
        if one_feed['elink_img'] == f'no link_img {i}' and d!="":
            one_feed['elink_img'] = d
        print(one_feed['elink_img'], f'->{url} \n')

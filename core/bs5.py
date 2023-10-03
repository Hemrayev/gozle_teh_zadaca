import base64

from bs4 import BeautifulSoup

import requests

url = requests.get('https://turkmenportal.com/tm/rss/')
soup = BeautifulSoup(url.content, 'xml')
entries = soup.findAll('item')

with open("test.txt", "w") as f:
    for entry in entries:
        for media_content in entry.find_all_next('media:content'):
            print(media_content['url'])
        title = entry.title
        link = entry.link
        summary = entry.enclosure['url']
        img = requests.get(summary)
        encoded_string = base64.b64encode(img.content)
        f.write(encoded_string.decode('utf-8') + "\n")
        f.write("----------------------------------------------\n\n")

import requests
from bs4 import BeautifulSoup


class trustedsource(object):

    def __init__(self):
        self.url = input('Enter a valid domain / url to check: ')

    def setup(self):
        headers = {
        'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5)',
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language' : 'en-US,en;q=0.9,de;q=0.8'
        }
        base_url = 'http://www.trustedsource.org/sources/index.pl'
        r = requests.get(base_url, headers=headers)
        bs = BeautifulSoup(r.content, "html.parser")
        form = bs.find("form", {"class" : "contactForm" })
        token1 = form.find("input", {'name': 'e'}).get('value')
        token2 = form.find("input", {'name': 'c'}).get('value')
        headers['Referer'] = base_url
        return headers, token1, token2

    def lookup(self, data):
        headers, token1, token2 = data
        payload = {'e': (None, token1),
                   'c': (None, token2),
                   'action': (None,'checksingle'),
                   'product': (None,'01-ts'),
                   'url': (None, self.url)}
        r = requests.post('https://www.trustedsource.org/en/feedback/url', headers=headers, files=payload)
        bs = BeautifulSoup(r.content, "html.parser")
        form = bs.find("form", { "class" : "contactForm" })
        table = bs.find("table", { "class" : "result-table" })
        td = table.find_all('td')
        categorized = td[len(td)-3].text
        category = td[len(td)-2].text[2:]
        risk = td[len(td)-1].text
        return '\033[1m' + 'Staus: {0}     |     Category: {1}     |     Risk: {2}'.format(categorized, category, risk) + '\033[0m'



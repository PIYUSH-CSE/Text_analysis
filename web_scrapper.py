import os

import requests
from bs4 import BeautifulSoup


class WebScrapper:

    def scrap(self, url, id):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
        }
        html_content = requests.get(url, headers=headers).text

        htmlParse = BeautifulSoup(html_content, 'html.parser')

        if os.path.isfile(r'./text files/' + str(id) + '.txt'):
            os.remove(r'./text files/' + str(id) + '.txt')
        htmlParse = BeautifulSoup(html_content, 'html.parser')
        for para in htmlParse.find_all("p"):
            extracted_text = para.get_text().encode(encoding = 'ascii', errors = 'ignore')
            with open('{}.txt'.format(r'./text files/' + str(id)), 'a+') as f:
                f.write(extracted_text.decode())
        if os.path.isfile(r'./text files/' + str(id) + '.txt'):
            return True
        else:
            return False

## -*- coding: utf-8 -*-

# from urllib import request
from urllib.request import Request, urlopen
import requests

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/51.0.2704.63 Safari/537.36'}
        r = requests.get(url,headers=headers)
        webpage = r.text
        return webpage
        # response = response.decode('utf-8')
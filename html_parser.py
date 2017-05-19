## -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.parse
import  requests

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.html
        links = soup.findAll('a', href=re.compile(r'/month/.*?/$')) # 不是html
        for link in links:
            new_url = link['href']
            # 让 new_url 以 page_url 为模板拼接成一个全新的 url
            new_full_url = 'http://www.baidu.com' + new_url
            #print(new_url) # /view/10812319.htm
            #print(new_full_url) # http://baike.baidu.com/view/10812319.htm
            new_urls.add(new_full_url)
        return new_urls


    def _get_second_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.html
        links = soup.findAll('a', href=re.compile(r'/view/.*?/$'))  # 不是html
        for link in links:
            new_url = link['href']
            # 让 new_url 以 page_url 为模板拼接成一个全新的 url
            new_full_url = 'http://www.baidu.com' + new_url
            #print(new_url) # /view/10812319.htm
            #print(new_full_url) # http://baike.baidu.com/view/10812319.htm
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        try:
            links =  soup.findAll('a',href = re.compile(r'file.php?.*?$'))
            name = soup.find('div',class_='content-container').h3.p.string
            for link in links:
                new_url = link['href']
                # 让 new_url 以 page_url 为模板拼接成一个全新的 url
                new_full_url = 'http://www.141jav.com' + new_url
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                         'Chrome/51.0.2704.63 Safari/537.36'}
                r = requests.get(new_full_url, headers=headers)
                file = r.content
                fp = open('D:/BeyondGoodandEvil/'+name +'.torrent','wb')
                fp.write(file)
                fp.close()
                return 'y'
            return 'n'
        except:
            return 'e'

    def paser_data(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding = 'utf-8')
        isData = self._get_new_data(page_url, soup)
        return isData

    def paser_first_urls(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        return new_urls

    def paser_second_urls(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_second_urls(page_url, soup)
        return new_urls

# python3对urllib和urllib2进行了重构，
# 拆分成了urllib.request, urllib.response, urllib.parse, urllib.error等几个子模块，
# urljoin现在对应的函数是urllib.parse.urljoin
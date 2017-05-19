## -*- coding: utf-8 -*-
# from baike_spider import url_manager, html_downloader, html_parser, html_outputer

import url_manager
import html_downloader
import html_parser
#import html_outputer

class SpiderMain(object):
    # 爬虫总调度程序会使用 url 管理器、 html 的下载器、解析器、输出器，下面初始化一下：
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.download = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        #self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url): # craw 方法，爬虫调度程序
        count = 1
        mode = 1
        # 入口 url 添加到 url 管理器
        self.urls.add_new_url(root_url)

        # 启动爬虫循环
        # 当 url 管理器里待爬取的 url 时，获取一个 url
        new_url = self.urls.get_new_url()
        print('craw %d : %s' % (count, new_url)) # 打印传入的第几个 url
        # 启动下载器并存储
        html_cont = self.download.download(new_url)
        # 解析数据
        new_urls = self.parser.paser_first_urls(new_url, html_cont)
        # 添加进 url 管理器
        self.urls.add_new_urls(new_urls)

        number = self.urls.count_new_url()
        while number > 0:
            try:
                # 当 url 管理器里待爬取的 url 时，获取一个 url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))  # 打印传入的第几个 url
                # 启动下载器并存储
                html_cont = self.download.download(new_url)
                # 解析数据
                new_urls = self.parser.paser_second_urls(new_url, html_cont)
                # 添加进 url 管理器
                self.urls.add_new_urls(new_urls)
                number = number - 1
            except:
                print('crew faild:')

        while self.urls.count_new_url() !=0 :
            # try:
                # 当 url 管理器里待爬取的 url 时，获取一个 url
                new_url = self.urls.get_new_url()
                print('craw %d : %s' % (count, new_url))  # 打印传入的第几个 url
                # 启动下载器并存储
                html_cont = self.download.download(new_url)
                # 解析数据
                isData = self.parser.paser_data(new_url, html_cont)
                if isData == 'y':
                    print('small movie: '+new_url+' download successfully!\n')
                elif isData == 'n':
                    print('small movie: '+new_url+' download failed!\n')
                elif isData == 'e':
                    print('we meet Yahoo!!\n')
            # except:
            #     print('crew faild:')


if __name__ == "__main__":
    root_url = 'http://www.baidu.com'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url) # 启动爬虫
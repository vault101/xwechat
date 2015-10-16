#!/usr/bin/env python
# encoding=utf-8
import re
import time
import urllib

import requests

from bs4 import BeautifulSoup

unix_time_stamp_2_time_str = lambda stamp: time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(long(stamp[0])))


class WechatCrawler(object):
    SEARCH_URL = 'http://weixin.sogou.com/weixin?type={type}&query=%22{key}%22&page={page}'
    GZH_CLASS = 'wx-rb bg-blue wx-rb_v1 _item'
    ARTICLE_CLASS = 'wx-rb wx-rb3'
    PATTERN_NUMBER = re.compile(ur"\('(\d+?)'\)")

    def __init__(self):
        self.request = requests.Session()
        self.request.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        self.request.headers['Accept-Language'] = 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
        self.request.headers['Connection'] = 'keep-alive'
        self.request.headers[
            'Cookie'] = 'ABTEST=7|1444830669|v1; SUID=9DCA808A6A20900A00000000561E5DCD; SUID=9DCA808A2524920A00000000561E5DCF; SUV=00B370CD8A80CA9D561E5DCFEA682943; weixinIndexVisited=1; SNUID=4E1E535ED3D6F6C5DE296604D46D53B6; IPLOC=CN5000; sct=4; wapsogou_qq_nickname='
        self.request.headers[
            'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

    def _get(self, url, deep=0):
        if deep == 3:
            return None
        try:
            return self.request.get(url).content
        except Exception, e:
            return self._get(url, deep + 1)

    def find_302_location(self, url):
        try:
            return self.request.get(url, allow_redirects=False).headers['location']
        except:
            try:
                return self.request.get(url, allow_redirects=False).headers['Location']
            except:
                return url

    @classmethod
    def _parse_gzh(cls, div):
        try:
            img = div.find('div', attrs={'class': 'img-box'}).find('img')['src']
        except Exception, e:
            print e
            img = ''
        try:
            qr_img = div.find('div', attrs={'class': 'pos-ico'}).find('img')['src']
        except Exception, e:
            print e
            qr_img = ''
        try:
            detail = div.find('div', attrs={'class': 'txt-box'})
            result = {
                'logo': img, 'qr_img': qr_img,
                'nickname': detail.find('h3').getText().strip(),
                'account': detail.find('h4').getText().replace(u'微信号：', '').strip(),
                'description': detail.find('span', attrs={'class': 'sp-txt'}).getText().strip(),
                'href': div['href']
            }
            return result
        except Exception, e:
            print e
        return None

    def _parse_article(self, div):
        try:
            title = div.find('h4')
            footer = div.find('div', attrs={'class': 's-p'})
            result = {
                'title': title.getText().strip(),
                'url': title.find('a')['href'].strip(),
                'source': footer.find('a', attrs={'id': 'weixin_account'})['title'],
                'time': unix_time_stamp_2_time_str(self.PATTERN_NUMBER.findall(footer.find_all('script')[-1].getText())),
                'abstract': div.find('p').getText(),
                'content': ''
            }
            if result['url'].startswith('/'):
                result['url'] = self.find_302_location('http://weixin.sogou.com' + result['url'])
            return result
        except Exception, e:
            print e
            return None

    def _crawl_article(self, key, page):
        try:
            soup = BeautifulSoup(self._get(self.SEARCH_URL.format(type='2', key=key, page=page)), "html.parser")
            lst = [self._parse_article(item) for item in soup.find_all('div', attrs={'class': self.ARTICLE_CLASS})]
            return filter(lambda x: x, lst)
        except Exception, e:
            print e
            return None

    def _crawl_gzh(self, key, page):
        try:
            soup = BeautifulSoup(self._get(self.SEARCH_URL.format(type='1', key=key, page=page)), "html.parser")
            lst = [self._parse_gzh(item) for item in soup.find_all('div', attrs={'class': self.GZH_CLASS})]
            return filter(lambda x: x, lst)
        except Exception, e:
            print e
            return None

    def crawl(self, key, page=1):
        key = urllib.quote(key.encode('gbk'))
        return [self._crawl_article(key, page), self._crawl_gzh(key, page)]


CRAWLER = WechatCrawler()


def crawl(key):
    return CRAWLER.crawl(key)

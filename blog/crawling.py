#!/usr/bin/env python

# builtin module
from datetime import datetime

# pip install module
import requests
from bs4 import BeautifulSoup

# user defined module


class Crawling(object):

    def __init__(self, url):
        self.url = url

    def get_html(self):
        _html = ""
        resp = requests.get(self.url)
        if resp.status_code == 200:
            _html = resp.text
        return _html

    def parse_html(self, html):
        """
        입력받은 마음의 소리 웹툰 페이지 html에서 마음의소리의 회차, 제목 url을 추출하여
        tuple로 만들고, 리스트에 갯수대로 저장하여 반환한다
        :param html: string
        :return: 마음의 소리 정보가 담긴 리스트
        """
        webtoon_list = list()
        soup = BeautifulSoup(html, 'html.parser')
        webtoon_area = soup.find("tbody", {"class": "hide_notice"}).find_all("td", {"class":"title"})
        for webtoon_index in webtoon_area:
            info_soup = webtoon_index.find("a")

            _url = info_soup["href"]
            _text = info_soup.text
            _title = _text;

            _num = webtoon_index.find("a", {"class": "replyNum"})
            #_title  = ""
            #_num = _text[0]
            #if len(_text) > 1:
            #	_title = _text[1]

            webtoon_list.append((_num, _title, _url, ))

        for titles in webtoon_list :
            print(titles)
        return webtoon_list



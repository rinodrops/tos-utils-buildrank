# coding: UTF-8

# iToS Class Build Ranking

# pip install: beautifulsoup4 selenium python-dateutil
# brew cask install chromedriver

from bs4 import BeautifulSoup
from collections import OrderedDict
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get():
    # run as headless mode
    options = Options()
    options.set_headless(True)

    # initiate browser
    driver = webdriver.Chrome(chrome_options=options)

    # obtain html, wait until ajax stuff finishes
    driver.get("https://treeofsavior.com/page/class/ranking.php")
    time.sleep(5)
    html = driver.page_source.encode('utf-8')

    # parse by BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # last updated
    classbuild_date_text = soup.select_one('#classbuild_date').text
    classbuild_date = re.search(r'Last updated : (.*)', classbuild_date_text).group(1)

    # title
    title = soup.select_one('#classbuild_title').text

    # ranking
    ranking = []
    for rank in soup.select('div.rank'):
        # rank number
        rank_number = rank.select_one('p.rank_number')

        # up down same
        updown = rank.select_one('p.rank_number + span')
        rank_updown = updown['class'][0]
        rank_updown_number = int(updown.text) if rank_updown == 'up' or rank_updown == 'down' else 0

        # class tree
        class_tree = rank.select_one('li.rank_first + li').text

        # class build
        class_build = OrderedDict()
        build = rank.select_one('ul.classbuild')
        for li in build.select('li'):
            class_name = li.select_one('p.class_name').text
            class_circle = 0
            for class_star in li.select_one('p.circle_star').select('img'):
                if 'star_on' in class_star['src']: class_circle += 1 
            class_build[class_name] = class_circle

        ranking.append([rank_number.text, rank_updown, rank_updown_number, class_tree, class_build])

    return (classbuild_date, title, ranking)

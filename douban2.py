import requests
import json
import time
import re
from bs4 import BeautifulSoup as bs
import random

def getComment(url,title,cast):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }
    cookies = {
        'cookie': 'bid=LoW-gcbNw4s; gr_user_id=89963d41-6d51-4aa6-80a5-2ea3b589188e; _vwo_uuid_v2=D79228CDBBAEE6BC0D96FF7E6E4BFD918|03ccdfcc181f1981879f36ec34eed339; __utmz=30149280.1528873027.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap=1; ps=y; ll="108288"; viewed="5414391_26986954_26958126_3360807_1103015"; __yadk_uid=96fRnsrWV5DjWpq8rcL8J4Qn6mtVS6ho; ct=y; loc-last-index-location-id="108288"; ue="544286175@qq.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.4939; _ga=GA1.2.1103338133.1528706829; _gid=GA1.2.267322816.1529983325; __utma=30149280.1103338133.1528706829.1530003046.1530010656.23; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1530010658%2C%22https%3A%2F%2Fwww.douban.com%2Fgallery%2Fall%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.154466763.1528883281.1529995298.1530010658.9; __utmb=223695111.0.10.1530010658; __utmz=223695111.1530010658.9.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/gallery/all; gr_cs1_f3af2095-d9cd-4996-93f3-56acf271a052=user_id%3A0; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=f3af2095-d9cd-4996-93f3-56acf271a052_true; __utmc=30149280; __utmt=1; _gat_UA-7019765-1=1; dbcl2="49393504:/XCjx2JQw2o"; ck=Y1-s; __utmb=30149280.7.10.1530010656; __utmc=223695111; _pk_id.100001.4cf6=3513548a83660639.1528883281.9.1530012790.1529995298.'
    }
    page = requests.get(url, cookies=cookies, headers=headers)
    soup = bs(page.text, "lxml")
    print(title)
    comment = soup.find_all(class_="comment")
    for c in comment:
        with open("豆瓣.txt", "a+", encoding="utf-8") as f:
            f.write("问题：" + title + " " + cast + '\n')
            f.write('回复：' + c.find("p").text + '\n')
            f.close()


for a in range(490):
    url_visit = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start={}'.format(a*20)
    file = requests.get(url_visit).json()   #这里跟之前的不一样，因为返回的是 json 文件
    time.sleep(random.random(2, 3))

    for i in range(20):
        dict=file['data'][i]   #取出字典中 'data' 下第 [i] 部电影的信息
        title=dict['title']
        rate=dict['rate']
        cast=dict['casts']
        cast_str = " ".join(cast)
        urlname=dict['url']
        time.sleep(random.random(1, 2))
        getComment(urlname, title, cast_str)

#coding=GBK
__author__ = 'jianyeliu'
import requests
import json
import bs4
from functools32 import lru_cache

def get_good_movies(threshold):

    return [(movie,get_average(movie)) for movie in get_movie_names() if(get_average(movie)>threshold)]
@lru_cache(maxsize=None)
def get_average(movie):
    response = requests.get('http://api.douban.com/v2/movie/search?q='+movie)
    movie_result = json.loads(response.text)
    score = movie_result['subjects'][0]['rating']['average'];
    return score

def get_movie_names():
    response = requests.get('http://www.ygdy8.net/html/gndy/dyzz/index.html')
    response.encoding = 'gbk'
    soup = bs4.BeautifulSoup(response.text,'html.parser')

    lines =[b.a.string for b in soup.find_all('b')]
    return [line[line.find("《".decode("gbk"))+1:line.find("》".decode("gbk"))] for line in lines]

for movie,score in get_good_movies(7):
    print movie,score
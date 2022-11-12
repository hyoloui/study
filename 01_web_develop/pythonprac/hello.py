import requests
from bs4 import BeautifulSoup

# MongoDB 연결!
from pymongo import MongoClient
client = MongoClient(
    'mongodb+srv://tmdgy9272:dltmdgy1@cluster0.ey8kvzl.mongodb.net/?retryWrites=true&w=majority')
db = client.tmdgy9272

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies:
    a = movie.select_one('td.title > div > a')
    if a is not None:
        title = a.text
        rank = movie.select_one('td > img')['alt']
        star = movie.select_one('td.point').text
        doc = {
            'rank': rank,
            'title': title,
            'star': star
        }
        db.movies.insert_one(doc)

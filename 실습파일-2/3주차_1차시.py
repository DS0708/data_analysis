import pandas
pandas.DataFrame()

import pandas as pd
pd.DataFrame()

from pandas import DataFrame
DataFrame()


def g(x):
    y=3*x**3 - 3*x -1
    return y

print(g(3))
x=3
print(g(x))



def discount_rate(price):
    if price < 10000:
        rate = 0
    elif price < 20000:
        rate = 1/100
    elif price < 40000:
        rate = 2/100
    else:
        rate = 4/100
    return rate

discount_rate(15000)



price = int(input("가격입력: "))
discount_rate = discount_rate(price)

discount = price * discount_rate
discount_price = price - discount

print("할인율: %d%%, 할인액: %d" %(int(discount_rate*100), discount))
print("할인전 가격: %d, 할인 후 가격: %d" %(price, discount_price))




# 3-1. p.16

# Daum 뉴스 웹 스크래핑

import requests
url = "https://news.daum.net/breakingnews/economic/stock?page=1"
agent = "Mozilla/5.0 (window NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, I like Gecko) Chrome/117.0.0.0 Safari/537.36"
responese = requests.get(url = url, headers = {"User-Agent": agent})

# 연결상태 확인 -> 200이 나오면 정상 연결
print(responese.status_code)




# 3-1. p.17
res_text = responese.text
print(res_text[:200])


# 3-1. p.18

# 뷰티풀수프를 이용한 파싱
# : response 객체의 text 속성은 문자열이므로 특정속성을 갖는 태그 찾기 어려움
# : 뷰티풀 수프 -> 웹 페이지 소스를 나타내는 문자열을 태그 간 관계와 태그의 속성정보를 반영한 새로운 객체로 변환

from bs4 import BeautifulSoup as BS
parsed_res_text = BS(res_text)
print(type(parsed_res_text))


# 3-1. p.19
news_li = parsed_res_text.find_all('strong', attrs = {"class":"tit_thumb"})
news_li


# 3-1. p.20
press_name = news_li[0].find('span', attrs={'class':'info_news'})
press_name.text


# 3-1. p.21
news_name = news_li[0].find('a', attrs = {'class':'link_txt'})
news_name['href']
news_name.text

# 3-1. p.27

# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
client_id = #id 입력
client_secret = #secret number 입력
encText = urllib.parse.quote("AI")
url = "https://openapi.naver.com/v1/search/news?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

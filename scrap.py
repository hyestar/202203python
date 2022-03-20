import requests as req
# requests모듈 => 웹페이지를 요청하고 응답데이터를 받을 수 있음.
from bs4 import BeautifulSoup

# 요청시 헤더 정보를 크롬으로 지정
request_headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보들을 다 쳐내기 때문에 기기정보를 작성해주는 것

response = req.get("https://news.daum.net/", headers=request_headers) # 특정 사이트에 페이지 요청. 응답데이터 반환
# html을 읽어와야 됨
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')  # soup을 이용해서 html_doc 문자열을 html 파싱
alist = soup.select(".list_newsissue a") 
print(alist[1].text)
url = alist[1]["href"]

response2 = req.get(url, headers=request_headers)
soup2 = BeautifulSoup(response2.text, 'html.parser')
title = soup2.select(".tit_view")
print(title[0].text)
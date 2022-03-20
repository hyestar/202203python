import requests as req
# requests모듈 => 웹페이지를 요청하고 응답데이터를 받을 수 있음.
from bs4 import BeautifulSoup

# 요청시 헤더 정보를 크롬으로 지정
request_headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98\Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보들을 다 쳐내기 때문에 기기정보를 작성해주는 것

response = req.get("https://news.naver.com/", headers=request_headers) # 특정 사이트에 페이지 요청. 응답데이터 반환

# html을 읽어와야 됨
# print(response.text)

# 파이썬한테 태그의 의미를 알려줘야되는데 div, a 엄청 많은 태그들을 알려줄 수 없으니 태그를 알려주는 모듈을
# 사용해서 html 해석을 하겠다.

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')  # soup을 이용해서 html_doc 문자열을 html 파싱
# 그 내용을 soup 변수로 대입
list1 = soup.select("a") # 선택자를 이용해 태그 선택, 결과는 리스트로 반환
print(list1[1])

# 텍스트 가져오기
print(list1[1].text)
# 속성값을 가져오기 <태그명 속성명="속성값">
print(list1[1]["href"])
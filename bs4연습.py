import requests as req 
from bs4 import BeautifulSoup
# 요청시 헤더 정보를 크롬으로 지정
request_headers = {'User-Agent': ('Mozilla/5.0 (Windows NT 10.0;Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98Safari/537.36'), }
# 네이버의 경우 알 수 없는 정보들을 6다 쳐내기 때문에 기기정보를 작성해주는 것


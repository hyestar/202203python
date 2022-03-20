from selenium import webdriver
import time
chrome_driver_path = "C:\py_test\chromedriver.exe"    # chromedriver.exe 경로 입력
url = "https://www.naver.com/"                        # 들어가고 싶은 url 입력
browser = webdriver.Chrome(chrome_driver_path)        # 드라이버로 크롬 
browser.get(url)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="account"]/a/i').click() # xpath로 가져오고 싶을때
time.sleep(1)
# browser.find_element_by_css_selector('#account > a').click() # selector로 가져오고 싶을때
id = "0109jhs"
browser.find_element_by_xpath('//*[@id="id"]').send_keys(id)
time.sleep(1)
pw = ""
browser.find_element_by_xpath('//*[@id="pw"]').send_keys(pw)
time.sleep(1)
browser.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1)
browser.switch_to.window(browser.window_handles[-1]) # 최신 팝업창으로 이동
browser.switch_to.window(browser.window_handles[0]) # 원래 창으로 복귀
browser.find_element_by_xpath('//*[@id="id"]').clear() # 글자 지움
time.sleep(1)
# browser.close()  # 브라우저 창 닫음
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(20)
url="http://1.116.81.228:8080/assets/#/index"
driver.get(url)
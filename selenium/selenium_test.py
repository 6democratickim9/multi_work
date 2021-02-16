from selenium import webdriver

path ="C:\\Users\\MIN\\Desktop\\multi_work\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.google.com")
search_box= driver.find_element_by_name("q")
search_box.send_keys("아마존 웹 서비스")
search_box.submit()# 엔터키


print(driver.title)
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path ="C:\\Users\\MIN\\Desktop\\multi_work\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com")
print(driver.title)

elem_email= driver.find_element_by_id("email")
elem_email.send_keys('look_ts@naver.com')
elem_pass= driver.find_element_by_id("pass")
elem_pass.send_keys('Vanilabean97!')


elem_pass.send_keys(Keys.RETURN)

profile_me = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/ul/li/div/a')
print("profile_me",profile_me.get_attribute('href'))

friends_a=driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/div[1]/ul/li[2]/span/div/a')
# print("friends",friends_a.get_attribute('href'))
driver.get(profile_me.get_attribute('href'))
from selenium import webdriver
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
import time

driver = webdriver.Chrome()
driver.get('https://doc.scrapy.org/en/latest/_static/selectors-sample1.html')
driver.implicitly_wait(3)

try:
    # tag=driver.find_element_by_xpath('/html') #从html标签找
    tags = driver.find_elements_by_xpath('//div//img')  # //找所有,找到div标签,找到div下的img
    # //*找所有标签[符合什么属性@id="images"]/a[4]/img
    print(tags[3].get_attribute('src'))

    # print(tags.tag_name)


finally:
    driver.close()



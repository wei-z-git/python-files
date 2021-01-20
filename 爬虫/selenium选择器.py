# 官网链接：http://selenium-python.readthedocs.io/locating-elements.html
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait  # 等待页面加载某些元素
import time

driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
# wait=WebDriverWait(driver,10)
driver.implicitly_wait(3)
try:

    input_tag = driver.find_element_by_id('kw')
    input_tag.send_keys("alex大宝贝")
    input_tag.send_keys(Keys.ENTER)
    time.sleep(5)

    # 2、find_element_by_link_text
    # login=driver.find_element_by_link_text('登录')
    # login.click()


finally:
    driver.close()

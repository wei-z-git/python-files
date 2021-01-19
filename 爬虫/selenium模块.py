from selenium import webdriver
# ActionChains破解滑动验证码
from selenium.webdriver import ActionChains
# 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.by import By
# 键盘按键操作
from selenium.webdriver.common.keys import Keys

# 等待页面加载某些元素
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import time

try:
    browser = webdriver.Chrome()
    # 拿到一个等的对象，等三秒
    wait = WebDriverWait(browser, 3)
    browser.get('https://www.taobao.com')
    # 根据id拿到输入框
    input_tag = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    # 输入框中输入内容
    input_tag.send_keys('唐诗三百首')
    input_tag.send_keys(Keys.ENTER)
    time.sleep(5)


finally:
    browser.close()

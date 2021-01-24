from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
import time

# driver = webdriver.Chrome()
# driver.get('https://www.jd.com/')
# driver.implicitly_wait(3)
# try:
#     input_tag = driver.find_element_by_id('key')
#     input_tag.send_keys('情趣用品')
#     input_tag.send_keys(Keys.ENTER)
#     time.sleep(3)

    
#     # 清空
#     input_tag = driver.find_element_by_id('key')
#     input_tag.clear()
#     time.sleep(3)
#     input_tag.send_keys('哈哈')
#     time.sleep(3)


# finally:
#     driver.close()


driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(3)

try:
    # 跳过iframe
    driver.switch_to.frame('')
    source=driver.find_element_by_id("draggable")
    print(source)
finally:
    driver.close()
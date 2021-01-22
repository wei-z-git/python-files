from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver import ActionChains
import time


driver = webdriver.Chrome()
driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.implicitly_wait(3)

try:
    # 跳过iframe
    driver.switch_to.frame('iframeResult')

    sourse = driver.find_element_by_id('draggable')
    target = driver.find_element_by_id('droppable')

    ActionChains(driver).click_and_hold(sourse).perform()
    # 滑动距离distance
    distance = target.location['x']-sourse.location['x']
    print(distance)
    s = 0
    while s < distance:
        # 如果两者距离不为0，则 移动动作链（动作链是“点击按住”的source）2个单位
        ActionChains(driver).move_by_offset(xoffset=2, yoffset=0).perform()
        time.sleep(0.2)
        s += 2
    
    ActionChains(driver).release().perform()
    time.sleep(5)


finally:
    driver.close()

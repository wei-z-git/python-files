from selenium import webdriver
from selenium.webdriver.common.by import By  # 按照什么方式查找，By.ID,By.CSS_SELECTOR
from selenium.webdriver.common.keys import Keys  # 键盘按键操作
from selenium.webdriver import ActionChains
from PIL import Image  # 用来截图的
import time


driver = webdriver.Chrome()
driver.get('https://account.cnblogs.com/signin')
driver.implicitly_wait(3)


def get_snap(driver):
    # 截图
    driver.save_screenshot('snap.png')
    snap_obj=Image.open('snap.png')
    return snap_obj


def get_image(driver):
    # 拿到图片
    img = driver.find_element_by_class_name(
        'geetest_widget')
    time.sleep(2)
    size = img.size
    location = img.location
    left = location['x']
    top = location['y']
    right = left+size['width']
    bottom = top+size['height']

    snap_obj = get_snap(driver)
    image_obj = snap_obj.crop((left, top, right, bottom))
    image_obj.show()
    return image_obj


try:
    input_user = driver.find_element_by_id('mat-input-0')
    input_pw = driver.find_element_by_id('mat-input-1')
    login_button = driver.find_element_by_xpath(
        '/html/body/app-root/mat-sidenav-container/mat-sidenav-content/div/div/app-sign-in/app-content-container/mat-card/div/form/div/button')

    input_user.send_keys('1419864987@qq.com1')
    time.sleep(2)
    input_pw.send_keys('wodeyuwen666 ')
    login_button.click()
    # 截图原始
    image=get_image(driver)
    time.sleep(5)


finally:
    driver.close()

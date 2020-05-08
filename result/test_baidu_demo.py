import time

import allure
import pytest
from selenium import webdriver

@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data",['allure','pytest','unittest'])
def test_septs_demo(test_data):

    with allure.step("打开百度网页"):
        driver = webdriver.Chrome("chromedriver.exe")
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词:{test_data}"):
        driver.find_element_by_id("kw").send_keys(test_data)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保持图片"):
        driver.save_screenshot("./result/b.png")
        allure.attach.file("./result/b.png", attachment_type=allure.attachment_type.PNG)
        allure.attach("<head></head><body>首页</body>", "Attach with HTML type", allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
        driver.quit()






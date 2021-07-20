# -*- coding:utf-8 -*-
# @Author: Phoebe
# @File:   test_touchactions.py
from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchActions:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_touchactions_scrollbottom(self):
        self.driver.get('https://www.baidu.com/')
        el = self.driver.find_element_by_id('kw')
        el_search = self.driver.find_element_by_id('su')
        el.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()

        action.scroll_from_element(el, 0, 1000).perform()

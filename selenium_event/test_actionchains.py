# -*- coding:utf-8 -*-
# @Author: Phoebe
# @File:   test_actionchains.py
from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        sleep(1)
        self.driver.quit()

    # @pytest.mark.skip  # 忽略
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        # element_click =self.driver.find_element_by_xpath('/html/body/form/input[3]')
        element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
        element_doubleclick = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
        element_rightclick = self.driver.find_element_by_xpath('//input[@value="right click me"]')

        action = ActionChains(self.driver)
        action.click(element_click)
        action.double_click(element_doubleclick)
        action.context_click(element_rightclick)
        action.perform()

    # @pytest.mark.skipZ
    def test_movetoelement(self):
        self.driver.get('http://www.baidu.com')
        # ????????????
        ele = self.driver.find_element_by_link_text("设置")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(3)

    def test_dragdrop(self):
        self.driver.get('http://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element_by_id('dragger')
        drop_element = self.driver.find_element_by_xpath('/html/body/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag_element, drop_element)
        # action.click_and_hold(drag_element).release(drop_element)
        # action.click_and_hold(drag_element).move_to_element(drop_element).release()
        action.perform()

    def test_keys(self):
        self.driver.get('http://sahitest.com/demo/label.htm')
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()  # 要操作元素，需要先将光标移动到元素上面，对元素进行点击操作
        action = ActionChains(self.driver)
        action.send_keys('username').pause(1)  # pause(1)等待1秒
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('tom').pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()


if __name__ == '__main__':
    pytest.main(['-v', 's', 'test_actionchains.py'])

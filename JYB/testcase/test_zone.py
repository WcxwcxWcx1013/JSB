"""
@desc 第三层
使用单元测试框架对业务逻辑进行测试

该demo用于园区的创建
"""

import unittest
from pages.zone import CreateZone
from selenium import webdriver
from pages.basePage import BasePage
import time
from pages.login import LoginPage


class ZoneCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dir = webdriver.Chrome()
        lg = BasePage(self.dir)
        lg.load_page()
        self.dir.maximize_window()
        time.sleep(2)

    def test_zone_create(self):
        username = '17721170771'
        password = 'a111111'
        # 类实例
        login_page1 = LoginPage(driver=self.dir)
        # 登录
        login_page1.login_s(username, password)
        time.sleep(2)
        # 创建园区
        z = CreateZone(self.dir)
        z.create_zone()

    def tearDown(self):
        # 关闭浏览
        self.dir.quit()


if __name__ == '__main__':
    unittest.main()

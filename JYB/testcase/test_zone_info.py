"""
@desc 第三层
使用单元测试框架对业务逻辑进行测试
对获取列表的第一行第一列数据，并对其进行编辑


"""

import unittest
from pages.zone import CreateZone
from selenium import webdriver
from pages.basePage import BasePage
import time
from pages.login import LoginPage
from pages.zone_list import ZoneList


class ZoneInfoCase(unittest.TestCase):

    def setUp(self) -> None:
        self.dir = webdriver.Chrome()
        lg = BasePage(self.dir)
        lg.load_page()
        self.dir.maximize_window()
        time.sleep(2)

    def test_zone_info(self):
        username = '17721170771'
        password = 'a111111'
        # 类实例
        login_page1 = LoginPage(driver=self.dir)
        # 登录
        login_page1.login_s(username, password)
        time.sleep(5)
        # 定位列表
        zone_l = ZoneList(self.dir)
        # 获取表格内容并点击编辑按钮进入详情
        zone_l.Zone_Info_list()

    def tearDown(self):
        # 关闭浏览
        self.dir.quit()


if __name__ == '__main__':
    unittest.main()

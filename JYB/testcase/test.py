"""
@desc 第三层
使用单元测试框架对业务逻辑进行测试

该demo用于运行登录捷园宝后台
"""
from selenium import webdriver
from pages.login import LoginPage
from pages.basePage import BasePage
from pages.worktable import wordkToDo
import unittest
import time


class LoginCase(unittest.TestCase):

    def setUp(self):
        # 实例化webserver
        self.dir = webdriver.Chrome()
        lg = BasePage(self.dir)
        lg.load_page()
        self.dir.maximize_window()
        time.sleep(3)

    def test_login_success(self):
        username = '17721170771'
        password = 'a111111'
        # 类实例
        login_page1 = LoginPage(driver=self.dir)
        # 登录
        work_page = login_page1.login_s(username, password)
        print(work_page)
        time.sleep(10)
        # 断言类
        lgin_text = wordkToDo(driver=self.dir)
        # 断言字段的获取
        lgin_text_get = lgin_text.wordktable_undo_text()
        print(lgin_text_get)
        # 断言
        self.assertEqual('捷园宝', lgin_text_get)

    def tearDown(self):
        # 关闭浏览
        self.dir.quit()


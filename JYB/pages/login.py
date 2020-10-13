"""
    @desc 第二层，页面元素分离，每个元素只定位一次
    用于登录的定位
"""
from pages.basePage import BasePage
import time


class LoginPage(BasePage):

    # 登录输入框定位（定位分离）
    def from_username(self):
        return self.by_xpath('//*[@id="app"]/div/form/div[5]/div[1]/div/div/input')

    # 密码输入框定位（定位分离）
    def from_password(self):
        return self.by_xpath('//*[@id="app"]/div/form/div[5]/div[2]/div/div/input')

    # 登录按钮按钮定位（定位分离）
    def from_Button(self):
        return self.by_xpath('//*[@id="app"]/div/form/div[5]/button/span')

    # 切换手机号登录方式
    def from_Phone(self):
        return self.by_xpath('//*[@id="app"]/div/form/div[3]/div[2]/div')

    # 登录操作(业务逻辑分离)
    def login_s(self, username, password):
        # 切换手机号登录
        self.from_Phone().click()
        time.sleep(3)
        # 输入账号
        self.from_username().send_keys(username)
        # 输入密码
        self.from_password().send_keys(password)
        time.sleep(2)
        # 点击登录
        self.from_Button().click()

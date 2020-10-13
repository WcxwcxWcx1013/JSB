"""
    第二层
    断言得封装
"""
from .basePage import BasePage


class wordkToDo(BasePage):

    # 定位登录网址‘捷园宝’
    def worktable_undo(self):
        return self.by_xpath('//*[@id="app"]/div/div[1]/div/div/ul/div/div/span')

    # 获取定位元素的内容
    def wordktable_undo_text(self) -> object:
        return self.worktable_undo().text

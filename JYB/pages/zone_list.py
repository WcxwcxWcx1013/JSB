"""
@desc 第二层
用于定位园区列表的数据
"""

from pages.basePage import BasePage
import time


class ZoneList(BasePage):

    # 招商工作台定位
    def from_canvass_business(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/div')

    # 园区列表定位
    def from_zone_list(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/ul/li/div')

    # 园区页面定位
    def from_zone_page(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/ul/li/ul/li')

    # 定位园区列表
    def Zone_Info(self):
        return self.by_xpath('//div[@class="el-row"]')

    # 方法一： 获取表的方法  但是不知道如何定位td里边的三个按钮
    def get_zone_list(self):
        row = self.by_tagName('tr')
        List = []
        for i in row:
            j = i.find_elements_by_tag_name('td')
            for item in j:
                text = item.text
                List.append(text)
        return List

    # 定位表格的第一行的，第16列  用次方法比较便捷
    def get_zone_list_td(self):
        return self.by_xpath('//table[@class="el-table__body"]/tbody/tr/td[18]/div/button[2]')

    def Zone_Info_list(self):
        # 点击招商工作台
        self.from_canvass_business().click()
        # 点击园区列表
        self.from_zone_list().click()
        # 点击园区
        self.from_zone_page().click()
        time.sleep(2)
        # 向下向左滚动窗口
        self.scroll_right()
        # 获取列表并点击【编辑】按钮
        self.get_zone_list_td().click()
        time.sleep(2)







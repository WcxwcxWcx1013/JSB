"""
   第二层：创建园区,页面元素分离，每个元素只定位一次
   @desc 用于园区创建的定位
"""
from pages.basePage import BasePage
import time
from faker import Faker


class CreateZone(BasePage):


    # 招商工作台定位
    def from_canvass_business(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/div')

    # 园区列表定位
    def from_zone_list(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/ul/li/div')

    # 园区页面定位
    def from_zone_page(self):
        return self.by_xpath('//div[@class="menuCol el-col el-col-24"]/ul/li[5]/ul/li/ul/li')

    # 新建园区定位
    def from_create_new_zone(self):
        return self.by_xpath('//div[@class="park-add-btn"]/button')

    # 园区名称
    def from_zone_name(self):
        return self.by_xpath('//div[@class="el-input el-input--small"]/input')

    # 新增园区-确定
    def form_zone_sure(self):
        return self.by_xpath('//div[@class="el-dialog__footer"]/span/button[2]')

    def create_zone(self):
        # 点击招商工作台
        self.from_canvass_business().click()
        # 点击园区列表
        self.from_zone_list().click()
        # 点击园区
        self.from_zone_page().click()
        # 点击新建园区
        self.from_create_new_zone().click()
        time.sleep(2)
        # 生成随机的园区名称
        fake = Faker("zh-CN")
        Name = fake.company_prefix()
        # 输入园区名称
        self.from_zone_name().send_keys(Name)
        time.sleep(3)
        # 点击确定
        self.form_zone_sure().click()
        time.sleep(3)



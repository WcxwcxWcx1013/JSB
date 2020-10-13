"""
@desc 第一层，对selenium进行二次封装，定义一个所有页面都继承的BaseP按个，
封装selenium基本方法，例如：元素定位，元素等待，导航页面，
不需要全部封装，用到多少方法就封装多少
"""


class BasePage(object):

    def __init__(self, driver):
        """
        :param driver: Webdriver 实例对象
        :param path:
        """
        self.driver = driver
        self.url = 'https://cms.jieyuanbao.vip/'

    # xpath方法寻找元素
    def by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # tag_name方法寻找元素
    def by_tagName(self, tagname):
        return self.driver.find_elements_by_tag_name(tagname)

    # 打开网页
    def load_page(self):
        return self.driver.get(self.url)

    # 滚动进入条至最右边
    def scroll_right(self):
        js = "window.scrollTo(1000,10000)"  # 参数是左边距，和上边距
        return self.driver.execute_script(js)
    '''
    # 滚动条至最下边
    def scroll_down(self):
        js1 = "document.documentElement.scrollTop=10000"
        return self.driver.execute_script(js1)
    '''


# coding=gbk
# conftest.py
import time
import pytest
from Base.Driver import Driver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.baidu.com/"
count = 0
class Testtest:

    def setup_class(self):
        # 打开浏览器
        self.driver = Driver.get_driver()
        self.size_Dict = self.driver.get_window_size()
        self.driver.get(url)
        
        time.sleep(3)

    def teardown_class(self):
        # 关闭浏览器
        time.sleep(1)
        Driver.quit_dirver()

    def test_baidu(self):

        # 百度搜索“青椒云”
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('青椒云')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()

    def test_qj(self):
        # 显示所有窗口
        wins = self.driver.window_handles
        time.sleep(3)

        # 打开新的窗口，进入青椒云官网
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a ').click()

        # 显示等待判断新窗口是否已经打开，每间隔1s进行检查，超过5s无法定位该窗口时，则抛出超时异常 TimeoutException
        WebDriverWait(self.driver, 5, 1).until(EC.new_window_is_opened(wins))

        # 切换窗口
        # 1.获取所有窗口
        wins1 = self.driver.window_handles

        # 2.元素定位切换到新窗口
        self.driver.switch_to.window(wins1[-1])
        time.sleep(3)

        # 打印浏览器的宽和高
        print("当前浏览器的宽：", self.size_Dict['width'])
        print("当前浏览器的高：", self.size_Dict['height'])


        # self.driver.close()
        #
        # # 2.元素定位切换到新窗口
        # self.driver.switch_to.window(wins1[0])
        #
        # time.sleep(3)
        #
        # print("切换回第一个页签： % s" % self.driver.title)
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('镭速')


    # 设置该测试用例重复执行 60 次，每执行一次用例耗费时间大概是1分钟左右，所以在这里设置60次即可达到1小时，执行完后通过该测试用例
    @pytest.mark.repeat(60)
    # 该测试用例用于循环浏览青椒云官网素材页面
    def test_Script(self):

        # 定位首页
        self.driver.find_element_by_class_name('atom__A-sc-1x9q1fw-0').click()
        time.sleep(1)

        # 定位素材页
        self.driver.find_elements_by_class_name('navbar__NavItem-sc-1hrjgr-1')[6].click()
        time.sleep(2)

        # 页面滚动条向下拉动
        js1 = "window.scrollTo(0,400)"
        self.driver.execute_script(js1)
        time.sleep(5)

        js2 = "window.scrollTo(0,800)"
        self.driver.execute_script(js2)
        time.sleep(5)

        js3 = "window.scrollTo(0,1200)"
        self.driver.execute_script(js3)
        time.sleep(5)

        js4 = "window.scrollTo(0,1600)"
        self.driver.execute_script(js4)
        time.sleep(5)

        js5 = "window.scrollTo(0,2000)"
        self.driver.execute_script(js5)
        time.sleep(5)

        js6 = "window.scrollTo(0,2400)"
        self.driver.execute_script(js6)
        time.sleep(5)

        js7 = "window.scrollTo(0,2800)"
        self.driver.execute_script(js7)
        time.sleep(5)

        js8 = "window.scrollTo(0,3200)"
        self.driver.execute_script(js8)
        time.sleep(5)

        js9 = "window.scrollTo(0,3600)"
        self.driver.execute_script(js9)
        time.sleep(5)

        # 滚动条滑倒最顶
        js10 = "window.scrollTo(0,0)"
        self.driver.execute_script(js10)
        time.sleep(5)

        print("~~~~~~~~~~~~~~~~~~~~hgc Test case is executed~~~~~~~~~~~~~~~~~~~~")


if __name__ == '__main__':
    pytest.main(["-s","test_repeat.py"])
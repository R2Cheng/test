# coding=gbk
# ע��
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
from selenium.webdriver.common.action_chains import ActionChains
import random

url = "https://cloud-sit.raysync.cn/register"
class TestRegister:

    def setup_class(self):

        self.driver = Driver.get_driver()
        logging.info("�����ȸ������")
        self.handle = Handle.HandleTotal(self.driver)
        self.driver.get(url)
        logging.info("���������'{}'��ַ".format(url))

    def teardown_class(self):
        logging.info("------��������ִ����ϣ�3s֮���Զ��ر������------")
        time.sleep(3)
        Driver.quit_dirver()
        logging.info("�ɹ��ر������")

    @pytest.mark.parametrize("info", Base.get_data("register", "register_success"))
    def test_Register(self, info):
        logging.info("-----------------test case register start-----------------")
        self.handle.init_register.input_num(info["num"])
        logging.info("�û�������Ϊ'{}'".format(info["num"]))

        self.handle.init_register.input_pwd(info["pwd"])
        logging.info("��������Ϊ'{}'".format(info["pwd"]))
        time.sleep(1)

        self.handle.init_register.input_tel(info["tel"])
        logging.info("�ֻ���������Ϊ'{}'".format(info["tel"]))
        time.sleep(1)


        # �����ƻ����޷�ʹ�ýű�ʵ�ֻ�����������δ�ҵ�����취
        div = self.driver.find_element_by_id("nc_2_n1z")
        ActionChains(self.driver).click_and_hold(on_element=div).perform()

        # ��������ƶ�������ֵ
        x1 = random.randrange(20, 200)

        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element_with_offset(to_element=div, xoffset=x1, yoffset=50).release().perform()
        logging.info("��������")
        time.sleep(3)


# ����allure���棺allure generate report/xml -o report/html --clean

if __name__ == '__main__':
    pytest.main(["-s", "test_register.py"])
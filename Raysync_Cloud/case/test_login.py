# coding=gbk
# ��¼
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging
import os,sys

sys.path.append(os.getcwd())
url = "https://client.raysync.cloud/login?language=zh-CN"
class TestLogin:

    def setup_class(self):

        self.driver = Driver.get_driver()
        logging.info("�����ȸ������")
        self.handle = Handle.HandleTotal(self.driver)
        self.driver.get(url)
        logging.info("���������'{}'��ַ".format(url))


    # def teardown_class(self):
    #     logging.info("------��������ִ����ϣ�3s֮���Զ��ر������------")
    #     time.sleep(3)
    #     Driver.quit_dirver()
    #     logging.info("�ɹ��ر������")


    @pytest.mark.parametrize("info", Base.get_data("login", "login_success"))
    def test_login(self,info):
        logging.info("-----------------test case login start-----------------")
        self.handle.init_login.input_num(info["num"])
        logging.info("�����ƴ����˺�����Ϊ'{}'".format(info["num"]))

        self.handle.init_login.input_pwd(info["pwd"])
        logging.info("�����ƴ�����������Ϊ'{}'".format(info["pwd"]))
        time.sleep(1)

        self.handle.init_login.tap_enter()
        logging.info("�����¼")
        time.sleep(3)


# ��Ŀ��Ŀ¼ִ�����ɱ���
# ����allure���棺allure generate report/xml -o report/html --clean

if __name__ == '__main__':
    pytest.main(["-s", "test_login.py"])
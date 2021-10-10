# coding=gbk
# �ǳ�
import time
import pytest
import Base
import Handle
import logging
import os
from Base.Driver import Driver
from public.email import email

class TestLogout:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    def teardown_class(self):
        logging.info("------������������------")
        time.sleep(3)
        Driver.quit_dirver()
        logging.info("�ر�����")
        email()


    def test_logout(self):
        self.handle.init_space.tap_account_information()
        logging.info("����˺���Ϣ������")
        time.sleep(2)

        self.handle.init_space.tap_logout()
        logging.info("����˳���ť")


if __name__ == '__main__':
    pytest.main(["-s", "test_logout.py"])

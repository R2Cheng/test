# coding=gbk
# �ҵķ���
import time
import pytest
from Base.Driver import Driver
import Base
import Handle
import logging

class TestSharing:

    def setup_class(self):

        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    def test_sharing(self):
        logging.info("-----------------test case sharing start-----------------")

        self.handle.init_sharing.tap_sharing()
        logging.info("����˵��ҵķ���")
        time.sleep(1)

        self.handle.init_sharing.tap_first_sharing()
        logging.info("��ѡ������������")
        time.sleep(2)

        self.handle.init_sharing.tap_Edit()
        logging.info("����༭")
        time.sleep(1)

        self.handle.init_sharing.tap_download()
        logging.info("����������ƴ���")
        time.sleep(1)

        self.handle.init_sharing.tap_without_login()
        logging.info("������½")
        time.sleep(1)

        element = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div[3]/div/div[2]").text
        logging.info("������������{}".format(element))

        self.handle.init_sharing.tap_confirm()
        logging.info("���ȷ��")
        time.sleep(1)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(2)

        self.handle.init_sharing.tap_first_sharing()
        logging.info("��ѡ������������")
        time.sleep(2)

        self.handle.init_sharing.tap_copy_link()
        logging.info("�����������")
        time.sleep(1)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(2)

        self.handle.init_sharing.tap_cancel_sharing()
        logging.info("���ȡ������")
        time.sleep(1)

        self.handle.init_sharing.tap_cancel_confirm()
        logging.info("���ȷ��")
        time.sleep(3)

        msg = self.driver.find_element_by_class_name("el-message__content").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

    # def test_upload(self):
    #     logging.info("-----------------test case upload start-----------------")
    #     self.handle.init_sharing.tap_upload()
    #     logging.info("��������ϴ�")
    #     time.sleep(1)
    #
    #     self.handle.init_sharing.tap_first_upload()
    #     logging.info("��ѡ�����ϴ�����")
    #     time.sleep(1)
    #
    #     self.handle.init_sharing.tap_copy_link()
    #     logging.info("�����������")
    #     time.sleep(1)
    #
    #     msg = self.driver.find_element_by_class_name("el-message__content").text
    #     logging.info("Message��ʾ��{}��".format(msg))
    #     time.sleep(2)
    #
    #     self.handle.init_sharing.tap_cancel_sharing()
    #     logging.info("���ȡ������")
    #     time.sleep(1)
    #
    #     self.handle.init_sharing.tap_cancel_confirm()
    #     logging.info("���ȷ��")
    #     time.sleep(3)
    #
    #     logging.info("Message��ʾ��{}��".format(msg))
    #     time.sleep(2)


if __name__ == '__main__':
    pytest.main(["-s", "test_sharing.py"])
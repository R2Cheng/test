# coding=gbk
# �ҵĿռ�
import time
import pytest
import Base
import Handle
import logging
import os
from Base.Driver import Driver

class TestSpace:

    def setup_class(self):
        self.driver = Driver.get_driver()
        self.handle = Handle.HandleTotal(self.driver)

    def test_Download_folder(self):
        logging.info("-----------------test case Download folder start-----------------")
        self.handle.init_space.tap_Space()
        time.sleep(6)

        self.handle.init_space.tap_checkbox_all()
        logging.info("ȫѡ��Ŀ¼�µ������ļ����У�")
        time.sleep(1)

        #�����ļ���
        # self.handle.init_space.tap_Download_Foloer()
        # logging.info("�������")
        # time.sleep(1)

        #�����ļ�
        self.handle.init_space.tap_Download_files()
        logging.info("�������")
        time.sleep(1)

        path = "E:\Python\Raysync_Cloud\Downlod\script/·��1.exe"
        # ����ָ��·���µ��ļ�
        os.startfile(path)
        time.sleep(8)

        self.handle.init_space.tap_checkbox_all()
        logging.info("ȡ��ȫѡ��Ŀ¼�µ������ļ����У�")
        time.sleep(1)

        # self.handle.init_space.tap_checkbox_first()
        # logging.info("ȡ����ѡ�ļ���")
        # time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "Share Link"))
    def test_Share_Link(self,info):
        logging.info("-----------------test case Share_Link start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("��ѡ��Ŀ¼�µ��׸��ļ����У�")
        time.sleep(1)

        self.handle.init_space.tap_Share_files()
        logging.info("����ļ�����ť")
        time.sleep(1)

        self.handle.init_space.tap_Expiration_date()
        logging.info("�������ӹ���ʱ��")
        time.sleep(1)

        self.handle.init_space.tap_Share_Deadkube()
        logging.info("������ӹ���ʱ�������")

        self.handle.init_space.input_Select_date(info["Date"])
        logging.info("���ӹ�������������'{}'".format(info["Date"]))
        time.sleep(2)

        self.handle.init_space.tap_Select_time()
        logging.info("������ӹ���ʱ��ʱ����")
        time.sleep(1)

        self.handle.init_space.input_Select_time_clear()
        logging.info("������ӹ���ʱ��ʱ����")

        self.handle.init_space.input_Select_time(info["Time"])
        logging.info("���ӹ���ʱ��������'{}'".format(info["Time"]))
        time.sleep(1)

        self.handle.init_space.tap_Select_affirm()
        logging.info("������ӹ���ʱ��ȷ�ϰ�ť")
        time.sleep(1)

        self.handle.init_space.tap_Share_download()
        logging.info("������ӹ������ش�����ť")
        time.sleep(1)

        self.handle.init_space.input_Share_num(info["Num"])
        logging.info("�������ش�������'{}'".format(info["Num"]))
        time.sleep(1)

        self.handle.init_space.tap_Share_login()
        logging.info("������½��ť")
        time.sleep(1)

        # self.driver.find_elements_by_class_name("el-switch__core")[3].click()
        # logging.info("�����ʼ�֪ͨ")
        # time.sleep(1)
        #
        # self.handle.init_space.tap_Email1_send()
        #
        # self.handle.init_space.input_Email2_send(info["E-mail"])
        # logging.info("���������ʼ��ռ�������'{}'".format(info["E-mail"]))
        # self.handle.init_space.tap_Email2_send()
        # time.sleep(1)
        #
        # self.handle.init_space.input_Email_text(info["Text"])
        # logging.info("���������ʼ�������������'{}'".format(info["Text"]))
        # time.sleep(2)
        #
        # down = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div[2]/div/div/div[9]/div").text
        # logging.info("������������{}".format(down))
        # time.sleep(1)

        self.handle.init_space.tap_Share_affirm()
        logging.info("ȷ�ϴ�����������")
        time.sleep(2)

        msg = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div/div[9]/div/div[2]/div[1]/div/div/span").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

        self.handle.init_space.tap_Share_close()
        logging.info("�ر�����������ش���")
        time.sleep(1)

        self.handle.init_space.tap_checkbox_first()
        logging.info("ȡ����ѡ�ļ���")
        time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "New directory name"))
    def test_New_folder(self,info):

        logging.info("-----------------test case New folder start-----------------")
        self.handle.init_space.tap_New_Foloer()
        logging.info("����½��ļ��а�ť")
        time.sleep(1)

        self.handle.init_space.input_name(info["name"])
        logging.info("�½��ļ�����������'{}'".format(info["name"]))
        time.sleep(1)

        self.handle.init_space.tap_New_affirm()
        logging.info("���ȷ���½���ť")
        time.sleep(1)

        # �ɹ���ʾ��Ϣ��ӡ
        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

        # ִ���쳣�����ļ���
        # self.handle.init_space.tap_New_cancel()
        # logging.info("���ȡ���½���ť")
        # time.sleep(2)

    @pytest.mark.parametrize("info", Base.get_data("space", "Search name"))
    def test_search_folder(self, info):
        time.sleep(2)
        logging.info("-----------------test case search folder start-----------------")
        self.handle.init_space.input_search(info["name"])
        logging.info("�����ļ�������'{}'".format(info["name"]))
        self.handle.init_space.tap_search_ico()
        logging.info("�������ͼ�갴ť")
        time.sleep(2)

        self.handle.init_space.input_search_clear()
        logging.info("��������ļ������������")
        self.driver.refresh()
        logging.info("ˢ�µ�ǰҳ��")
        time.sleep(3)

    # ������������ť���޷���λ���ò�����������ִ��
    # @pytest.mark.parametrize("info", Base.get_data("space", "Rename directory"))
    # def test_Rename_folder(self,info):
    #     logging.info("-----------------test case Rename folder start-----------------")
    #     self.handle.init_space.tap_Operation()
    #     logging.info("���������ť")
    #     time.sleep(3)
    #
    #     self.handle.init_space.tap_Operation_rename()
    #     logging.info("���������������ť")
    #     time.sleep(1)
    #
    #     self.handle.init_space.input_rename(info["name"])
    #     logging.info("�������ļ����У���������Ϊ'{}'".format(info["name"]))
    #     time.sleep(1)
    #
    #     self.handle.init_space.tap_Rename_affirm()
    #     logging.info("���ȷ����������ť")
    #     time.sleep(3)

    @pytest.mark.parametrize("info", Base.get_data("space", "Invite_to_upload"))
    def test_Invite_to_upload(self,info):
        logging.info("-----------------test case Invite_to_upload start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("��ѡ�ļ���")
        time.sleep(1)

        self.handle.init_space.tap_Invite_to_upload()
        logging.info("��������ϴ���ť")
        time.sleep(1)

        self.handle.init_space.tap_Expiration_date()
        logging.info("�������ӹ���ʱ��")
        time.sleep(1)

        self.handle.init_space.tap_Select_Deadkube()
        logging.info("������ӹ���ʱ�������")
        self.handle.init_space.input_Select_date(info["Date"])
        logging.info("���ӹ�������������'{}'".format(info["Date"]))
        time.sleep(2)

        self.handle.init_space.tap_Select_time()
        logging.info("������ӹ���ʱ��ʱ����")
        time.sleep(1)

        self.handle.init_space.input_Select_time_clear()
        logging.info("������ӹ���ʱ��ʱ����")

        self.handle.init_space.input_Select_time(info["Time"])
        logging.info("���ӹ���ʱ��������'{}'".format(info["Time"]))
        time.sleep(1)

        self.handle.init_space.tap_Select_affirm()
        logging.info("������ӹ���ʱ��ȷ�ϰ�ť")
        time.sleep(1)

    #     self.driver.find_elements_by_class_name("el-switch__core")[1].click()
    #     logging.info("�����ʼ�֪ͨ")
    #     time.sleep(1)
    #
    #     self.handle.init_space.tap_Email1_send()
    #     self.handle.init_space.input_Email2_send(info["E-mail"])
    #     logging.info("���������ʼ��ռ�������'{}'".format(info["E-mail"]))
    #     self.handle.init_space.tap_Email2_send()
    #     time.sleep(1)
    #
    #     self.handle.init_space.input_Email_text(info["Text"])
    #     logging.info("���������ʼ�������������'{}'".format(info["Text"]))
    #     time.sleep(1)
    #
    #     upload = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div[2]/div/div/div[8]/div/div[2]").text
    #     logging.info("������������{}".format(upload))

        self.handle.init_space.tap_upload_affirm()
        logging.info("ȷ�ϴ�����������")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("//*[@id='app']/section/main/section/section/div/div/div/div/div[8]/div/div[2]/div[1]/div/div").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

        self.handle.init_space.tap_upload_close()
        logging.info("�ر����������ϴ�����")
        time.sleep(2)

    def test_Copy_folder(self):
        logging.info("-----------------test case Copy folder start-----------------")
        # self.handle.init_space.tap_checkbox_first()
        # logging.info("��ѡ�ļ���")
        # time.sleep(1)

        self.handle.init_space.tap_Copy_Foloer()
        logging.info("������ư�ť")
        time.sleep(2)

        self.handle.init_space.tap_Copy_space()
        logging.info("����ҵĿռ�Ŀ¼")
        time.sleep(1)

        self.handle.init_space.tap_Copy_catalogue()
        logging.info("����ҵĿռ��Ŀ¼�µĵڶ�����Ŀ¼")
        time.sleep(1)

        self.handle.init_space.tap_Copy_affirm()
        logging.info("���ȷ��")
        time.sleep(1)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

    def test_Move_folder(self):
        logging.info("-----------------test case Move folder start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("��ѡ�ļ���")
        time.sleep(1)

        self.handle.init_space.tap_Move_Foloer()
        logging.info("����ƶ�")
        time.sleep(2)

        self.handle.init_space.tap_Move_space()
        logging.info("����ҵĿռ�Ŀ¼")
        time.sleep(1)

        self.handle.init_space.tap_Move_catalogue()
        logging.info("����ҵĿռ��Ŀ¼�µĵ�������Ŀ¼")
        time.sleep(1)

        self.handle.init_space.tap_Move_affirm()
        logging.info("���ȷ��")
        time.sleep(3)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

    @pytest.mark.repeat(2)
    def test_Delete_folder(self):
        logging.info("-----------------test case Delete folder start-----------------")
        self.handle.init_space.tap_checkbox_first()
        logging.info("��ѡ�ļ����У�")
        time.sleep(1)

        # self.handle.init_space.tap_checkbox_all()
        # logging.info("ȫѡ��Ŀ¼�µ������ļ����У�")
        # time.sleep(1)

        self.handle.init_space.tap_Delete_Folder()
        logging.info("���ɾ���ļ���")
        time.sleep(1)

        # self.handle.init_space.tap_Delete_files()
        # logging.info("����ļ�ɾ����ť")
        # time.sleep(1)

        # self.handle.init_space.tap_Delete_all()
        # logging.info("���ȫѡ�ļ�ɾ����ť")
        # time.sleep(1)

        self.handle.init_space.tap_Delete_affirm()
        logging.info("���ȷ��")
        time.sleep(3)

        msg = self.driver.find_element_by_xpath("/html/body/div[2]/p").text
        logging.info("Message��ʾ��{}��".format(msg))
        time.sleep(1)

if __name__ == '__main__':
    pytest.main(["-s", "test_space.py"])
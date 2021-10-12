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
        # �������
        self.driver = Driver.get_driver()
        self.size_Dict = self.driver.get_window_size()
        self.driver.get(url)
        
        time.sleep(3)

    def teardown_class(self):
        # �ر������
        time.sleep(1)
        Driver.quit_dirver()

    def test_baidu(self):

        # �ٶ��������ཷ�ơ�
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('�ཷ��')
        self.driver.find_element_by_xpath('//input[@id="su"]').click()

    def test_qj(self):
        # ��ʾ���д���
        wins = self.driver.window_handles
        time.sleep(3)

        # ���µĴ��ڣ������ཷ�ƹ���
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a ').click()

        # ��ʾ�ȴ��ж��´����Ƿ��Ѿ��򿪣�ÿ���1s���м�飬����5s�޷���λ�ô���ʱ�����׳���ʱ�쳣 TimeoutException
        WebDriverWait(self.driver, 5, 1).until(EC.new_window_is_opened(wins))

        # �л�����
        # 1.��ȡ���д���
        wins1 = self.driver.window_handles

        # 2.Ԫ�ض�λ�л����´���
        self.driver.switch_to.window(wins1[-1])
        time.sleep(3)

        # ��ӡ������Ŀ�͸�
        print("��ǰ������Ŀ�", self.size_Dict['width'])
        print("��ǰ������ĸߣ�", self.size_Dict['height'])


        # self.driver.close()
        #
        # # 2.Ԫ�ض�λ�л����´���
        # self.driver.switch_to.window(wins1[0])
        #
        # time.sleep(3)
        #
        # print("�л��ص�һ��ҳǩ�� % s" % self.driver.title)
        # self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('����')


    # ���øò��������ظ�ִ�� 60 �Σ�ÿִ��һ�������ķ�ʱ������1�������ң���������������60�μ��ɴﵽ1Сʱ��ִ�����ͨ���ò�������
    @pytest.mark.repeat(60)
    # �ò�����������ѭ������ཷ�ƹ����ز�ҳ��
    def test_Script(self):

        # ��λ��ҳ
        self.driver.find_element_by_class_name('atom__A-sc-1x9q1fw-0').click()
        time.sleep(1)

        # ��λ�ز�ҳ
        self.driver.find_elements_by_class_name('navbar__NavItem-sc-1hrjgr-1')[6].click()
        time.sleep(2)

        # ҳ���������������
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

        # �����������
        js10 = "window.scrollTo(0,0)"
        self.driver.execute_script(js10)
        time.sleep(5)

        print("~~~~~~~~~~~~~~~~~~~~hgc Test case is executed~~~~~~~~~~~~~~~~~~~~")


if __name__ == '__main__':
    pytest.main(["-s","test_repeat.py"])
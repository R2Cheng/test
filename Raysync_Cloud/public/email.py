# -*-coding:GBK -*-

sender = "18126480338@163.com"
receivers = "1402430303@qq.com"
mail_host = "smtp.163.com"
mail_user = "18126480338@163.com"
mail_pass = "MMPCJNRVZSMJUWME"
subject = "Raysync_Cloud"

import smtplib
import time
import config
import logging
from email.mime.text import MIMEText  # ��������
from email.mime.multipart import MIMEMultipart  # ���Ͷ������
from email.mime.application import MIMEApplication  # ���͸���
from email.header import Header  # ��email������Header()�����������������ʼ�ͷ

def email():

    now = time.strftime('%Y-%m-%d')
    # ����һ���ʼ��壺���ġ�����
    msg = MIMEMultipart()  # �ʼ���
    msg['From'] = sender  # ������
    msg['To'] = receivers  # �ռ���
    tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))  # ��ȡϵͳʱ��
    msg['Subject'] = Header(subject + '_' + tm, 'utf-8')  # �ʼ�����

    # ��������
    content = """
                             ִ�в����С���
                             ��������ɣ���
                             ���ɱ����С���
                             ���������ɡ���
                             �������ʼ����ͣ���
                            """
    email_body = MIMEText(content, 'plain', 'utf-8')
    msg.attach(email_body)

    # ��������ӵ��ʼ�����
    # ��������
    att = MIMEText(open((config.BASE_DIR)+'/report/' + 'html/'+ 'index.html', 'rb').read(), 'html', 'utf-8')  # �򿪸���
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename="%s.html"' % now
    msg.attach(att)  # ��Ӹ������ʼ�����

    try:
        smtpObj = smtplib.SMTP()
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # ʹ��smtpЭ�鷢���ʼ���SSLЭ�������м��ܴ��䣬465Ϊ�˿ں�
        smtpObj.login(mail_user, mail_pass)  # �����¼
        smtpObj.sendmail(sender, receivers, msg.as_string())  # �����ʼ�
        logging.info('send mail OK')
        smtpObj.quit()

    except smtplib.SMTPException:
        logging.info('send mail Fail')
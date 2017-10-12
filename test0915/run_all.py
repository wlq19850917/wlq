#coding:utf-8
import unittest
import os
import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import time

def add_case(case_path,rule):
        testunit = unittest.TestSuite()
        discover = unittest.defaultTestLoader.discover(case_path,
                                                       pattern=rule,
                                                       top_level_dir=None)
        testunit.addTest(discover)
        print(testunit)
        return testunit
def run_case(all_case,report_path):
        now = time.strftime("%Y_%m_%d %H_%M_%S")
        report_abspath = os.path.join(report_path,now + "result.html")
        fp = open(report_abspath,"wb")
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                               title=u'自动化测试报告，测试结果如下：',
                                               description=u'用例执行情况：')
        runner.run(all_case)
        fp.close()
def get_report_file(report_path):
        lists = os.listdir(report_path)
        lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))
        print(u'最新测试生成的报告：'+lists[-1])
        report_file=os.path.join(report_path,lists[-1])
        return report_file
def send_mail(sender,psw,receiver,smtpserver,report_file):
        with open(report_file,"rb")as f:
            mail_body = f.read()
            msg = MIMEMultipart()
            body = MIMEText(mail_body,_subtype='html',_charset='utf-8')
            msg['Subject']=u'自动化测试报告'
            msg["from"]=sender
            msg["to"]=[receiver]
            msg["date"]=time.strftime('%a,%d,%b%Y%H_%M_%S %Z')
            msg.attach(body)
            att = MIMEText(open(report_file,"rb").read(),"base64","utf-8")
            att["Content-Type"]="application/octet-stream"
            att["Content-Disposition"]='attachment;filename="report.html"'
            msg.attach(att)
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
    #         用户名密码
            smtp.login(sender,psw)
            smtp.sendmail(sender,receiver,msg.as_string())
            smtp.quit()
            print('test report email has send out!')
if __name__=="__main__":
        case_path="D:\\github\\test0915\\case"
        rule = "test*.py"
        all_case=add_case(case_path,rule)
        report_path = "D:\\github\\test0915\\case\\report"
        run_case(all_case,report_path)
        report_file=get_report_file(report_path)

        # sender = "wlq19850917@163.com"
        # psw = "wlq123455"
        #
        # receiver = "wlq19850917@163.com"
        # smtp_server = 'smtp.163.com'
        # send_mail(sender,psw,receiver,smtp_server,report_file)








# #用例路径
# case_path = os.path.join(os.getcwd(),"CAVE")
# #报告存放路径
# report_path=os.path.join(os.getcwd(),"report")
# def all_case():
#     discover = unittest.defaultTestLoader.discover(case_path,
#                                                    pattern="test*.py",
#                                                    top_level_dir=None)
#     print(discover)
#     return discover
# if __name__=="__main__":
#     # runner =unittest.TextTestRunner()
#     # runner.run(all_case())
#     # report_abspath=os.path.join(report_path,"result.html")
#     # fp = open(report_abspath,"wb")
#     filename = 'C:\\Python34\\Lib\\test0915\\CAVE\\Result\\aesult.html'
#     # C:\Python34\Lib\test0915
#     # 定义个报告存放路径，支持相对路径。
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
#                                            title=u'自动化测试报告，测试结果如下：',
#                                            description=u'用例执行情况：')
#     runner.run(all_case())
#     fp.close()
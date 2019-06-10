import csv  # 导入csv模块，用于读取csv文件内容
import os,time
from email.mime.text import MIMEText
import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart

BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 获取项目路径
CASESPATH = os.path.join(BASEPATH,'cases')   # 获取保存测试用例文件的目录路径
DATAPATH = os.path.join(BASEPATH,'data')    # 获取保存测试数据文件的目录路径
DRIVERSPATH = os.path.join(BASEPATH,'drivers')  # 获取保存浏览器驱动的目录路径
IMAGESPATH = os.path.join(BASEPATH,'images')    # 获取保存截图的目录路径
PAGESPATH = os.path.join(BASEPATH,'pages')      # 获取保存页面类的目录路径
REPORTPATH = os.path.join(BASEPATH,'reports')    # 获取保存测试报告的目录路径
URL = 'http://192.168.1.19:8080/oa/login.jsp'
def get_test_data(file):
    '''
    读取测试数据
    :param file: 保存测试数据的csv文件
    :return: 读取到的数据
    '''
    with open(file,'r') as f:  # 打开测试数据文件
        data = []
        fo = csv.reader(f)  # csv调用reader()方法，读取csv文件的内容，返回一个对象
        # print(fo)   <_csv.reader object at 0x10463e748>
        for i in fo:  # 遍历返回的对象，将每一行的内容保存为一个列表
            data.append(i)
            # [['admin', '123456'], ['admin', ''], ['', 'sys123456'], ['admin', 'sys123456']]
    return data
print(get_test_data(DATAPATH+'/set_email_data.csv'))
def send_mail(file):
    msg = MIMEMultipart()
    msg.attach(MIMEText('hasaki very good,且随疾风前行，身后问号满屏', 'plain', 'utf-8'))
    f_addr = '750507589@qq.com'
    pwd = 'aelauaqjqfjrbedj'
    smtp_server = 'smtp.qq.com'
    to_addr = ['601718164@qq.com']

    msg['from'] = Header('年薪百万的测试工程师!!!<%s>' % (f_addr))
    msg['to'] = Header('瓜皮中单<%s>' % (to_addr))
    msg['subject'] = Header('我打中单，亚索贼六', 'utf-8').encode()

    att = MIMEText(open(REPORTPATH + '/' + file, 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename = "test report.html"'
    msg.attach(att)
    server = smtplib.SMTP(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(f_addr, pwd)
    server.sendmail(f_addr, to_addr, msg.as_string())
    server.quit()

def get_current_time():
    t = time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())
    return t

def get_report(t):
    r = os.listdir(REPORTPATH)
    file = ''
    for i in r:
        temp = i.split('.')
        if temp[0] == t:
            file = i
    return file
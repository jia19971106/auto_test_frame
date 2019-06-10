import unittest,time
from utils.HTMLTestReportCN import HTMLTestRunner  # 导入HTMLTestRunner，用于创建测试执行对象
import utils.utils as ut
# 加载指定目录下的所有测试用例文件中的测试用例，测试用例的文件名必须以test开头
cases_dir = ut.CASESPATH  # 指定保存测试用例文件的目录
# 加载指定目录下所有以test开头的.py文件中测试用例
# discover(path,pattern)
# path，表示测试用例文件所在目录
# pattern，表示需要加载的用例文件名的格式，默认参数
cases = unittest.defaultTestLoader.discover(cases_dir,pattern='test_set_email.py')
case_cout = cases.countTestCases()  # 返回测试套件中的用例数量
print(f'用例总数：%d' %(case_cout))
time.sleep(2)
# 获取系统当前时间，YYYY-MM-DD H-M-S
t = ut.get_current_time()
# 创建运行对象，执行测试
# 使用当前时间作为测试报告文件名，避免以前的报告被覆盖
# f = open(t+'.html','wb')  # 以二进制写的方式打开文件
with open(ut.REPORTPATH+'/'+t+'.html','wb') as f:
    runner = HTMLTestRunner(stream=f,title='协同OA测试报告')
    runner.run(cases)

file = ut.get_report(t)
ut.send_mail(file)


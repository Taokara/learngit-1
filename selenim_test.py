import unittest
suite = unittest.defaultTestLoader.discover("./case","test_*.py")
runner = unittest.TextTestRunner()
runner.run(suite)
# 导入用例并执行

from HTMLTestReportCN import HTMLTestRunner
test_dir="./case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
f=open("./result.html","wb")
runner = HTMLTestRunner(stream=f,title="冒烟测试",description="纤细信息")
runner.run(discover)
f.close()
# 生成报告方式一

import unittest
import time
from BeautifulReport import BeautifulReport
test_dir="./case"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test_*.py")
BeautifulReport(discover).report(description=u"自动化测试报告",log_path="./",
                                 filename=time.strftime("%Y-%m-%d %H_%M_%S"))
# 生成报告方式二



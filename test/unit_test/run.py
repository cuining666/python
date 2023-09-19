# __author: ioi
# date: 2021/8/7
# 批量执行测试模块，生成测试报告
import unittest

# 只支持py2
# import HTMLTestRunner

if __name__ == '__main__':
    # 加载当前目录下所有有效测试模块，'.'表示当前目录
    testSuite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(testSuite)
    # with open("report.html", 'wb') as fp:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='report result', verbosity=2, description='desc')
    #     runner.run(testSuite)

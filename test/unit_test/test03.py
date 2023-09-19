# __author: ioi
# date: 2021/8/7
# 测试执行顺序
import unittest

from unit_test.calc import Clac


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.c = Clac()

    def test_add(self):
        self.assertEqual(MyTest.c.add_func(1, 2, 3), 6, 'test add fail')

    def test_sub(self):
        self.assertEqual(MyTest.c.sub_func(2, 1, 3), -2, 'test sub fail')

    # 忽略测试方法
    @unittest.skip('skipping')
    def test_mul(self):
        self.assertEqual(Clac.mul_func(2, 3, 5), 30, 'test mul fail')

    def test_div(self):
        self.assertEqual(Clac.div_func(8, 2, 4), 1, 'test div fail')


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(MyTest("test_mul"))
    suite.addTest(MyTest("test_div"))
    suite.addTest(MyTest("test_add"))
    suite.addTest(MyTest("test_sub"))
    runner = unittest.TextTestRunner()
    runner.run(suite)

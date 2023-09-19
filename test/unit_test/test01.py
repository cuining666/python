# __author: ioi
# date: 2021/7/31
import unittest


class Myclass():
    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b


class Mytest(unittest.TestCase):
    def setUp(self) -> None:
        self.a = 3
        self.b = 1
        print("----setUp")

    def tearDown(self) -> None:
        print("----tearDown")

    @classmethod
    def setUpClass(cls) -> None:
        print("----setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("----tearDownClass")

    def testsum(self):
        self.assertEqual(Myclass.sum(self.a, self.b), 4, 'test sum fail')

    def testsub(self):
        self.assertEqual(Myclass.sub(self.a, self.b), 2, 'test sub fail')


if __name__ == '__main__':
    unittest.main()

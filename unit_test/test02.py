# __author: ioi
# date: 2021/7/31
# 测试集合
import random
import unittest


class TestSequenceFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.seq = range(10)

    def tearDown(self) -> None:
        pass

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        # 验证执行的语句是否抛出异常
        with self.assertRaises(ValueError):
            # 列表中随机取20个数
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)


class TestDictValueFormatFunctions(unittest.TestCase):

    def setUp(self) -> None:
        self.seq = list(range(10))

    def tearDown(self) -> None:
        pass

    def test_shuffle(self):
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(10)))
        self.assertRaises(TypeError, random.shuffle, (1, 2, 3))


if __name__ == '__main__':
    testCase1 = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
    testCase2 = unittest.TestLoader().loadTestsFromTestCase(TestDictValueFormatFunctions)
    suite = unittest.TestSuite([testCase1, testCase2])
    # verbosity<=0 输出结果中不提示执行成功的用例数
    # verbosity=1 输出结果中仅以点表示执行成功的用例数
    # verbosity>=2 可以输出每个用例执行的详细信息
    unittest.TextTestRunner(verbosity=2).run(suite)

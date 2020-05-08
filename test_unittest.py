import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDpwnClass")


    def setUp(self) -> None:
        print("setup")


    def tearDown(self) -> None:
        print("tearDown")


    def test_case01(self):
        print("testcase01")
        self.assertEqual(3, 3, "判断不相等")
        self.assertIn('owen', 'owensir')

    def test_case02(self):
        print("testcase02")
        self.assertEqual(3, 3, "判断不相等")
        self.assertIn('owen', 'owensir')

    @unittest.skipIf(1+1==2, "满足条件时跳过该条用例")
    def test_case03(self):
        print("testcase03")
        self.assertEqual(3, 3, "判断不相等")
        self.assertIn('owen', 'owensir')

class demo1(unittest.TestCase):
    def test_demo1_case1(self):
        print("test_demo1_case1")

    def test_demo1_case2(self):
        print("test_demo1_case2")


class demo2(unittest.TestCase):
    def test_demo2_case1(self):
        print("test_demo2_case1")

    def test_demo2_case2(self):
        print("test_demo2_case2")


if __name__ == '__main__':
    report_title = "测试用例执行报告"
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'TestReport.html'

    #unittest.main()
    # suite=unittest.TestSuite()
    # #添加用例到套件--指定用例执行
    # suite.addTest(demo("test_case01"))
    # suite.addTest(demo1("test_demo1_case2"))
    #  unittest.TextTestRunner().run(suite)


    #将测试类加载到套件---指定类执行
    suit1= unittest.TestLoader().loadTestsFromTestCase(demo)
    suit2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    suit3 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    suitall= unittest.TestSuite([suit1,suit2,suit3])
    #unittest.TextTestRunner().run(suitall)

    #执行指定路径下所有以test开头的py文件
    # discover= unittest.defaultTestLoader.discover("./","test*.py")
    # unittest.TextTestRunner().run(discover)

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description="测试用例")
        runner.run(suitall)


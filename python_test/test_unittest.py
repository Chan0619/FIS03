import unittest


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('teardown class')

    def setUp(self) -> None:
        print('setup')

    def tearDown(self) -> None:
        print('teardown')

    def test_case01(self):
        print('testcase01')
        self.assertEqual(2, 2, '判断相等')  # 当程序出错时显示msg='判断相等'
        self.assertIn('h', 'this')  # 判断包含

    def test_case02(self):
        print('testcase02')
        self.assertEqual(2, 2, '判断相等')

    # @unittest.skipIf(1 + 1 == 2, '跳过这条用例')
    @unittest.skip("这次不想执行这个测试")  # 跳过此方法，不执行
    def test_case03(self):
        print('testcase03')
        self.assertEqual(2, 2, '判断相等')


class demo1(unittest.TestCase):
    def test_demo1_case0(self):
        print('test_demo1 case0')

    def test_demo1_case1(self):
        print('test_demo1 case1')


class demo2(unittest.TestCase):
    def test_demo2_case0(self):
        print('test_demo2 case0')

    def test_demo2_case1(self):
        print('test_demo2 case1')


if __name__ == '__main__':
    # 1. unittest.main()
    # unittest.main()  # 将当前页面所有以test_开头的测试用例全部加载并执行
    # 2. 加入容器中执行
    # suite = unittest.TestSuite()
    # suite.addTest(demo('test_case01'))
    # suite.addTest(demo1('test_demo1_case0'))
    # unittest.TextTestRunner().run(suite)
    # 3. 同时测试多个类
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suite = unittest.TestSuite([suite1,suite2])
    # unittest.TextTestRunner().run(suite)
    # 4. 匹配某个目录下所有以test开头的py文件，执行这些文件下的所有测试用例
    discover = unittest.defaultTestLoader.discover('../python/', 'test*.py')
    unittest.TextTestRunner().run(discover)

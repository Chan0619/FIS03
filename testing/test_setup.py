class TestDemo():

    def setup(self):
        print('方法级别 setup')

    def teardown(self):
        print('方法级别的 teardown')

    def test_demo1(self):
        print('test_demo1')

    def Test_demo2(self):
        print('')

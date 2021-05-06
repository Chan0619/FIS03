def setup_module(self):
    print('模块级别 setup')


def teardown_module(self):
    print('模块级别的 teardown')


def setup_function(self):
    print('函数级别 setup')


def teardown_function(self):
    print('函数级别的 teardown')


def test_fun():
    print('测试函数')


class TestDemo:

    def setup_class(self):
        print('类级别 setup')

    def teardown_class(self):
        print('类级别的 teardown')

    def setup(self):
        print('方法级别 setup')

    def teardown(self):
        print('方法级别的 teardown')

    def test_demo1(self):
        print('test_demo1')

    def test_demo2(self):
        print('test_demo2')


class TestDemo1:

    def setup_class(self):
        print('类级别 setup')

    def teardown_class(self):
        print('类级别的 teardown')

    def setup(self):
        print('方法级别 setup')

    def teardown(self):
        print('方法级别的 teardown')

    def test_demo1(self):
        print('test_demo1')

    def test_demo2(self):
        print('test_demo2')

# @pytest.fixture(scope='module')  # function-函数 class-类 module-模块py文件 session-多个文件调用一次
# def connectdB():
#     print('连接数据库操作')
#     yield
#     print('断开数据库连接')


class TestDemo:

    def test_a(self, connectdB):
        print('测试用例a')

    def test_b(self, connectdB):
        print('测试用例b')


class TestDemo1():

    def test_a(self, connectdB):
        print('测试用例a')

    def test_b(self, connectdB):
        print('测试用例b')

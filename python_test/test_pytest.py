# pytest测试框架
import pytest


def func(x):
    return x + 1


# 参数化
@pytest.mark.parametrize('a,b', [
    (1, 2),
    (10, 20),
    ('a', 'a1'),
    (3, 4),
    (5, 6)
])
def test_answer(a, b):
    assert func(a) == b


def test_answer1():
    assert func(4) == 5


# 装饰器
@pytest.fixture()
def login():
    print('登录操作')
    username = 'chan'
    return username


class TestDemo:
    def testa(self):
        print('a')

    # test_a需要提前登录，就传入login，在执行测试用例前会先执行login方法
    def test_a(self, login):
        print(f' username = {login}')

    def test_b(self):
        print('b')

    def test_c(self, login):
        print(f'c username = {login}')


if __name__ == '__main__':
    # pytest.main(['test_pytest.py'])
    # 相当于命令号执行 python test_pytest.py
    # pytest.main(['test_pytest.py::test_answer1','-v'])
    # pytest.main(['test_pytest.py::TestDemo','-v'])
    pytest.main(['test_pytest.py::TestDemo::test_b', '-v'])
    # 在terminal中执行python test_pytest.py查看，
    # 不加'-v'则会在输出时在文件名后面以.的形式表示执行了几个测试用例

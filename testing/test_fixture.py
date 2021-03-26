import pytest


# @pytest.fixture(autouse=True)  # 默认为False，不推荐使用
@pytest.fixture()
def login():
    print('登录操作')
    username = 'chan'
    password = '123'
    token = 'token123'
    yield [username, password, token]
    print('登出操作')
    # 有teardown的操作，就用yield返回数据，
    # 如果没有teardown操作，就把yield换成return
    # yield 和return都可以返回数据


# 提前登录
# def test_case1(login):
def test_case1(connectdB):
    print(f'login information: {login}')
    print('测试用例1')


def test_case2():
    print('测试用例2')


# 提前登录
def test_case3():
    print('测试用例3')


# 提前登录
# @pytest.mark.usefixtures('login')
def test_case4():
    print('测试用例4')

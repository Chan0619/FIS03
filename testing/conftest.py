import pytest


@pytest.fixture(scope='session')  # function-函数 class-类 module-模块py文件 session-多个文件调用一次
def connectdB():
    print('连接数据库操作')
    yield
    print('断开数据库连接')

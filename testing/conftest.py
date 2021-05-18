import pytest
import yaml
import os

from python_pytest.calc import Calculator

yaml_file_path = os.path.dirname(__file__) + '/datas/calc.yaml'
print(yaml_file_path)

with open(yaml_file_path) as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


@pytest.fixture(params=add_datas, ids=myid)
def get_add_datas(request):
    print('开始计算')
    data = request.param
    print(f'request.param 里面的测试数据：{data}')
    yield data
    print('结束计算')


@pytest.fixture(scope='session')
def connectdB():
    print('连接数据库操作')
    yield
    print('断开数据库连接')


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc

import yaml
import pytest

from python_pytest.calc import Calculator

# ***********************************
# 查看第10章的第五节视频的20-30分钟
with open('./datas/calc.yaml') as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)


# @pytest.fixture(params=add_datas,ids=myid)
# def get_add_datas(request):
#     print('开始计算')
#     data = request.param
#     print(f'request.param 里面的测试数据：{data}')
#     yield data
#     print('结束计算')

# **********************************

def test_a():
    print('测试用例a')


def func():
    print('普通函数')


class TestCalc():
    def setup_class(self):
        print('开始计算')
        # 实例化计算器类
        self.calc = Calculator()
    def teardown_class(self):
        print('计算结束')

    @pytest.mark.parametrize('a, b, expect', add_datas
        , ids=myid)
    def test_add(self, a, b, expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用 add 方法
        result = self.calc.add(a, b)
        # 判断result是浮点数，并处理
        if isinstance(result, float):
            result = round(result, 2)
        # 得到结果之后，要有断言
        assert result == expect

    def test_add2(self):
        result = self.calc.add(0.1, 0.2)
        assert round(result, 2) == 0.3

    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add 方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 得到结果之后，要有断言
    #     assert result == 0.2
    #
    # def test_add2(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add 方法
    #     result = self.calc.add(-1, -1)
    #     # 得到结果之后，要有断言
    #     assert result == -2

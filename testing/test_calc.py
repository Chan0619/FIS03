import yaml
import pytest
from python_pytest.calc import Calculator


# 放入conftest中了
# with open('./datas/calc.yaml') as f:
#     datas = yaml.safe_load(f)['add']
#     add_datas = datas['datas']
#     print(add_datas)
#     myid = datas['myid']
#     print(myid)

# @pytest.fixture(scope='class')
# def get_calc():
#     print('获取计算器实例')
#     calc = Calculator()
#     return calc

# @pytest.fixture(params=add_datas, ids=myid)
# def get_add_datas(request):
#     print('开始计算')
#     data = request.param
#     print(f'request.param 里面的测试数据：{data}')
#     yield data
#     print('结束计算')


class TestCalc():
    # def setup_class(self):
    #     print('开始计算')
    #     # 实例化计算器类
    #     self.calc = Calculator()
    # def teardown_class(self):
    #     print('计算结束')

    # @pytest.mark.parametrize('a, b, expect', add_datas, ids=myid)
    def test_add(self, get_calc, get_add_datas):
        result = None
        try:
            # 实例化计算器类
            # calc = Calculator()
            # 调用 add 方法
            result = get_calc.add(get_add_datas[0], get_add_datas[1])
            # 判断result是浮点数，并处理
            if isinstance(result, float):
                result = round(result, 2)
        except Exception as e:
            print(e)

        # 得到结果之后，要有断言
        assert result == get_add_datas[2]

    def test_add2(self, get_calc):
        result = get_calc.add(0.1, 0.2)
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

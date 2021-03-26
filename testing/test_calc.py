from python_code.calc import Calculator


def test_a():
    print('测试用例a')


def func():
    print('普通函数')


class TestCalc():

    def test_add(self):
        # 实例化计算器类
        calc = Calculator()
        # 调用add 方法
        result = calc.add(1, 1)
        # 得到结果之后，要有断言
        assert result == 2

        def test_add1(self):
            # 实例化计算器类
            calc = Calculator()
            # 调用add 方法
            result = calc.add(0.1, 0.1)
            # 得到结果之后，要有断言
            assert result == 0.2

        def test_add2(self):
            # 实例化计算器类
            calc = Calculator()
            # 调用add 方法
            result = calc.add(-1, -1)
            # 得到结果之后，要有断言
            assert result == -2

# pytest 数据参数化
import pytest
import yaml


class TestData:
    # @pytest.mark.parametrize('a,b',[(10,20),(10,5),(3,9)])
    # @pytest.mark.parametrize(('a','b'),[(10,20),(10,5),(3,9)])
    # @pytest.mark.parametrize(['a','b'],[(10,20),(10,5),(3,9)])
    # 使用字符串和元祖、列表的区别，列表可以改变  ->['a','b'].append()
    # 使用yaml加载
    @pytest.mark.parametrize(['a', 'b'], yaml.safe_load(open('./data.yaml')))
    def test_data(self, a, b):
        print(a + b)

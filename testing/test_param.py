import pytest


@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    print('获取测试用例')
    return data


def test_case1(login1):
    print(login1[0])
    print('测试用例1')

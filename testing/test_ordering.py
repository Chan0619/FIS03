from time import sleep

import pytest


@pytest.mark.run(order=2)
# @pytest.mark.last
def test_foo():
    sleep(1)
    assert True


@pytest.mark.run(order=1)
# @pytest.mark.first
def test_bar():
    sleep(1)
    assert True


def test_bar1():
    sleep(1)
    assert True

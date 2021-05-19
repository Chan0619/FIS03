# -*- coding:utf-8 -*-
# @Author: Phoebe
# @Time:   2021/5/20 0:36
# @File:   test_rerun.py
from time import sleep


def test_rerun():
    sleep(0.5)
    assert 1 == 2


def test_rerun1():
    sleep(0.5)
    assert 2 == 2


def test_rerun2():
    sleep(0.5)
    assert 3 == 2

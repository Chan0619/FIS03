# from gift import have_gift
import gift

"""
from import 与import 的区别:
import 引用了模块的地址
from import 相当于复制了一份变量到本地
"""


# 发礼物
def send():
    print('发送礼物')
    # global have_gift
    # have_gift = True
    gift.have_gift = True
    # 使用from import时gift.have_gift的值会发生改变
    print(id(gift.have_gift))

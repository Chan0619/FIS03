def div(a, b):
    return a / b


f = open('data.txt')
try:
    print(div(1, 1))
    list1 = [1, 2, 3]
    print(list1[2])

    f.readline()

except Exception as e:
    print(e)
else:
    print('没有异常时执行')
finally:  # finally 最终都会被执行，无论有无异常
    print('finally')
    f.close()


class MyException(Exception):
    def __init__(self, msg):
        print(f'这是一个异常：{msg}')


def set_age(age):
    if age <= 0 or age > 200:
        # raise ValueError
        raise MyException(f'值错误：{age}')
    else:
        print(f'设置的年龄为：{age}')


set_age(-1)

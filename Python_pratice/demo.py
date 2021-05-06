a = 1


def fun():
    # global a
    a = 2
    print(f"方法中a的值：{id(a)}")  # 打印a的内存地址
    print(f'变量a的值：{a}')
    print('这是方法')


print(a)
print(f'初始值a：{id(a)}')
fun()
print(f"最后a的值：{id(a)}")
print(a)

if __name__ == '__main__':
    print('start')
    fun()

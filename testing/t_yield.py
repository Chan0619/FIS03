# yield 生成器
def provider():
    # 循环读取
    for i in range(10):
        print('开始操作')
        # 相当于 return i，记录上一次执行的位置
        yield i
        print('结束操作')


p = provider()
# 打印的对象类型就是生成器 generator
# 在生成器中想拿到里面的内容，使用必须调用next()方法
# print(p)
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))
for i in p:
    print(i)

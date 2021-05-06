# 1 列表
def list_basic():
    list_t = [666, 2]
    list_t.append(1)
    list_t.insert(0, 333)
    # list_t.remove(333)
    # print(list_t.pop(0))
    # list_t.sort()  # 升序
    # list_t.sort(reverse=True)  # 降序
    # list_t.reverse()  # 反转
    print(list_t)


# list_basic()
def list_squre():
    list_squre = []
    for i in range(1, 4):
        list_squre.append(i ** 2)
    print(list_squre)

    # 列表生成式
    list_squre2 = [i ** 2 for i in range(1, 4)]
    print(list_squre2)

    list_squre3 = [i ** 2 for i in range(1, 4) if i != 1]
    print(list_squre3)

    list_squre4 = []
    for i in range(1, 4):
        for j in range(1, 4):
            list_squre4.append(i * j)

    list_squre4 = [i * j for i in range(1, 4) for j in range(1, 4)]
    print(list_squre4)


# list_squre()

# 2 元祖
def tuple_basic():
    # 2 元祖的定义
    # tuple_t = (1, 2, 3)
    # tuple_t1 = 1, 2, 3
    # print(tuple_t)
    # print(type(tuple_t))
    # print(tuple_t1)
    # print(type(tuple_t1))

    # 元祖的不可变特性   --变量指针不变
    # list1 = [1, 2, 3]
    # list1[0] = 'q'
    # print(list1)
    # tuple1 = (1, 2, 3)
    # tuple1[0] = 'q'

    # a = [1, 2, 3]
    # tuple1 = (1, 2, a)
    # print(id(tuple1[2]))
    # tuple1[2][0] = 'a'
    # print(id(tuple1[2]))
    # print(tuple1)

    # 内置函数
    a = (1, 2, 3, 1)
    print(a.count(1))
    print(a.index(1, 1, 4))
    print(a)


# tuple_basic()

# 3 集合
def set_basic():
    # 集合定义
    # a={1}
    # b=set()
    # print(len(b))
    # print(type(a))
    # print(type(b))

    # 内置函数
    a = {1, 2, 3}
    b = {1, 4, 5}
    print(a.union(b))  # 并集
    print(a.intersection(b))  # 交集
    print(a.difference(b))  # 差集  --a有b没有的元素
    a.add('a')  # 集合添加元素
    print(a)

    print({i for i in 'fjajgajdaddahdfdjhgjfaaa'})  # 字符串去重后的集合
    # {'a', 'f', 'g', 'd', 'h', 'j'}
    c = 'jgirgokafgaaaaa'
    print(set(c))  # {'i', 'k', 'g', 'r', 'a', 'o', 'f', 'j'}


# set_basic()

# 4 字典
def dict_basic():
    # 字典定义
    dict_d = {'a': 1, 'b': 2}
    dict_d2 = dict(a=1, b=2)

    print(dict_d)
    print(type(dict_d))
    print(dict_d2)
    print(type(dict_d2))

    print(dict_d.keys())  # 得到所有 key
    print(dict_d.values())  # 得到所有 value

    print(dict_d.pop('a'))  # 1；返回value值，并删除key为a的键值对
    print(dict_d)  # {'b': 2}

    print(dict_d.popitem())  # popitem()随机删除键值对。返回被删除的键值对
    print(dict_d)

    a = {}
    b = a.fromkeys((1, 2, 3), 'a')  # 分别把元祖里面的参数当做key值，建立一个新的列表。
    print(b)  # {1: 'a', 2: 'a', 3: 'a'}

    # 列表推导式
    print({i: i * 2 for i in range(1, 3)})  # {1: 2, 2: 4}

# dict_basic()

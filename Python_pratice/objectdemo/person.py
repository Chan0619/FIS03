"""# class 类名:
    # 静态属性
    # 动态方法"""


class Person:  # 类名 驼峰命名法
    # 属性
    name: str = None
    age: int = 0
    gender: str = '男'
    # 私有属性
    __money: float = 0

    def get_money(self):
        return self.__money

    def __init__(self, name, age, gender, money):
        print('构造函数')
        self.name = name
        self.age = age
        self.gender = gender
        self.__money = money

    # 方法
    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')

    # @classmethod
    def run(self):
        print(f'{self.name} is running')


class FunnyMan(Person):
    skill: str = ''

    def __init__(self, skill, name, age, gender, money):
        self.skill = skill
        super().__init__(name, age, gender, money)

    def fun(self):
        print(f'{self.name} is funny， his kill {self.skill}')


st = FunnyMan('相声', 'ST', 32, '男', 10000)
print(st.name)
st.fun()

# 实例化对象
# ls = Person('李四', 22, '男', 1111)
# print(ls.name)
# print(ls.age)
# print(ls.get_money())
# ls.run()
#
# print(dir(ls))
# print(ls._Person__money)
#
# ls.name = '李小四'
# print(ls.name)
#
# Person.name = 'default_name'
# print(Person.name)
# print(ls.name)
#
# ls = Person('李四', 22, '男', 1111)

# 类
# print(Person.name)
# Person.run()  # 需要将方法变为类方法

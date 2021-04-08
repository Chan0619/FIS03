# 创建一个人类
# 通过class 关键字，定义了一个类
class Person:
    # 类变量
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    # 构造方法，在类实例化的时候被调用
    def __init__(self, name, age, gender, weight):
        # self.变量名的方式，访问到的变量，叫做实例变量
        self.name = name
        self.age = age
        self.gender = gender
        self.weight = weight

    def set_param(self, name, age):
        # self.name 代表类里面的name，
        # 等号后面的name是外面传过来的name
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} eating')

    def play(self):
        print(f'{self.name} playing')

    def jump(self):
        print(f'{self.name} jump')


# 类的实例化，创造了一个实例
zs = Person('张三', 20, '男', 66)
# zs.set_param('张三', 20)
zs.eat()
print(f'姓名：{zs.name}, 年龄：{zs.age}, 性别：{zs.gender}, 体重：{zs.weight}')

ls = Person('李四', 55, '男', 55)
print(f'姓名：{ls.name}, 年龄：{ls.age}, 性别：{ls.gender}, 体重：{ls.weight}')

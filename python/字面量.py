name = 'lilli'
age = 20
print('my name is %s，age is %d' % (name, age))
print('my name is {1}，age is {0}'.format(name, age))

list1 = [1, 2, 3]
dict1 = {'name': 'tom', 'gender': 'male'}
print('list is {},dict is{}'.format(list1, dict1))
print(f'my name is {name}，age is {age}，list is {list1[2]},dict is {dict1["name"]}')
print(f'my name is {name.upper()}')
print(f'result is {(lambda x: x + 1)(2)}')  # 写表达式有：时要加括号括起来

list_name = ['lili', 'tom', 'jerry']
print('we name :{} {} {}'.format(*list_name))  # 列表解包

print('my name is {name},gender is {gender}'.format(**dict1))  # 字典解包

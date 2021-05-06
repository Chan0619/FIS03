import os

# os.mkdir('11')  # 创建文件
# os.removedirs('11')  # 删除文件
# print(os.listdir('./'))  # 以列表形式列出当前路径中的文件，目录
# print(os.getcwd())  # 列出当前路径

print(os.path.exists('b'))  # 判断b文件是否存在,False表示不存在
# 判断是否存在b文件，如果文件不存在，则创建文件夹
if not os.path.exists('b'):
    os.mkdir('b')
# 判断b下面有没有test.txt文件，如果没有，则打开文件，写入
# if 后面为True时，才会执行下面的语句块
if not os.path.exists('b/test.txt'):
    f = open('b/test.txt', 'w')
    f.write('hello,python')
    f.close()

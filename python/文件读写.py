print(open('data.txt', ))
# f = open('data.txt',)
# print(f.readable())
# # print(f.readlines())
# print(f.readline())
# print(f.readline())
# f.close()

# with 语句块，可以将文件打开操作完后自动关闭
# 图片读取需要使用rb  读取二进制的格式
# 正常文本rt，默认
with open('data.txt') as f:
    # print(f.readlines())
    while True:
        line = f.readline()
        if line:
            print(line, end='')
        else:
            break

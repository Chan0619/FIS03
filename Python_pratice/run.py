# 导入模块时会先解释执行模块里面的方法。
# 放在if __name__ == '__main__':时就不会执行
from Python_pratice.sendgift import send, show

print(f"name变量的值为 {__name__}")
if __name__ == '__main__':
    send()
    show()

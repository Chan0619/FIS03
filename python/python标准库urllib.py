import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response)
print(response.status)
print(response.read())
print(response.headers)  # 头部信息

import math

print(math.ceil(1.5))
print(math.floor(1.5))
print(math.sqrt(25))

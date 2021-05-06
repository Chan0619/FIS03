import requests

r = requests.get('http://www.baidu.com')
# r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
# r = requests.post('http://httpbin.org/post', data = {'key':'value'})

# print(r.status_code)  # 200 响应状态码
# print(r.headers['content-type'])  # 'application/json; charset=utf8'
# print(r.encoding)  # 'utf-8' 打印编码
# r.encoding = 'utf8'  # 修改编码
# print(r.text)  # 响应内容 '{"type":"User"...'
# r.json()  # {'disk_usage': 368627, 'private_gists': 484, ...}

import yaml

# yaml格式 定义字典类型
document = """
  a: 1
  b:
    c: 3
    d: 4
"""
# print(yaml.load(document))
# safe_load()将yaml对象加载成python的字典对象
print(yaml.safe_load(document))
print(type(yaml.safe_load(document)))
#
print(yaml.dump(yaml.safe_load(document)))

# yaml格式 定义列表类型
# - 加空格加'列表的值'定义列表
print(yaml.safe_load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
"""))

# yaml 定义文档
# 使用 --- 隔开
documents = """
---
name: The Set of Gauntlets 'Pauraegen'
description: >
    A set of handgear with sparks that crackle
    across its knuckleguards.
---
name: The Set of Gauntlets 'Paurnen'
description: >
  A set of gauntlets that gives off a foul,
  acrid odour yet remains untarnished.
---
name: The Set of Gauntlets 'Paurnimmen'
description: >
  A set of handgear, freezing with unnatural cold.
"""
for data in yaml.safe_load_all(documents):
    print(data)

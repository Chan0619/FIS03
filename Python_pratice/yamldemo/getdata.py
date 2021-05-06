import yaml


# yaml.safe_load() 将yaml数据流转成Python对象
# yaml.safe_dump() 将Python对象转成yaml数据格式
def get_datas():
    with open('data.yml', encoding='utf8') as f:
        datas = yaml.safe_load(f)
        return datas


print(get_datas())
# print(yaml.safe_dump(get_datas()))

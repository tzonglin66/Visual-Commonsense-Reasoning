# 作 者：田宗林
# 时 间：2021/7/24
# 字典元素的获取
    # 1. dict_name['key']  # 如果key不存在，抛出KeyError异常
    # 2. dict_name.get('key')  # 如果key不存在，返回None
    # 3. dict_name.get('key', value)  # 如果key不存在，返回指定的value值

info = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}
print(info['姓名'])
# print(info['place'])
print(info.get('姓名'))
print(info.get('place'))
print(info.get('place', 'China'))

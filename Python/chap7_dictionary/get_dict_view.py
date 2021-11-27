# 作 者：田宗林
# 时 间：2021/7/24
# 获取字典视图一个方法，通过list函数--->列表
    # keys()：获取字典中的所有key
    # values()：获取字典所有value
    # items()：获取字典所有key， value对

info = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}

keys = info.keys()
print(keys)
print(type(keys))
print(list(keys))

values = info.values()
print(values)
print(type(values))
print(list(values))

items = info.items()
print(items)
print(type(items))
print(list(items))  # 转换后的列表元素由元组组成
# 作 者：田宗林
# 时 间：2021/11/2
# 字典所支持的操作
d = {'name': 'Temm', "age": 25, "school": 'CCNU'}


print(list(d))  # 返回字典 d 中使用的所有键的列表

print(len(d))  # 返回字典 d 中的项数

print(iter(d), next(iter(d)))  # 返回以字典的键为元素的迭代器——iter(d.keys()) 的快捷方式


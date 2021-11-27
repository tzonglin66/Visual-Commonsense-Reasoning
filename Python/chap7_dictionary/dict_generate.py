# 作 者：田宗林
# 时 间：2021/7/24
# 字典生成式
    # 内置函数zip()
        # 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
        # 用list将zip的返回值转为列表
        # 以长度短的对象为基准打包
info = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}
print(info)
keys = list(info.keys())
values = list(info.values())
# lst = list(zip(keys, values))
# print(lst)
# print(type(lst))
generate_info = {key: value for key, value in zip(keys, values)}
print(generate_info)

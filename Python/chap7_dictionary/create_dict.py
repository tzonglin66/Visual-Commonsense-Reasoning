# 作 者：田宗林
# 时 间：2021/7/24
# 字典
    # python内置的数据结构之一，与列表一样是一个可变序列
    # 以键值对的方式存储数据，是一个无序的序列
    # 创建方式1：dict_name={'key1':val1, 'key2':val2, ...}
    # 创建方式2：dict(key1=val1, key2=val2, ...)  # dict是python内置函数
    # 空字典：empty_dict={}
    # 字典中key不允许重复
    # 创建方式3：字典生成式  ---> Reference dict_generate.py
info1 = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}
info2 = dict(姓名='田宗林', age=25, gender='male')
info3 = {}
info4 = dict()
print(info1)
print(info2)
print(info3)
print(info4)

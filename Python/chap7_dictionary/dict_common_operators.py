# 作 者：田宗林
# 时 间：2021/7/24
# 字典的常用操作
    # key的判断：key in dict_name OR key not in dict_name ---> TRUE & FALSE
    # key-value的删除：del dict_name['key']  # dict_name.clear() 清空字典的元素
    # key-value的增加/修改：dict_name['key']=value

info = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}
print('姓名' in info)
print('姓名' not in info)

info['place'] = 'China'  # 新增键值对
print(info)

info['place'] = 'GuangXi'
print(info)

del info['place']
print(info)
info.clear()
print(info)

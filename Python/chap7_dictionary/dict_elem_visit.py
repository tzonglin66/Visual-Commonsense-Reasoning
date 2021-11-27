# 作 者：田宗林
# 时 间：2021/7/24
# 字典元素的遍历

info = {'姓名': '田宗林', 'age': 25, 'gender': 'male'}
for item in info:
    print(item, info[item], info.get(item))  # item是info中的key，然后利用[] OR get方法获取对应的value

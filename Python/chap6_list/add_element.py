# 作 者：田宗林
# 时 间：2021/7/31
# 列表元素的增加
    # append() 在列表的末尾添加一个元素
    # extend() 在列表的末尾至少添加一个元素
    # insert() 在列表的任意位置添加一个元素
    # 切片 在列表的任意位置添加至少一个元素

lst = ['Hell0', 'python', 1, 'Hello', 'python']
lst.append(['加油', 'Temm'])
print(lst)
lst.extend(['2', 3])
print(lst)
lst.insert(2, [4, 5])
print(lst)
lst[2:] = [4, 5]
print(lst)

# 作 者：田宗林
# 时 间：2021/7/24
# 获取列表中指定元素的索引：list_name.index(element_name, start_ind, stop_ind)
    # 如果列表中存在N个相同的元素，只返回相同元素中的第一个元素的索引
    # 如果查的元素不存在，则抛出ValueError
    # 可在指定的index间查找：index in [start_ind, stop_ind)

lst = ['Hell0', 'python', 1, 'Hello', 'python']
print(lst.index('python'))
print(lst.index('Hello', 2, 4))
print(lst.index('world'))


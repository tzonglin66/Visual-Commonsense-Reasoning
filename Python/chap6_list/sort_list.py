# 作 者：田宗林
# 时 间：2021/7/31
# 列表元素的排序
    # 调用sort()方法，可以指定reverse=True，进行降序排序
    # 调用sorted()函数  ---->产生新的列表
lst = ['Hell0', 'python', '1', 'Hello', 'python']
print('排序前的列表：', lst, id(lst))
lst.sort()
print('排序后的列表：', lst, id(lst))
new_lst = sorted(lst, reverse=True)
print('sorted 函数排序产生的列表：', new_lst, id(new_lst))

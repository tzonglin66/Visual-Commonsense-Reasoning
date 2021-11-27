# 作 者：田宗林
# 时 间：2021/7/24

# 获取列表中指定索引的元素：list_name[ind]
    # 正向索引[0, N-1]
    # 负向索引[-N, -1]
    # 指定索引不存在，抛出IndexError

lst = ['Hell0', 'python', 1, 'Hello', 'python']
print(lst[2])
print(lst[-3])
print(lst[5])

# 作 者：田宗林
# 时 间：2021/10/5
# 内置函数enumerate(iterable, start)
# 返回一个枚举对象，iterable 必须是一个序列，或iterator，或其他支持迭代的对象

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))

print(list(enumerate(seasons, start=1)))
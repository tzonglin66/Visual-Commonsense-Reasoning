# 作 者：田宗林
# 时 间：2021/10/29
# 内置函数 iter(object)，返回一个 iterator 对象[迭代器类型]
a = iter(range(5))
print(a)
print(next(a), next(a))
print(list(a))
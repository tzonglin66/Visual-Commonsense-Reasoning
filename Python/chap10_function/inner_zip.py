# 作 者：田宗林
# 时 间：2021/11/3
# 内置函数 zip(*iterables, strict=False)
"""
在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组:
zip() 返回元组的迭代器，其中第 i 个元组包含的是每个参数迭代器的第 i 个元素
    会把行变成列，把列变成行，类似于矩阵转置
zip() 是延迟执行的：直至迭代时才会对元素进行处理，比如 for 循环或放入 list 中
"""
for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
    print(item)
# zip() 与 * (解包)运算符相结合可以用来拆解一个列表:
x = [1, 2, 3]
y = [4, 5, 6]
print(list(zip(x, y)))

x2, y2 = zip(*zip(x, y))

print(x == list(x2) and y == list(y2))


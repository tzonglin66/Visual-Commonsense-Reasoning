# 作 者：田宗林
# 时 间：2021/7/24
# 元组
    # Python 内置的数据结构之一，是一个不可变序列
    # tuple_name = (val1, val2, ...)
# 序列
    # 可变序列：可以对序列进行增、删、改操作，对象地址不发生改变 <---- 列表、字典
    # 不可变序列 <--- 字符串、元组

tup = (1, 2, 3)
print(type(tup))
print(tup)

lst = [1, 2, 3]
print(id(list))
lst.append(5)
print(id(list))

st = 'Hello'
print(id(st))
st = st + ' Python'
print(id(st))

# 作 者：田宗林
# 时 间：2021/7/24
# 元组的创建
    # 直接()：tup = (val1, val2, ...)  # ()可
    # 内置函数tuple()：tup = tuple((val1, val2, ...))
    # 只含一个一个元素的元组用, 和 ()：tup = (val1,)  # , 不可省，否则tup为一个val1类型变量
    # 空元组：empty_tup = () OR empty_tup = tuple()
tup1 = ('name', 'age', 25)
print(tup1, type(tup1))

tup2 = tuple(('name', 'age', 25))
print(tup2, type(tup2))

tup3 = ('name',)
print(tup3, type(tup3))

tup4 = ()
print(tup4, type(tup4))
tup5 = tuple()
print(tup5, type(tup5))

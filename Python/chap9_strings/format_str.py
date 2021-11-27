# 作 者：田宗林
# 时 间：2021/8/6
"""
格式化字符串  ----> 字符串
# %作占位符：str(%,%,...) % (var1, var2, ...)
    # %s 字符串
    # %i OR %d 整数
    # %f 浮点数
    # 设置宽度和精度：s1 = '%10.3f' % 3.14159
# {}作占位符：str({0},{1},...).format(var1, var2, ...)
    # 设置宽度和精度：s2 = '{0:10.3f}'.format(3.14159)
# f格式化：fstr({var1},{var2},...)
"""

name = 'Temm'
age = 25
print('我叫%s，今年%d岁了，我真的叫%s' % (name, age, name))
print('我叫{0}，今年{1}岁了，我真的叫{0}'.format(name, age))
print(f'我叫{name}，今年{age}岁了，我真的叫{name}')
s1 = '%10.3f' % 3.14159
print(s1)
s2 = '{0:10.3f}'.format(3.14159)
print(s2)
print('12345678910')

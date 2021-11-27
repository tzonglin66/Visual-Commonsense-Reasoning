# 作 者：田宗林
# 时 间：2021/8/14
"""
匿名函数：不需要显式的指定函数名，用lambda开头，通常和其它函数搭配使用
fun_var = lambda arg1, arg2, ...:f(arg1, arg2, ...)
"""


def calc(x, y):
    return x**y


print(calc(2, 5))
# 等价于匿名函数calc_ano
calc_ano = lambda x, y: x**y
print(calc_ano(2, 5))

print('----------------------------')
res = map(lambda i: 2 * i if i % 2 else i, [1, 2, 3, 4])
for item in res:
    print(item)

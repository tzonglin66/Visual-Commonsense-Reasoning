# 作 者：田宗林
# 时 间：2021/8/14
"""
高阶函数：函数的参数或者返回值是函数（当作变量）
"""
from collections import Callable


def get_abs(n: float):
    if n < 0:
        n = - n
    return n


def add_abs(x, y, fun):
    return fun(x) + fun(y)


res = add_abs(2, -3, get_abs)
print(res)

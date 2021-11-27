# 作 者：田宗林
# 时 间：2021/10/29
# assert 词句
"""
语句的格式: assert 表达式, 返回数据  ---->  当表达式为False时, 触发AssertionError异常
"""


def func(a, b):
    assert a > b
    print(a)


func(2, 1)
func(1, 2)

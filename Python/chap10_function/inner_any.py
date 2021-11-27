# 作 者：田宗林
# 时 间：2021/11/2
# 内置函数any(iterable)
"""
如果 iterable 的任一元素为真值则返回 True
如果可迭代对象为空，返回 False
"""


# 等价于:
def t_any(iterable):
    for element in iterable:
        if element:
            return True
    return False


print(any([True, False]), t_any([True, False]))

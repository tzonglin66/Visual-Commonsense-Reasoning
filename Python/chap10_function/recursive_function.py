# 作 者：田宗林
# 时 间：2021/8/14
"""
递归函数
"""

# 逆序打印数字


def inverse(n: int):
    if n > 0:
        print(n % 10)
        inverse(n // 10)


inverse(106)

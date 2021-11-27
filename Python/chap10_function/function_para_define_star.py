# 作 者：田宗林
# 时 间：2021/7/8
# *后参数指定为关键字实参传递
# 形参定义顺序：位置形参 > (*args | *, var) > **args
def fun_a(a, b, *args1, **args2):
    pass


def fun_b(a, b, *, c, d, **args):
    pass

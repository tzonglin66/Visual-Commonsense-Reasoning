# 作 者：田宗林
# 时 间：2021/7/8
# 函数可变个数参数定义←不知道传递实参的个数
#   个数可变的位置参数：*args，至多一个，args把位置参数组合为一个元组
#   个数可变的关键字参数：**args，至多一个，args把所有关键字参数组合为一个字典
#   *args和**args可共存，但*args关键字形参必须在前
def fun_position(*args):
    print(args)


fun_position(1)
fun_position(1, 2)

print('hello', 'world')


def fun_key(**args):
    print(args)


fun_key(a=1)
fun_key(a=1, b=2)

# 程序员：田宗林
# 时 间：2021/7/8
# 函数调用过程中
#   对于不可变对象，函数体内的修改不会影响实参值
#   对于可变对象，函数体内的修改会影响实参值
def fun(arg1, arg2):
    print('arg1= ', arg1)
    print('arg2= ', arg2)
    arg1 = 10
    arg2.append(55)
    print('arg1= ', arg1)
    print('arg2= ', arg2)


n1 = 1
n2 = [22, 33, 44]
print('n1= ', n1)
print('n2= ', n2)

fun(n1, n2)

print('n1= ', n1)
print('n2= ', n2)

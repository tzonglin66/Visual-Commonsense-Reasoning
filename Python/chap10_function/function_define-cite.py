# 程序员：田宗林
# 时 间：2021/7/8
def calc(a, b):  # 形参 → 函数定义处
    c = a + b
    return c


result = calc(1, 2)  # 实参 → 函数调用处
print(result)

# 关键字参数传递
res = calc(b=1, a=2)  # 关键字实参
print(res)

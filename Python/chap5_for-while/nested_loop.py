# 作 者：田宗林
# 时 间：2021/8/5
"""
嵌套循环
"""
# 打印99乘法口诀
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')  # print输出后不换行
    print()
# 作 者：田宗林
# 时 间：2021/8/1
"""
for in 循环
    for 自定义变量 in 可迭代对象:
        loop_body
        # 自定义变量从可迭代对象中依次取值（遍历）
        # 如果循环体不需要访问自定义变量，可以将自定义变量替代为下划线
"""
for _ in range(5):
    print('I love Python!')
# 输出100到999之间的水仙花数，例：153 = 1**3 + 5**3 +3**3
for item in range(100, 1000):
    ge = item % 10  # 个位数
    shi = item//10 % 10  # 十位数
    bai = item//100  # 百位数
    if ge**3+shi**3+bai**3 == item:
        print(item, '是水仙花数')

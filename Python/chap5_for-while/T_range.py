# 作 者：田宗林
# 时 间：2021/8/1
# 内置函数range()：用于生成一个整数序列
    # 创建方式: range(start, stop, step)  ----->  [start, stop), step 为步长
        # stop不可缺少, start 默认 0, step 默认 1
    # 返回值是一个迭代器对象
    # 特点：只有用到range对象时，才会去计算序列中的相关元素
    # in 与 not in 判断是否存在指定的整数

print(range(5))
lst = list(range(5))
print(lst)
print(1 in range(5))

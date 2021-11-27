# 作 者：田宗林
# 时 间：2021/7/24

# 获取列表中指定索引范围内的元素  --> 切片操作 : list_name[start: stop: stop)
    # step 默认是1 || step取正数：start 默认是第一个元素，stop默认是最后一个元素
    # step 取负数：start 默认是最后一个元素，stop默认是第一个元素

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print('--------步长为正--------')
print(lst[1:6:1])
print(lst[1:6:])
print(lst[:6:2])
print(lst[1::2])
print('--------步长为负--------')
print(lst[::-1])
print(lst[7::-2])

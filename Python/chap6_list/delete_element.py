# 作 者：田宗林
# 时 间：2021/7/31
# 列表元素的删除操作
    # remove() 一次删除一个元素，元素不存在抛出ValueError
    # pop() 删除一个指定索引位置的元素（默认删除最后一个元素）
    # 切片 一次至少删除一个元素[]
    # clear() 清空列表
    # del list_name 删除列表
lst = [10, 20, 30, 40, 50, 60, 20]
lst.remove(20)
print(lst)
lst.pop(3)
print(lst)
lst.pop()
print(lst)
lst[1:3] = []
print(lst)
lst.clear()
print(lst)

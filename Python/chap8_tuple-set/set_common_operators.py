# 作 者：田宗林
# 时 间：2021/8/5
"""集合的常见操作"""
# 判断元素是否在集合中
    # (not) in ----> True OR False
# 元素新增
    # set_name.add(e)  # 一次添加一个元素e
    # set_name.update(elements)  # 一次添加多个元素
# 元素删除
    # set_name.remove(e)  # 一次删除一个元素e，不存在抛出KeyError
    # set_name.discard(e)  # 一个删除一个元素，不存在不抛出异常
    # set_name.pop()  # 无调用参数，一次删除任意一个元素
    # set_name.clear()  # 清空集合
# 集合遍历
    # for ele in set_name:

s1 = set(range(10))
print(s1)
s1.update('python')
print(s1)

# 作 者：田宗林
# 时 间：2021/8/5
"""
字符串的替换操作  ----> string
# str_name.replace(old, new ,count)
    # old: 被替换字符串
    # new: 替换字符串
    # count: 可选参数，最大替换次数
字符串的连接操作  ----> string（split的调用参数）
# join_char.join(item)
    # join_char: 连接符
    3 item: 由字符串组成的元组或列表（split劈分后的结果）
"""
lst = ['hello', 'python', 'world']
str1 = "".join(lst)
print(str1)
tup = ("hello", "python", "world")
str2 = ", ".join(tup)
print(str2)
str3 = " ".join("hello")
print(str3)

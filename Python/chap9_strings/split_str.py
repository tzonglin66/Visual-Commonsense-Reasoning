# 作 者：田宗林
# 时 间：2021/8/5
"""
字符串的劈分操作  ----> lst = [str1, str2, ...]
# str_name.(r)split(sep=sep_char, maxsplit=number)
    # 从字符串的(右)左侧开始劈分，返回的值是一个列表
    # 可选参数sep指定劈分符是sep_char，默认是空格
    # 可选参数maxsplit指定最大劈分次数为number，在经过最大劈分次数后，剩余的子串会单独作为一部分
"""

str1 = "Hello Python World"
print(str1)
str2 = str1.split()
print(str2)
str1 = "Hello, Python, World"
print(str1)
str3 = str1.split(sep=',', maxsplit=1)
print(str3)

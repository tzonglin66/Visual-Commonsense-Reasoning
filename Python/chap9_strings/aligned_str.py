# 作 者：田宗林
# 时 间：2021/8/5
"""
字符串对齐(填充)操作  ----> string（输出时格式的好看）
# 两个参数：str_name.align_method(width, fill_char)
    # align_method: 对齐方式 center(居中)、ljust(左对齐)、rjust(右对齐)
    # width: 宽度，如果小于实际宽度则返回原字符串
    # fill_char: 填充符，可选参数，默认是空格
# 一个参数：str_name.zfill(width)
    # 右对齐，左边用0填充
"""

str1 = "Temm"
print(str1)
str2 = str1.center(8, '*')
print(str2)

# 作 者：田宗林
# 时 间：2021/8/6
"""
字符串的编码和解码  ---->bytes(字节类型数据)
# 编码：code_str = str_name.encode(encoding=str)
    # str = 'GBK' OR 'UTF-8
    # 'GBK' 一个中文两个字节，'UTF-8' 一个中文三个字节
# 解码：str_name = code_str.decode(encoding=str)
"""

s = '天涯共此时'
# 编码
code_gbk = s.encode(encoding='GBK')
print(code_gbk, type(code_gbk))
code_utf = s.encode(encoding='UTF-8')
print(code_utf, type(code_utf))
# 解码
str_gbk = code_gbk.decode(encoding='GBK')
print(str_gbk)
str_utf = code_utf.decode(encoding='UTF-8')
print(str_utf)

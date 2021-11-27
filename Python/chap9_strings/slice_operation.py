# 作 者：田宗林
# 时 间：2021/8/6
"""
字符串切片操作
new_str = str_name[start: stop: step]  <----不包括stop
"""
s = 'Hello,Python'
s1 = s[:5]
s2 = s[6:]
s3 = '!'
new_str = s1 + s3 + s2
print(new_str)

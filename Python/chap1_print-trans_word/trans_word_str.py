# 作 者：田宗林
# 时 间：2021/7/11
# 转义字符
print('Hello\nworld')  # 换行

print('hello\tworld')  # 水平制表位
print('helloooo\tworld')

print('hello\rworld')   # 回车
print('hello\bworld')  # 退格
print('http:\\\\www.baidu.com')  # 反斜杠
print('老师说: \'大家好\"')  # 单双引号

# 原字符: 不希望字符串中的转义字符起作用 <-- 在字符串前加r，或者R
print(r'hello\nworld')
# 最后一个字符不能是反斜杠\，但可以是两个\\
# 错误输入: print(r'hello\nworld\')
print(r'hello\nworld\\')

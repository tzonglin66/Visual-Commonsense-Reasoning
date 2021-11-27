# 作 者：田宗林
# 时 间：2021/10/7
"""
ython 字符串前面加u, r, b的含义
"""

# 1. 字符串前面加u
"""
例: u"我是含有中文字符组成的字符串"
作用：后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面
"""

# 2. 字符串前加r
"""
例：r"\n\n\n"  # 表示一个普通字符串\n\n\n，而不表示换行
作用：去掉反斜杠的转义机制
"""
print(r"\n\n\n")

# 字符串前加b
"""
例：response = b"<h1>Hello World!</h1>  # b""表示是一个bytes对象
作用：b" "前缀表示反而字符串是bytes类型
"""
v_byte = b"<h1>Hello World!</h1>"
print(type(v_byte))  # <class 'bytes'>

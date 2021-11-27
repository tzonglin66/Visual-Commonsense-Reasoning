# 作 者：田宗林
# 时 间：2021/7/11
# print函数 ->输出
"""
内容：
    1. 数字
    2. 字符串
    3. 含有运算符的表达式
目的地
    1. 显示器
    2. 文件
形式：
    1. 换行
    2. 不换行
"""
# print完整语法
"""
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
将objects打印输出至file指定的文本流，以sep分隔并在末尾加上end
sep, end, file 和 flush 必须以关键字参数的形式给出
所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end
sep 和 end 都必须为字符串；它们也可以为 None，这意味着使用默认值
如果没有给出objects，则print()将只写入end
file 参数必须是一个具有write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout
输出是否缓存通常取决于file，但如果 flush 关键字参数为 True，输出流会被强制刷新[及时输出内容，不用等到文件关闭]
"""

print(520)
print(3 + 1)

# 将数据输出到文件中
#   1. 指定盘符→E:/Programs/file_name
#   2. 指定关键字形参file=

fp = open('../T_files/print.txt', 'a+')
print('Hello world', file=fp)

# 同行输出
print('hello', 'python')
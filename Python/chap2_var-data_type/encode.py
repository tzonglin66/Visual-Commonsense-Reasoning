# 作 者：田宗林
# 时 间：2021/7/11
"""二进制与字符编码
    二进制0,1 -> ASCll表：一个字节（8bit）表示一个字符
    中文字符：GB2312 -> GBK -> GB18030(一个或者两个或者四个字节表示一个字符)
    全世界字符：
        Unicode(统一用两个字节表示一个字符)
        UTF-8(英文ASll编码一个字节一个字符；中文用三个字节表示)
不管是中文还是英文，在计算机当中都是字符，对应一个整数，可以使用二进制、十进制、八进制、十六进制表示 -> 二进制
"""
print(chr(20056))
print(ord('乘'))

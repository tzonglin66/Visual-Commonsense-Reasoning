# 作 者：田宗林
# 时 间：2021/7/31
"""
粗心导致的常见bug常见（查资料）
    1. 末尾的冒号
    2. 缩进错误
    3. 英文符号写成中文符号
    4. 没有定义变量就使用
    5. ==和=混用
"""
"""
知识不熟练（多加练习）

思路不清晰
<-----(1)print()函数打印输出
<-----(2)使用'#'暂时注释部分代码

被动掉坑：用户错误操作或者一些例外请问导致程序崩溃
try exception
BaseException(任何一种错误)
"""

try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a/b
    print('a/b=', result)
except ZeroDivisionError:
    print('除数不能为0!')
except ValueError:
    print('只能输入数字!')
print('程序结束')
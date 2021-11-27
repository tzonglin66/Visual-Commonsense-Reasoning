# 作 者：田宗林
# 时 间：2021/9/22
"""
argparse模块编写用户友好的命令行界面
argparse解析sys.argv中的参数
自动生成帮助和用法消息，并在用户向程序提供无效参数时发出错误
"""
import argparse

# 创建解析器——ArgumentParser object
parser = argparse.ArgumentParser(description='Process some integers.')
"""
参数信息
description - Text to display before the argument help (default: none)
"""
# 增加参数——add_argument()
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
# 解析参数——parse_args()

args = parser.parse_args()
print(args.accumulate(args.integers))
# 作 者：田宗林
# 时 间：2021/8/6
"""
文件打开模式
    # 文件类型
        # 文本文件 <----记事本
        # 二进制文件：数据内容用“字节”进行存储，例 .mp3、.jpg、.doc
    # 打开模式
        必须
        # 'r' 只读
        # 'w' 只写，文件不存在，创建；文件存在，覆盖
        # 'a' 追加，文件不存在，创建；文件存在，追加
        修饰
        # 'b' 二进制方式，需与r w a 一起使用，例 'rb'、'wb'
        # '+' 读写方式 常用 a+
"""

# w -> 写的方式
file = open('../T_files/c.txt', 'w')
file.write('python')
file.close()

# a -> 追加方式
# a+ -> 以追加方式读写
file = open('../T_files/c.txt', 'a')
file.write('\npython')
file.close()

# b -> 二进制文件
src_file = open('../T_files/kenan1.jpg', 'rb')
target_file = open('../T_files/kenan1_copy.jpg', 'wb')
target_file.write(src_file.read())

target_file.close()
src_file.close()

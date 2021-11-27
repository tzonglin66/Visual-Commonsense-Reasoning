# 作 者：田宗林
# 时 间：2021/8/6
"""
文件对象常用方法 filename.method
# read
    read([size]) 读取size个字节或字符的内容，若省略[size]，则读取所有内容
    readline() 读取一行内容
    readlines() 每一行作为独立字符串对象，放入列表
# write
    write(str) 将字符串str写入文件
    writelines(s_list) 将字符串列表s_list写入文件，不添加换行符
# 文件指针移动
    seek(offset[,whence]) 把文件指针移动到新的位置
        offset：相对whence的移动量
        whence：0--文件开头（默认）、1--当前位置、2--文件尾
    tell() 返回文件指针的当前位置
# 文件关闭
    flush() 把缓冲区内容写入文件，但不关闭文件
    close() 把缓冲区内容写入文件，关闭文件，释放文件对象相关资源
"""
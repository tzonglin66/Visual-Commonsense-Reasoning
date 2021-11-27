# 程序员：田宗林
# 时 间：2021/7/8
"""
文件读写原理
# 操作流程：Python操作文件 -> 打开或新建文件 -> 读、写文件 -> 关闭资源
# 具体操作：open()创建文件对象（映射磁盘上的真实文件）
    # filename = open(filenames [,mode,encoding]
        filename 被创建的文件对象
        filenames 要创建或打开的文件名称
        mode 打开模式，默认为只读
        encoding 默认文本文件的字符编码格式为gbk
"""
file = open('../T_files/a.txt', encoding='utf-8')
# print(filename.readline())  # readline 读一行
print(file.readlines())  # readlines 读所有行 -> 列表
file.close()

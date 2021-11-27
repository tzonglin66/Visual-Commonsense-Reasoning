# 程序员：田宗林
# 时 间：2021/7/8
"""
os模块：与操作系统相关的一个模块
# 操作系统程序
# 对目录或者文件进行操作  <-----os.function()
    # getcwd()  当前工作目录
    # chdir(path)  将path设置为当前工作目录
    # listdir([path])  path(默认是当前工作目录)下的文件和目录信息
    # mkdir(path[,mode])  创建目录
    # mkdirs(path1/path2...[,mode])  创建多级目录
    # rmdir(path)  删除目录
    # removedirs(path1/path2...)  删除多级目录
"""

import os

# os.system('calc.exe')
# os.system('notepad.exe')

# 直接调用可执行文件
os.startfile('E:\\Program Files\\7-Zip\\7zFM.exe')


print(os.getcwd())  # 当前目录
os.chdir('../T_files')  # 改变当前目录
print(os.getcwd())
# print(os.listdir('../T_files'))  # 罗列文件
print(os.listdir())

os.mkdir('new_dir1')  # 建立文件夹
print(os.listdir('../T_files'))
os.makedirs('new_A/B/C')  # 建立多级文件夹
print(os.listdir('../T_files'))
os.rmdir('new_dir1')  # 删除文件夹
os.removedirs('new_A/B/C')  # 删除多级文件夹

os.chdir('../')
print(os.getcwd())

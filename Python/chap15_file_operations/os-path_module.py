# 程序员：田宗林
# 时 间：2021/7/8
"""
os.path模块：主要操作对象为路径
# __file__表示当前脚本运行的路径
os.path.function()
    # abspath(path)  获取path的绝对路径
    # exists(path)  判断path是否存在
    # join(path, name)  将path与name拼接
    # splitext(filename)  分离file的文件名和扩展名
    # split(path)  分离path中路径和文件名
    # basename(path)  从path中提取文件（夹）名
    # dirnames(path)  从path中提取文件（夹）所在目录路径
    # isdir(path)  判断path是否是目录
"""

import os.path as op

print(__file__)  # 当前脚本的路径 <---- E:/root/Projects/learn_python/chap15_file_operations/os-path_module.py
print(op.abspath('os-path_module.py'))  # 绝对路径
print(op.exists('demo.py'), op.exists('../T_files'))  # 文件是否存在
# 路径和文件名连接（中间自动路径连接符）
path_name = op.join('E:\\root\\Projects\\learn_python\\chap15_file_operations', 'os_module.py')
print(path_name)
print(op.split(path_name))  # 分离路径和文件名
print(op.splitext('dir_os.py'))  # 分离文件名和后缀名
print(op.basename('E:\\root\\Projects\\learn_python'))  # 提取文件（夹）名
print(op.dirname('E:\\root\\Projects\\learn_python'))  # 提取文件（夹）所在目录路径
print(op.isdir('E:\\root\\Projects\\learn_python'))  # 是否是目录

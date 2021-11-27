# 程序员：田宗林
# 时 间：2021/7/8

import os

# 输出T_files下的.jpg文件名
path = os.path.dirname(os.getcwd())
path = os.path.join(path, 'T_files')
lst = os.listdir(path)
for filenames in lst:
    if filenames.endswith('.jpg'):
        print(filenames)

# os.walk(path)方法  ----> 获取path下（子）目录的路径、（子）目录、文件
path = os.path.dirname(os.getcwd())  # learn_python
walk_files = os.walk(path)
for dirpath, dirnames, filenames in walk_files:
    '''
    print(dirpath)
    print(dirnames)
    print(filenames)
    print("-------------------------------")
    '''

    for dirname in dirnames:
        print(os.path.join(dirpath, dirname))

    for filename in filenames:
        print(os.path.join(dirpath, filename))
    print("-------------------------------")

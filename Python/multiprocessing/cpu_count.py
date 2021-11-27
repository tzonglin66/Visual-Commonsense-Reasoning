# 作 者：田宗林
# 时 间：2021/10/28
import multiprocessing
import os

# multiprocessing.cpu_count()
"""
返回系统的CPU数量
该数量不同于当前进程可以使用的CPU数量
等同于os.cpu_count(): 返回系统CPU数量，不确定则返回 None
"""

print(multiprocessing.cpu_count())
print(os.cpu_count())

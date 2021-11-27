# 程序员：田宗林
# 时 间：2021/7/8
"""
安装：pip install Module_Name
使用：import Module_Name
"""
import schedule  # 定时执行
import time


def job():
    print('哈哈-------------')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)

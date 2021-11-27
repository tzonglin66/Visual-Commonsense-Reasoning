# 作 者：田宗林
# 时 间：2021/7/31
# 使用traceback模块打印异常信息
import traceback
try:
    print('-------------------------')
    print(1/0)
except:
    traceback.print_exc()

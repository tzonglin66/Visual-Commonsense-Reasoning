# 程序员：田宗林
# 时 间：2021/7/8
# 类实现了特殊方法__enter__()和__exit__() -> 类对象遵循上下文管理器协议
# 该类对象的实例对象称为上下文管理器←MyContentMgr()
class MyContentMgr:
    def __enter__(self):
        print("enter方法被执行了")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit方法被执行了")

    def show(self):
        print('show方法被执行了')


with MyContentMgr() as file:  # 相当于file = MyContentMgr
    file.show()

# 程序员：田宗林
# 时 间：2021/7/7
# object类是所有类的父类
# 内置函数dir()可查看指定对象所有属性
# object类的方法__str__()用于返回"对象的描述（内存地址）"，可用print(对象名)会默认调用__str__方法
    # 常常对__str__方法重写，便于查看对象信息
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):  # 返回对像的描述
        return '返回对象的描述'


stu = Student('Temm', 25)
print(dir(stu))
print(stu)  # 默认调用__str__()方法
print(type(stu))

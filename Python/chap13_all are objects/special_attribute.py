# 程序员：田宗林
# 时 间：2021/7/7
# 特殊属性
# __dict__ 返回实例对象的所有属性或者类对象的所有方法
# __class__ 实例对象所属的类
# __bases__ 类对象的父类元组
# __base__ 类对象的基类（最近的父类）
# __mro__ 类对象的层次结构
# __subclasses__ 对象类的子类列表
class A:
    pass


class B:
    pass


class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def cname(self):
        print(self.name)

class D(A):
    pass


c = C('Temm', 25)
print(c.__dict__)  # 实例对象的属性字典
print(C.__dict__)  # 类对象的属性字典
print('-------------------')
print(c.__class__)  # 实例对象所属的类
print(C.__bases__)  # C类的父类元组
print(C.__base__)  # C类的基类（最近的父类）
print(C.__mro__)  # C类的层次结构
print(A.__subclasses__())   # A类的子类列表

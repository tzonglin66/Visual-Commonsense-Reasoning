# 类的组成
    # 类属性
    # 实例方法
    # 静态方法
    # 类方法
    # 初始化方法
class Student:
    native_place = '广西'  # 直接写在类里的变量，称为类属性
    # 初始化方法
    def __init__(self, name, age):  # self不可缺少
        self.name = name  # self.name 称为实例属性，进行了一个赋值的操作，将局部变量的name值赋给实例属性
        self.age = age

    # 实例方法
    def eat(self):  # self不可缺少
        print('学生'+self.name+'在吃饭……')

    # 静态方法
    @staticmethod
    def st_method():  # 不可写self
        print('我使用了staticmethon进行修饰，所以我是静态的方法')

    # 类方法
    @classmethod
    def cl_method(cls):  # cls不可缺少
        print('我是类方法，因为我使用了classmethod进行修饰')
# 在类之外定义的称为函数，在类之内定义的称为方法

# 程序员：田宗林
# 时 间：2021/7/7
# 特殊方法
# __add__()  <---->  +运算
# __len__()  <---->  len运算
a = 1
b = 2
c = a + b
print(c)
d = a.__add__(b)
print(d)


class Student:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name  # 通过重写__add__方法，可使自定义对象具有“+”功能

    def __len__(self):
        return len(self.name)  # 通过重写__len__方法，让内置函数len()的参数可以是自定义类型


stu1 = Student('张三')
stu2 = Student('李四')
s = stu1 + stu2  # 实现了两个对象的加法运算（因为在Student类中，编写了__add__()特殊的方法）
t = stu1.__add__(stu2)
print(type(s))
print(type(t))
print(s)
print(t)
print('-------------------------------')
lst = [1, 2, 3, 4]
print(len(lst))
print(stu1.__len__())
print(len(stu1))

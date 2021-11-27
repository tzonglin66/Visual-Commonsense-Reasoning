# 作 者：田宗林
# 时 间：2021/7/31
# 面向对象三大特征之继承  ---->
    # 支持多继承class sub_class_name(part_name1, part_name2, ...):
    # 默认继承object，class class_name: = class class_name(object):
    # 子类可利用super().__init__()调用父类的初始化方法编写初始化方法
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


# Person的子类
class Student(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)  # 使用super().调用父类的方法__init__
        self.stu_no = stu_no


# Teacher子类
class Teacher(Person):
    def __init__(self, name, age, teach_year):
        super().__init__(name, age)
        self.teach_year = teach_year


stu = Student('Temm', 25, '2101679')
teacher = Teacher('Temm', 32, 3)

stu.info()
print('----------------------')
teacher.info()

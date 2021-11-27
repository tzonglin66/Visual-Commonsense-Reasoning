# 作 者：田宗林
# 时 间：2021/7/31
# 子类方法重写
# 对继承自父类的某个属性或方法不满意，可以在子类中对其方法体进行重新编写
# 重写时可以通过super().method_name()调用父类中被重写的方法
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

    def info(self):  # 方法重写
        super().info()  # 利用super().调用父类的方法info()，self参数不用写
        print('学号', self.stu_no)



# Teacher子类
class Teacher(Person):
    def __init__(self, name, age, teach_year):
        super().__init__(name, age)
        self.teach_year = teach_year

    def info(self):
        super().info()
        print('教龄', self.teach_year)


stu = Student('Temm', 25, '2101679')
teacher = Teacher('Temm', 32, 3)

stu.info()
print('----------------------')
teacher.info()

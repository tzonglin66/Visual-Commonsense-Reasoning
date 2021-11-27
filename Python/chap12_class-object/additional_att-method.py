# 一个类可以创建多个实例对象，每个实例的属性值可不同（初始化方法中定义的属性）
# 且可自定义属性和方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name + '在吃饭')

# 创建实例属性不同的实例
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(id(stu1))
print(id(stu2))
print('---------------为stu1动态绑定性别属性--------------')
stu1.gender = '男'
print(stu1.name, stu1.age, stu1.gender)
print(stu2.name, stu2.age)


def show():
    print('定义在类之外的，称为函数')


stu1.show = show  # 给stu1绑定show方法
stu1.show()

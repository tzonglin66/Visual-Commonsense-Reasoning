# 面向对象三大特征之封装  ---->提高程序安全性
# 属性和方法包装到类对象中，在方法内部对属性操作，在类对象外部调用方法
# 私有属性，使用self.__pri_att
    # dirname(实例名)列出所有属性  ---->访问私有属性

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print('汽车已启动...')


car = Car('宝马x5')
car.start()
print(car.brand)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def show(self):
        print(self.name, self.__age)


stu = Student('Temm', 25)
stu.show()
# 在类的外部使用name和age
print(stu.name)
# print(stu.__age)
# print(dirname(stu))
print(stu._Student__age)  # 在类的外部可以通过 _Student__age进行访问
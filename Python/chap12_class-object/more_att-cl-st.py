# 类属性：类中方法外的变量，被类的所有对象所共享，使用类（实例）名直接访问
# 类方法：使用@classmethod修饰的方法，使用类（实例）名直接访问
# 静态方法：使用@staticmethod修饰的方法，使用类（实例）名直接访问
from class_compose import Student

print('----------类属性的使用方法------------')
print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '天津'
print(stu1.native_place)
print(stu2.native_place)
print('---------类方法的使用方式-----------------')
Student.cl_method()
stu1.cl_method()
print('----------静态方法的使用方式---------------')
Student.st_method()
stu2.st_method()

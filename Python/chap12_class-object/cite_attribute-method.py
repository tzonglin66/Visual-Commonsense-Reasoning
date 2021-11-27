# 实例，可以调用类中的方法
    # 对象名.属性名
    # 对象名.方法名() = 类名.方法名(对象名)-->实际上就是方法定义处的self
from create_object import Student, stu

print(stu.name)
print(stu.age)
# 调用Student中的eat方法
stu.eat()
Student.eat(stu)

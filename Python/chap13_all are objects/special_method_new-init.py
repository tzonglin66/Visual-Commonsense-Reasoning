# 程序员：田宗林
# 时 间：2021/7/7
# 特殊方法
# __new__(cls): 创建cls的实例对象，作为返回值，并传递给self
# __init__(self, arg1, ...): 为__new__创建的实例对象属性赋值
class Person:
    def __new__(cls, *args, **kwargs):  # 用于创建对象
        print('__new__被调用执行了，cls的id值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象id为{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):  # 对创建的对象进行寝化
        print('__init__被调用执行，self的id值为{0}'.format(id(self)))
        self.name = name
        self.age = age


print('object类对象的id值为{0}'.format(id(object)))
print('Person类对象的id值为{0}'.format(id(Person)))

# 创建Person类的实例对象
person = Person('Temm', 25)
print('person类实例对象的id值为{0}'.format(id(person)))

# 作 者：田宗林
# 时 间：2021/10/6
# Object的__call__(self, params)方法
    # 使该类的实例（对象）像函数一样被调用。
    # 默认情况下该方法在类中是没有被实现的，使用callable()方法可以判断某对象是否可以被调用
    # object_name(params)  -->  调用__call__方法
    # 等价调用object_name.__call__(params)

class Student:
    def __call__(self, *args, **kwargs):
        print('__call__方法被调用，输入为：\n', args, kwargs)  # 输出输入的任何内容


student = Student()
print(callable(student))  # 判断对象是否可调用
student(["Hello Python", "Happy"], {"name": "Python", "today": "Wednesday"})
student(*["Hello Python", "Happy"], **{"name": "Python", "today": "Wednesday"})

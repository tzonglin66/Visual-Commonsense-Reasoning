# 程序员：田宗林
# 时 间：2021/7/7
# 面向对象三大特征之多态  ---->
#
class Animal(object):
    def eat(self):
        print('动物会吃')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼...')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头...')


class Person:
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()


# 开始调用函数
fun(Cat())
fun(Dog())
fun(Animal())
print('-------------------------')
fun(Person())

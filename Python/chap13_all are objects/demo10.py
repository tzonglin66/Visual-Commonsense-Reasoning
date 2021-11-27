# 程序员：田宗林
# 时 间：2021/7/7
import copy


class Cpu:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# (1) 变量的赋值→只是形成两个变量，实际上还是指向同一个对像
cpu1 = Cpu()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))
print(type(cpu1), type(cpu2))
print('-------------------------')
# (2)类对象的浅拷贝→只拷贝源对象，子对象不拷贝，仅引用同一个子对象
disk1 = Disk()
print(disk1)
computer1 = Computer(cpu1, disk1)
# import copy
computer2 = copy.copy(computer1)
print(type(computer1), type(computer2))
print(computer1, computer1.cpu, computer1.disk)
print(computer2, computer2.cpu, computer2.disk)
print('-------------------------')
# (3)深拷贝→递归拷贝源对象包含的子对象
computer3 = copy.deepcopy(computer1)
print(computer1, computer1.cpu, computer1.disk)
print(computer3, computer3.cpu, computer3.disk)

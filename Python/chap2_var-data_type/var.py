# 作 者：田宗林
# 时 间：2021/7/11
# 变量的定义和使用
# 变量多次赋值后会指向新的空间
"""
    1. 标识：对象的存储地址，id(obj)
    2. 类型：对象的数据类型，type(obj)
    3. 值：对象存储的具体数据，print(obj)
"""
name = 'Temm'
print('标识：', id(name))
print('类型：', type(name))
print('值：', name)
name = '田宗林'
print(name)

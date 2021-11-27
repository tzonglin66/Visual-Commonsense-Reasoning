# 程序员：田宗林
# 时 间：2021/7/8
"""
with语句 上下文管理器
#   自动调用__enter()__方法，并返回值
#   离开时调用__exit()__方法，异常时也会调用
不论什么原因跳出with块，都能确保文件正确的关闭，从而释放资源
# 语法
    with open(filenames [,mode,encoding] as filename:
        filename.method
"""

# eg1
print(type(open('../T_files/d.txt', 'r')))
with open('../T_files/d.txt', 'r') as file:
    print(file.read())

# eg2
with open('../T_files/kenan1.jpg', 'rb') as src_file:
    with open('../T_files/kenan1_with_copy.jpg', 'wb') as target_file:
        target_file.write(src_file.read())


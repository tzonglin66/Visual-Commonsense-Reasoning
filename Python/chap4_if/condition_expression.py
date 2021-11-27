# 作 者：田宗林
# 时 间：2021/8/1
# 条件表达式：if...else的简写(简化操作)
    # x if condition else y：如果condition为True，执行x(statement1)，否则执行y(statement2)
num_a = int(input('请输入第一个整数：'))
num_b = int(input('请输入第二个整数：'))
# 输出num_a和num_b的大小关系
if num_a >= num_b:
    print(str(num_a)+'>='+str(num_b))
else:
    print(str(num_a)+'<'+str(num_b))
# 利用条件表达式书写
print(str(num_a)+'>='+str(num_b) if num_a >= num_b else str(num_a)+'<'+str(num_b))


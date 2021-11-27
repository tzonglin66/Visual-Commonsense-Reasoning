# 作 者：田宗林
# 时 间：2021/7/31
# python异常处理——try...except...else...finally
# 如果try块中没有抛出异常，执行else块，抛出异常，执行except块
# finally块无论是否发生异常才会执行，常用来释放try块中申请的资源
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
except BaseException as e:
    print('出错了 ', e)
else:
    print('a/b=', result)
finally:
    print('谢谢使用!')
print('程序结束')

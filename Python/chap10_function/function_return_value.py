# 程序员：田宗林
# 时 间：2021/7/8
# 函数返回值
#   ０：不需要给调用处提供数据，return可省略
#   1：return返回值类型为原类型
#   2：return返回值类型为元组
def odd_even(num):
    odd = []
    even = []
    for number in num:
        if number % 2:
            odd.append(number)
        else:
            even.append(number)
    return odd, even


numbers = [11, 22, 33, 23, 37, 95]
sep_num = odd_even(numbers)
print(type(sep_num))
print(sep_num)

函数调用参数传递
    1. 位置实参：根据参数位置传递
    2. 关键字实参：根据形参名进行实参传递 
        fun(var1=val1, var2=val2, ...)  # var是函数fun的形参名
    3. 将序列中的每个元素都转化为位置实参  <--**  对1进行合并  对应个数可变的位置形参
        fun(*params_list)
    4. 将字典中的每个键值对都转换为关键字实参  <--**  对2进行合并  对应个数可变的关键字形参
        fun(**params_dict)
        

函数返回值个数 --> 类型
    0：不需要给调用处提供数据，return可省略
    1：return返回值类型为原类型 
    2：return返回值类型为元组(val1, val2, ...)
函数参数定义
    1. 默认值参数：给形参默认值，只有与默认值不符的时候才需要传递实参
        def fun(a=1):
    2. 关键字形参：参数只能通过关键字实参传递，用*
        def fun(*,var)   # *后的变量为关键字形参
    3. 个数可变的位置参数
        i)无法事先确定传递实参的个数
        ii)用*定义
        iii)结果为元组
        iv)至多一个
            def fun(*args):
            print --> args = (val1, val2, ...)
    4. 个数可变的关键字形参
        i)无法事先确定传递的关键字实参个数
        ii)用**定义
        iii)结果为字典
        iv)至多一个
            def fun(**args):
            print --> args = {key1:val1, key2:val2, ...}
    若几者共存：位置形参 > (*args | *, var) > **args




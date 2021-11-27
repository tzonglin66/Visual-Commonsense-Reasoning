# 作 者：田宗林
# 时 间：2021/10/7
import json


# loads(): json解码函数[load()与此相同] ---> Python对象(dict or list)
"""
json.loads(fp, *, cls=None, object_hook=None, 
    parse_float=None, parse_int=None, 
    parse_constant=None, object_pairs_hook=None, **kw)
将 fp (一个支持 .read() 并包含一个 JSON 文档的 text file 或者 binary file) 反序列化为一个 Python 对象
"""
"""
参数含义：
    object_hook 是一个可选的函数(名)，它会被调用于每一个解码出的字典
        object_hook 的返回值会取代原本的 dict

    object_pairs_hook 是一个可选的函数(名)，它会被调用于每一个列表中解码出的字典
        object_pairs_hook 的返回值将会取代原本的 dict
        如果 object_hook 也被定义， object_pairs_hook 优先

    parse_float ，如果指定，将与每个要解码 JSON 浮点数的字符串一同调用
        默认状态下，相当于 float(num_str) 
        可以用于对 JSON 浮点数使用其它数据类型和语法分析程序 （比如 decimal.Decimal ）

    parse_int ，如果指定，将与每个要解码 JSON 整数的字符串一同调用
        默认状态下，相当于 int(num_str) 
        可以用于对 JSON 整数使用其它数据类型和语法分析程序 （比如 float ）

    parse_constant ，如果指定，将要与以下字符串中的一个一同调用： '-Infinity' ， 'Infinity' ， 'NaN' 
        如果遇到无效的 JSON 数字则可以使用它引发异常
"""


# 常规解码
json_text1 = '["foo", {"bar":["baz", null, true, false]}]'  # null--None, true--True, false--False
print(json.loads(json_text1))

json_text2 = '"\\"foo\\bar"'
print(json.loads(json_text2))


# 指定object_hook
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


json_text3 = '[1, {"__complex__": true, "real": 1, "imag": 2}]'
print(json.loads(json_text3, object_hook=as_complex))  # 用as_complex作用于loads解码对象中的所有字典作为最终返回对象

print(json.loads(json_text3, object_pairs_hook=as_complex))

json_text4 = '{"__complex__": true, "real": 1, "imag": 2}'
print(json.loads(json_text4, object_pairs_hook=as_complex))


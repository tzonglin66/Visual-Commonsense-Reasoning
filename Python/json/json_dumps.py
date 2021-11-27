# 作 者：田宗林
# 时 间：2021/10/7
import json


# dumps(): json编码函数[dump()与此相同]  ----> Json text
"""
json.dump(obj, fp,
    *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True,
    cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)
将 obj 序列化为 JSON 格式化流形式的 fp (支持 .write() 的 file-like object)
"""
"""
参数含义：
    skipkeys 是 true （默认为 False），那么那些不是基本对象（包括 str, int、float、bool、None）的字典的键会被跳过；否则引发一个 TypeError
        json 模块始终产生 str 对象而非 bytes 对象。因此，fp.write() 必须支持 str 输入
        
    ensure_ascii 是 true （即默认值），输出保证将所有输入的非 ASCII 字符转义
        如果 ensure_ascii 是 false，这些字符会原样输出
        
    check_circular 是为假值 (默认为 True)，那么容器类型的循环引用检验会被跳过并且循环引用会引发一个 OverflowError (或者更糟的情况)
    
    allow_nan 是 false（默认为 True），那么在对严格 JSON 规格范围外的 float 类型值（nan、inf 和 -inf）进行序列化时会引发一个 ValueError
        如果 allow_nan 是 true，则使用它们的 JavaScript 等价形式（NaN、Infinity 和 -Infinity）
        
    indent 是一个非负整数或者字符串，那么 JSON 数组元素和对象成员会被美化输出为该值指定的缩进等级
        如果缩进等级为零、负数或者 ""，则只会添加换行符
        None (默认值) 选择最紧凑的表达。
        使用一个正整数会让每一层缩进同样数量的空格
        如果 indent 是一个字符串 (比如 "\t")，那个字符串会被用于缩进每一层。

    separators 当被指定时，应当是一个 (item_separator, key_separator) 元组
        当 indent 为 None 时，默认值取 (', ', ': ')，否则取 (',', ': ')
        为了得到最紧凑的 JSON 表达式，应指定其为 (',', ':') 以消除空白字符

    default 当被指定时，其应该是一个函数，每当某个对象无法被序列化时它会被调用
        它应该返回该对象的一个可以被 JSON 编码的版本或者引发一个 TypeError
        
    sort_keys 是 true（默认为 False），那么字典的输出会以键的顺序排序
"""

# 常规编码 <--separators=(', ', ': '), indent=None
obj1 = ['foo', {'bar': ('baz', None, 1.0, 2)}]  # None --> null
print(json.dumps(obj1))

obj2 = "\"foo\bar"
print(json.dumps(obj2))

obj3 = ["Hell0", {"c": True, "b": 0, "a": None}]  # True --> true
print(json.dumps(obj3, sort_keys=True))


# 紧凑编码 <--separators=(item_separator, key_separator)
obj4 = [1, 2, 3, {'4': 5, '6': 7}]
print(json.dumps(obj4, separators=(',', ':')))  # 默认有空格

# 美化输出 <--indent=int_num
obj5 = [1, {'4': 5, '6': 7}]
print(json.dumps(obj5, sort_keys=True, indent='4'))  # 指定indent后，元素间默认无空格，仅字典键值间有空格

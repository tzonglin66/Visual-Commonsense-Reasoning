# 作 者：田宗林
# 时 间：2021/10/7
"""
JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式
易于人阅读和编写，同时也易于机器解析和生成
文件后缀名: .jsonnet
    额外后缀名：i).json支持字符串用单引号
              ii).jsonl每行是一个JSON对象

"""

"""
JSON建构于两种结构(可嵌套)
1. “名称/值”对的集合collection of name/value pairs)  ----  字典(dictionary)
    一个字典以 {左括号 开始， }右括号 结束
    每个名称后跟一个 :冒号 
    名称/值 对之间使用 ,逗号 分隔
json1 = {"name": "Temm", "age": 25}
2. 值的有序列表(An ordered list of values) ---- 列表(list)
   一个列表以 [左中括号 开始， ]右中括号 结束
   值之间使用 ,逗号 分隔
json2 = ["name", "Temm", "age", 25]


Note: 值(value)可以是双引号(必须)括起来的字符串(string)、数值(number)、true(<--True)、false(False)、 null(<--None)、字典和列表
"""

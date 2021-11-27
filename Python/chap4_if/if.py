# 作 者：田宗林
# 时 间：2021/8/1
"""
if语句
"""
""""
----------------------------------
A. 单分支
    if condition:
        statement
"""
"""
----------------------------------
B. 双分支(二选一)
    if condition:
        statement1
    else:
        statement2
"""
"""
----------------------------------
C. 多分支结构(多选一)
condition可以写成数学形式，例：a < var < b
    if condition1:
        statement1
    elif condition2:
        statement2
    .......
    elif conditionN:
        statementN
    [else:]
        statementN+1
"""
"""
----------------------------------
D. 嵌套if
    if condition1:
        if condition11:
            statement11
        else:
            statement12
    else:
        if condition21:
            statement21
        else:
            statement22
"""
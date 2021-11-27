# 程序员：田宗林
# 时 间：2021/7/8
# 使用import开头导入，其后只能接(多个)package_name或者module_name
import T_Package
import T_Package.module_a, T_Package.module_b
# 使用from开头导入，import后可接任意(多个)对象（fun_name, var_name）
from T_Package import module_a, module_b
from T_Package.module_a import a

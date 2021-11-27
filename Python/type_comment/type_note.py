# 作 者：田宗林
# 时 间：2021/10/5
from typing import (
    List,
    NewType,
    Callable,
    TypeVar,
    Sequence,
    NoReturn,
    Tuple
)
# typing --- 类型提示支持

# 最基础组件：Any、Union、Tuple、Callable、TypeVar、Generic、None

# 实例：greeting函数接收与返回的都是字符串，注解方式如下
def greeting(name: str) -> str:
    return 'Hello ' + name


# 6. 常见类型注解
# 6.1 Any: 不受限的特殊类型
# 6.2 NoReturn: 标记没有返回值的函数的特殊类型，例如：
def stop() -> NoReturn:
    raise RuntimeError('no way')

# 6.3 Tuple: 元组类型
    # Tuple: 表示是一个元组，等价于Tuple[Any, ...]
    # Tuple[X, Y]: 二项元组类型，第一个元素的类型是 X，第二个元素的类型是 Y
    # 可用省略号指定同类变长元组
    # 空元组的类型可写为 Tuple[()]
t3: Tuple[int, float, str]  # t3 是由整数、浮点数、字符串组成的三项元组
t3 = (1, 1.0, "t")
t: Tuple[int, ...]
t = (2, 2,)

# 6.4 Union: 联合类型
    # Union[X, Y]: 非 X 即 Y
    # 联合类型之联合类型会被展平，例：
        # Union[Union[int, str], float] == Union[int, str, float]
    # 单参数之联合类型就是该参数自身，例：
        # Union[int] == int
    # 冗余的参数会被跳过，例如：
        # Union[int, str, int] == Union[int, str]
    # 最终类型不涉及参数顺序，例如：
        # Union[int, str] == Union[str, int]
    # Optional[X] 是 Union[X, None] 的缩写

# 6.5 Optional: 可选类型↑

# 6.6 Callable: 可调类型
    # 函数声明
        # Callable[[int], str]: input -- int; output -- str 函数
    # 参数列表和返回类型必须同时出现
        # 参数列表只能是类型列表或省略号，返回类型只能是单一类型: Callable[..., ReturnType]
# 6.7 Generic: 抽象基类
# 6.8 TypeVar: 类型变量
    # T =TypeVar('T')  # Can be anything
    # A = TypeVar('A', str, bytes)  # Must be str or bytes
# 6.9 Dict: 字典注解
    # Dict[str, int]: 表示字典的key是str类型, value是int类型
# 6.10 List: 列表注解
# 6.11 Set:
# 6.12 Sequence:
# 6.13 Iterator:



# 1. 类型别名
    # 类型别名适用于简化复杂的类型定义
"""
把类型赋给别名，就可以定义类型别名
下例中Vector 和 List[float] 相同，可互换
"""
Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]


new_vector = scale(2, [1.0, -4.2, 5.4])
print(new_vector)

# 2. 创建新类型
    # NewType(name,tp) 返回一个函数，这个函数返回其原本的值，值类型是原始类型tp的一个子类
    # 等价于取tp的一个"子类"
UserId = NewType('UserId', int)
some_id = UserId(524313)
print(some_id, type(some_id))


def get_user_name(user_id: UserId) -> None:
    print(user_id)
# typechecks
user_a = get_user_name(UserId(42351))

# does not typecheck: an int is not a UserId
# user_b = get_user_name(-1)

# 3. 可调对象(Callable)
    # Callable[[Arg1Type, Arg2Type], ReturnType]函数声明
    # Callable[..., ReturnType]仅声明返回值类型

def feeder(get_next_item: Callable[[], str]) -> None:
    get_next_item()

def async_query(on_success: Callable[[int, float], None],
                on_error: Callable[..., None]) -> None:
    on_success(1, 0.1)
    on_error(2)   # 参数任意填

# 4. 泛型(Generic)
    # TypeVar() 定义类型变量 ---> 泛型类型/函数定义的参数
    # 泛型类型 抽象类
T = TypeVar('T')  # Can be anything
A = TypeVar('A', str, int) # Must be str or int

def abstract_fun(arg: Sequence[T]) -> T:   # Generic function
    return arg[0]


# 5. Any类型
    # 与任意变量/值兼容
    # 未指定返回值与参数类型的函数，默认使用Any








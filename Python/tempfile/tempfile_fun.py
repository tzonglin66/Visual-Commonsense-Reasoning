# 作 者：田宗林
# 时 间：2021/10/7
# tempfile --- 生成临时文件和目录
""""
# 常用：
    # TemporaryFile() 和 TemporaryDirectory() 是带有自动清理功能的高级接口，可用作上下文管理器
    # mkstemp() 和 mkdtemp() 是低级函数，使用完毕需手动清理
# 为了代码清晰，调用函数时使用关键字参数
"""


# tempfile.TemporaryFile(mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
"""
返回一个 file-like object （文件类对象）作为临时存储区域
生成的对象可以用作上下文管理器
完成上下文或销毁临时文件对象后，临时文件将从文件系统中删除
创建该文件使用了与 mkstemp() 相同的安全规则: 
    它将在关闭后立即销毁（包括垃圾回收机制关闭该对象时）
    在 Unix 下，该文件在目录中的条目根本不创建，或者创建文件后立即就被删除了
    代码不应依赖使用此功能创建的临时文件名称，因为它在文件系统中的名称可能是可见的，也可能是不可见的
"""
"""
mode 参数默认值为 'w+b'，所以创建的文件不用关闭，就可以读取或写入，因为用的是二进制模式，所以无论存的是什么数据，它在所有平台上都表现一致
buffering、encoding、errors 和 newline 的含义与 open() 中的相同
参数 dir、prefix 和 suffix 的含义和默认值都与它们在 mkstemp() 中的相同
"""


# tempfile.TemporaryDirectory(suffix=None, prefix=None, dir=None, ignore_cleanup_errors=False)
"""
此函数会使用与 mkdtemp() 相同的规则安全地创建一个临时目录，结果对象可被用作上下文管理器
在完成上下文或销毁临时目录对象时，新创建的临时目录及其所有内容会从文件系统中被移除
可以从返回对象的 name 属性中找到临时目录的名称
当返回的对象用作上下文管理器时，这个 name 会作为 with 语句中 as 子句的目标（如果有 as 的话）
此目录可通过调用 cleanup() 方法来显式地清理
"""


# tempfile.NamedTemporaryFile(mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True, *, errors=None)
"""
此函数执行的操作与 TemporaryFile() 完全相同，但确保了该临时文件在文件系统中具有可见的名称
从返回的文件类对象的 name 属性中可以检索到文件名
如果 delete 为 true（默认值），则文件会在关闭后立即被删除
该函数返回的对象始终是文件类对象 (file-like object)，它的 file 属性是底层的真实文件对象
文件类对象可以像普通文件一样在 with 语句中使用。
"""


# tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=- 1, encoding=None, newline=None, suffix=None, prefix=None, dir=None, *, errors=None)
"""
此函数执行的操作与 TemporaryFile() 完全相同
但会将数据缓存在内存中，直到文件大小超过 max_size，或调用文件的 fileno() 方法为止，此时数据会被写入磁盘，并且写入操作与 TemporaryFile() 相同
此函数生成的文件对象有一个额外的方法——rollover()，可以忽略文件大小，让文件立即写入磁盘
返回的对象是文件类对象 (file-like object)
"""


# tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
"""
以最安全的方式创建一个临时文件
与 TemporaryFile() 不同，mkstemp() 用户用完临时文件后需要自行将其删除
如果 suffix 不是 None 则文件名将以该后缀结尾，是 None 则没有后缀
    mkstemp() 不会在文件名和后缀之间加点，如果需要加一个点号，请将其放在 suffix 的开头。
如果 prefix 不是 None，则文件名将以该前缀开头，是 None 则使用默认前缀
    默认前缀是 gettempprefix() 或 gettempprefixb() 函数的返回值（自动调用合适的函数）
如果 dir 不为 None，则在指定的目录创建文件，是 None 则使用默认目录
    默认目录是从一个列表中选择出来的，这个列表不同平台不一样，但是用户可以设置 TMPDIR、TEMP 或 TMP 环境变量来设置目录的位置
如果 suffix、prefix 和 dir 中的任何一个不是 None，就要保证它们是同一数据类型
    如果它们是 bytes，则返回的名称的类型就是 bytes 而不是 str
    如果确实要用默认参数，但又想要返回值是 bytes 类型，请传入 suffix=b''。
如果指定了 text 且为真值，文件会以文本模式打开， 否则，文件（默认）会以二进制模式打开
"""


# tempfile.mkdtemp(suffix=None, prefix=None, dir=None)
"""
以最安全的方式创建一个临时目录，创建该目录时不会有竞争的情况，该目录只能由创建者读取、写入和搜索。
mkdtemp() 用户用完临时目录后需要自行将其删除
prefix、suffix 和 dir 的含义与它们在 mkstemp() 中的相同。
mkdtemp() 返回新目录的绝对路径。
"""


# tempfile.gettempdir()
"""
返回放置临时文件的目录的名称，这个方法的返回值就是本模块所有函数的 dir 参数的默认值
"""


# tempfile.gettempdirb()
"""
与 gettempdir() 相同，但返回值为字节类型
"""


# tempfile.gettempprefix()
"""
返回用于创建临时文件的文件名前缀，它不包含目录部分
"""


# tempfile.gettempprefixb()
"""
与 gettempprefix() 相同，但返回值为字节类型
"""


# tempfile.tempdir
"""
当设为 None 以外的值时，此变量会为本模块中定义的函数的 dir 参数定义默认值，包括确定其类型为字节串还是字符串
它不可以为 path-like object
"""

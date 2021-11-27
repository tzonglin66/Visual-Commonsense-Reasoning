# 作 者：田宗林
# 时 间：2021/10/7
# create a temporary directory using the context manager(上下文管理器)
import tempfile


with tempfile.TemporaryDirectory() as tmpdirname:  # tmpdirname(after as) is the directory name
    print('created temporary directory', tmpdirname)

# directory and contents have been removed

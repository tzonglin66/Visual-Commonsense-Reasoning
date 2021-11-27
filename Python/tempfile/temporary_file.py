# 作 者：田宗林
# 时 间：2021/10/7
import tempfile


# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b"Hello world!")  # 输入字符串类型为byte类型
# read data from file
fp.seek(0)
print(fp.read())
# close the file, it will be removed
fp.close()


# create a temporary file using a context manager(上下文管理器)
with tempfile.TemporaryFile() as fp:
    fp.write(b"Hello world!")
    fp.seek(0)
    print(type(fp.read()))
# file is now closed and removed


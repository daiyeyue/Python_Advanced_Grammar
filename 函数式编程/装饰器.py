import time

# 高阶函数，以函数作为参数
def printTime(f):
    def wrapper(*args, **kwargs): #装饰器函数的参数的写法固定，先记着
        print("Time: ", time.ctime())
        return f(*args, **kwargs) #装饰器函数的参数的写法固定，先记着
    return wrapper

@printTime
def hello():
    print("Hello world")

hello()


def hello3():
    print("我是手动执行的")


# hello3()
#
# hello3 = printTime(hello3)
# hello3()

f= printTime(hello3)
f()
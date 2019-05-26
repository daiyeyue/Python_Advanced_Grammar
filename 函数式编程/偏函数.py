import functools
#实现上面int16的功能
int16 = functools.partial(int, base=16)  #固定int函数的base参数

print(int16("12345"))
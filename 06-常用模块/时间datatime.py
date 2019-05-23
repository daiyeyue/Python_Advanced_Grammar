import datetime
dt = datetime.date(2018, 3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

help(datetime.date)
print(type(dt))
print(datetime.date)

from datetime import datetime, timedelta

t1 = datetime.now()
print( t1.strftime("%Y-%m-%d %H:%M:%S"))
# td表示以小时的时间长度
td = timedelta(hours=-1)
# 当前时间加上时间间隔后，把得到的一个小时后的时间格式化输出
print( (t1+td).strftime("%Y-%m-%d %H:%M:%S"))


sum = []
for i in range(1000):
    sum.append(i)
print(sum)

sum = [i for i in range(1000)]
print(sum)

import timeit

# 生成列表两种方法的比较
# 如果单纯比较生成一个列表的时间，可能很难实现
c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
b = '''
sum = [i for i in range(1000)]
'''

# 利用timeit调用代码，执行100000次，查看运行时间
# stmt是我们衡量的代码片段
t1 = timeit.timeit(stmt=b, number=100000)
# 测量代码c执行100000次运行结果
t2 = timeit.timeit(stmt=c, number=100000)
print(t1)
print(t2)

import time
t = time.localtime()
print(t)
print(type(t))
print(t.tm_hour)

print(time.time())

t = time.localtime()

tt = time.asctime(t)
print(type(tt))
print(tt)

help(time.struct_time)

print(time.clock())

for i in range(10):
    print(i)
    time.sleep(1)

import time
def p():
    time.sleep(2.5)


t0 = time.clock()
p()
#time.sleep(3)
t1 = time.clock()
print(t1 - t0)



import time
def procedure():
    time.sleep(2.5)

# measure process time
t0 = time.clock()
procedure()
t1 = time.clock()
print(t1 - t0)

# measure wall time
t0 = time.time()
procedure()
print(time.time() - t0)
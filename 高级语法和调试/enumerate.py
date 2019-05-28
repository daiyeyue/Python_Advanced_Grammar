# enumerate案例1
l1 = [11,22,33,44,55]

em = enumerate(l1)  ## index从0开始
print(type(em))

l2 = [i for i in em]
print(l2)

em = enumerate(l1, start=100) ##index从100开始

l2 = [ i for i in em]
print(l2)
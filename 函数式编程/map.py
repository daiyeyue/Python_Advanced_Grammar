l1 = [i for i in range(10)]

def mulTen(n):
    return n*10

print(l1)
l3 = list(map(mulTen, l1 ))###不加list强制转换，返回来是一个map的类型，也是一个可迭代的变量
# map类型是一个可迭代的结构，所以可以使用for遍历
print(l3)
print(type(l3)) ###返回来是一个map的类型，也是一个可迭代的变量
for i in l3:
    print(i)


# 以下列表生成式得到的结果为空， why？
l4 = [i for i in l3]
print(type(l4))
print(l4)
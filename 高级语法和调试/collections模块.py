import collections
P1 = collections.namedtuple("Point", ['x', 'y']) #新建了一个类叫point，属性是x和y
P2 = collections.namedtuple("Point2", ['x', 'y','z'])
p1 = P1(11, 22) # 这里是进行实例化
p2 = P2('lx','ly','lz')
print(p1.x)
print(p1[0])

print(p2.z)

Circle = collections.namedtuple("Circle", ['x', 'y', 'r'])

c = Circle(100, 150, 50)
print(c)
print(type(c))

# 想检测以下namedtuple到底属于谁的子类
print(isinstance(c, tuple))
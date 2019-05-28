l1 = ["wangwang", "mingyue", "yyt"]
l2 = [89, 23, 78]

z = zip(l1, l2)
#print(z)
z1 = list(z)
# print(z)
# print(z1)

for i in z:
    print(i)

# 考虑下面结果，为什么会为空
l3 = [i for i in z1]
print(l3)
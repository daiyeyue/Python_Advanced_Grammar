from collections import Counter

# 为什么下面结果不把abcdefgabced.....作为键值，而是以其中每一个字母作为键值
# 需要括号里内容为可迭代
c = Counter("abcdefgabcdeabcdabcaba")
print(c)

s = ["liudana", "love", "love", "love", "love", "wangxiaona"]
c = Counter(s)

print(c)
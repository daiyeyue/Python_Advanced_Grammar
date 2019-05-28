d1 = {"one":1, "two":2, "three":3}
print(d1['one'])
#print(d1['four'])  #如果打开的话会报错：KeyError: 'four'

from collections import defaultdict
# lambda表达式，直接返回字符串
func = lambda: "刘大拿"
d2 = defaultdict(func)

d2["one"] = 1
d2["two"] = 2

print(d2['one'])
print(d2['four'])
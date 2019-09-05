# 查找
#- search(str, [, pos[, endpos]])：在字符串中查找匹配，pos和endpos表示起始位置
#- findall:查找所有
#- finditer： 查找，返回一个iter结果，iter是一个可迭代结果

import re
p = re.compile(r'\d+')
m  = p.search("one12two34three567four")
print(m)
print(m.group())

m = p.findall("one12two34three567four")
print(m)

m = p.finditer("one12two34three567four")
print(m)

for i in m:
    print(i)
    print(i.group())
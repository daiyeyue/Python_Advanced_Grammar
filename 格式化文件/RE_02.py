import re
# I表示忽略掉大小写
p = re.compile(r'([a-z]+) ([a-z]+)',re.I)

m = p.match('I am really love wangxiaojing')
print(m)
print(m.group()) #group()和group(0)表示整个字符串结果
print(m.group(1))
print(m.group(2))
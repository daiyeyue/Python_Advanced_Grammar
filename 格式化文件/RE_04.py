# Sub替换
# sub(rep1, str[, count])

import re
p = re.compile(r'(\w+) (\w+)') #\w单词字符， 就是a-z, A-Z, 0-9, _

s = "hello 123 wang 456 xiaojing, i love you"
m = p.sub(r'HELLO WORLD', s)
print(m)
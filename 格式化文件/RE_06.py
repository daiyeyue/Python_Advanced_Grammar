# 贪婪和非贪婪
# 贪婪：尽可能多的匹配，(*)表示贪婪匹配
# 非贪婪：找到符合条件的最小内容即可，(?) 表示非贪婪
# 正则表达式默认使用贪婪匹配

import re
title = u'<div>name</div><div>age</div>'
p1 = re.compile(r'<div>.*</div>')
p2 = re.compile(r'<div>.*?</div>')

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
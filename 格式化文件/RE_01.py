#导入相关包
import re

#查找数字
# r表示字符串不转义
# 使用compile将表示正则的字符串编译为一个pattern对象
p = re.compile(r'\d+')

#在字符串"one12"中进行查找，按照规则p制定的正则进行查找
# 返回结果如果是none的话，就是没找到，否则返回match对象
# 参数3，4表示在字符串中的查找范围
# match可以输入参数表示起始位置
# 查找到的结果只包含一个
m = p.match('one1244',3,7)
print(m)
print(m[0])
print(m.start(0))  ##开始位置
print(m.end(0))    ##结束位置

ss = 'one12'
num = re.findall('\d+',ss)
print(num)
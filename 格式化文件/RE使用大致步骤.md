#RE使用的大概步骤
1. 使用compile将表示正则的字符串编译为一个pattern对象
2. 通过pattern对象提供的一系列方法对文本进行查找匹配，获得匹配结果，一个Match对象
    最后使用Match对象提供的属性和方法获取信息，根据需要进行操作

#RE的常用函数
- group():获得一个或者多个分组匹配的字符串，当要获得整个匹配的子串时，直接使用group或者group(0)
- start：获取分组匹配的子串在整个字符串中的起始位置，参数默认为0
- end：获取分组匹配的子串在整个字符串中的结束位置，参数默认为0
- span：返回的结构技术(start(group), end(group)) 


# with案例
with open(r'test01.txt', 'r') as f:
    # 按行读取内容
    strline = f.readline()
    count = 1
    # 此结构保证能够完整读取文件知道结束
    while strline:
        print(strline)
        strline = f.readline()
        count = count + 1
    print(count)

# list能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r'test01.txt', 'r') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    #print(l)
    for line in l:
        print(line)

# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有制定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符

with open(r'D:\python_project\Python_Advanced_Grammar\文件file\test01.txt', 'r') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)

    # 作业：
    # 使用read读取文件，每次读取一个，使用循环读完
    # 尽量保持格式

with open(r'D:\python_project\Python_Advanced_Grammar\文件file\test01.txt', 'r') as f:
    strChar = f.read(1)
    while strChar:
        print(strChar)
        strChar = f.read(1)
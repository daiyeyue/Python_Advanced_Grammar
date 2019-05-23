#简单异常案例
try:
    num = int(input("plz input your number:"))
    rst = 100/num
    #如果上面的运算出错，下面的print就不执行了，直接跳到except里面了。
    print("计算结果是：{0}".format(rst))
except:
    print("你输入的数字有错误")
    exit()

#简单异常案例
#给出错误提示
try:
    num = int(input("plz input your number:"))
    rst = 100/num
    #如果上面的运算出错，下面的print就不执行了，直接跳到except里面了。
    prnt("计算结果是：{0}".format(rst))
    #如果是多种error情况
    #需要把越具体的错误越往前放
    #在异常类继承关系中，越是子类的异常，越要往前放
    #越是父类的异常，越要往后放

    #在处理异常时，一旦拦截了某个异常，则不继续往下查看，直接执行下一个代码，即有finally则执行finally语句块，否则就执行下一个大的语句
except ZeroDivisionError as e:
    print("你输入的数字有错误")
    print(e)
    exit()
except NameError as e:
    print("名字起错了")
    print(e)
    exit()
except AttributeError as e:
    print("好像属性有问题")
    print(e)
except Exception as e:
    print("我也不知道就错了")
    print(e)

print("hahah")

#作业：为什么我们可以直接打印出实例e，此时实例e应该事先调哪个函数

#用户手动引发异常
    #当某些情况，用户希望自己引发一个异常的时候，可以使用
    #raise 关键字来引发异常
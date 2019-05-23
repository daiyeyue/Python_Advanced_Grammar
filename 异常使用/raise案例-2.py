#自己定义异常
#需要注意：自定义异常必须是系统异常的子类
class DanaError(ValueError):
    pass
try:
    print("我爱静静")
    print("3.141")
    # 手动引发一个异常
    # 注意语法 raise ErrorClassName
    raise DanaError
    print("还没完啊")

except NameError as e:
    print("NameError")
# except DanaError as e:
#    print("DanaError")
#如果没有定义DanaError，则会被DanaError的父类捕获
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定是会被执行的")
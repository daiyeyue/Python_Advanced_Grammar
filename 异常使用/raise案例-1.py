try:
    print("我爱静静")
    print("3.141")
    # 手动引发一个异常
    # 注意语法 raise ErrorClassName
    raise ValueError
    print("还没完啊")

except NameError as e:
    print("NameError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定是会被执行的")
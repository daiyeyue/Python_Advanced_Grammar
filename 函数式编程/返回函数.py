def myF2():
    def myF3():
        print("In myF3")
        return 3

    return myF3

f3 = myF2()
print(type(f3))
print(f3)

a = f3()
print(a)

def myF4( *args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst
    return myF5

f5 = myF4(1,2,3,4,5,6,7,8,9,0)
print(f5())

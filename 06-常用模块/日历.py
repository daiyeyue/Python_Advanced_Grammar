import calendar

cal = calendar.calendar(2017)
print(type(cal))  #输出结果是字符串
print(cal)

w,t = calendar.monthrange(2017, 3)
wt = calendar.monthrange(2017, 3)
print(w)
print(t)
print(wt)
print(type(wt))

m = calendar.monthcalendar(2019, 5)
print(type(m))
print(m)
print(m[0])

calendar.prcal(2018)
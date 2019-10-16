# Label的例子

import tkinter

base = tkinter.Tk()

# 负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text="Python Label") #Label放在哪个base里面

# 给相应组件指定布局
lb.pack()

base.mainloop()
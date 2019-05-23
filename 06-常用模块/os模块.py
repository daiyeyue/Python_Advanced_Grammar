import os
dir = os.getcwd()
print(dir)
os.path

ld = os.listdir()
print(ld)

rst = os.system("dir")
print(rst)

os.system("dir")

rst = os.getenv("PATH")
print(rst)

print(os.pardir)
print(os.curdir)
print(os.sep)
print(os.linesep) ##换行符
print(os.name)

import os.path as op
bn = op.basename("D:\python_project\Python_Advanced_Grammar")
print(bn)
bn = op.basename("/home/tlxy")
print(bn)

import shutil
shutil.copyfile("D:\安信杀毒网址.txt","D:\daiye.txt")

#rst = shutil.make_archive("D:\daiye","zip","D:\PPT素材包（上午版）")
#print(rst)

import zipfile
zp = zipfile.ZipFile("D:\daiye.zip")
print(zp.getinfo("test.txt"))
print(zp.namelist())

import random
print(random.randint(0,100))
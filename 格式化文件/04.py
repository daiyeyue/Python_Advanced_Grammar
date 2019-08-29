import xml.etree.ElementTree as et
import io
import sys
import urllib.request
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
stu = et.Element("Student1")
print(stu)
name = et.SubElement(stu, 'Name')  ##生成了叫Name的子元素
name.attrib = {'lang':'en'}  #Name子元素的下面有个属性lang，值为en
name.text = 'maozedong'
age = et.SubElement(stu, 'Age')
age.text = '18'
et.dump(stu)
print(stu)

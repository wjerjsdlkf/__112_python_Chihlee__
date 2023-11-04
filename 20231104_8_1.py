#第一種 import tools  #全部引用
#stu1 = tools.Student(name="AAA",chinese=89,english=92,math=65)
#print(stu1.name)
#print(stu1.chinese)
#print(stu1.english)
#print(stu1.math)
#print(stu1.sum())

#第二種 from tools import Student #單獨引用class
#單獨引用不用前面再加tools.
#stu1 = Student(name="AAA",chinese=89,english=92,math=65)
#print(stu1.name)
#print(stu1.chinese)
#print(stu1.english)
#print(stu1.math)
#print(stu1.sum())

#第三種 使用tools內的 getStudent
from tools import getStudent
stu1 = getStudent(name="robert",chinese=89,math=92,english=75)
print(stu1.name)
print(stu1.chinese)
print(stu1.english)
print(stu1.math)
print(stu1.sum())
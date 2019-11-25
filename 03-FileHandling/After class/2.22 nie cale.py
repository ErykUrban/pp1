import re
tab=[]
x = open('students.txt', 'r')
for i in x:
    y= re.findall(r'[a-zA-Z]+\,[a-zA-Z]+\,\d+',i)
    print(y)
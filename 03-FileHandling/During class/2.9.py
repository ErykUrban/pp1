f = open('C:/Users/W10Home/Desktop/pp1/03-FileHandling/NoEducation.txt', 'r')
x=1
for i in f:
    print(f'{x}:'+ i, end='')
    x+=1
f.close()
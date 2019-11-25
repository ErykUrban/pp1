x = open('numbers.txt' , 'r')
parzyste=[]
for i in x:
    if int(i)%2==0:
        parzyste.append(int(i))
x.close()
y = open('evennumbers.txt', 'w')
for i in parzyste:
    y.write(f'{str(i)}\n')
y.close()

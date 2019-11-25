
x = open('numbers.txt', 'r')
lista=[]
for i in x:
    lista.append(int(i))
lista.sort()
for x in lista:
    print(x, end=' ')

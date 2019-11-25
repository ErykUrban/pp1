x = open('universities.txt', 'r')
lista=[]
for i in x:
    lista.append(i)
lista.sort()
x.close()
x = open('universities.txt', 'w')
for i in lista:
    x.write(i)
x.close()
f=open('C:/Users/W10Home/Desktop/pp1/03-FileHandling/numbers.txt', 'r')
lista=[]
for i in f:
    lista.append(int(i))
print(sum(lista))
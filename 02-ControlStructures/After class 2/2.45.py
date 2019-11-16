N=int(input("Ilość liczb: "))
n=2 #jako l pierw
zbiór=[]
while len(zbiór)<N:
    for i in range(2, n):
        if (n%i) == 0:
            break
    else:
        zbiór.append(n)
    n+=1
print("liczby pierwsze: ", end='')
for x in zbiór:
    print(f'{x}', end=" ")
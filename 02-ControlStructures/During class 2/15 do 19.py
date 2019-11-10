#2.15
liczba = int(input("Podaj liczbę: "))
mnożnik =1
while liczba <=10:
    wynik = liczba * mnożnik
    mnożnik +=1
    print(str(liczba) + " x " + str(mnożnik-1)+ " = " + str(wynik))
    if mnożnik >10:
        break
    
print(' ')
#2.16
x=1
for y in range(1, 11):
    print(f'{x}/{y} = {x/y}')

print(" ")
#2.17
suma_odd=sum(range(1, 50, 2))
suma_even=sum(range(0, 50, 2))
print(f'Suma nieparzystych {suma_odd}\n'
      f'Suma parzystych {suma_even}')

print(' ')
#2.18
for n in range(1,31):
    if n%3 == 0 and n%5 == 0:
        print("Bingo")
    elif n%3 == 0:
        print("Three")
    elif n%5 == 0:
        print("Five")
    else:
        print(n)
        
print(' ')
#2.19
m=1
n=int(input("Podaj liczbę wyrazów ciągu: "))
for x in range (0,n):
    print(m, end =' ')
    m = m + 3

ilość_liczb=0
a=10
suma=0
while a!=0:
    a=int(input("Podaj liczbę: "))
    if a!=0:
        ilość_liczb+=1
        suma+=a
srednia=(suma/ilość_liczb)
print(f'Rezultat: Liczb: {ilość_liczb}, Suma: {suma}, Średnia: {srednia}')
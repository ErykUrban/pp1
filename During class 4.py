#4.5 Durring class

def imię():
    print('Eryk Urban')
imię()

# 4.6
def uek():
    print('Uniwersytet Ekonomiczny w Krakowie,')
    print('ul.Rakowicka27,')
    print('31-510 Kraków')
uek()
#4.7

x=0
while x<7:
    print(str(x+1) + " " + str(x+2) + " " + str(x+3))
    x +=3

#4.12
def iloczyn(x,y):
    print(x*y)
iloczyn(5,5)
#4.13
tablica=[4,3,7,1,3]
def suma(x):
    print("Suma wartości: " + str(sum(tablica)))
    print("Tablica: " + str(tablica[0])+" "+str(tablica[1])+" "+str(tablica[2])+" "+str(tablica[3])+" "+str(tablica[4]))
suma(tablica)
#4.14
tablica=[15,38,7,23,14]
liczba = 23
def wystepuje(liczba, tablica):
    if liczba in tablica:
        print("Liczba: 23")
        print("Tablica: " + str(tablica[0])+" "+str(tablica[1])+" "+str(tablica[2])+" "+str(tablica[3])+" "+str(tablica[4]))
        print("Rezultat: Podana liczba występuje w tablicy")
wystepuje(liczba,tablica)
#4.15
def multiplication(x,y):
    return x*y
    
print(multiplication(15,14))
#4.16
def czytajLiczbe():
    x= input("wprowadź liczbę:")
    y= input("wprowadź liczbę: ")
    print(int(x)+int(y))
czytajLiczbe()
#4.17
import random
def rzut():
    rzut1 = random.randrange(1,7)
    rzut2 = random.randrange(1,7)
    rzut3 = random.randrange(1,7)
    print("Wyrzucone oczka: " + str(rzut1) +" " + str(rzut2)+" "+ str(rzut3))
    print("Suma oczek: " + str(int(rzut1)+int(rzut2)+int(rzut3)))
rzut()
#4.18
def silnia(n):

    #0!=1 oraz 1!=1
    if n==0 or n==1:
        return 1

    #n! = n * (n-1)!
    if n > 1:
        return n * silnia(n-1)
  
print( f"10!= {silnia(10)}" )


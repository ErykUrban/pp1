#2.4
x = int(input("Wprowadź liczbę: "))
if x >10:
    print("liczba wieksza od 10")
elif x == 10:
    print("liczba równa 10")
else:
    print("liczba mniejsza od 10")

print(" ")
#2.5
wiek = int(input("Wprowadź wiek: "))
if wiek >= 18: print("Pełnoletni")
elif wiek<0: print("Nieprawidłowe dane")
else: print("Niepełnoletni")

print(" ")
#2.6
imie_nazwisko = "Eryk Urban"
x = 0
for x in range(5):
    print(imie_nazwisko)
    x += 1
    
print(" ")
#2.7
imie_nazwisko = "Eryk Urban"
x = 0
while x<5:
    print(imie_nazwisko)
    x += 1

import random
rzut_komputera = random.randrange(1,7)
b = int(input("Podaj, ile oczek wyrzucił komputer: "))
print("Komputer wyrzucił nastepującą liczbę oczek: " + str(rzut_komputera))
if b == rzut_komputera:
    print("True")
else:
    print("False")
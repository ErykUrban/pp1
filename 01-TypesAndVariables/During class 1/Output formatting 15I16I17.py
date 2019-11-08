# 1.15
a = int(input("Podaj liczbę całkowitą: "))
print("Wartość liczby to {}".format(a) +", a {} to jej druga potęga".format(a**2))

#1.16
imie="Eryk"
wiek=19
wzrost= 178
print("Mam na imię {} ".format(imie) +"i mam {} lat, ".format(wiek) +"a mój wzrost to {} cm".format(wzrost))

#1.17
kwota = 15.84
vat = 0.23
Vat_nalezny = kwota*vat
print("Kwota: " + str(kwota) + "zł")
print("VAT 23%: {}".format(round(Vat_nalezny, 2)) + "zł")

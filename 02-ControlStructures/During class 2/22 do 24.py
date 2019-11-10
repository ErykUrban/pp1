#2.22
tablica = [15,8,31,47,2,19]
l_wyraz = 0
suma = 0
for x in tablica:
    if x%2 != 0:
     suma += x
     l_wyraz += 1
print(f'Średnia arytmetyczna wyrazów nieparzystych w tablicy wynosi: {suma/l_wyraz}')

print(' ')
#2.23
ocena =int(input("Podaj ocenę: "))
oceny_słownie = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']
a = ocena -1
if a in range(0,6):
    print(f'Ocena słownie: {oceny_słownie[a]}')
else:
    print("Nieprawidłowe dane")

print(' ')
#2.24
imiona=["Genowefa","Onufry","Celestyna","Alojzy","Pankracy","Teofil"]
dł=0
imie=0
for i in imiona:
    if len(i)>dł:
        dł=len(i)
        imie=(i)
print(f'Najdłuższe imię: {imie}')
        
    
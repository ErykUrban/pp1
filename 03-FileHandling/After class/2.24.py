import csv
tablica=[['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]
tablica2=['Imie','Nazwisko','Email']
with open('tablica.csv', 'w', newline='') as plik:
    a = csv.writer(plik)
    a.writerow(tablica2)
    for i in tablica:
        a.writerow(i)
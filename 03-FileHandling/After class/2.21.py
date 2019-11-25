tab=[]
txt = open('numbersinrows.txt', 'r')
for liczba in txt:
    cyfry = liczba.split(',')
    for i in cyfry:
        tab.append(int(i))
print(f'Ilość cyfr: {len(tab)}, suma: {sum(tab)}')
txt.close()

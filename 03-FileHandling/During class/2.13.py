f = open('Tablica cyfr.txt','a')
l=[32,16,5,8,24,7]
for x in l:
    f.write(f'{x}\n')
f.close()
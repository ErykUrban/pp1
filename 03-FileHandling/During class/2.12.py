f = open("shoppinglist.txt", 'a')
for x in range(999):
    item=input("Podaj przedmiot: ")
    if item=='':
        break
    else:
        f.write(f'{item}\n')
f.close()
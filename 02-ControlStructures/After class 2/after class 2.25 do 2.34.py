#2.25
a = 7
for x in range(3):
    print(a*"*")

print(' ')
#2.26
q=1
for x in range(1,10):
    print(q*f'{x}')
    q+=1

print(' ')
#2.27
a = 10
b = 6
for x in range(a):
    if b>x:
     print(x*"*")
    else:
        print((a-x)*"*")

print(" ")
#2.28
a = 4 #wys
b = 10 #szer
for x in range(a):
    if x == 1:
        print(b*"*")
    elif x > 1 or x < a and x !=0:
        print("*"+(b-2)*" "+"*")
else:
    print(b*"*")
    
print(' ')
#2.29
tab= [15,8,31,47,2,19]
print(f'tab: {tab}')
tab.reverse()
print(f'tab in reverse: {tab}')

print(' ')
#2.30
a=0
pin = "0805"
pin_input = input("Podaj kod PIN: ")
if pin != pin_input:
    print("Kod PIN niepoprawny.")
    pin_input = input("Podaj kod PIN: ")
    if pin != pin_input:
        print("Kod PIN niepoprawny.")
        pin_input = input("Podaj kod PIN: ")
        if pin != pin_input:
            print("Kod PIN niepoprawny.\n"
                  "Karta płatnicza zostaje zablokowana.")

print('')
#2.31
uczelnia = "Uniwersytet Ekonomiczny w Krakowie"
print(f"Uczelnia: {uczelnia}\nSzeroko:",end=' ')
for x in uczelnia:
    print(x, end= ' ')
    
print('')
#2.32
a= list(input("Wprowadź dane: "))
print(f'Dane wspak: ',end='')
a.reverse()
for i in a:
    print(i , end=" ")

print('')
#2.33
slowa=["zero","jeden","dwa","trzy","cztery","pięć","sześć","siedem","osiem","dziewięć"]
liczba=input("Wprowadź dane: ")
print(liczba, end=' - ')
for x in liczba:
    print(slowa[int(x)], end=' ')

print('')
#2.34
pesel =input("Podaj pesel: ")
plec= int(pesel[9])
M = [1, 3, 5, 7, 9]
if plec in M:
    print("Płeć: mężczyzna")
else: print("Płeć: kobieta")
if int(pesel[:2]) <= 18:
    print('Wiek: 'f'{18-int(pesel[:2])}')
elif int(pesel[:2]) >= 18:
        print('Wiek: 'f'{118-int(pesel[:2])}')


         

            
       

    
         

    

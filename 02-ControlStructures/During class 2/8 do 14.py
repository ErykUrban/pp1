#2.8
x =int(input("Wprowadź cyfrę: "))
y =int(input("Wprowadź cyfrę: "))
if x>y:
    print("x: "+ str(x) + " jest wartością wiekszą")
else:
    print("y: "+ str(y) + " jest wartością wiekszą")
     
print(" ")
#2.9
z = int(input("Wprowadź cyfrę: "))
if z%2 == 0:
    print("even")
else:
    print("odd")

print(" ")
#2.10
a = int(input("Wprowadź cyfrę: "))
if a>=0  and a%2 != 0:
    print("Dodatnia nieparzysta")
else: print("Podana liczba nie jest, \njednoczesnie nieparzysta i dodatnia")

print(" ")
#2.11
login = "marek"
hasło = "m-123"
login_wprowadzony= input("Podaj login: ")
hasło_wprowadzone= input("Podaj hasło: ")
if login == login_wprowadzony and hasło == hasło_wprowadzone:
    print("Dane zostały wprowadzone poprawnie")
else:
    print("Login lub hasło jest nieprawidłowe")

print(" ")
#2.12
x = int(input("Wprowadź liczbę: "))
y = int(input("Wprowadź liczbę: "))
if x < 0 or y <0:
    print("Jedna lub obie wartości są ujemne.")
    if x <0 and y <0:
        print("Obie wartości są ujemne")
    elif x<0:
        print("Tylko x: "+str(x)+" jest ujemne")
    elif y<0:
        print("Tylko y: "+str(y)+" jest ujemne")

print(" ")
#2.13
x = (input("Wprowadź 'x': "))
y = (input("Wprowadź 'y': "))
if int(x) == 0 and int(y) ==0:
    print("Punkt P("+x+","+y+") znajduje się na początku układu wspólrzędnych")
elif int(x) > 0 and int(y) >0:
    print("Punkt P("+x+","+y+") znajduje się w pierwszej ćwiartce układu wspólrzędnych")
elif int(x) <0 and int(y) >0:
    print("Punkt P("+x+","+y+") znajduje się w drugiej ćwiartce układu wspólrzędnych")
elif int(x) > 0 and int(y) <0:
    print("Punkt P("+x+","+y+") znajduje się w czwartej ćwiartce układu wspólrzędnych")
elif int(x) == 0 and int(y) >0:
    print("Punkt P("+x+","+y+") znajduje się na osi y układu współrzędnych")
elif int(x)>0 and int(y) ==0:
    print("Punkt P("+x+","+y+") znajduje się na osi x układu współrzędnych")
else:
    print("Punkt P("+x+","+y+") znajduje się w trzeciej ćwiartce układu współrzędnych")
    
print(" ")
#2.14
wiek = int(input("Podaj wiek psa w ludzkich latach: "))
if wiek in range(3):
    print("Wiek psa w psich latach to "+str(wiek*10.5))
elif wiek>2:
    print("Wiek psa w psich latach to "+str(21+(wiek-2)*4))

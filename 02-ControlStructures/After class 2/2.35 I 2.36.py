#2.35
import math
a = int(input("Wprowadź a: "))
b = int(input("Wprowadź b: "))
c = int(input("Wprowadź c: "))
delta=(b**2)-((4)*a*c)
if delta == 0:
    print(f'Pierwiastkiem równania jest liczba: {-b/2*a}')
elif delta>0:
    delta_pierw= math.sqrt(delta)
    print(f'Pierwiastkami równania sa: {-b+delta_pierw/2*a} i {-b-delta_pierw/2*a}')
    
else:
    print("Równanie nie ma pierwiastka")
    
#2.36
l=7
while l>=7:
    if l%2==1 and l%3==1 and l%4==1 and l%5==1 and l%6==1:
        print (f'Liczba spełniajaca warunki zadania: {l}')
        break
    else:
        l+=7

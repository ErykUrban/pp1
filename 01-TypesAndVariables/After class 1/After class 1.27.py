import math
liczba1=input("Pierwszą liczba: ")
liczba2=input("Drugą liczba: ")
NWD = math.gcd(int(liczba1),int(liczba2))
print("Najwiekszy wspólnym dzielnik: " + str(NWD))

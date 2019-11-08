#1.20
import math
radius=input("Wprowadź r: ")
area = math.pi * (int(radius))**2
circumference = 2 * math.pi * int(radius)
print("Pole powierzchni koła dla r=" +radius +" wynosi: " + str(area))
print("Obwód koła dla r=" +radius +" wynosi: " + str(circumference))

#1.21
celsius = input("Wprowadź temperaturę w celcjuszach: ")
wzór_kelvin = float(celsius) + 273
wzór_fahrenheit = 1.8*(float(celsius)) +32
print(wzór_kelvin)
print(wzór_fahrenheit)

#1.22 #sqrt- pierwiastek #wzór herona P= pierw kw(p(p-a)(p-b)(p-c)) gdzie p= a+b+c/2
a = int(input("Długość boku: "))
b = int(input("Długość boki: "))
c = int(input("Długość boki: "))
p = (float(a)+float(b)+float(c))/2
Area=float(math.sqrt(float(p)*(float(p)-a)*(float(p)-b)*(float(p)-c)))
print(Area)

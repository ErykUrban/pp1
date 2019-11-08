# BMI= waga/wzrost**2
wzrost = input("Podaj wzrost w cm: ")
waga = input("Podaj wagę w kg: ")
BMI = int(waga)/(int(wzrost)/100)**2
if BMI >= 25 and BMI <30 : 
    print("Wskaźnik BMI: " + str(round(BMI, 2)) + "(nadwaga)")
elif BMI >19 and BMI<25:
        print("Wskaźnik BMI: " + str(round(BMI, 2)) + "(norma)")
elif BMI <= 19:
    print("Wskaźnik BMI: " + str(round(BMI, 2)) + "(niedowaga)")
elif BMI >= 30:
    print("Wskaźnik BMI: " + str(round(BMI, 2)) + "(otyłość)")
    
    
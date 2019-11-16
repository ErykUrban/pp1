limit=int(input("Podaj limit prędkości (km/h): "))
prędkość=int(input("Podaj prędkość pojazdu (km/h): "))
if prędkość>limit:
    if prędkość-limit==10: #Jęsli jade mniej niz 10km/h powyzej limitu moze byc to bład pomiarowy a tym samym obedzie sie bez mandatu
        print(f'Mandat (zł): {(prędkość-limit)*5}')
    if prędkość-limit>10:
         print(f'Mandat (zł): {50+((prędkość-(limit+10))*15)}')
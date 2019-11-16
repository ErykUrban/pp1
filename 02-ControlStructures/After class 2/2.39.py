ciag=[0,1]
for a in ciag:
    print (a,end=" ")
for b in range(50):  #0 do 49 to 50
    Sum_ostatnich=ciag[-1]+ciag[-2]
    ciag.append(Sum_ostatnich)
    print(Sum_ostatnich, end=' ')
    
    


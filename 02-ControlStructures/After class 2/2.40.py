import random
jeden=0
dwa=0
trzy=0
cztery=0
piec=0
szesc=0

for b in range(0,101):
    a= random.randrange(1,7)
    if a==1:
        jeden+=1
    elif a==2:
        dwa+=1
    elif a==3:
        trzy+=1                       
    elif a==4:
        cztery+=1
    elif a==5:
        piec+=1
    elif a==6:
        szesc+=1
print(f' Jeden wypadło: {jeden} razy\n'
      f' Dwa wypadło: {dwa} razy\n'
      f' Trzy wypadło: {trzy} razy\n'
      f' Cztery wypadło: {cztery} razy\n'
      f' Pięć wypadło: {piec} razy\n'
      f' Sześć wypadło: {szesc} razy')
      
            
            
            
            
            
    
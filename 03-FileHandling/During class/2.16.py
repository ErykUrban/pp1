import re
pogoda = 'wtorek - 23C, środa - 21C, czwartek 25C'
wzor = re.compile(r'\d\d')
pasuja = wzor.findall(pogoda)
lista=[]
for i in pasuja:
    lista.append(int(i))
print(sum(lista)/3)
   
    

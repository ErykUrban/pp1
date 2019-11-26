import re
a=''
txt= open('land.txt', 'r')
for i in txt:
    a+=i
pattern = re.compile(r'\d')
matches = pattern.findall(a)

suma=0
for match in matches:
    suma+=int(match)
print(f'suma cyfr wystepujaca w pliku: {suma}')
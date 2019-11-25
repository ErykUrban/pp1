f = open('C:/Users/W10Home/Desktop/pp1/03-FileHandling/NoEducation.txt', 'r')
print(f.read())
f.close()

print()

#sposób 2
with open('C:/Users/W10Home/Desktop/pp1/03-FileHandling/NoEducation.txt', 'r') as f:
	print(f.read())

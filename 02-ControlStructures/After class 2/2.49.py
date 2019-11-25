tyg=["PN", "WT", "SR", "CZ", "PT", "SB", "ND"]
b=0
c=1
for a in range(6):
    for x in range(7):
        if a==0:
            print(f'|{tyg[b]}|',end='')
            b+=1
        elif a==1 and x==0:
            print(f'|  |',end='')
        elif a==1 and x>=2:
            print(f'| {c}|',end='')
            c+=1
        elif a==2 and x<=3:
             print(f'| {c}|',end='')
             c+=1
        elif a==2 and x>=4:
            print(f'|{c}|',end='')
            c+=1
        elif a>=3 and c!=31:
            print(f'|{c}|',end='')
            c+=1
        else:
            print("|  |",end='')
    print()
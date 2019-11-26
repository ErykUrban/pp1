txt = open('students.txt', 'r')
for l in txt:
    splited_txt=l.strip('\n').split(',')
    if splited_txt[2]!="age":
        if int(splited_txt[2])<30:
            print('%-6s' % splited_txt[0], '%-7s' % splited_txt[1], splited_txt[4])
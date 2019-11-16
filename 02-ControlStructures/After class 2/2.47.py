Kwota=int(input("Podaj kwotę w zł: "))
piatki=Kwota//5
dwójki=(Kwota-(piatki*5))//2
zlotowki=(Kwota-((piatki*5)+(dwójki*2)))
print(f'5 zł – {piatki} szt\n'
      f'2 zł - {dwójki} szt\n'
      f'1 zł - {zlotowki} szt')
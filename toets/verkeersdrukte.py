#invoer
pv1 = input('De verkeersdichtheid van het vrachtvervoer op het eerste rijvak; ')
pv2 = input('De snelheid van het vrachtverkeer op het eerste rijvak;  ')
pa1 = input('De verkeersdichtheid van het personenvervoer op het tweede rijvak; ')
pa2 = input('De snelheid van de personenwagens op het tweede rijvak. ')

#bewerking
pv = input(float((pv1 * pv2)/ 40))
pa = input(float((pa1 * pa2)/ 40))


if min(pv) > float(0.7) and min(pa) > float(0.7):
    kleurcode = 'zwart'
elif max(pv) > float(0.7) and max(pa) > float(0.7) and abs(abs(pv)-abs(pa)) > 0.2:
    kleurcode = 'rood'
elif abs(abs(pv)-abs(pa)) > 0.7:
    kleurcode = 'geel'
else:
    kleurcode = 'groen'

#uitvoer
print(kleurcode)
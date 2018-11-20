#invoer
kaart = int(input('kaart: '))
totaal = 0

#bewerking

while totaal < 21 and kaart > 0:
    totaal += kaart
    if totaal < 21:
        kaart = int(input('kaart: '))

if kaart == 0:
    print('Voorzichtig gespeeld ({})'.format(totaal))

if totaal == 21:
    print('Gewonnen!')

if totaal > 21:
    print('Verbrand ({})'.format(totaal))

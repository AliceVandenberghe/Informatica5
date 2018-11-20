#invoer
prijs = 1
som = 0

#berekening
while prijs > 0:
    prijs = float(input('De prijs: '))
    som += prijs


print('De totale prijs is €', '{:.2f}'.format(som))
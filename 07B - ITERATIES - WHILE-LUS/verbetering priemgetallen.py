#invoer
getal = int(input('getal: '))

# zolang je het niet kan delen door 2,3,4 is het wss een priemgelat

deler = 2

#while getal/ deler != getal // deler:
while getal % deler != 0 and getal != 1:
    deler += 1

if deler == getal:
    print('priemgetal')

else:
    print('geen priemgetal')
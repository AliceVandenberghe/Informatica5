verliezer = 'aanvaller verliest 1 leger, verdediger verliest 1 leger'

#input
a = int(input('de eerste dobbelsteen van de aanvaller: '))
b = int(input('de tweede dobbelsteen van de aanvaller: '))
c = int(input('de derde dobbelsteen van de aanvaller: '))
d = int(input('de eerste dobbelsteen van de verdediger: '))
e = int(input('de tweede dobbelsteen van de verdediger: '))

getal_2 = (a + b + c) - max(a, b, c)- min(a, b, c)

# sorteren
#a1 = max(a1, max(a2 , a3))
#ssa2 = a1 + a2 + a3 - sa1 - min(a1,a2,a3)
#sa3 = min(a1, a2, a3)

#sv1 = max((v1)
#sv2 = min(v2)

#winnaar bepalen
# if sa1 > sa2 and sa2 > sv2:
# mess = ...
#elif sv1 >= sa1 and Sv2 >= sa2:
# mes = 'aanvaller verliest 2 legers...
#else:
# mes = 'verliezer'
# uitvoer
#print(mes)



#berekeningen
if max(a, b, c) > max(d, e):
   if getal_2 > min(d, e):
        print('aanvaller verliest 0 legers, verdediger verliest 2 legers')
    elif getal_2 <= min(d, e):
         print(verliezer)
elif max(a, b, c) <= max(d, e):
    if getal_2 <= min(d, e):
        print('aanvaller verliest 2 legers, verdediger verliest 0 legers')
    elif getal_2 > min(d, e):
        print(verliezer)
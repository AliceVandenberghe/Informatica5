k = 8.99 * (10 ** 9)
q1 = 2 * (10 ** (-6))
q2 = 1.0 * (10 ** (-6))

#de invoer
r = float(input('straal: '))

resultaat = 'Fc'
resultaat = (k * q1 * q2) / (r ** 2)
#uitvoer
print(resultaat)

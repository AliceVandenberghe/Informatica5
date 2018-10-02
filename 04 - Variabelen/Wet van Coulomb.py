k = 8.99 * (10 ** 9)
q1 = 2.0 * (10 ** (-6))
q2 = 1.0 * (10 ** (-6))

#de invoer
r = float(input('straal: '))
r *= 10 ** -2

#berekening
fc = k *(( q1 * q2) / (r ** 2))

#uitvoer
resultaat = fc

print(resultaat)

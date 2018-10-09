from math import sqrt

#input
a = float(input('a: '))
b = float(input('b: '))

#bewerking
c = sqrt((a ** 2) + (b ** 2))

uitkomst = 'In een rechthoekige driehoek met rechthoekzijden a = {:.2f} en b = {:.2f} is de schuine zijde c = {:.2f}'.format(a, b, c)

print(uitkomst)

x = float(input('x: '))
y = float(input('y: '))

linker_lid = abs(abs(x)-abs(y))
rechter_lid =abs(x-y)

#uitvoer

print('{} < {}'.format(linker_lid, rechter_lid))
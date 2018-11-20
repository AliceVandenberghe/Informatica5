from random import randint

vorst_periode = 0
temperatuur = int(input('Dagtemperatuur: '))

while temperatuur <= 0:
    print(temp)
    vorst_periode += 1
    temp = randint(-10, 0)

print(vorst_periode, 'dagen')
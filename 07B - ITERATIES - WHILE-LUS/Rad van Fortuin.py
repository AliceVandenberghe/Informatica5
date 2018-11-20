#invoer
woord = str(input('Wat is het verborgen woord? '))
bedrag = int(input('Voor welk bedrag wordt er gespeeld? '))
letter = str(input('Letter: '))
totaal_bedrag = 0
i = ''

#bewerking
while letter in woord and letter not in i:
    totaal_bedrag += bedrag
    i += letter
    letter = str(input('Letter: '))

if letter not in woord:
    totaal_bedrag == 0

print(totaal_bedrag)
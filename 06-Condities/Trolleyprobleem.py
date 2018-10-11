hendel_trekken = input('trek aan de hendel van de wissel? (ja / nee)')
man_duwen = input('man van de brug duwen? (ja / nee)')

if hendel_trekken == 'ja' and man_duwen == 'ja':
    doden = 2

elif hendel_trekken == 'nee' and  man_duwen == 'nee':
    doden = 5

else:
    doden = 1

print(doden)
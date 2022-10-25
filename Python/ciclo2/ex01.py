#pYTHON 3.10.8
import math
while True:
    try:
        IdadeEmDias = int(input('\033[36mDigite sua Idade em Dias:\033[m'))
        if IdadeEmDias <= 0:
            print('Favor Digitar Valores Positivos')
        else:
            break
    except ValueError:
        print('Favor Digitar um Valor e não um Texto!')

Anos = math.trunc(IdadeEmDias / 365)
Meses = math.trunc((IdadeEmDias % 365) / 30)
Dias = math.trunc((IdadeEmDias % 365) % 30)
print()
print('\033[32m--\033[m'*22)
print(f'\033[36mVocê possui\033[3m \033[32m{Anos} Ano(s),\033[m \033[33m{Meses} Mes(es) e\033[m \033[34m{Dias} Dia(s)\033[m')
print('\033[33m--\033[m'*22)








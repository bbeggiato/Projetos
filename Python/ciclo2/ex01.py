#pYTHON 3.10.8
from time import sleep
from math import trunc
print('--'*35)
print('Forneça o valor em Dias para Calcular sua Idade em Anos, Meses e Dias')
print('--'*35)
while True:
    try:
        IdadeEmDias = int(input('\033[36mDigite sua Idade em Dias: \033[m'))
        if IdadeEmDias <= 0:
            print('Favor Digitar Valores Positivos')
        else:
            break
    except ValueError:
        print('Favor Digitar um Número Positivo e não um Texto!')

Anos = floor(IdadeEmDias / 365)
Meses = floor((IdadeEmDias % 365) / 30)
Dias = floor((IdadeEmDias % 365) % 30)
print()
print('Calculando sua Idade com Exatidão, Processando...')
sleep(2.5)
print('\033[32m--\033[m'*22)
print(f'\033[36mVocê possui\033[3m \033[32m{Anos} Ano(s),\033[m \033[33m{Meses} Mes(es) e\033[m \033[34m{Dias} Dia(s)\033[m')
print('\033[33m--\033[m'*22)








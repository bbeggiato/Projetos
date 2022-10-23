import math

IdadeEmDias = int(input('Digite sua Idade em Dias: '))

Anos = math.trunc(IdadeEmDias / 365)
Meses = math.trunc((IdadeEmDias % 365) / 30)
Dias = math.trunc((IdadeEmDias % 365) % 30)
print(f'Você possui {Anos} Anos, {Meses} Meses e {Dias} Dias')








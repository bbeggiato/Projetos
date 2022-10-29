# Feito em Python 3.10.8
from time import sleep
while True:
    lista = []
    print('--' * 28)
    print('Qual o menor valor entre os 3 Números Digitados Abaixo?')
    print('--'* 28)
    try:
        Valor1 = int(input('Digite o Primeiro valor: '))
        Valor2 = int(input('Digite o Segundo valor:  '))
        Valor3 = int(input('Digite o Terceiro valor: '))

    except ValueError:
        print('Favor digitar apenas valores numéricos')

    else:
        break

lista.append(Valor1)
lista.append(Valor2)
lista.append(Valor3)
print()
print(f'Você Digitou os Valores {lista}')
print()
menor = min(lista)
print('Processando....')
sleep(2)
print('--'*18)
print(f'\033[36mO Menor Valor entre os três é:\033[m \033[33m {menor}\033[m')
print('--'*18)

















# Feito em Python 3.10.8
from time import sleep
print('--'*22)
print('Digite Abaixo para ver uma frase Invertida:')
print('--'*22)
# Letra "a" do exercício
frase = str(input("Escreva uma Frase: ")).strip()
print()
def frasecerta(texto):
    print(f'A frase digitada na ordem correta é: \n\033[31m{frase}\n\033[m')

frasecerta(frase)

# Letra "b" do exercício
def inversor(txt):
    return txt[::-1]
fraseinversa = inversor(frase)

print("A Frase Maluca ao Contrário é: ")
print("\n Aguarde, Processando a Maluquice....")
sleep(2.5)
print(f'\n\033[32m{fraseinversa}\033[m')










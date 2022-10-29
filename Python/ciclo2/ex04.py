from time import sleep
while True:
    print()
    print('--' * 11)
    print('Valor é Primo ou Não?')
    print('--' * 11)
    print()
    try:
        Numero = int(input('Digite um Número inteiro entre 1 e 100: '))
        if Numero <= 0 or Numero > 100:
            print('--'*19)
            print('Favor digitar apenas valores positivos entre 1 e 100!')
            print('--'*19)
        else:
            break
    except ValueError:
        print('Você não digitou um número!')
#print(num)
def AnalisaNumero(num):
    total = 0
    for c in range(1, num+1):
        if num % c == 0:
            total += 1
    if total == 2:
        #print('É Primo')
        return True
    else:
        #print('Não é primo!')
        return False
print()
print('O Número digitado é Primo?')
print()
print('Aguarde, Processando....')
sleep(2)
print()

primo = True
naoprimo = False
if AnalisaNumero(Numero) == True:
    print(f'\033[33m{primo}\033[m')
else:
    print(f'\033[31m{naoprimo}\033[m')












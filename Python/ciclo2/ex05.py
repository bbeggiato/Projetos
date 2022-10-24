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
print(f'A frase maluca ao contrário é: \n\033[32m{fraseinversa}\033[m')










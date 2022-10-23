# Letra "a" do exercício
frase = str(input("Escreva uma Frase: "))

def frasecerta(texto):
    print(f'A frase digitada na ordem correta é: {frase}')

frasecerta(frase)

# Letra "b" do exercício
def inversor(txt):
    return txt[::-1]
fraseinversa = inversor(frase)
print(f'A frase maluca ao contrário é: {fraseinversa}')










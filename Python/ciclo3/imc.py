# Python 3.10.8
from tkinter import *
from tkinter import messagebox

# Validação para não permitir string nos campos peso e altura
def valida(input):
  if input.replace('.','',1).isdigit():
    return True
  elif input == "":
    return True
  else:
    return False

# Executa comando da funcão ao clicar no botão Calcular
def analisaDados():
  # Recebe os valores com o get() e os atribui a variável somente se tudo estiver preenchido
  if vnome.get() != "" and vnome.get() != "" and vendereco.get() != "" and valtura.get() != "" and vpeso.get() != "":
    nom = vnome.get()
    end = vendereco.get()
    alt = float(valtura.get())
    pes = float(vpeso.get())

    # Converte altura para metro
    altmetros = alt / 100
    altura2 = f'{altmetros:.2f}'

    # Cálculo do IMC jogado a uma variável
    imc = pes / (altmetros * altmetros)

    # Calcula como a pessoa se enquadra baseado no IMC
    estado = ''
    if imc < 17:
      estado = 'Muito abaixo do Peso'
    elif imc >= 17 and imc < 18.5:
      estado = 'Abaixo do Peso'
    elif imc >= 18.5 and imc <= 24.99:
      estado = 'Peso Normal'
    elif imc >= 25 and imc <= 29.99:
      estado = 'Acima do Peso'
    elif imc >= 30 and imc <= 34.99:
      estado = 'Obesidade I'
    elif imc >= 35 and imc <= 39.99:
      estado = 'Obesidade Severa'
    elif imc >= 40:
      estado = 'Obesidade Mórbida'

    # Atribui a resposta a res
    res = f' O IMC  é: {imc:.2f}\n\n {estado}'

    # Escreve o conteúdo de res
    lb["text"] = res
  else:
    # messagebox para não calcular o IMC sem preencher todos os campos
    messagebox.showwarning(title="Aviso", message="Favor Preencher Todos os Campos!")

# Executa comando da funcao ao clicar no botão Limpar
def reset():
  # messagebox para limpar o campo Resultado
  resposta = messagebox.askyesno("Resetar", "Deseja Limpar todos os Dados?")
  if resposta == True:
    # Limpa o campo Resultado
    res = ''
    lb["text"] = res

    # Limpa as Entry
    vnome.delete(0, END)
    vendereco.delete(0, END)
    valtura.delete(0, END)
    vpeso.delete(0, END)

# messagebox para sair ou não
def sair():
  resposta2 = messagebox.askyesno("Sair", "Deseja Sair?")
  if resposta2 == True:
     main.quit()

# Nome e configs do Container
main = Tk()
main.title("Cálculo do IMC - Índice de Massa Corporal")
main.geometry("600x320")
main.configure(background="#dde")

# Campo Nome
nome = Label(main,text="Nome do Paciente: ",bg="#dde",fg="#000", font="14", anchor=W)
nome.place(x=30,y=30,width=150,height=30)
vnome=Entry(main, font="14")
vnome.place(x=210,y=30,width=350,height=30)

# Campo Endereço
endereco = Label(main,text="Endereço Completo: ",bg="#dde",fg="#000", font="14", anchor=W)
endereco.place(x=30,y=80,width=150,height=30, )
vendereco=Entry(main, font="14")
vendereco.place(x=210,y=80,width=350,height=30)

# Campo Altura
altura = Label(main,text="Altura(cm)",bg="#dde",fg="#000", font="14", anchor=W)
altura.place(x=30,y=130,width=100,height=30)
valtura=Entry(main, font="14")
valtura.place(x=210,y=130,width=100,height=30)
registro = main.register(valida)
valtura.config(validate="key", validatecommand=(registro,'%P'))

# Campo Peso
peso = Label(main,text="Peso (Kg)",bg="#dde",fg="#000", font="14", anchor=W)
peso.place(x=30,y=180,width=100,height=30)
vpeso=Entry(main, font="14")
vpeso.place(x=210,y=180,width=100,height=30)
registro = main.register(valida)
vpeso.config(validate="key", validatecommand=(registro,'%P'))

# Botão Calcular
btnCalcular = Button(main,text="Calcular",command=analisaDados)
btnCalcular.place(x=210,y=280,width=70,height=25)

# Botão Reiniciar
btnReiniciar = Button(main,text="Reiniciar", command=reset)
btnReiniciar.place(x=285,y=280,width=70,height=25)

# Botão Sair
btnSair = Button(main,text="Sair", command=sair)
btnSair.place(x=490,y=280,width=70,height=25)

# Resultado
lb = Label(main,text="",bg="#fff",fg="#000", font=('arial', 16, 'bold'))
lb.place(x=320,y=130,width=240,height=135)
main.mainloop()



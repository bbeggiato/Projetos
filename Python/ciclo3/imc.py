from tkinter import *

def valida(input):
  if input.replace('.','',1).isdigit():
    return True
  elif input == "":
    return True
  else:
    return False

# Executa comando da funcão ao clicar no botão Calcular
def analisaDados():
  # Recebe os valores com o get() e os atribui a variável
  alt = float(valtura.get())
  pes = float(vpeso.get())

  # Converte altura para metro
  altmetros = alt / 100

  # Cálculo do IMC jogado a uma variável
  imc = pes / (altmetros * altmetros)

  # Atribui a resposta á res
  res = f' O IMC  é: {imc:.2f}'

  # Escreve o conteúdo de res
  lb["text"] = res

# Executa comando da funão ao clicar no botão Limpar
def reset():
  # Limpa o campo Resultado
  res  = ''
  lb["text"] = res

  # Limpa as Entry
  vnome.delete(0, END)
  vendereco.delete(0, END)
  valtura.delete(0, END)
  vpeso.delete(0, END)

# Nome e configs do Container
main = Tk()
main.title("Cálculo do IMC - Índice de Massa Corporal")
main.geometry("400x275")
main.configure(background="#dde")

# Campo Nome
nome = Label(main,text="Nome do Paciente: ",bg="#dde",fg="#000", anchor=W)
nome.place(x=10,y=30,width=120,height=20)
vnome=Entry(main, highlightbackground='#f00')
vnome.place(x=130,y=30,width=250,height=20)

# Campo Endereço
endereco = Label(main,text="Endereço Completo: ",bg="#dde",fg="#000", anchor=W)
endereco.place(x=10,y=80,width=120,height=20)
vendereco=Entry(main)
vendereco.place(x=130,y=80,width=250,height=20)

# Campo Altura
altura = Label(main,text="Altura(cm)",bg="#dde",fg="#000", anchor=W)
altura.place(x=10,y=130,width=100,height=20)
valtura=Entry(main)
valtura.place(x=130,y=130,width=100,height=20)
registro = main.register(valida)
valtura.config(validate="key", validatecommand=(registro,'%P'))

# Campo Peso
peso = Label(main,text="Peso (Kg)",bg="#dde",fg="#000", anchor=W)
peso.place(x=10,y=180,width=100,height=20)
vpeso=Entry(main)
vpeso.place(x=130,y=180,width=100,height=20)
registro = main.register(valida)
vpeso.config(validate="key", validatecommand=(registro,'%P'))

# Botão Calcular
btnCalcular = Button(main,text="Calcular",command=analisaDados)
btnCalcular.place(x=120,y=230,width=70,height=20)

# Botão Reiniciar
btnReiniciar = Button(main,text="Reiniciar", command=reset)
btnReiniciar.place(x=195,y=230,width=70,height=20)

# Botão Sair
btnSair = Button(main,text="Sair", command=main.quit)
btnSair.place(x=310,y=230,width=70,height=20)

# Resultado
lb = Label(main,text="",bg="#fff",fg="#000", font=('arial', 13, 'bold'))
lb.place(x=240,y=130,width=140,height=90)

main.mainloop()



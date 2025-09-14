import tkinter as tk
import math

# Função backend para avaliar a expressão
def calcular():
    try:
        resultado = eval(entrada.get())  # avalia expressão digitada
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para inserir valores na caixa
def inserir(valor):
    entrada.insert(tk.END, valor)

# Função para limpar
def limpar():
    entrada.delete(0, tk.END)

# Função para calcular raiz quadrada
def raiz():
    try:
        valor = float(entrada.get())
        resultado = math.sqrt(valor)
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Função para elevar ao quadrado
def quadrado():
    try:
        valor = float(entrada.get())
        resultado = valor ** 2
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(tk.END, "Erro")

# Criando a janela
janela = tk.Tk()
janela.title("Calc. Castertech")

# Caixa de texto
entrada = tk.Entry(janela, width=22, font=("Arial", 16))
entrada.grid(row=0, column=0, columnspan=4)

# Botões principais
botoes = [
    ("7",1,0), ("8",1,1), ("9",1,2), ("/",1,3),
    ("4",2,0), ("5",2,1), ("6",2,2), ("*",2,3),
    ("1",3,0), ("2",3,1), ("3",3,2), ("-",3,3),
    ("0",4,0), (".",4,1), ("=",4,2), ("+",4,3),
    ("000",5,3)
]

for (texto, linha, coluna) in botoes:
    if texto == "=":
        tk.Button(janela, text=texto, width=5, height=2, command=calcular).grid(row=linha, column=coluna)
    else:
        tk.Button(janela, text=texto, width=5, height=2, command=lambda t=texto: inserir(t)).grid(row=linha, column=coluna)

# Botão limpar
tk.Button(janela, text="C", width=5, height=2, command=limpar).grid(row=5, column=0)

# Botão raiz quadrada
tk.Button(janela, text="√", width=5, height=2, command=raiz).grid(row=5, column=1)

# Botão ao quadrado
tk.Button(janela, text="x²", width=5, height=2, command=quadrado).grid(row=5, column=2)

# Loop da janela
janela.mainloop()
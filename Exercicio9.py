# Peça para o usuário digitar um número e diga se ele é positivo, negativo ou zero.
while True:
    numero = float(input("Digite um número:\n "))
    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

    pausa = input("Pressione Enter para continuar...")

    idade = int(input("Digite sua idade: "))
    if idade < 13:
        print("Você é uma criança.")
    elif idade >= 13 and idade <= 17:
        print("Você é um adolescente.")
    else:
        print("Você é um adulto.")
    
    repetir = input("\nDeseja reiniciar? (s para sim / qualquer tecla para sair): ").strip().lower()
    if repetir != 's':
        print("Programa encerrado.")
    break

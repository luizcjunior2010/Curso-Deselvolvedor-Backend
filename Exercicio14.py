# use um loop que leia numeros até que o usuário digite "0" e depois ixiba a soma deles.
soma = 0
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))
    if numero == 0:
        break
    soma += numero
print(f"A soma dos números digitados é: {soma}")
print("Programa encerrado.")








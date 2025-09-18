# Crie um programa que peça 5 números ao usuário e calcule a soma deles.
numero1 = int(input(f"Digite o1º número: "))
numero2 = int(input(f"Digite o2º número: "))
numero3 = int(input(f"Digite o3º número: "))
numero4 = int(input(f"Digite o4º número: "))
numero5 = int(input(f"Digite o5º número: "))
for i in range(5):
    soma = numero1 + numero2 + numero3 + numero4 + numero5
 
print(f"A soma dos números é: {soma}") 
print("Finalizado.")
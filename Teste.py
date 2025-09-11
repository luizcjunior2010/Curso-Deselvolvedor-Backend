# Criando uma tupla com informações de uma pessoa
pessoa = (0,"teste", 2, 3,4,5,6,7,8,9,10)

# Acessando os dados da tupla
print(type (pessoa[1]))
print( type (pessoa[7]))
print( type (pessoa[2]))

# Tentando alterar um valor da tupla (vai gerar erro)
# pessoa[1] = 26  # Descomentar essa linha causa um TypeError
numero = 1021
resto = numero % 2

if resto == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
# Saída: O número 7 é ímpar.
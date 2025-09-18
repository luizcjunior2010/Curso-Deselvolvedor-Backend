# elemento exclusivo de uma lista
grupo_pessoas_1 = {"Ana","Carlos","João"}
grupo_pessoas_2 = {"Maria","Carlos", "Pedro"}
# quantos nomes estão apenas na primeira lista
nomes_exclusivos = grupo_pessoas_1 - grupo_pessoas_2
print(f"Nomes exclusivos do grupo 1: {nomes_exclusivos}")
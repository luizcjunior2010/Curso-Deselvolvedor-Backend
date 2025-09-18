#criar uma  lista vazia
lista = []
# perguntar ao usuario (em loop) quais itens ele deseja adicionar na lista
# while True:
item = 0
while  True:
    item = input("\nDigite um item para adicionar na lista (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    else:
        lista.append(item)
# Quando o usuario digitar sair, o programa deve parar de pedir novos itens
# ao final o programa deve: Exibir os itens da lista; Mostrar quantos itens foram adicionados  e mostrar a lista em ordem alfabetica

# Mostrar Resultados
print(f"\nItens na lista:")
for item in lista:
    print(f"-{item}")
print(f"\nQuantidade de itens na lista: {len(lista)}")
# Mostrar lista em ordem alfabetica

lista.sort()
print("\nLista em ordem alfabética:")
for item in lista:
    print(f"-{item}")
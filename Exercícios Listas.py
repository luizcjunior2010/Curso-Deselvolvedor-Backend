#criar uma  lista vazia
lista = []
# perguntar ao usuario (em loop) quais itens ele deseja adicionar na lista
while True:
    item = input("Digite um item para adicionar na lista (ou 'sair' para finalizar): ")
    if item.lower() == 'sair':
        break
    lista.append(item)
# Quando o usuario digitar sair, o programa deve parar de pedir novos itens
# ao final o programa deve: Exibir os itens da lista; Mostrar quantos itens foram adicionados  e mostrar a lista em ordem alfabetica
print("Itens na lista:", lista)
print("Quantidade de itens na lista:", len(lista)) 
lista.sort()
print(f"Lista em ordem alfabética:", lista)
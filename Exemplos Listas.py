# pop com indice remove o elemento do indice especifico
lista = [1, 2, 3, 4, 5]
lista.pop(3)
print(lista)


# pop sem indice remove o ultimo elemento
lista.pop()
print(lista)


#remove remove o elemento especifico
lista1 = [1, 2, 3, 4, 5]
lista1.remove(3)
print(lista1)

# clear remove todos os elementos da lista
lista2 = [1, 2, 3, 4, 5]
lista2.clear()
print(lista2)

# index retorna o indice do elemento especifico
lista3 = [1, 2, "3", 4, 5]
lista3.index("3")
lista3.index(4)


# count retorna a quantidade de vezes que o elemento aparece na lista
lista4 = [1, 2, 3, 3, 3,5]
lista4.count(3)
print (lista4.count(3))

# reverse inverte a lista
lista5 = [1, 2, 3, 3, 3,5]
lista5.reverse()
print (lista5)

#concatenar listas
print (lista + lista1)

#repetir listas
print (lista * 3)

#copiar listas
lista6 = lista.copy()
print (lista6)

#lista append
lista7 = [1,2,3]
lista7.append(10)
print (lista7)

#lista.sort()
lista8 = [5,3,1,4,2]
lista8.sort()
print (lista8)



# compare len palavra com len(set(palavra)) para saber se tem repetição
palavra = input("digite uma palavra\n")

if len(palavra) == len(set(palavra)):
    print("-",len(palavra))
    print("-",len(set(palavra)))
    print("A palavra não tem caracteres repetidos")
else:
    print("-",len(palavra))
    print("-",len(set(palavra))) 
    print("A palavra tem caracteres repetidos")



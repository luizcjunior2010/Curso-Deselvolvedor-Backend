# peça ao usuario digitar uma frase e mostre todas as palavras unicas (sem repetição) que aparecem na frase
frase = input("Digite uma frase:")
palavras = frase.split()
palavras_unicas = set(palavras)
print("Palavras únicas na frase:", palavras_unicas)
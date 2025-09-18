frase = "luiz carlos da silva junior"
frase = frase.lower().replace(" ", "")
dicionario = {}

for letra in frase:
    if letra in dicionario:
       
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)
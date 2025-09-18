
banana = float(input("digite o valor da banana"))
maçã = float(input("digite o valor da maçã"))
Uva = float(input("digite o valor da Uva"))
preços_produtos = {"banana": banana, 
                   "maçã": maçã, 
                   "Uva": Uva
                   }
#soma os valores e mostre o total gasto
total = preços_produtos["banana"] + preços_produtos["maçã"] + preços_produtos["Uva"]
print("O Total Gasto foi de:" , total, "Reais")

nome = input("Digite seu nome é: ") 
print(nome)
idade = int(input("Digite sua idade: "))
print("Daqui há",100-idade, "anos você terá 100 anos")
print("Você é um adulto?:",idade >= 18)
print("Você é um adolescente?:",idade <= 18 and idade >= 13)
print("Você é uma criança?:",idade < 13)
idade += 5
print("daqui 5 anos você terá:",idade, "anos")
print("Seu nome contém a letra a?:","a" in nome.lower())